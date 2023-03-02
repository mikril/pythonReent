from flask import Flask
import random
import datetime
import os
import re
app = Flask(__name__)

def get_array_words():
    with open(BOOK_FILE) as book:
        words=(re.sub(r'[^\w\s]','', book.read())).split()
    return words

def counter():
    global counter_visits
    counter_visits+=1
    return counter_visits

counter_visits = 0
carsNames=["Chevrolet", "Renault", "Ford", "Lada"]
catsBreeds=["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt') 
words=get_array_words()

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def cars():
    return ', '.join(carsNames)

@app.route('/cats')
def cats():
    return random.choice(catsBreeds)

@app.route('/get_time/now')
def get_time_now():
    current_time=datetime.datetime.now()
    return "Точное время: %s" % current_time

@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour=datetime.datetime.now()+datetime.timedelta(hours=1)
    return "Точное время: %s" % current_time_after_hour

@app.route('/get_random_word')
def get_random_word():
    return random.choice(words)

@app.route('/counter')
def get_counter_visits():
    return str(counter())

if __name__ == '__main__': 
    app.run(debug=True)