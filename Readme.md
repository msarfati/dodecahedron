# :six_pointed_star: Dodecahedron :six_pointed_star:
:page_with_curl: MIT License

:black_nib: Copyright (c) 2016 Michael Sarfati

**Status: Pre-alpha**

## :interrobang: What's this?
- A fork of [:rocket: Flask-Diamond](https://flask-diamond.readthedocs.org/en/latest/) web framework, forked for pedagogical purposes.
- Inspired as well by [Sinatra](www.sinatrarb.com) and [NodeJS](https://nodejs.org/en/)

## :clipboard: Getting started
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

## :chart_with_upwards_trend: Current Direction
### Strong RESTful API Support
- Adhere more strictly to RESTful principles:
    - [*Architectural Styles and the Design of Network-based Software Architectures*](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) by Roy Fielding
    - *RESTful Web APIs* by Leonard Richardson and Mike Amundsen
    - [*REST CookBook*](http://restcookbook.com/)
    - [*REST API Tutorial: Status Codes*](http://www.restapitutorial.com/httpstatuscodes.html)
    - HATEOAS compliance
- RESTful code generation based on models and simplify model creation with generation scripts

#### TODO
* *Versioning*: Embed in the header
- **Pagination**: Limit collection queries to some number (25?) globally. Support *limit* and *offset*, embed into query.
- **Query** GET response: `api.dodecahedron.net/book?fields=title,author` will return `{"title": "my title", "author": [{"id": 1, "href": "..."} ]}`
- Resource references / linking - in addition to returning object as JSON, return a `href` linking to the exact resource. Also, if there are any explicit relations, include 'href'
- REST metaclass supporting HTTP verbs: POST, GET, PUT, DELETE, and possibly PATCH and HEAD
- :white_check_mark: ~~[reqparse](https://flask-restful-cn.readthedocs.org/en/0.3.5/reqparse.html) is deprecated, integrate [Marshmallow](https://marshmallow.readthedocs.org/en/latest/)~~
- :white_check_mark: ~~Auto-generate schemas from models with [Marshmallow-SQLAlchemy](https://marshmallow-sqlalchemy.readthedocs.org/en/latest/)~~

### Conveniences
- Better `dbshell` support
