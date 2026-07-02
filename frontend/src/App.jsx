import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import BlockPage from "./pages/BlockPage";
import SearchPage from "./pages/SearchPage";
import FacultyPage from "./pages/FacultyPage";
import RoomPage from "./pages/RoomPage";
import SectionPage from "./pages/SectionPage";
import DepartmentPage from "./pages/DepartmentPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
         <Route path="/block/:slug" element={<BlockPage />} /> 
        <Route path="/search" element={<SearchPage />} />
        <Route path="/faculty/:id" element={<FacultyPage />} />
<Route path="/room/:id" element={<RoomPage />} />
<Route path="/section/:id" element={<SectionPage />} />
<Route path="/department/:id" element={<DepartmentPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;