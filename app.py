from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Initial data
data = {
    "shelf": "A1","Product": "A1",
    "price": 120.50,
    "discount": 10
}

# Home route with input form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get data from the form and update
        data["shelf"] = request.form["shelf"]
        data["Product"] = request.form["Product"]
        data["price"] = float(request.form["price"])
        data["discount"] = int(request.form["discount"])
    
    return render_template("index.html", data=data)

# API endpoint to fetch data
@app.route("/UiV4Qr5Udbpr3Jm/L1", methods=["GET"])
def get_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

