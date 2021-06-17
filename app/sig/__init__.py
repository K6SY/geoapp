from flask import Blueprint
sig = Blueprint('sig', __name__) 
from . import views, errors