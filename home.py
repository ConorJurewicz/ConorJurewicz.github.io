from flask import Blueprint, render_template, request, jsonify, redirect, url_for

home = Blueprint(__name__, "home")


@home.route("/")
def home_dir():
    return render_template("index.html")
    
@home.route("/mustreads")
def mustreads():
    return render_template("mustreads.html")
    
@home.route("/mybooks")
def mybooks():
    return render_template("mybooks.html")

@home.route("/bookreviews")
def bookreviews():
    return render_template("bookreviews.html")