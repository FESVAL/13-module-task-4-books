from flask import Flask, request, render_template, redirect, url_for
from app import app, db
from app.models import Author, Book, Borrow


def books_add():
    author = Author(name="Марк Лутц", id=1)
    book = Book(title="Изучаем Python", author_id=author.id, book_id=1)
    borrow = Borrow(borrower="читач_1", book_id=book.id)
    db.session.add(author, book, borrow)
        

    author = Author(name="Бизли и Джонс", id=1)
    book = Book(title="Python. Книга рецептов", author_id=author.id, book_id=1)
    borrow = Borrow(borrower="читач_2", book_id=book.id)
    db.session.add(author, book, borrow)
        
    db.session.commit()

  
 
@app.route("/books/", methods=["GET", "POST"]) 
def site():
    if request.method == "GET": 
        books_add()        
        authors = Author.query.all()
        books = Book.query.all()
        borrows = Borrow.query.all()
        return render_template("books.html", authors=authors, books=books, borrows=borrows)
    else: 
        return redirect(url_for("books_add"))





    



