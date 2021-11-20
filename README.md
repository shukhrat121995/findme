

#### Setup
```
git clone git@github.com:shukhrat121995/findme.git
```
Create ```.env``` file inside ```website``` folder and
you have to enter the following credentials

```angular2html
SECRET_KEY=
GOOGLE_MAP_API=

API_KEY=
AUTH_DOMAIN=
DATABASE_URL=
PROJECT_ID=
STORAGE_BUCKET=
MESSAGING_SENDER_ID=
APP_ID=
```

**Unless explicitly stated all the following 
commands should be executed in the root directory of the project.**
```
pip install pipenv
pipenv install
pipenv sync
pipenv shell
python manage.py runserver
```