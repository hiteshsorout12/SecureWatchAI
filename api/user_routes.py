from flask import Blueprint
from flask import jsonify
from flask import request

from models.user import User
from database.connection import engine

from sqlalchemy.orm import sessionmaker

user_bp = Blueprint(
    "users",
    __name__
)

Session = sessionmaker(bind=engine)


# GET ALL USERS
@user_bp.route("/users", methods=["GET"])
def get_users():

    session = Session()

    users = session.query(User).all()

    result = []

    for user in users:

        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        })

    session.close()

    return jsonify(result)


# CREATE USER
@user_bp.route("/users", methods=["POST"])
def create_user_api():

    data = request.get_json()

    session = Session()

    user = User(
        name=data["name"],
        email=data["email"],
        role=data["role"]
    )

    session.add(user)
    session.commit()

    session.close()

    return jsonify({
        "message": "User Created Successfully"
    })