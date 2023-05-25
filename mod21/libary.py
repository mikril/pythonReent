

if __name__ == "__main__":
    import csv
    from sqlalchemy.ext.hybrid import hybrid_property
    from sqlalchemy import  func, ForeignKey, DATE, create_engine, Column, Integer, String,FLOAT, BOOLEAN,DATETIME
    from sqlalchemy.ext.associationproxy import association_proxy
    from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
    from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
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
        author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
        author = relationship("Authors", backref=backref("books",
                                                        cascade="all, "
                                                                "delete-orphan",
                                                        lazy='joined'))
        students = association_proxy('book', 'Receiving_books')

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
        phone=Column(String, nullable=False)
        email = Column(String, nullable=False)
        average_score = Column(FLOAT, nullable=False)
        scholarship = Column(BOOLEAN, nullable=False)
        books = association_proxy('student', 'Receiving_books')
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
        student = association_proxy("books", "Students")
        book = association_proxy("students", "Books")
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


    @app.route('/booksAuthor/<int:author_id>')
    def booksAuthor(author_id):



        available_books = session.query(Books). \
            filter(Books.author_id == author_id,
                   Books.id == Receiving_books.book_id,
                   Receiving_books.date_of_return == None).all()
        books_list = []
        for book in available_books:
            json_book = book.to_json()
            books_list.append(json_book)
        return jsonify(available_books_list=books_list), 200


    @app.route('/booksStudents/<int:student_id>')
    def booksStudents(student_id):
        books_student = session.query(Receiving_books.book_id).distinct().filter(Receiving_books.book_id == Books.id,Receiving_books.student_id == student_id).all()
        authors_id = session.query(Books.author_id).distinct().filter(Receiving_books.book_id == Books.id,Receiving_books.student_id == student_id).all()


        authors_id=[item[0] for item in authors_id]
        books_by_authors = session.query(Books).filter(Books.author_id .in_(authors_id)).all()
        books_authors=session.query(Books.id).filter(Books.author_id .in_(authors_id)).all()

        missing_elements = [item for item in books_authors if item not in books_student]
        indexes = [books_authors.index(element) for element in missing_elements]
        print(indexes)
        books_list = []

        for i in indexes:
            json_book = books_by_authors[i].to_json()
            books_list.append(json_book)
        return jsonify(recomended_books_list=books_list), 200


    @app.route('/average_books_month', methods=['GET'])
    def average_books_month():

        current_year = datetime.now().year
        current_month = datetime.now().month
        current_month_start = datetime(current_year, current_month, 1, 0, 0, 0, 0)
        taken_books_count = session.query(func.count(Receiving_books.book_id)).filter(Receiving_books.date_of_issue >= current_month_start).scalar()
        students_count = session.query(func.count(Students.id)).scalar()
        average_book_month_count = round(taken_books_count / students_count, 3)
        return f'Cреднее количество книг, которые студенты брали в этом месяце: {average_book_month_count}', 200


    @app.route('/most_popular_book', methods=['GET'])
    def most_popular_book():
        book_id = session.query(func.count(Receiving_books.book_id)).filter(Receiving_books.student_id == Students.id,Students.average_score >= 4.0).group_by(Receiving_books.book_id).order_by(func.count(Receiving_books.book_id).desc()).limit(1).all()
        book = session.query(Books).filter(Books.id == book_id[0][0]).all()
        json_book = book[0].to_json()
        return jsonify(most_popular_book=json_book), 200


    @app.route('/most_reading_students',methods=['GET','POST'])
    def most_reading_students():
        if request.method == 'GET':
            current_year = datetime.now().year
            current_year_start = datetime(current_year, 1, 1, 0, 0, 0, 0)
            students = session.query(Students).filter(Receiving_books.student_id == Students.id,Receiving_books.date_of_issue >= current_year_start).group_by(Receiving_books.student_id).order_by(func.count(Receiving_books.book_id).desc()).limit(10).all()
            students_list = []
            for student in students:
                json_student = student.to_json()
                students_list.append(json_student)
            return jsonify(most_reading_students=students_list), 200

        elif request.method == 'POST':
            if request.method == 'POST':
                stud_file = request.files.get('stud_file')
                if stud_file:
                    try:
                        stud_file.save('stud_file.csv')
                        stud_list = []
                        with open('stud_file.csv', 'r', newline='') as csvfile:
                            reader = csv.DictReader(csvfile, delimiter=';')
                            for student in reader:
                                if student['scholarship'].lower() == 'true':
                                    student['scholarship'] = True
                                elif student['scholarship'].lower() == 'false':
                                    student['scholarship'] = False
                                stud_list.append(student)
                        session.bulk_insert_mappings(Students, stud_list)



                    except Exception:

                        Session.rollback()
                        return 'Ошибка при обработке файла "stud_file"', 400
                    session.commit()
                    return 'Студенты из файла "students_file" были добавлены', 200
                return 'Файл "students_file" не найден', 400

    app.run()


