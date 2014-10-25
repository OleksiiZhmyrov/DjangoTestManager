del db.sqlite3
del /F /S /Q TestManagerCore\migrations\*
del /F /S /Q TestManagerContent\migrations\*
del /F /S /Q static\*
del /F /S /Q media\*
python manage.py syncdb --noinput
python manage.py migrate
python manage.py makemigrations TestManagerCore
python manage.py migrate TestManagerCore 0001
python manage.py makemigrations TestManagerContent
python manage.py migrate TestManagerContent 0001
python manage.py migrate
python manage.py createcachetable
python manage.py loaddata initialdata.json
python manage.py loaddata testdata.json
python manage.py collectstatic --noinput
python manage.py test
