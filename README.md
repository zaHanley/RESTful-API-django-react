
# RESTful API for Django-React-Bootstrap Application

This is intended to be used as boilerplate for full-stack web applications built using Django and React, that provides a RESTful API. The backend is built using Django and Django Rest Framework, and the frontend is built using React, with styling provided by Bootstrap (Bootswatch).


## Installation

To run this project locally, you need to have Python 3, Node.js, and npm installed on your machine. You can then follow these steps:

Clone this repository
```bash
  git clone https://github.com/zaHanley/RESTful-API-django-react.git
```
Go to the project directory
```bash
  cd RESTful-API-django-react
```
Install the Python dependencies: 
```bash
  pip install -r requirements.txt
```

Install the frontend dependencies: 
```bash
  cd frontend
  npm install
```

Start the backend server: 
```bash
  python manage.py runserver
```
In a separate terminal, start the frontend server: 
```bash
  cd frontend
  npm start
```