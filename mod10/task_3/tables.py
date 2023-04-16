import sqlite3

with sqlite3.connect('hw_3_database.db') as connection:
    cursor = connection.cursor()

    result = []
    for i in range(3):
        cursor.execute(f'SELECT COUNT (id) FROM table_{i+1}')
        result.append(cursor.fetchall()[0][0])

    print(f'Запесей в 1,2,3 таблице - соответсвенно {result}')

    cursor.execute('SELECT COUNT(*) FROM (SELECT DISTINCT * FROM table_1)')
    result=cursor.fetchall()[0][0]
    print(f'Уникальных записей в таблице 1 - {result}')

    cursor.execute('SELECT COUNT(*) FROM (SELECT * FROM table_1 INTERSECT SELECT * FROM table_2)')
    result = cursor.fetchall()[0][0]
    print(f'Записи которые и в первой и во второй таблице - {result}')

    cursor.execute('SELECT COUNT(*) FROM (SELECT * FROM table_1 INTERSECT SELECT * FROM table_2 INTERSECT SELECT * FROM table_3)')
    result = cursor.fetchall()[0][0]
    print(f'Записи которые и в первой и во второй таблице и в третей - {result}')
