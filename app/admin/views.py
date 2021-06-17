from flask import render_template, session, redirect, url_for 
from . import admin

@admin.route('/admin', methods=['GET']) 
def accueil():
    return render_template('admin/adminviews/accueil.html')