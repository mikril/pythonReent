import sqlite3

with sqlite3.connect('hw_4_database.db') as connection:
    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM salaries WHERE (salary < 5000)')
    result = cursor.fetchall()[0][0]
    print(f'Людей за чертой бедности - {result}')

    cursor.execute('SELECT AVG(salary) FROM salaries')
    result = cursor.fetchall()[0][0]
    print(f'Средняя зарплата - {result}')

    cursor.execute('SELECT salary FROM salaries ORDER BY salary')
    result=cursor.fetchall()
    result = result[(len(result)+1) // 2][0]
    print(f'Медианная зарплата - {result}')

    cursor.execute('SELECT COUNT (*) FROM salaries')
    total = cursor.fetchall()[0][0]
    cursor.execute(f'SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * {total})')
    T=cursor.fetchall()[0][0]
    cursor.execute(f'SELECT SUM(salary) - {T} FROM salaries')
    K= cursor.fetchall()[0][0]
    print(f'F - {round(T * 100 / K, 2)}')