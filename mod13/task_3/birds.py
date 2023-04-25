import sqlite3

def log_bird(
        cursor,
        bird_name,
        date_time,
):
  cursor.execute(f"INSERT INTO 'birds' (bird_name,date_time) VALUES('{bird_name}','{date_time}');")


def check_if_such_bird_already_seen(
        cursor,
        bird_name
):
    cursor.execute(f"SELECT COUNT(*) FROM birds WHERE (bird_name='{bird_name}')")
    return cursor.fetchone()[0] > 0



with sqlite3.connect('birds.db') as connection:
    log_bird( connection.cursor(),"пингвин","22.12.2022")
    print(check_if_such_bird_already_seen(connection.cursor(),"голубь"))
