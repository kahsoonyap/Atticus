# Atticus
Atticus Challenge
Kah Soon Yap
Language: Python 2.7
  Third-Party Libraries:
    * Flask
    * mysql
    * uuid

How to Run:
First a virtualenv needs to be setup. Information on that depends on the machine. Info can be found here https://flask.palletsprojects.com/en/1.1.x/installation/#install-install-virtualenv.
After the virtualenv is set up, activate the environment by doing `$ . venv/bin/activate` or `> venv\Scripts\activate` if on windows.
Run `pip install Flask`
Run `pip install mysql`
Run `python seed.py` once to set up the db and put some dummy data inside.
Run `python server.py` to start the back end.
Things are up and running now.

Flask Setup
I followed these two links to setup Flask. Since I was not using Python 3, a virtualenv was necessary.
https://flask.palletsprojects.com/en/1.1.x/installation/
https://flask.palletsprojects.com/en/1.1.x/installation/#install-install-virtualenv

Some Explanations:
I did not create any of the templates or any of the front end components. Rather than return the render_template(), I returned what the code should have been with quotes wrapped around it.
I was unable to write tests in time.

Anticipated Flow for Not Creation:
1. User puts as much information about the song into the form
2. Result may be the song, many songs, or no songs
  - If no songs, show error
  - If many songs, user must select song from the results
  - If one song continue on
3. Choose action of Update, Delete, or Play

Anticipated Flow for Creation:
1. Not dependent on if a song already exists so different from other flows
2. Fill out form and submit
