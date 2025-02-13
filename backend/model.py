from PyPDF2 import PdfReader
from typing import List, Dict
import nltk
from nltk.tokenize import sent_tokenize
from rake_nltk import Rake

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")


class FlashcardGenerator:
    @staticmethod
    def extract_text_from_pdf(pdf_path: str) -> str:
        """Extract text content from PDF file"""
        text = ""
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()

        # Clean up the text
        text = " ".join(text.split())  # Remove extra spaces
        text = text.replace("\n", " ")  # Replace newlines with spaces
        return text

    @staticmethod
    def generate_flashcards(text: str, num_questions: int = 10) -> List[Dict]:
        """Generate QA pairs using keyword extraction"""
        # Initialize RAKE for keyword extraction
        r = Rake(stopwords=nltk.corpus.stopwords.words("english"))
        r.extract_keywords_from_text(text)

        # Get ranked phrases with scores
        keywords = r.get_ranked_phrases_with_scores()

        flashcards = []
        seen = set()

        for score, phrase in keywords:
            if len(flashcards) >= num_questions:
                break
            # Filter out low-quality phrases
            if (
                phrase.lower() not in seen
                and len(phrase.split()) > 1  # At least two words
                and not phrase.startswith("http")  # Exclude URLs
                and not phrase.isnumeric()  # Exclude numbers
            ):
                seen.add(phrase.lower())
                # Find context sentence
                context = FlashcardGenerator.find_context(text, phrase)
                if context:
                    flashcards.append(
                        {"question": f"What is {phrase}?", "answer": context}
                    )

        return flashcards

    @staticmethod
    def find_context(text: str, phrase: str) -> str:
        """Find the first sentence containing the phrase"""
        sentences = sent_tokenize(text)
        for sentence in sentences:
            if phrase in sentence:
                return sentence
        return ""
