from flask import Flask
app = Flask(__name__)
@app.route('/')
def star_trek():
    return 'Welcome to the Collective!'