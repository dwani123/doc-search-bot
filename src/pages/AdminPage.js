import React from "react";
import UploadForm from "../components/UploadForm";
import QueryForm from "../components/QueryForm";

const AdminPage = () => (
  <div>
    <h2>Admin Panel</h2>
    <UploadForm />
    <QueryForm />
  </div>
);

export default AdminPage;
