\# Primetrade Backend Assignment



\## Overview

This project implements a secure and scalable REST API with JWT-based authentication

and role-based access control. A minimal frontend using Django templates is included

to demonstrate API integration and protected user flows.



The application allows users to register, log in, and manage tasks through

secured APIs, following REST best practices.



---



\## Tech Stack

\- Backend: Django, Django REST Framework

\- Authentication: JWT (SimpleJWT)

\- Database: SQLite (development), PostgreSQL/MySQL ready

\- Frontend: Django Templates + Vanilla JavaScript

\- Async Architecture: Celery + Redis (configured)

\- API Documentation \& Testing: Postman



---



\## Core Features



\### Authentication \& Authorization

\- User registration and login with password hashing

\- JWT access and refresh tokens

\- Role-based access control (USER / ADMIN)

\- Protected APIs



\### Task Management

\- CRUD APIs for task entity

\- Ownership-based access control

\- Admin users can view all tasks



\### Frontend Integration

\- Register → Login → Dashboard flow

\- JWT-protected dashboard

\- API-driven task creation and viewing

\- Success and error messages displayed from API responses



---



\## API Endpoints



\### Authentication

\- POST `/api/v1/auth/register/`

\- POST `/api/v1/auth/login/`

\- POST `/api/v1/auth/refresh/`



\### Tasks

\- GET `/api/v1/tasks/`

\- POST `/api/v1/tasks/`

\- PUT `/api/v1/tasks/{id}/`

\- DELETE `/api/v1/tasks/{id}/`



---



\## Asynchronous Processing (Celery \& Redis)



Celery and Redis are configured to handle asynchronous tasks such as sending

emails after user registration.



\*\*Note:\*\*  

On Windows systems, Redis typically runs via WSL or Docker.

For this assignment, asynchronous processing is demonstrated architecturally.

In production, Redis and Celery workers would run as separate services.



---



\## Setup Instructions



```bash

git clone https://github.com/akshata78/primetrade-backend-assignment.git

cd primetrade-backend-assignment/config

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver



