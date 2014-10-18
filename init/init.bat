del db.sqlite3
del /F /S /Q TestManagerCore\migrations\*
del /F /S /Q ManualTester\migrations\*
del /F /S /Q static\*
python manage.py syncdb --noinput
python manage.py migrate
python manage.py makemigrations TestManagerCore
python manage.py migrate TestManagerCore 0001
python manage.py makemigrations ManualTester
python manage.py migrate ManualTester 0001
python manage.py migrate
python manage.py createcachetable
python manage.py loaddata initialdata.json
python manage.py loaddata testdata.json
python manage.py collectstatic --noinput
python manage.py test
