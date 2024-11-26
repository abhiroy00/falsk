from config import connectDB
from app.router import router
from app.model import User

# Initialize Flask app and database
app, db = connectDB()

# Register blueprint
app.register_blueprint(router)

# Create database tables
with app.app_context():  # Ensure the app context is active
    db.create_all()  # Call create_all on the db object

if __name__ == '__main__':
    app.run(debug=True)
