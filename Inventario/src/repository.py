from models import User, Producto, Vuelo, db

class UserRepository:
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create_user(username, email, password, role, cedula):
        new_user = User(username=username, email=email, password=password, role=role, cedula=cedula)
        db.session.add(new_user)
        db.session.commit()
