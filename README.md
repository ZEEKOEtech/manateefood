# Manateefood


## Installation instructions
1. Git clone this repositry
2. Navigate to root folder of project, run
        ```
        $ virtualenv --python=python3 .venv
        ```
3. Activate the virtualenv `$ source .venv/bin/activate`
4. Run
        ```
        $ pip install -r requirements.txt
        ```
5. In the `manateefood/app` folder, copy `settingsLocal.py.dist` to `settingsLocal.py` and setup correct values. Also use pip to install your favorite django-database engine (`pip install psycopg2` for Mac).
6. In `manateefood` run
        ```
        $ python manage.py bower_install
        ```
7. Run
        ```
        $ python manage.py migrate
        ```
8. Finally
        ```
        $ python manage.py runserver
        ```