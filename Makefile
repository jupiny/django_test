migrate:
	- python django_test/manage.py makemigrations users posts likes
	- python django_test/manage.py migrate 
test:
	- python django_test/manage.py test users posts likes
	- pep8 .
