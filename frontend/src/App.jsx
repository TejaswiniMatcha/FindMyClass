import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import BlockPage from "./pages/BlockPage";
import SearchPage from "./pages/SearchPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
         <Route path="/block/:slug" element={<BlockPage />} /> 
        <Route path="/search" element={<SearchPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;