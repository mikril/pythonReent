import requests
from sqlalchemy import  create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import time
import multiprocessing
from multiprocessing.pool import ThreadPool, Pool

engine = create_engine("sqlite:///starwars.db", connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()
characters=[]
Base = declarative_base()

url = "https://swapi.dev/api/people/"

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(String)
    gender = Column(String)

def getCharcter(i):
    response = requests.get(url + str(i))

    if response.status_code == 200:

        character=dict(response.json())
        new_issue = Characters(id=i,
                               name=character["name"],
                               birth_year=character["birth_year"],
                               gender=character["gender"])
        characters.append(new_issue)
        session.add(new_issue)
        return new_issue


def with_ThreadPool():
    with ThreadPool(processes=multiprocessing.cpu_count() * 5) as pool:
        timeStart = time.time()
        pool.map(getCharcter, range(1,22))
        session.commit()
    print(f'(ThreadPool) Заполнилось за {time.time()-timeStart}')

def with_Pool():
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        timeStart = time.time()
        result=pool.map(getCharcter, range(1,22))

    session.add_all(filter(None, result))
    session.commit()

    print(f'(Pool) Заполнилось за {time.time()-timeStart}')

if __name__=="__main__":
    Base.metadata.create_all(engine)
    session.query(Characters).delete()
    with_ThreadPool()
    characters=[]
    session.query(Characters).delete()
    with_Pool()



