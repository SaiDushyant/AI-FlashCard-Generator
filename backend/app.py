from fastapi import FastAPI, File, UploadFile
from backend.model import FlashcardGenerator
import tempfile
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
    text = FlashcardGenerator.extract_text_from_pdf(temp_path)
    flashcards = FlashcardGenerator.generate_flashcards(text)

    # Cleanup
    os.unlink(temp_path)

    return {"flashcards": flashcards}


@app.get("/")
async def root():
    return {"message": "PDF to Flashcards Converter"}
