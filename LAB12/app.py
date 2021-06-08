from flask import Flask, render_template,request
import sqlite3 as sql

app = Flask(__name__)
@app.route("/")
def main():
    return  render_template('baza.html')


@app.route("/dodaj")
def new_pracownik():
    return render_template('dodajpracownika.html',tytul="Dodaj pracownika")

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            imie = request.form['imie']
            nazwisko = request.form['nazwisko']
            nrpracownika = request.form['nrpracownika']
            adres = request.form['adres']
            # con = sqlite3.connect("database.db) u mnie nie działa
            with sql.connect("C:\\Users\\Łukasz\\Desktop\\PWJSJS\\LAB12\\database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO pracownicy (imie,nazwisko,nrpracownika,adres) VALUES(?,?,?,?)",(imie,nazwisko,nrpracownika,adres) )
                con.commit()
                msg = "Dodano pracownika"
        finally:
            con.close()
            return render_template('dodajpracownika.html', tytul="Dodano",msg=msg)





@app.route('/lista')
def list():

    #con = sqlite3.connect("database.db) u mnie nie działa
    con = sql.connect("C:\\Users\\Łukasz\\Desktop\\PWJSJS\\LAB12\\database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM pracownicy ORDER BY nazwisko')
    dane = cur.fetchall()
    return render_template("lista.html",tytul="Lista" ,dane = dane)

if __name__ == "__main__":
    app.run()

