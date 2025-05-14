from flask import request, jsonify
from app.models import Book
from app import db

def add_book():
    data = request.get_json()
    new_book = Book(**data)
    db.sesion.add(new_book)
    db.sesion.commit()
    return jsonify(
        {"message": "Livro adicionado com sucesso!"}), 201
    
    