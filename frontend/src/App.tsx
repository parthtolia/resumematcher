import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import UploadResume from "./pages/UploadResume";
import MatchResults from "./pages/MatchResults";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/upload" element={<UploadResume />} />
        <Route path="/match" element={<MatchResults />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;