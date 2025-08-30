from flask import Flask, jsonify

app = Flask(__name__)

# API endpoint for ESP8266
@app.route("/UiV4Qr5Udbpr3Jm/L1", methods=["GET"])
def get_data():
    data = {
        "shelf": "A1",
        "price": 120.50,
        "discount": 10
    }
    return jsonify(data)

# Root test page
@app.route("/")
def home():
    return "<h2>ESP8266 Flask API running on Render 🚀</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
