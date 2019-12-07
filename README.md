# API

### Installation

```sh
$ virtualenv auth
$ cd auth && source bin/active
$ git clone https://github.com/LSDkk5/app
$ pip install -r src/REQUIREMENTS.txt
```

### Db config
#### settings.py line 27

```python
MONGODB_SETTINGS = {
        'db': '<your_database_name>',
        'host': '<database_host>'
    }
```
### Run development server

```sh
$ python src/run.py
```

```python
 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
