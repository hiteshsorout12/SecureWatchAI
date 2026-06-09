from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.user import User

Session = sessionmaker(bind=engine)


def create_user(name, email, role):

    session = Session()

    user = User(
        name=name,
        email=email,
        role=role
    )

    session.add(user)
    session.commit()

    print("User Created Successfully")

    session.close()