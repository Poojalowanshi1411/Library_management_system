from models import Book,member,Transaction
from database import session
from datetime import date
def add_books(title,author,isbn,count):
    print("Adding books--------->")
    book=Book(title=title,author=author,isbn=isbn,count=count)
    session.add(book)
    session.commit()

def get_book():
    return session.query(Book).all()

def add_members(name,email):
    print("Adding Members--------->")
    membe=member(name=name,email=email)
    session.add(membe)
    session.commit()

def get_member():
    return session.query(member).all()
def Issue_book(book_id, member_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book and book.count > 0:
        # Explicitly set return_date to None if not available
        transaction = Transaction(
            book_id=book_id,
            member_id=member_id,
            issue_date=date.today(),
            return_date=None  # Explicitly set return_date to None
        )
        book.count -= 1
        session.add(transaction)
        session.commit()
        print("Book Issued")
    else:
        print("Book Not Available for issue")


def return_book(transaction_id):
    transaction=  session.query(Transaction).filter_by(id=transaction_id).first()
    if transaction and not transaction.return_date:
        book=session.query(Book).filter_by(id=transaction.book_id).filter_by()
        book.count=+1
        print("Book Returned")
        session.commit()
    else:
        print("Books Already Returned")

def view_transaction(member_id):
    return session.query(Transaction).filter_by(member_id=member_id).all()
    