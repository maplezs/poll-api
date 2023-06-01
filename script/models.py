from script import db

class User(db.Model):

    __tablename__ = 'user_table'

    id = db.Column(db.String(16), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    photo_url = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.Date)
    updatedAt = db.Column(db.Date)

    place = db.relationship('Place', backref='user', lazy=True)

    def __repr__(self):
        return f"Place('{self.id, self.name}')"

class Place(db.Model):
    
    __tablename__ = 'place_table'

    id = db.Column(db.String(16), primary_key=True)
    user_id = db.Column(db.String(16), db.ForeignKey('user_table.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.Date)

    poll = db.relationship('Poll', backref='place', lazy=True)
 
    def __repr__(self):
        return f"Place('{self.id, self.name}')"


class Poll(db.Model): 
    
    __tablename__ = 'poll_table'

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.String(16), db.ForeignKey('place_table.id'), nullable=False)
    createdAt = db.Column(db.Date)

    def __repr__(self):
        return f"Poll('{self.id}', '{self.createdAt}')"
