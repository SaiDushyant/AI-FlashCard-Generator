import { useState } from "react";
import { ClipLoader } from "react-spinners";

function FlashcardGenerator() {
  const [file, setFile] = useState<File | null>(null);

  interface Flashcard {
    question: string;
    answer: string;
  }

  const [flashcards, setFlashcards] = useState<Flashcard[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState(1);
  const flashcardsPerPage = 5;

  // Custom type for file change event
  interface FileChangeEvent extends React.ChangeEvent<HTMLInputElement> {
    target: HTMLInputElement & EventTarget;
  }

  const handleFileChange = (e: FileChangeEvent) => {
    if (e.target.files) {
      const selectedFile = e.target.files[0];
      // Corrected file type check: make sure to compare to the correct MIME type string.
      if (selectedFile.type !== "application/pdf") {
        setError("Please upload a valid PDF file.");
        setFile(null);
      } else {
        setError(null);
        setFile(selectedFile);
      }
    }
  };

  const handleSubmit = async () => {
    if (!file) {
      setError("Please select a PDF file.");
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload-pdf/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to upload PDF. Please try again.");
      }

      const data = await response.json();
      setFlashcards(data.flashcards);
      setCurrentPage(1); // Reset to first page after new upload
    } catch {
      setError("An error occurred while processing the PDF. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  // Pagination logic
  const indexOfLastFlashcard = currentPage * flashcardsPerPage;
  const indexOfFirstFlashcard = indexOfLastFlashcard - flashcardsPerPage;
  const currentFlashcards = flashcards.slice(
    indexOfFirstFlashcard,
    indexOfLastFlashcard
  );

  const paginate = (pageNumber: number) => setCurrentPage(pageNumber);

  return (
    <div className="relative min-h-screen overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute inset-0 bg-gradient-to-br from-blue-200 to-purple-200 opacity-30 blur-3xl animate-gradient"></div>
      </div>

      {/* Custom Keyframes */}
      <style>{`
        @keyframes gradientMove {
          0% { background-position: 0% 50%; }
          50% { background-position: 100% 50%; }
          100% { background-position: 0% 50%; }
        }
        .animate-gradient {
          background-size: 200% 200%;
          animation: gradientMove 15s ease infinite;
        }
      `}</style>

      <div className="max-w-4xl mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold text-center text-gray-800 mb-8">
          PDF to Flashcards
        </h1>

        {/* File Upload */}
        <div className="bg-white p-6 rounded-lg shadow-lg mb-8 transition-transform transform">
          <div className="mb-4">
            <input
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
              className="file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
          </div>
          <button
            onClick={handleSubmit}
            disabled={loading || !file}
            className="w-full bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 disabled:bg-blue-300 transition duration-300"
          >
            {loading ? (
              <ClipLoader size={20} color="#ffffff" />
            ) : (
              "Generate Flashcards"
            )}
          </button>
          {error && <p className="text-red-500 mt-2 text-center">{error}</p>}
        </div>

        {/* Flashcards */}
        {flashcards.length > 0 && (
          <div className="bg-white p-6 rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold text-gray-800 mb-6">
              Generated Flashcards
            </h2>
            <div className="space-y-4">
              {currentFlashcards.map((card, index) => (
                <div
                  key={index}
                  className="p-4 border border-gray-200 rounded-lg hover:shadow-xl transition-shadow"
                >
                  <p className="font-semibold text-blue-600">
                    Q: {card.question}
                  </p>
                  <p className="mt-2 text-gray-700">A: {card.answer}</p>
                </div>
              ))}
            </div>

            {/* Pagination */}
            <div className="flex flex-wrap justify-center mt-6 gap-2">
              {Array.from(
                { length: Math.ceil(flashcards.length / flashcardsPerPage) },
                (_, i) => (
                  <button
                    key={i + 1}
                    onClick={() => paginate(i + 1)}
                    className={`px-4 py-2 rounded-lg transition-colors ${
                      currentPage === i + 1
                        ? "bg-blue-600 text-white"
                        : "bg-blue-50 text-blue-600 hover:bg-blue-100"
                    }`}
                  >
                    {i + 1}
                  </button>
                )
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default FlashcardGenerator;
