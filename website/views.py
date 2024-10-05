from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
# adding this decorator function because we cannot get to the home page unless we are logged in
def home():
    # pass
    # return "<h1>Test</h1>"
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note)<1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added.', category='success')

    return render_template("home.html", user = current_user)

@views.route('/delete-note', methods = ['POST'])
def delete_note():
    # data does not come here as a form but as a data parameter of a request object.
    # thats why we need to load it as a json.
    note = json.loads(request.data)
    # noteId data comes from the index.js file. And this converts it into a python dictionary object
    noteId = note['noteId']
    # from the dictionary object we are accessing the noteId value.
    note = Note.query.get(noteId)
    # look for the note that has that ID.
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})
    # just returning an empty response because it is mandatory to return something.
    # here we are just jsonifying an empty python dictionary.
    # turning it into a json object to return
    # try emptying all the cache and do a hard reload on the website. Sometimes it fixes all the issues.
    