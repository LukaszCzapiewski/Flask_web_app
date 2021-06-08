import sqlite3

conn = sqlite3.connect('database.db')
print("Baza otwarta")

conn.execute('CREATE TABLE pracownicy (imie TEXT,nazwisko TEXT, nrpracownika TEXT, adres TEXT)')
conn.execute('CREATE TABLE User (id INTEGER,username TEXT, password TEXT)')
print("Tabela utworzona")



cur = conn.cursor()
cur.execute("INSERT INTO pracownicy (imie,nazwisko,nrpracownika,adres) VALUES(?,?,?,?)",('Czyngis', 'Chan','1','Temudżyn 1'))
cur.execute("INSERT INTO pracownicy (imie,nazwisko,nrpracownika,adres) VALUES(?,?,?,?)",('Cao', 'Cao','2','Wei 2'))


cur.execute('SELECT * FROM pracownicy ORDER BY nazwisko')
conn.commit()
print(cur.fetchall())#drukowanie rezultatu
conn.close()


