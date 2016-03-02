#  Dodecahedron
MIT License
Copyright (c) 2016 Michael Sarfati

## What's this?
- A fork of [Flask-Diamond](https://flask-diamond.readthedocs.org/en/latest/) web framework, forked for pedagogical purposes.
- Inspired as well by [Sinatra](www.sinatrarb.com) and [NodeJS](https://nodejs.org/en/)

## Getting started
1. Clone project
```bash
git clone git@github.com:msarfati/dodecahedron.git
```

2. Make the virtual environment
```bash
mkvirtualenv -a . --always-copy dodecahedron
```

3. Install and test
```bash
make install && make db && make test
```

4. Run the server
```bash
make server
```

## TODO
### Conveniences
- better `dbshell` support

### RESTful API
- [reqparse](https://flask-restful-cn.readthedocs.org/en/0.3.5/reqparse.html) is deprecated, integrate [Marshmallow](https://marshmallow.readthedocs.org/en/latest/)
- Auto-generate schemas from models with [Marshmallow-SQLAlchemy](https://marshmallow-sqlalchemy.readthedocs.org/en/latest/)

