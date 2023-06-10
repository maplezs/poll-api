import nanoid
from datetime import datetime
from flask import request, jsonify, url_for, render_template, flash

from script import app, db
from script.models import PlaceForm, Poll

@app.route('/poll/<string:id>', methods=['GET', 'POST'])
def poll_submit(id):
    place = PlaceForm.query.first_or_404(id)
    if request.method == 'GET':
        agree = 0
        disagree = 0
        polls = Poll.query.filter(Poll.place_id==id).all()
        for poll in polls:
            if poll.agree:
                agree += 1
            else:
                disagree += 1 
        return render_template('index.html', place=place, polls=polls, agree=agree, disagree=disagree)
    else:
        poll = Poll(place_id=id, voter_name=request.form['name'], agree=1 if request.form['vote']=='1' else 0, created_at=datetime.now())
        db.session.add(poll)
        db.session.commit()
        agree = 0
        disagree = 0
        polls = Poll.query.filter(Poll.place_id==id).all()
        for poll in polls:
            if poll.agree:
                agree += 1
            else:
                disagree += 1 
        flash('Vote berhasil dilakukan!', category='success')
        return render_template('index.html', place=place, polls=polls, agree=agree, disagree=disagree) 

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