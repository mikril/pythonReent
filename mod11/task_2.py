import requests
from sqlalchemy import  create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import time
import threading

engine = create_engine("sqlite:///starwars.db", connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

url = "https://swapi.dev/api/people/"

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(String)
    gender = Column(String)

def getCharcter(url,i):
    response = requests.get(url + str(i))
    if response.status_code == 200:
        character=dict(response.json())
        new_issue = Characters(id=i,
                               name=character["name"],
                               birth_year=character["birth_year"],
                               gender=character["gender"])
        session.add(new_issue)




def without_threads():
    timeStart = time.time()
    for i in range(1, 21):
        getCharcter(url, i)
    session.commit()
    print(f'(Один поток) Заполнилось за {time.time()-timeStart}')
def with_threads():
    timeStart = time.time()
    threads = []
    for i in range(1, 21):
        thread = threading.Thread(target=getCharcter, args=(url, i))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    session.commit()
    print(f'(Много) Заполнилось за {time.time()-timeStart}')

if __name__=="__main__":
    Base.metadata.create_all(engine)
    session.query(Characters).delete()
    without_threads()
    session.query(Characters).delete()
    with_threads()