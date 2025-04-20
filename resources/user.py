from flask import request
from flask_restful import Resource
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return [
            {
                "id": u.id,
                "email": u.email,
                "created_at": u.created_at.isoformat(),
            }
            for u in users
            ], 200

    def post(self):
        data = request.get_json()
        email = data.get("email")

        if not email:
            return {
                "message": "Email is required."
            }, 400
        
        if User.query.filter_by(email=email).first():
            return {
                "message": "User alredy exists."
            }, 409
        
        user = User(email=email)
        db.session.add(user)
        db.session.commit()
        return {
            "id": user.id,
            "email": user.email
        }, 201
    
