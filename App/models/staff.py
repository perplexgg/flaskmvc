from App.database import db
from .user import User

class Staff(User):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    department = db.Column(db.String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'staff',
    }
