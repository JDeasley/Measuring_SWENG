# Measuring_SWENG
Software Engineering module Measuring Software Engineering project repo.

## Usage
Once setup has been completed, usage is as simple as typing in your desired repo to the search bar in the top right corner of the webapp.

## Setup
I have made my visualisation through a webapp using Flask, which builds a webapp using Python code.

To run the webapp, you will need to have installed:
- Python (and pip)
- Flask
- PyGithub
- pymongo

all of which can be installed within a virtual environment if you wish.

I have tried my best to make setup simple through setup scripts:

- `setup_macos_linux.sh` for use on macOS or Linux, and
- `setup_windows.ps1` for use on Windows.

However, these scripts do depend somewhat on what you already have installed on your machine, e.g. Python and pip, so I would advise continuing to read through this setup section.

If nothing else, they are at least a good guide for how the setup process should run.

---

### Python (and pip)

Presumably you already have Python and therefore Pip installed, but if not this should be easy to find online.

---

### Virtual Environment setup

_Note:_ _This step can be skipped if you would rather just install the 3 required packages into your default location rather than a virtual environment, however this is what I've been using in making the app._

A very simple description of how to set up a virtual environment and Flask can be found here: https://flask.palletsprojects.com/en/2.0.x/installation/

All you need to do is set up the venv folder:
- macOS/Linux: `python3 -m venv venv`
- Windows: `py -3 -m venv venv`

and then activate the virtual environment:
- macOS/Linux: `. ven/bin/activate`
- Windows: `venv\Scripts\activate`

---

### Flask, PyGithub, and pymongo

To install Flask, PyGithub, and pymongo, you then simply type:

- `pip install Flask`
- `pip install PyGithub`
- `pip install pymongo`

This can be done in the virtual environment too.

---

### Starting the app
To start the webapp, you will need to start the database and then the Flask app.

Before starting the database for the first time, you will need to make a `data` folder in the main directory, i.e. the same directory as the `docker-compose.yml` file.

Then we can use `docker-compose up` to start the database and then `flask run` to start the app.
