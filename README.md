Data Pulse
Overview
Data Pulse is a Python-based project designed to fetch and manage data from external sources using a FastAPI-based API. It includes scheduled tasks to retrieve and store data, with a focus on modular design for extensibility.
Features

Data Cleaning: Handle missing values, outliers, and data inconsistencies.
Modular Design: Easily extendable scripts for custom data processing workflows.
API Integration: FastAPI-based API for managing posts.
Scheduled Data Fetching: Automatically fetch data from an external API every minute using APScheduler.

Installation

Clone the repository:git clone https://github.com/kananbabayev92/data_pulse.git


Navigate to the project directory:cd data_pulse


Install the required dependencies:pip install -r requirements.txt


Set up the environment variables:
Create a .env file with DATABASE_URL set to your PostgreSQL database URL.



Usage

Initialize the database:python init_db.py


Run the application:uvicorn main:app --reload


Access the API at http://127.0.0.1:8000/.

Project Structure

data/: Directory for input datasets.
output/: Generated reports and visualizations.
routers/: API or routing logic for the application (contains posts.py for post-related endpoints).
__init__.py: Package initialization file.
database.py: Database configuration and connection logic using SQLAlchemy.
init_db.py: Script to initialize the database tables.
main.py: Main FastAPI application script.
models.py: SQLAlchemy models for the database.
scheduler.py: Background scheduler configuration.
tasks.py: Task definitions for fetching data.
schemas.py: Pydantic models for API request/response validation.
requirements.txt: List of Python dependencies.

Dependencies

Python 3.8+
FastAPI
Uvicorn
Requests
APScheduler
Psycopg2-binary
SQLAlchemy
python-dotenv

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or suggestions, feel free to reach out via GitHub Issues or email at kananbabayev92@gmail.com.
