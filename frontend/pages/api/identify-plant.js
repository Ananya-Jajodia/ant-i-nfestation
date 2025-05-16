import { spawn } from "child_process";
import fs from "fs";
import path from "path";
import formidable from "formidable";

export const config = {
  api: {
    bodyParser: false,
  },
};

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).send("Method Not Allowed");

  const form = formidable({ multiples: false });

  form.parse(req, async (err, fields, files) => {
    if (err || !files.image) {
      return res.status(400).json({ error: "Image upload failed" });
    }

    const imagePath = files.image[0].filepath;

    const pythonScriptPath = path.resolve(process.cwd(), "../backend/identifier/identify_wrapper.py");

    const python = spawn("/Applications/anaconda3/envs/ollama_env/bin/python", [pythonScriptPath, imagePath]);

    let result = "";

    python.stdout.on("data", (data) => {
      result += data.toString();
    });

    python.stderr.on("data", (data) => {
      console.error("Python stderr:", data.toString());
    });

    python.on("close", (code) => {
      if (code === 0) {
        res.status(200).json({ plantName: result.trim() });
      } else {
        res.status(500).json({ error: "Python script failed" });
      }
    });
  });
}
