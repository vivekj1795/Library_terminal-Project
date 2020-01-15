import sqlite3

conn = sqlite3.connect("library1.db")
c=conn.cursor()
c.execute("""create table IF NOT EXISTS usersDB(
          [USERID] integer primary key autoincrement NOT NULL,
          [USERNAME] VARCHAR NOT NULL,
          [PASSWORD] VARCHAR NOT NULL,
          [ACCESS] INTEGER Not Null,
          [fees] Integer 
          );""")
c.execute("""create table IF NOT EXISTS  librarian(
          [USERID] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
          [NAME] VARCHAR NOT NULL,
          [CONTACT_INFORMATION] VARCHAR NOT NULL
          );""")
c.execute("""create table IF NOT EXISTS books(
          [index] integer primary key autoincrement not null,
          [author]  VARCHAR not null,
          [name] VARCHAR not NULL,
          [PUBLICATION_COMPANY] VARCHAR not NULL,
          [RENTED_DATE] DATE,
          [RENTED_USER] VARCHAR
          );""")

conn.commit()
conn.close()
