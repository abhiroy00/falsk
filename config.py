from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy instance globally
db = SQLAlchemy()

def connectDB():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://abhiroy:abhi@7464@192.168.1.100/flask_db'



    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  
    return app, db
