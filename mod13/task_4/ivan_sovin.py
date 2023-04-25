import sqlite3

def ivan_sovin_the_most_effective(
        cursor,
          name,
):
    if name !=  'Иван Совин':
        cursor.execute(f"SELECT salary FROM table_effective_manager WHERE (name='Иван Совин')")
        ivan_salary=int(cursor.fetchone()[0])
        cursor.execute(f"SELECT salary FROM table_effective_manager WHERE (name='{name}')")
        rab_salary =int(cursor.fetchone()[0])
        rab_salary = int(rab_salary) + int(rab_salary) * 0.1
        if ivan_salary<=rab_salary:
            cursor.execute(f"DElETE FROM table_effective_manager WHERE (name='{name}') ")
        else:
            cursor.execute(f"UPDATE table_effective_manager SET salary='{rab_salary}' WHERE name='{name}'")






with sqlite3.connect('hw.db') as connection:
    ivan_sovin_the_most_effective( connection.cursor(),"Смирнов Ф.М.")
