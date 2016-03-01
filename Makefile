SHELL=/bin/bash
PROJECT_NAME="Dodecahedron"
TEST_DUMP="./maketests.log"

install:
	python setup.py install

prototype:
	ipython -i bin/prototype.py

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`
	find . -name "__pycache__" -delete

wheelhouse:
	python setup.py bdist_wheel

server:
	python app.py runserver

shell:
	python app.py shell

watch:
	watchmedo shell-command -R -p "*.py" -c 'echo \\n\\n\\n\\nSTART; date; $(TEST_CMD) -c etc/nose/test-single.cfg; date' .

test:
	rm -f $(TEST_DUMP)
	nosetests

single:
	nosetests --attr=single --verbosity=3

db:
	python app.py init_db
	python app.py populate_db

dbshell:
	sqlite3 $(DB_URI)

build-wheels:
	pip wheel .
	pip wheel -r requirements.txt

install-wheels:
	pip install --use-wheel --find-links=wheelhouse --no-index -r requirements.txt

.PHONY: clean install test server watch db single docs shell dbshell wheelhouse prototype build-wheels install-wheels