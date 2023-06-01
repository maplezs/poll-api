import nanoid
from datetime import datetime
from flask import request, jsonify, url_for, render_template

from script import app, db
from script.models import Place, Poll

@app.route('/poll/<string:id>', methods=['GET', 'POST'])
def poll_submit(id):
    place = Place.query.filter_by(id=id).first_or_404()
    if request.method == 'GET':
        place = Place.query.get_or_404(id)
        poll_number = Poll.query.filter(Poll.place_id == id).count()
        return render_template('poll.html', place=place, poll_number=poll_number)
    else:
        poll = Poll(place_id=id, createdAt=datetime.now())
        db.session.add(poll)
        db.session.commit()
        place = Place.query.get_or_404(id)
        poll_number = Poll.query.filter(Poll.place_id == id).count()
        return jsonify({
            'status': 'sukses',
            'message': 'Voting berhasil dilakukan!',
            'data': poll_number
        }) 

@app.route('/poll/create', methods=['POST'])
def poll_create():
    id = nanoid.generate(size=16)
    data = request.json
    place = Place(user_id=data['user_id'], id=id, name=data['name'], address=data['address'], createdAt=datetime.now())
    db.session.add(place)
    db.session.commit()
    return jsonify({
        'status': 'sukses',
        'message': 'Form poll berhasil dibuat!',
        'data': f'localhost:5000/poll/{id}'
    })

@app.route('/test')
def test():
    return render_template('hello.html')