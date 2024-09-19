from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String)
    year_published = Column(Integer)
    loans = relationship('Loan', back_populates='book')

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', genre='{self.genre}', year_published={self.year_published})>"


class Member(Base):
    __tablename__ = 'members'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    membership_date = Column(Date, default=datetime.date.today)
    loans = relationship('Loan', back_populates='member')

    def __repr__(self):
        return f"<Member(name='{self.name}', email='{self.email}')>"


class Loan(Base):
    __tablename__ = 'loans'
    
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    loan_date = Column(Date, default=datetime.date.today)
    return_date = Column(Date, nullable=True)

    book = relationship('Book', back_populates='loans')
    member = relationship('Member', back_populates='loans')

    def __repr__(self):
        return (f"<Loan(book_id={self.book_id}, member_id={self.member_id}, "
                f"loan_date={self.loan_date}, return_date={self.return_date})>")


# Create the database engine
engine = create_engine('sqlite:///database.db')

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()