export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Only POST requests allowed" });
  }

  try {
    const flaskRes = await fetch("http://localhost:5050/api/plant-chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(req.body),
    });

    const contentType = flaskRes.headers.get("content-type");
    if (contentType && contentType.includes("application/json")) {
      const data = await flaskRes.json();
      res.status(200).json(data);
    } else {
      const text = await flaskRes.text();
      res.status(500).json({ error: "Non-JSON response", details: text });
    }
  } catch (err) {
    console.error("Error proxying to Flask:", err);
    res.status(500).json({ error: "Failed to contact backend", details: err.message });
  }
}
