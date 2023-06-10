from script import db

class User(db.Model):

    __tablename__ = 'user_table'

    id = db.Column(db.String(16), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    photo_url = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

    place_form_user = db.relationship('PlaceForm', backref='user', lazy=True)

    def __repr__(self):
        return f"Place('{self.id, self.name}')"

class PlaceCategory(db.Model):

    __tablename__ = 'place_category_table'

    id = db.Column(db.String(16), primary_key=True)
    place_category = db.Column(db.String(255), nullable=False, unique=True)

    place_form_cat = db.relationship('PlaceForm', backref='placeCat', lazy=True)


    def __repr__(self):
        return f"Place('{self.id, self.place_category}')"

class PlaceForm(db.Model):
    
    __tablename__ = 'place_form_table'

    id = db.Column(db.String(16), primary_key=True)
    user_id = db.Column(db.String(16), db.ForeignKey('user_table.id'), nullable=False)
    category_id = db.Column(db.String(16), db.ForeignKey('place_category_table.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    photo_url = db.Column(db.String(255))
    rate_score = db.Column(db.Float, nullable=False)
    num_of_voters = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date)

    poll = db.relationship('Poll', backref='place', lazy=True)
 
    def __repr__(self):
        return f"Place('{self.id, self.name}')"


class Poll(db.Model): 
    
    __tablename__ = 'poll_table'

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.String(16), db.ForeignKey('place_form_table.id'), nullable=False)
    voter_name = db.Column(db.String(255), nullable=False)
    agree = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.Date)

    def __repr__(self):
        return f"Poll('{self.id}', '{self.created_at}')"
