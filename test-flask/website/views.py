from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Todo
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST':
    note = request.form.get('note')

    if len(note) < 1:
      flash('Note is too short!', category='error')
    else:
      new_note = Note(data=note, user_id=current_user.id)
      db.session.add(new_note)
      db.session.commit()
      flash('Note added!', category='success')

  return render_template("home.html", user=current_user)


@views.route("/todo", methods=["GET", "POST"])
@login_required
def todo():
  if request.method == "POST":
    todo = request.form.get("todo")

    new_todo = Todo(data=todo, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    flash("To do added!", category="success")


  return render_template("todo.html", user=current_user)



@views.route('/delete-note', methods=['POST'])
def delete_note():
  note = json.loads(request.data)
  noteId = note['noteId']
  note = Note.query.get(noteId)
  if note:
    if note.user_id == current_user.id:
      db.session.delete(note)
      db.session.commit()

  return jsonify({})

@views.route('/delete-todo', methods=['POST'])
def delete_todo():
  todo = json.loads(request.data)
  todoId = todo['todoId']
  todo = Todo.query.get(todoId)
  if todo:
    if todo.user_id == current_user.id:
      db.session.delete(todo)
      db.session.commit()

  return jsonify({})

@views.route("/change-done", methods=["POST"])
def change_todo():
  todo = json.loads(request.data)
  todoId = todo["todoId"]
  todo = Todo.query.get(todoId)
  if todo:
    if todo.user_id == current_user.id:
      todo.done = not todo.done
      db.session.commit()

  return ""