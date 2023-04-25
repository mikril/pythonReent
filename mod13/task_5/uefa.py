import random
import sqlite3

def generate_test_data(cursor,number_of_groups):
    cursor.execute("DELETE FROM 'uefa_commands'")
    cursor.execute("DELETE FROM 'uefa_draw'")

    countries = ['Россия', 'Германия', 'Испания', 'Франция', 'Италия', 'Англия']
    levels=['сильная','средняя','средняя','слабая']
    group_number=0
    for i in range(number_of_groups*4):
        if i%4==0:
            random.shuffle(levels)
            group_number+=1

        cursor.execute(
            'INSERT INTO uefa_commands (command_number, command_name, command_country, command_level) VALUES (?,?,?,?)',
            (i + 1, 'команда ' + str(i + 1), random.choice(countries), levels[i%4]))

        cursor.execute('INSERT INTO uefa_draw (id, command_number, group_number) VALUES (?, ?, ?)',
                     (i, i + 1, 'группа ' + str(group_number)))




with sqlite3.connect('hw.db') as connection:
    generate_test_data( connection.cursor(),16)