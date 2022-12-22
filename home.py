from flask import Blueprint, render_template, request, jsonify, redirect, url_for

home = Blueprint(__name__, "home")

@home.route("/")
def home_dir():
    return render_template("index.html")
    