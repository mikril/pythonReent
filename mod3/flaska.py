from flask import Flask
from datetime import datetime
import os
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
weeksDays=["Хорошего понедельника","Хорошего вторника","Хорошей среды","Хорошего четверга","Хорошей пятницы","Хорошей субботы","Хорошего воскресенья"]
months=["Январь","Февраль","Март" ,"Апрель" ,"Май" ,"Июнь" ,"Июль" ,"Август" ,"Сентябрь" ,"Октябрь" ,"Ноябрь" ,"Декабрь"]
salarys={}
@app.route('/hello-world/<username>')
def hello_world(username):
    weekday = datetime.today().weekday()
    return f"Привет {username}. {weeksDays[weekday]}!"

@app.route('/max_number/<path:numbers>')
def max_number(numbers):

    try:
        return f'Максимальное число: <i>{str(max(map(int, numbers.split("/"))))}</i>'
    except:
        return "Не могу работать не с цифрами"

@app.route('/preview/<int:SIZE>/<path:RELATIVE_PATH>')
def preview(SIZE,RELATIVE_PATH):
    abs_path = os.path.abspath(RELATIVE_PATH)
    with open(abs_path) as file:
        return f'<b> {abs_path}</b> {SIZE}<br>{file.read(SIZE)}'

@app.route('/add/<date>/<int:number>')
def add(date,number):
    try:
        salarys.setdefault(int(date[0:4]), {}).setdefault(int(date[4:6]), 0)
        salarys[int(date[0:4])][int(date[4:6])] += number
        return f"Успешно добавлено {number} на {months[int(date[4:6])-1]} {int(date[0:4])} года"
    except:
        return "Неправильная дата"
@app.route('/calculate/<int:year>')
def calculateYear(year):
    try:
        sumS=0
        for month in salarys[year]:
            sumS+=salarys[year][month]
        return f"{sumS} денег на  {year} год"
    except:
        return "Такого года нет"
@app.route('/calculate/<int:year>/<int:month>')
def calculateMonth(year,month):
    try:
        return f"{str(salarys[year][month])} денег на {months[month-1]} {year} года"
    except:
        return "Такой даты нет"

if __name__ == '__main__':
    app.run(debug=True)