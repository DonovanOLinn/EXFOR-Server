# Expeditionary Force API Backend

This is a simple start to an API for one of my favorite book series - Expeditionary Force. This is the backend component and is still being developed. 

For now, the goal is to be able to do some light webscraping to retrieve information off a series of wiki pages. I take that information and I push it to my temp database.
Currently I'm using MySQL, but I'll adjust the database to a PostgreSQL database for production. I'm looking to transition to Amazon RDS for the database.

## Roadmap

- Finish up the Characters scraper and test on temp database

- Set up login and auth functionality

- Create routes that allow for more dynamic data retrieval. 

- Set up database using Amazon RDS

- Host the built Flask application using EBS 

- Clean up commented out code and rework the previous scrapers using utilities in util.py

- Set up automation to perform the scrapes once a month

- Set up test cases

- Set up CI/CD workflow

- Begin development of React Frontend Application

## How to clone: 
First, grab the clone command: 
```bash
    git clone https://github.com/DonovanOLinn/EXFOR-Server.git
```

Second, Navigate to a directory on your computer and enter in the command above

Third, CD into the directory: 
```bash
    cd EXFOR-server
```

Fourth, set up your virtual environment: 
```bash
    windows: python -m venv venv
    mac/linux: python3 -m venv venv
```

fifth, turn on the virtual environment: 
```bash
    windows: venv\scripts\activate
    mac/linux: source venv/bin/activate
```

sixth, do the installs: 
```bash
    pip install -r requirements.txt
```

Lastly, switch out the password in the app.py and head over to mysql workbench to configure your schema. Or use your own database hosting service. 


Once done, running the server with flask run command should allow this to run. 

