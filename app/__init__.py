from flask import Flask



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'



from app import routes

