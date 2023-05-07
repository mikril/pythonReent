from sqlalchemy.ext.hybrid import hybrid_property

if __name__ == "__main__":
    from sqlalchemy import  DATE, create_engine, Column, Integer, String,FLOAT, BOOLEAN,DATETIME
    from sqlalchemy.orm import sessionmaker, declarative_base
    from sqlalchemy.exc import NoResultFound
    from flask import Flask, jsonify, abort, request
    from datetime import datetime, timedelta

    app = Flask(__name__)

    engine = create_engine("sqlite:///python.db", connect_args={'check_same_thread': False})
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    class Books(Base):
        __tablename__ = 'books'

        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        count = Column(Integer, default="1")
        release_date = Column(DATE, nullable=False)
        author_id = Column(Integer, nullable=False)

        def to_json(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    class Authors(Base):
        __tablename__ = 'authors'
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        surname = Column(String, nullable=False)
        def to_json(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}


    class Students(Base):
        __tablename__ = 'students'
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        surname = Column(String, nullable=False)
        email = Column(String, nullable=False)
        average_score = Column(FLOAT, nullable=False)
        scholarship = Column(BOOLEAN, nullable=False)

        @classmethod

        def studentsIndormitory(cls):
            return session.query(Students).filter(Students.scholarship).all()

        @classmethod
        def get_all_good_students(cls, score):
            return session.query(Students).filter(Students.average_score > score).all()
        def to_json(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    class Receiving_books(Base):
        __tablename__ = 'receiving_books'
        id = Column(Integer, primary_key=True)
        book_id = Column(Integer, nullable=False)
        student_id = Column(Integer, nullable=False)
        date_of_issue = Column(DATETIME, nullable=False)
        date_of_return = Column(DATETIME)

        @hybrid_property
        def count_date_with_book(self):
            if self.date_of_return:

                return (self.date_of_return - self.date_of_issue)
            else:
                return (datetime.now() - self.date_of_issue)
        def to_json(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}


    @app.before_request
    def before_request_func():
        Base.metadata.create_all(engine)


    @app.route('/get_all_books')
    def get_all_books():
        books = session.query(Books).all()
        books_list = []
        for book in books:
            books_list.append(book.to_json())
        return jsonify(books_list=books_list), 200


    @app.route('/get_robbers')
    def get_robbers():
        books = session.query(Receiving_books).filter(datetime.now()-Receiving_books.date_of_issue < timedelta(days=14)).all()
        books_list = []
        for book in books:
            books_list.append(book.to_json())
        return jsonify(books_list=books_list), 200


    @app.route('/issue_book', methods=['POST'])
    def issue_book():
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        new_issue = Receiving_books(book_id=book_id,
                                    student_id=student_id,
                                    date_of_issue=datetime.now())
        session.add(new_issue)
        session.commit()
        return "Книга выдана", 201


    @app.route('/pass_book', methods=['POST'])
    def pass_book():
        try:
            book_id = request.form.get('book_id', type=int)
            student_id = request.form.get('student_id', type=int)
            book = session.query(Receiving_books).filter(Receiving_books.book_id == book_id).filter((Receiving_books.student_id == student_id)).one()
            book.date_of_return = datetime.now()
            session.commit()
            return "Книга принята"
        except NoResultFound:
            return 'Эта книга не связанна с учеником'


    @app.route('/get_books_by_title/<title>')
    def get_books_by_name(name):
        books = session.query(Books).filter(Books.name.like(f"%{name}%")).all()
        books_list = []
        for book in books:
            books_list.append(book.to_json())
        return jsonify(books_list=books_list), 200


    app.run()