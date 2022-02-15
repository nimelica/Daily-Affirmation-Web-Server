from flask import Flask, render_template, request, flash, g
import sqlite3, random

# Create instance of Flask by calling its class constructor
app = Flask(__name__)
app.secret_key = "12ev@0947!fBjs8AA#4$32jHbd_sjhAdhc%mhn_773gvPPahG/HSI*IH_jbs"

# Main page
@app.route('/', methods=['GET'])
def index():
    return "HELLO"