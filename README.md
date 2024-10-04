# fitness-challenge-and-competition-app

## The project includes the following components

Front End: React.js single-page application (SPA) for user interaction

API: Flask-based backend to manage user data, challenges, activity logging, and integrations with external fitness APIs

Database: PostgreSQL or MySQL for storing user information, challenges, activity logs, and leaderboard data

Cloud Deployment: AWS services (ECS, RDS, API Gateway, Lambda) for cloud infrastructure and integrations

## starting the project

### create a venv

1) create a venv in the root directory
    `python3 -m venv venv`

2) activate venv 
    `source venv/bin/activate`

3) install requirements

    `pip install Flask Flask-JWT-Extended Flask-SQLAlchemy psycopg2-binary`

## Project Structure

### Modules

#### Flask

This imports the Flask class to create a Flask application instance.

Blueprint is used to organize routes into modular components.

Request allows us to use HTTP requests.

Jsonify converts Python dictionaries to JSON format.

#### flask_jwt_extended (JWTManager)

This is the class from flask_jwt_extended to manage JWT authentication.

Creates a new JWT for the user (Flask-JWT-Extended)

#### Flask_sqlalchemy (SQLAlchemy)

This is an ORM (Object Relational Mapper) to interact with the database in a Pythonic way.

#### werkzeug.security.check_password_hash

check_password_hash is a utility from the werkzeug library (which is used internally by Flask) that securely compares a hashed password (typically stored in a database) with a plaintext password provided by the user during login. It's used to verify if the entered password matches the stored hashed password.
