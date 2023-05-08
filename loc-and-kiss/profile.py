from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from init import db
from models import User
import read_src
import folium

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@login_required
def see_profile():
    score = 0
    return render_template("profile.html", name=current_user.name, score=score)
