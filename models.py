from sqlalchemy import Column, Integer , String,ForeignKey ,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base =declarative_base()


#tables

class Book(Base):
    __tablename__ ='books'
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    author=Column(String,nullable=False)
    isbn=Column(String,nullable=False)
    count=Column(Integer,nullable=False,default=1)

class member(Base):
    __tablename__='members'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    
class Transaction(Base):
    __tablename__ = 'Transactions'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    issue_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)  # Nullable column

    book = relationship('Book')
    member = relationship('member')
