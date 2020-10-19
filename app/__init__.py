from flask import Flask,render_template

app = Flask(__name__) # name est une variable prédéfinie transmise à Flask

from . import dash
