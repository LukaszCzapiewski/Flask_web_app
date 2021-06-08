from flask import Blueprint, render_template, request, flash, session
from flask_login import login_user, login_required
from sqlalchemy import sql, select
from werkzeug.security import generate_password_hash
from . import db
from .models import User

bp = Blueprint('',__name__)


@bp.route('/')
def main():
    return render_template('baza.html')


@bp.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        new_user = User(username=username, password=generate_password_hash(
            password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Account created!', category='success')
    return  render_template('sign_up.html')


@bp.route("/dodaj")
@login_required
def new_pracownik():
    return render_template('dodajpracownika.html', tytul="Dodaj pracownika")

@bp.route('/dodajpracownika',methods = ['POST', 'GET'])
@login_required
def addrec():
    if request.method == 'POST':
        try:
            imie = request.form['imie']
            nazwisko = request.form['nazwisko']
            nrpracownika = request.form['nrpracownika']
            adres = request.form['adres']
            new_pracownik = pracownicy(imie,nazwisko,nrpracownika,adres)
            db.session.add(new_pracownik)
            db.session.commit()

        finally:
            return render_template('dodajpracownika.html', tytul="Dodano", msg="Dodano pracownika")





@bp.route('/lista')
@login_required
def list():
    query = select('*').select_from(pracownicy)
    result = session.execute(query).fetchall()
    return render_template("lista.html", tytul="Lista", dane = result)

