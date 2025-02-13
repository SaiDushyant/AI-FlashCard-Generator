// import { Link, Route, BrowserRouter as Router, Routes } from "react-router-dom";
// import TestBG from "./TestBG";
// Assume you have a Home component for your main page
// import Home from "./Home";

import FlashcardGenerator from "./FlashcardGenerator";

function App() {
  return (
    <FlashcardGenerator />

    // <Router>
    //   <nav className="p-4 bg-gray-100">
    //     <Link to="/" className="mr-4 text-blue-600 hover:underline">
    //       Home
    //     </Link>
    //     <Link to="/testbg" className="text-blue-600 hover:underline">
    //       Test BG
    //     </Link>
    //   </nav>
    //   <Routes>
    //     <Route path="/" element={<Home />} />
    //     <Route path="/testbg" element={<TestBG />} />
    //   </Routes>
    // </Router>
  );
}

export default App;
