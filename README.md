# Atticus
Atticus challenge

Using Python 2.7

Using Flask for ReST
https://flask.palletsprojects.com/en/1.1.x/installation/
https://flask.palletsprojects.com/en/1.1.x/installation/#install-install-virtualenv

pip install mysql


Anticipated Flow for Not Creation:
1. User puts as much information about the song into the form
2. Result may be the song, many songs, or no songs
  - If no songs, show error
  - If many songs, user must select song from the results
  - If one song continue on
3. Choose action of Update, Delete, or Play

Run `python seed.py once to set up db and songs table`
