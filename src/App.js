import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import AdminPage from "./pages/AdminPage";
import UserPage from "./pages/UserPage";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/admin">Admin</Link> | <Link to="/user">User</Link>
      </nav>
      <Routes>
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/user" element={<UserPage />} />
      </Routes>
    </Router>
  );
}

export default App;
