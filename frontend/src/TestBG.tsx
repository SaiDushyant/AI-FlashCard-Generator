import React from "react";

const TestBG: React.FC = () => {
  return (
    <div className="relative min-h-screen overflow-hidden">
      {/* Background Animation */}
      <div className="absolute inset-0 -z-10">
        <div
          className="absolute inset-0 opacity-50 animate-gradient"
          style={{
            backgroundImage: "linear-gradient(45deg, #bfdbfe, #e0d7f5)",
          }}
        ></div>
      </div>

      <div className="relative z-10 flex items-center justify-center min-h-screen">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-gray-800">
            Test Animated Background
          </h1>
          <p className="mt-4 text-lg text-gray-600">
            This page is used to test the animated gradient background.
          </p>
        </div>
      </div>
    </div>
  );
};

export default TestBG;
