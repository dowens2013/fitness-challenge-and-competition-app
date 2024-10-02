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
