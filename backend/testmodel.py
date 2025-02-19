from model import FlashcardGenerator


def test_text_extraction():
    # Test PDF text extraction
    test_text = FlashcardGenerator.extract_text_from_pdf("me5.pdf")

    # Basic type and length checks
    assert isinstance(test_text, str)
    assert len(test_text) > 0

    # Print first 200 characters for visual verification
    print("\nExtracted Text (first 200 chars):")
    print(test_text[:200] + "...")

    # Return the extracted text for use in the next test
    return test_text


def test_flashcard_generation():
    # First, extract text from the PDF
    extracted_text = test_text_extraction()

    # Ensure text extraction worked
    assert isinstance(extracted_text, str)
    assert len(extracted_text) > 0

    # Generate flashcards from the extracted text
    flashcards = FlashcardGenerator.generate_flashcards(extracted_text)

    # Basic structure checks
    assert isinstance(flashcards, list)
    assert len(flashcards) > 0
    assert "question" in flashcards[0]
    assert "answer" in flashcards[0]

    # Print generated flashcards for visual verification
    print("\nGenerated Flashcards:")
    for i, card in enumerate(flashcards, 1):
        print(f"\nCard {i}:")
        print(f"Q: {card['question']}")
        print(f"A: {card['answer']}")

    # Check if specific expected content appears in flashcards


if __name__ == "__main__":
    print("Running tests...")
    test_flashcard_generation()  # This will run both text extraction and flashcard generation
    print("\nAll tests completed!")
