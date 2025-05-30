import React, { useState } from "react";
import axios from "axios";

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    await axios.post("http://localhost:5000/upload", formData);
    alert("File uploaded!");
  };

  return (
    <div className="p-4">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default UploadForm;
