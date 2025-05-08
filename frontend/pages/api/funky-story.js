export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Only POST requests allowed" });
  }

  try {
    const flaskRes = await fetch("http://localhost:5050/api/funky-story", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(req.body),
    });

    const data = await flaskRes.json();
    res.status(200).json(data);
  } catch (err) {
    console.error("Error proxying to Flask:", err);
    res.status(500).json({ error: "Failed to generate story" });
  }
}
