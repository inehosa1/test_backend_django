# Product Management System

This project is a Django-based system for managing products. It allows you to register products and perform CRUD operations on them. When products are created, alerts are generated, which can be active, pending, or expired, based on different time periods. The system also includes filters, Swagger documentation, and test cases.

## Features

- Product CRUD operations (Create, Read, Update, Delete)
- Alert generation for products with active, pending, or expired statuses
- Filtering functionality for products and alert
- Swagger documentation for API endpoints
- Test cases for the project

## Initial Setup

Create a virtual environment:


Install requirements:

```
pip install -r requirements.txt
```

Apply database migrations:

```
python manage.py migrate
```

## Usage

Start the Django development server:

```
python manage.py runserver
```

## Access the API documentation:

Open your browser and go to http://localhost:8000/docs/ to view the Swagger documentation.


## Coverage Report


To view the test coverage report, follow these steps:

Run your tests with coverage:

```
coverage run manage.py test
```

Generate a coverage report in console format:

```
coverage report -m
```

