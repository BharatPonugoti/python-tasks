from flask import Flask
from app import app
from routes.auth_routes import auth_bp
from routes.book_routes import book_bp
from routes.client_routes import client_bp
from routes.issue_routes import issue_bp
from routes.account_routes import account_bp

app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)
app.register_blueprint(client_bp)
app.register_blueprint(issue_bp)
app.register_blueprint(account_bp)

if __name__ == "__main__":
    app.run(debug=True)