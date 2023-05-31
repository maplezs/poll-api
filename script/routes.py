from flask import request, render_template

from script import app, db
from script.models import Polling

@app.route('/poll/<id>', methods=['POST'])
def poll(id):

    content = request.json
    
    name = content['name']
    link = content['link']
    address = content['address']

    polling = Polling(
        id=id,
        name=name,
        link=link,
        address=address
    )

    db.session.add(polling)
    db.session.commit()

    return render_template('home.html', name=name, link=link, address=address, id=id)