SHELL=/bin/bash
PROJECT_NAME=Dodecahedron
CURRENT_CONFIG=$(DEV_CONFIG)
DEV_CONFIG=$$PWD/etc/dev.conf
PRODUCTION_CONFIG=/etc/dodecahedron.conf
TEST_DUMP=./maketests.log
TESTING_CONFIG=$$PWD/etc/testing.conf
TEST_CMD=SETTINGS=$(TESTING_CONFIG) nosetests --verbosity=2 --where=./dodecahedron/tests

install:
	python setup.py install

prototype:
	ipython -i bin/prototype.py

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`
	find . -name "__pycache__" -delete

server:
	SETTINGS=$(CURRENT_CONFIG) bin/manage.py runserver

shell:
	SETTINGS=$(CURRENT_CONFIG) bin/manage.py shell

test:
	rm -f $(TEST_DUMP)
	$(TEST_CMD) 2>&1 | tee -a $(TEST_DUMP)

single:
	$(TEST_CMD) --attr=single

watch:
	watchmedo shell-command -R -p "*.py" -c 'echo \\n\\n\\n\\nSTART; date; $(TEST_CMD); date' .

db:
	SETTINGS=$(CURRENT_CONFIG) bin/manage.py init_db
	SETTINGS=$(CURRENT_CONFIG) bin/manage.py populate_db

dbshell:
	sqlite3 /tmp/dodecahedron-dev.db

wheelhouse:
	python setup.py bdist_wheel

build-wheels:
	pip wheel .
	pip wheel -r dependencies.txt

install-wheels:
	pip install --use-wheel --find-links=wheelhouse --no-index -r dependencies.txt

.PHONY: clean install test server watch db single docs shell dbshell wheelhouse prototype build-wheels install-wheels