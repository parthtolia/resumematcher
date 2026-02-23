import { useState } from "react";

function UploadResume() {
  const [file, setFile] = useState<File | null>(null);

  const upload = async () => {
    if (!file) return alert("Please select a file");
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://localhost:8000/upload-resume", {
        method: "POST",
        body: formData,
      });

      if (res.ok) alert("Uploaded successfully!");
      else alert("Upload failed!");
    } catch (err) {
      console.error(err);
      alert("Error uploading file");
    }
  };

  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold mb-4 text-primary">Upload Resume</h2>
      <input
        type="file"
        onChange={(e) => e.target.files && setFile(e.target.files[0])}
        className="border p-2 w-full"
      />
      <button
        className="mt-4 bg-accent text-white px-4 py-2 rounded hover:bg-blue-700"
        onClick={upload}
      >
        Upload Resume
      </button>
    </div>
  );
}

export default UploadResume;