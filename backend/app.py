from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, db
import uuid
from datetime import datetime

# =========================
# INITIALIZE FLASK
# =========================
app = Flask(__name__)
CORS(app)

# =========================
# INITIALIZE FIREBASE
# =========================
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://emergix-99208-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# =========================
# 1️⃣ USER REGISTRATION
# =========================
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    
    user_id = str(uuid.uuid4())
    
    user_data = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "password": data.get("password"),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    db.reference(f'users/{user_id}').set(user_data)

    return jsonify({
        "message": "User registered successfully",
        "user_id": user_id
    })


# =========================
# 2️⃣ USER LOGIN
# =========================
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    
    users_ref = db.reference("users").get()

    if users_ref:
        for uid, user in users_ref.items():
            if user.get("email") == data.get("email") and user.get("password") == data.get("password"):
                return jsonify({
                    "message": "Login successful",
                    "user_id": uid,
                    "name": user.get("name")
                })

    return jsonify({"message": "Invalid credentials"}), 401


# =========================
# 3️⃣ CREATE LOAN REQUEST
# =========================
@app.route('/create-loan', methods=['POST'])
def create_loan():
    data = request.json
    
    loan_id = str(uuid.uuid4())
    
    loan_data = {
        "user_id": data.get("user_id"),
        "amount": data.get("amount"),
        "reason": data.get("reason"),
        "status": "pending",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    db.reference(f'loans/{loan_id}').set(loan_data)

    return jsonify({
        "message": "Loan request created",
        "loan_id": loan_id
    })


# =========================
# 4️⃣ EMERGENCY REQUEST
# =========================
@app.route('/emergency', methods=['POST'])
def emergency():
    data = request.json
    
    request_id = str(uuid.uuid4())
    
    emergency_data = {
        "user_id": data.get("user_id"),
        "location": data.get("location"),
        "voice_verified": True,
        "status": "pending",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    db.reference(f'emergency_requests/{request_id}').set(emergency_data)

    return jsonify({
        "message": "Emergency request sent",
        "request_id": request_id
    })


# =========================
# 5️⃣ CHECK LOAN STATUS  (NEW ADDED)
# =========================
@app.route('/check-status/<user_id>', methods=['GET'])
def check_status(user_id):

    loans_ref = db.reference("loans").get()

    if loans_ref:
        for loan_id, loan in loans_ref.items():
            if loan.get("user_id") == user_id:
                return jsonify({
                    "loan_id": loan_id,
                    "amount": loan.get("amount"),
                    "reason": loan.get("reason"),
                    "status": loan.get("status"),
                    "timestamp": loan.get("timestamp")
                })

    return jsonify({
        "message": "No loan found for this user"
    })


# =========================
# RUN SERVER
# =========================
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)