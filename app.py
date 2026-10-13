from flask import Flask, render_template, request, jsonify
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json

app = Flask(__name__)

MODEL = "gemma2:2b"
OLLAMA_URL = "http://localhost:11434/api/chat"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}

    product = str(data.get("product", "")).strip()[:150]
    features = str(data.get("features", "")).strip()[:800]
    style = str(data.get("style", "Friendly")).strip()

    if not product:
        return jsonify({"error": "Enter a product name."}), 400

    if style not in ["Professional", "Friendly", "Catchy"]:
        style = "Friendly"

    prompt = f"""
Write an attractive online product description.

Product: {product}
Features: {features or "No features supplied"}
Style: {style}

Use only supplied facts. Do not invent prices or claims.
Include a heading, short description and call to action.
Keep it under 150 words.
"""

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are QuickSell AI, a helpful product copywriting assistant."
            },
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    req = Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(req, timeout=180) as response:
            result = json.loads(response.read().decode("utf-8"))

        description = result.get("message", {}).get("content", "").strip()

        if not description:
            return jsonify({"error": "AI returned an empty response. Try again."}), 502

        return jsonify({
            "description": description,
            "model": MODEL
        })

    except HTTPError as e:
        return jsonify({"error": f"Ollama returned error {e.code}."}), 502

    except URLError:
        return jsonify({
            "error": "Cannot connect to Ollama. Make sure Ollama is running."
        }), 503

    except Exception:
        app.logger.exception("Generation failed")
        return jsonify({
            "error": "Generation failed. Check Ollama and the installed model."
        }), 500


if __name__ == "__main__":
    app.run(debug=False, port=5000)
