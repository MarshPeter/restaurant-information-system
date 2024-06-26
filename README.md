# restaurant-information-system

## What you will need to be able to run this project

1. A local Database that can run mySQL (recommended local, remote sometimes fails to work despite instructions all being the same)
2. To have the frontend working, we recommend node (v20.11) and NPM (v10.2.4) to be installed. If you have another javascript runtime, it is up to you to ensure your tooling is capable.
3. For the backend to work, we recommend that python (v3.10.12) and pip (v22.3.1) is installed.

Do note that all of these instructions are for the Windows Platform. And all code was produced on VSCode

## Frontend Usage

The frontend is a Vue Based application that runs with the VUE CLI tooling. This means that you will need to run a server locally, to view the frontend of the project.

from this directory, open a console. Then do the following:

```powershell

cd ./frontend
npm install
# Wait for installation to complete
npm run serve

```

the frontend will be available in the browser on: localhost:8000

## Backend Usage Guide

First, identify where you would like the database to be stored. You can find the sql code in ./backend/serversql.sql Copy that file and paste it in your database schema. Then return to this location.

To activate and use the server, you need to setup a virtual environment
*FROM THIS DIRECTORY, OPEN A TERMINAL*
Use the following commands:

```powershell
> cd ./backend
> py -3 -m venv .venv
```

You should only ever need to do that once on your machine. Now when you run python, you need to activate your environment with the following command from the /backend directory

```powershell
> .venv\Scripts\activate # CMD
> .venv\Scripts\activate.ps1 # POWERSHELL
```

*NOTE* Make sure you are using the correct command for whatever terminal you are using, later there will be differences.
*NOTE2* You can leave the virtual environment at any time with: 'deactivate'

When you are in the activated environment, you will need to use the following set of commands the first time:

```powershell
pip install Flask
pip install mysql-connector-python
pip install Flask-CORS
```

Flask Documentation[https://flask.palletsprojects.com/en/3.0.x/quickstart/#about-responses]
mysql-connector-python Documentation[https://www.w3schools.com/python/python_mysql_getstarted.asp] - kinda
More exact mysql-connector-python documentation[https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html]

*NOTE 3* THE FOLLOWING 2 SECTIONS SHOULD BE FOLLOWED BASED ON WHAT COMMAND LINE YOU USE ON WINDOWS. ALTERNATIVE COMMANDS FOR MAC/LINUX CAN BE IDENITIFED THROUGH TRIVIAL GOOGLING, OR CHATGPT.

### POWERSHELL

After this line on roughly line 167 of the activate.ps1 file in .venv/Scripts:

```script
<# Begin Activate script --------------------------------------------------- #>
```

type the following:

```powershell
$env:DB_HOST=HOST #(typically 'localhost' for local database)
$env:DB_USER=USER #(typically 'root')
$env:DB_PASSWORD=PASSWORD #(enter what you need, omit if you do not use one)
$env:DATABASE=DATABASE_SCHEMA_NAME #(Where ever the schema is that the sql code has been placed)
```

ENSURE THAT THESE ARE ALL SURROUNDED BY QUOTES
*NOTE* YOU MAY NEED TO DEACTIVATE ENVIRONMENT AND REACTIVATE IT TO SEE RESULTS
You should be able to check that it works if you type: 'echo %MY_VARIABLE%' while the environment is on. It should spit the password back to you

### CMD

Somewhere in the file activate.bat in .venv/Scripts, probably at the end is fine, idk type the following

```cmd
SET DB_HOST=HOST (typically 'localhost' for local database)
SET DB_USER=USER (typically 'root')
SET DB_PASSWORD=PASSWORD
SET DATABASE=DATABASE_SCHEMA_NAME
```

Where the password is what you find on discord. Place it in quotes. I did mine on line 172
You should be able to check that it works if you type: echo $env:MY_VARIABLE while the environment is on. It should spit the password back to you
*NOTE* YOU MAY NEED TO DEACTIVATE ENVIRONMENT AND REACTIVATE IT TO SEE RESULTS

### WSL

IF you are using WSL for this, probably just chatgpt the equivalent commands. I think those will end up in the 'activate file'.

### Starting the server

At this point if you followed everything, it should be ready to go. First activate the environment, then you can use one of two commands

```powershell
flask run
OR
flask run --debug
```

--debug will put it in a 'watch' mode where you will not have to restart the server when you make changes, and is generally more resistent to bugs. This can mean that bugs can go unnoticed. Do the final demo in flask run just to make sure things work.

### REST API TESTS

If you want to make tests to test some routes, you can create tests in the api_tests folder. In there you can already see some test templates. Create a new folder and follow them for a guideline. To use the tests you must have a VSCode Extension: REST Client installed. Otherwise, you may need to use POSTMAN or any other equivalent service instead.