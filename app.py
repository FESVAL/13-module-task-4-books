from app import app, db
from flask import Flask, request, render_template, redirect, url_for
from app.models import Author, Book, Borrow

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Author": Author,
       "Book": Book,
       "Borrow": Borrow
   }

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
    if request.method == "POST": 
        books_add()        
        authors = Author.query.all()
        books = Book.query.all()
        borrows = Borrow.query.all()

    return render_template("books.html", authors=authors, books=books, borrows=borrows)


if __name__ == "__main__":
  app.run(debug=True)