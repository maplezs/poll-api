import nanoid
from datetime import datetime
from flask import request, jsonify, url_for, render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required

from script import app, db, bcrypt
from script.models import PlaceForm, Poll, User
from script.forms import LoginForm, DeleteUserForm

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
        return render_template('/poll/index.html', place=place, polls=polls, agree=agree, disagree=disagree)
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
        return render_template('/poll/index.html', place=place, polls=polls, agree=agree, disagree=disagree) 

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

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Selamat datang, {user.name}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('admin_user'))
        else:
            flash('Login gagal. Isi data email dan password dengan benar!', 'danger')
    return render_template('login.html', form=form)

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_required
@app.route('/admin/user', methods=['GET', 'POST'])
def admin_user():
    form = DeleteUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.first_or_404(form.user_id.data)
            db.session.delete(user)
            db.session.commit()
            flash(f'Pengguna {user.name} berhasil dihapus dari sistem!', 'success')
            return redirect('/admin/user')
        else:
            flash(f'{form.errors}', 'danger')
            return redirect('/admin/user')
    users = User.query.filter_by(role_id = 2).all()
    return render_template('/admin/index.html', users=users, form=form, user=current_user)

@app.route('/404')
def error_404():
    return render_template('404.html')