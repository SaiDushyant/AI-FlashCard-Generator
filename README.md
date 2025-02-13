# AI FlashCard Generator

## Overview

**AI FlashCard Generator** is a full-stack application that helps students quickly review key points from lengthy study materials. By uploading a PDF, the application extracts and cleans the text, then uses AI techniques to automatically generate flashcards (questions and answers) based on the document content. This saves you valuable study time and makes revision more efficient.

## Features

- **PDF Upload:** Easily upload your study material in PDF format.
- **Text Extraction & Cleaning:** Extracts text from PDFs using PyPDF2 and cleans it for further processing.
- **Flashcard Generation:** Uses natural language processing (with nltk and RAKE) along with AI models to generate meaningful Q&A flashcards.
- **Animated & Responsive UI:** Built with React, Vite, and Tailwind CSS, featuring an animated, gradient background and responsive design.
- **Pagination:** Navigate through flashcards with a user-friendly pagination system.

## Tech Stack

- **Backend:** FastAPI, Python, PyPDF2, nltk, rake-nltk
- **Frontend:** React, Vite, Tailwind CSS, React Spinners
- **Server:** Uvicorn (for FastAPI)
- **Testing:** Pytest

## Project Structure

```plaintext
AI-FlashCard-Generator/
├── backend/
│   ├── main.py            # FastAPI application entry point
│   ├── model.py           # FlashcardGenerator class and helper functions
│   └── requirements.txt   # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.tsx        # Main React component (flashcard generator)
│   │   ├── TestBG.tsx     # Test page for background animation
│   │   └── index.css      # Global CSS file (includes Tailwind and custom styles)
│   ├── package.json       # Frontend dependencies and scripts
│   └── vite.config.ts     # Vite configuration
└── README.md              # This file
```

## Installation

### Backend Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SaiDushyant/AI-FlashCard-Generator.git
   cd AI-FlashCard-Generator/backend
   ```

2. **Create a Virtual Environment and Install Dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the FastAPI Server:**

   ```bash
   uvicorn main:app --reload
   ```

   The backend server will run at `http://127.0.0.1:8000`.

### Frontend Setup

1. **Navigate to the Frontend Directory:**

   ```bash
   cd ../frontend
   ```

2. **Install Dependencies:**

   ```bash
   npm install
   ```

3. **Run the Development Server:**

   ```bash
   npm run dev
   ```

   The frontend should now be available at `http://localhost:3000` (or as indicated by Vite).

## Usage

1. **Open the Frontend:**  
   Go to your browser and navigate to the frontend URL.

2. **Upload a PDF:**  
   Use the file upload input to select and upload your PDF study material.

3. **Generate Flashcards:**  
   Click the "Generate Flashcards" button. The system will process your PDF and display a paginated list of flashcards containing AI-generated questions and answers.

4. **Navigate Flashcards:**  
   Use the pagination buttons to navigate through the flashcards.

### Flashcard Generation

You can modify the flashcard generation logic in the backend (`backend/model.py`) to fine-tune how keywords are extracted or how the AI generates questions and answers.

## Troubleshooting

- **SSH/Push Issues:**  
  If you have issues pushing to GitHub, consider switching your remote URL to HTTPS or configure SSH to use port 443.

- **Backend Errors:**  
  Ensure your virtual environment is activated and the PDF file is valid.

- **Frontend Styling Issues:**  
  Verify that your CSS file is imported correctly and that your content paths are correctly set in your Tailwind configuration.

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests. For any major changes, please open an issue first to discuss what you'd like to change.
