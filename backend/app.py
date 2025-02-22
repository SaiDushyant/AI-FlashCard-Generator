from fastapi import FastAPI, File, UploadFile
from model import generate_enhanced_flashcards
import tempfile
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
        temp_pdf.write(await file.read())
        temp_path = temp_pdf.name

    # Process PDF
    with open(temp_path, "rb") as f:
        # Extract text from PDF using PyPDF2
        import PyPDF2

        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    # Generate flashcards
    flashcards = generate_enhanced_flashcards(text)

    # Cleanup
    os.unlink(temp_path)

    return {"flashcards": flashcards}


@app.get("/")
async def root():
    return {"message": "PDF to Flashcards Converter"}
