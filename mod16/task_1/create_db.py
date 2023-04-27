import sqlite3
ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"

CREATE_ACTORS_TABLE="""
DROP TABLE IF EXISTS 'actors';
CREATE TABLE 'actors' (
act_id INTEGER NOT NULL PRIMARY KEY,
act_first_name VARCHAR(50),
act_last_name VARCHAR(50) ,
act_gender VARCHAR(1)
);
"""

CREATE_MOVIE_TABLE="""
DROP TABLE IF EXISTS 'movie';
CREATE TABLE 'movie' (
mov_id INTEGER NOT NULL PRIMARY KEY,
mov_tittle VARCHAR(50)
);
"""

CREATE_DIRECTOR_TABLE="""
DROP TABLE IF EXISTS 'director';
CREATE TABLE 'director' (
dir_id INTEGER NOT NULL PRIMARY KEY,
dir_first_name VARCHAR(50),
dir_last_name VARCHAR(50)
);
"""

CREATE_MOVIE_CAST_TABLE="""
DROP TABLE IF EXISTS 'movie_cast';
CREATE TABLE 'movie_cast' (
act_id INTEGER REFERENCES actors(act_id) ON DELETE CASCADE,
mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE,
role VARCHAR(50)
);
"""

CREATE_OSCAR_AWARDED_TABLE="""
DROP TABLE IF EXISTS 'oscar_awarded';
CREATE TABLE 'oscar_awarded' (
award_id INTEGER NOT NULL PRIMARY KEY,
mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE
);
"""

CREATE_MOVIE_DIRECTION_TABLE="""
DROP TABLE IF EXISTS 'movie_direction';
CREATE TABLE 'movie_direction' (
dir_id INTEGER REFERENCES director(dir_id) ON DELETE CASCADE,
mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE
);
"""

def create_tables():
    with sqlite3.connect('database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.executescript(CREATE_ACTORS_TABLE)
        cursor.executescript(CREATE_MOVIE_TABLE)
        cursor.executescript(CREATE_DIRECTOR_TABLE)
        cursor.executescript(CREATE_MOVIE_CAST_TABLE)
        cursor.executescript(CREATE_OSCAR_AWARDED_TABLE)
        cursor.executescript(CREATE_MOVIE_DIRECTION_TABLE)
        cursor.executescript(ENABLE_FOREIGN_KEY)
create_tables()
"""
movie_cast -> actors (act_id) многие к одному
movie_cast -> movie (mov_id) многие к одному
oscar_awarded -> movie (mov_id) многие к одному
movie_direction -> movie (mov_id) один к одному(считаю что у фильма может быть один директор)
movie_direction -> director (dir_id) многие к одному()
"""