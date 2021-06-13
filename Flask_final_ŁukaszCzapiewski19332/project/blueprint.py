import flask_login
from flask import Blueprint, render_template, request, flash
from flask_login import login_user, current_user, logout_user
from werkzeug.security import generate_password_hash

from . import db
from .models import user, worker

bp = Blueprint('',__name__)



@bp.route('/')
def main():
    if current_user.is_authenticated:
        return render_template('mainpage.html',username = current_user.username)
    else:
        return render_template('mainpage.html')


@bp.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        new_user = user(username=username, password=generate_password_hash(
            password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Account created!', category='success')
        return render_template('baza.html', username = current_user.username)
    return  render_template('sign_up.html')




@bp.route('/addrec',methods = ['POST', 'GET'])
@flask_login.login_required
def addrec():
    if request.method == 'POST':
            imie = request.form['imie']
            nazwisko = request.form['nazwisko']
            adres = request.form['adres']
            if (len(imie)<2 or len(nazwisko)<2 or len(adres)<2):
                return render_template('dodajpracownika.html', msg="Dane nieprawidłowe!")
            new_worker = worker(name=imie, surname=nazwisko,adres=adres)
            db.session.add(new_worker)
            db.session.commit()
            return render_template('dodajpracownika.html',msg = "Dodano pracownika")
    return render_template('dodajpracownika.html',username = current_user.username)

@bp.route('/lista')
@flask_login.login_required
def list():
    dane = db.session.query(worker)
    return render_template("lista.html",tytul="Lista" ,dane = dane,username = current_user.username)

@bp.route('/logout')
@flask_login.login_required
def logout():
    logout_user()
    return render_template("logout.html")