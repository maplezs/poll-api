from script import db

class Polling(db.Model): 
    __tablename__ = 'polling_table'

    id = db.Column(db.String(16), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False, unique=True)
    link = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"Polling('{self.id}', '{self.name}')"
