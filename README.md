# Python Sanic Boilerplate

## Directory Structure
```
Project Root
·
├── README.md
└── services
    └── backend
        ├── Pipfile
        ├── Pipfile.lock
        ├── apps
        │   ├── __init__.py
        │   ├── public
        │   │   ├── routes.py
        │   │   └── views.py
        │   └── user
        │       ├── routes.py
        │       └── views.py
        ├── config
        │   ├── __init__.py
        │   ├── app.py
        │   ├── config.py
        │   └── routes.py
        ├── proxy.py
        ├── scripts
        │   └── run.sh
        ├── server.py
        └── setup.cfg
```