import { useState } from "react";

function MatchResults() {
  const [jdText, setJdText] = useState("");
  const [results, setResults] = useState<any[]>([]);

  const match = async () => {
  if (!jdText) return alert("Please enter JD text");

  try {
    const res = await fetch("http://localhost:8000/match", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ jd_text: jdText }),
    });
    const data = await res.json();
    setResults(data.results || []);
  } catch (err) {
    console.error(err);
    alert("Error matching JD");
  }
};

  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold mb-4 text-primary">Match Job Description</h2>
      <textarea
        className="border p-2 w-full"
        rows={5}
        value={jdText}
        onChange={(e) => setJdText(e.target.value)}
        placeholder="Paste your JD here..."
      />
      <button
        className="mt-4 bg-accent text-white px-4 py-2 rounded hover:bg-blue-700"
        onClick={match}
      >
        Match
      </button>

      <div className="mt-6 space-y-4">
        {results.map((r) => (
          <div key={r.file_name} className="border p-4 rounded shadow-sm">
            <div className="font-semibold text-primary">{r.file_name}</div>
            <div>Skill Score: {r.skill_score || "N/A"}%</div>
            <div>Semantic Score: {r.semantic_score || "N/A"}%</div>
            <div>Overall Score: {r.final_score || "N/A"}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MatchResults;