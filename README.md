# Flask MVC App

## Running Locally
To run this application locally, you need to have **Python** installed on your machine. Then follow these steps:

1- Clone the repository:
```bash
git clone https://github.com/cruzmath/Flask_MVC.git
```
2- Navigate to the project directory:
```bash
cd Flask_MVC
```
3- (Optional but recommended) Create and activate a virtual environment to avoid dependency conflicts:
```bash
python -m venv .venv
# On Windows (Git Bash)
source .venv/Scripts/activate
# On macOS/Linux
source .venv/bin/activate
```
4- Install the required dependencies:
```bash
pip install -r requirements.txt
```
5- Run the application:
```bash
python src/main.py
```

## About the project
This project follows the MVC (Model–View–Controller) architecture, which separates the application into clear layers:
- /models — Defines how data is structured and saved in the database.
- /views — Contains static HTML files that define the visual part of the web app.
- /controllers — Handles the logic that connects models and views, defining how the application behaves.
- /repositories — Encapsulates database operations (e.g., SELECT, INSERT).
- /routes — Defines all the available routes (endpoints) of the application.

The main.py file inside /src initializes and configures the Flask app based on config.py. This is the only file that needs to be executed to start the project.
