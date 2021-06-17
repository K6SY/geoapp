from flask import render_template, session, redirect, url_for 
from . import main
@main.route('/', methods=['GET']) 
def accueil():
    auth=False
    return render_template('main/mainviews/accueil.html', auth=auth)