import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState("");
  const [extractedText, setExtractedText] = useState(""); // New state for extracted text

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      alert("Please upload a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:5000/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setResponse(res.data.message);
      setExtractedText(res.data.extracted_text); // Set the extracted text
    } catch (error) {
      console.error(error);
      setResponse("Error uploading file");
      setExtractedText(""); // Clear extracted text on error
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Receipt Upload</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {response && <p>{response}</p>}
      {extractedText && (
        <div>
          <h2>Extracted Text:</h2>
          <p>{extractedText}</p>
        </div>
      )}
    </div>
  );
}

export default App;
