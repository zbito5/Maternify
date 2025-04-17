# Maternify Backend - Flask Starter

from flask import Flask, jsonify, request

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Maternify API"})

# Example route for appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify([
        {"id": 1, "date": "2025-05-01", "type": "Prenatal Checkup"},
        {"id": 2, "date": "2025-05-15", "type": "Ultrasound"}
    ])

# Example route to post user data
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    return jsonify({"status": "success", "data_received": data})

if __name__ == '__main__':
    app.run(debug=True)
