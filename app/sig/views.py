from flask import render_template, session, redirect, url_for 
from . import sig
@sig.route('/sig', methods=['GET']) 
def accueil():
    return render_template('sig/sigviews/accueil.html')