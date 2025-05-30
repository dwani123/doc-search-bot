import React, { useState } from "react";
import axios from "axios";

const QueryForm = () => {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuery = async () => {
    const res = await axios.post("http://localhost:5000/query", {
      query: query
    });
    setAnswer(res.data.response);
  };

  return (
    <div className="p-4">
      <textarea value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Ask your question..." />
      <button onClick={askQuery}>Ask</button>
      <p><strong>Response:</strong> {answer}</p>
    </div>
  );
};

export default QueryForm;
