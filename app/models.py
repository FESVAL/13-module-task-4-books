from datetime import datetime
from app import db

class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), index=True, unique=True)
   books = db.relationship("Book", backref="author", lazy="dynamic")
   def __str__(self):
       return f"<Autor {self.name}>"
   
class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), index=True, unique=True)
   date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   autor_id = db.Column(db.Integer, db.ForeignKey('author.id'))
   autors = db.relationship("Author", backref="book", lazy="dynamic")
   def __str__(self):
       return f"<Book {self.id} {self.title}"
   

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(100), index=True)
    borrow_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    books = db.relationship("Book", backref="borrow", lazy="dynamic")

    def __str__(self):
        return f"< Borrow {self.id} {self.borrower}>"