import os
import logging
from typing import List, Dict
import nltk
from nltk.tokenize import sent_tokenize
from rake_nltk import Rake
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Download NLTK data
nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_path, exist_ok=True)
nltk.data.path.append(nltk_data_path)

nltk.download("punkt_tab", download_dir=nltk_data_path)
nltk.download("punkt", download_dir=nltk_data_path)
nltk.download("stopwords", download_dir=nltk_data_path)


# Initialize Groq model
groq_model = init_chat_model("llama3-8b-8192", model_provider="groq")


def generate_enhanced_flashcards(text: str, num_questions: int = 10) -> List[Dict]:
    """Generate diverse and meaningful flashcards with controlled output."""
    clean_text = " ".join(text.strip().split())

    # Configure RAKE for diverse keyword selection
    r = Rake(
        stopwords=nltk.corpus.stopwords.words("english"),
        min_length=2,
        max_length=8,  # Allow slightly longer phrases
        ranking_metric=0.8,
    )  # Quality threshold

    r.extract_keywords_from_text(clean_text)
    keywords = [
        phrase for (score, phrase) in r.get_ranked_phrases_with_scores() if score > 3.0
    ]  # Quality filter

    flashcards = []
    used_phrases = set()  # Track used phrases to avoid repetition

    for phrase in keywords:
        if len(flashcards) >= num_questions:
            break

        if phrase.lower() not in used_phrases:
            used_phrases.add(phrase.lower())
            context = find_context(clean_text, phrase)

            if context:
                try:
                    prompt = f"""Generate exactly one flashcard about '{phrase}':
                    Context: {context}
                    
                    - Create a specific, non-repetitive question
                    - Answer must be under 40 words
                    - Focus on key concepts in the context
                    - Avoid generic questions like "What is X?"
                    
                    Format strictly as:
                    Q: [question]
                    A: [answer]"""

                    response = groq_model.invoke(prompt)
                    content = (
                        response.content
                        if hasattr(response, "content")
                        else str(response)
                    )

                    # Extract with regex for reliability
                    import re

                    match = re.search(r"Q:\s*(.*?)\nA:\s*(.*)", content, re.DOTALL)

                    if match:
                        question = match.group(1).strip()
                        answer = match.group(2).strip()[:200]  # Slightly longer answers

                        # Ensure question is unique
                        if not any(q["question"] == question for q in flashcards):
                            flashcards.append({"question": question, "answer": answer})

                except Exception as e:
                    logging.error(f"Error processing '{phrase}': {str(e)}")

    return flashcards[:num_questions]  # Final safeguard


def find_context(text: str, phrase: str, window: int = 2) -> str:
    """Get context with surrounding sentences."""
    sentences = sent_tokenize(text)
    for i, sentence in enumerate(sentences):
        if phrase in sentence:
            start = max(0, i - window)
            end = min(len(sentences), i + window + 1)
            return " ".join(sentences[start:end])
    return ""
