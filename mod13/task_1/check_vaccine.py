import random
import sqlite3

def check_if_vaccine_has_spoiled(cursor,truck_number):
    cursor.execute(f"SELECT COUNT(*) FROM table_truck_with_vaccine WHERE (truck_number='{truck_number}') AND (NOT temperature_in_celsius BETWEEN 16 and 20 )  ")
    return cursor.fetchone()[0] <3



with sqlite3.connect('hw.db') as connection:
    print(check_if_vaccine_has_spoiled( connection.cursor(),"с783ну147"))



