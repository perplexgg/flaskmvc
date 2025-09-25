from App.database import db
from App.models.user import User

class Staff(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    department = db.Column(db.String, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity':'staff',
    }
