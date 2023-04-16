import sqlite3
with sqlite3.connect('hw_2_database.db') as connection:
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM table_checkout ORDER BY sold_count DESC")
    result = cursor.fetchall()
    answer = result[0][0]
    print(f'Чаще всегo покупают - {answer}')

    cursor.execute("SELECT * FROM table_checkout WHERE phone_color = 'Red'")

    reds = cursor.fetchall()[0]
    cursor.execute("SELECT * FROM table_checkout WHERE phone_color = 'Blue'")
    blues = cursor.fetchall()[0]
    if reds[1] > blues[1]:
        print('Чаще покупают красные')
    elif reds[1] < blues[1]:
        print("Чаще покупают синие")
    else:
        print('Красные и синие покупают одинаково')

    cursor.execute('SELECT * FROM table_checkout ORDER BY sold_count')
    result = cursor.fetchall()
    answer = result[0][0]
    print(f'Cамый непопулярный цвет телефона? - {answer}')