from flask import request
from datetime import datetime, timezone
from flask_restful import Resource
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class Register(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        if not password:
            return {
                "message": "Password is required."
            }, 400
        
        if User.query.filter_by(email=email).first():
            return {
                "message": "Email already registered."
            }, 400
        hashed_pw = generate_password_hash(password)
        new_user = User(email=email, password=hashed_pw, created_at=datetime.now(timezone.utc))
        db.session.add(new_user)
        db.session.commit()
        return {
            "message": "User created successfully."
        }, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return {
                "message": "Invalid credentials."
            }, 401
        
        access_token = create_access_token(identity=str(user.id))
        return {
                "access_token": access_token
            }, 200

class MeResource(Resource):
    @jwt_required()
    def get(self):
        user_id = int(get_jwt_identity())
        user = User.query.get_or_404(user_id)
        return {
            "id": user.id,
            "email": user.email,
            "created_at": user.created_at.isoformat()
        }, 200
