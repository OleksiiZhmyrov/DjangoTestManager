rm db.sqlite3
rm -Rf TestManagerCore/migrations/*
rm -Rf TestManagerContent/migrations/*
rm -Rf TestManagerExec/migrations/*
rm -Rf static/*
mkdir media/media/uploads
cp init/test_images/* media/media/uploads
python manage.py syncdb --noinput
python manage.py migrate
python manage.py makemigrations TestManagerCore
python manage.py migrate TestManagerCore 0001
python manage.py makemigrations TestManagerContent
python manage.py migrate TestManagerContent 0001
python manage.py makemigrations TestManagerExec
python manage.py migrate TestManagerExec 0001
python manage.py migrate
python manage.py createcachetable
python manage.py loaddata initialdata.json
python manage.py loaddata testdata.json
python manage.py collectstatic --noinput
python manage.py test
