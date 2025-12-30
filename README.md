# User Management System (Backend)

## Stack
- Django
- Django REST Framework
- JWT Authentication
- PostgreSQL / SQLite (dev)

## Features
- User signup & login
- JWT authentication
- Role-based access (admin/user)
- Profile update & password change
- Admin user management (list, activate, deactivate)
- Pagination
- Environment-based configuration

## Setup
1. Clone repo
2. Create `.env`
3. Install requirements
4. Run migrations
5. Start server

## Project Structure
- backend/: Django backend service
- backend/backend/: Django project settings and configuration

## Live Backend API

Base URL:
https://user-management-system-jik1.onrender.com

Example endpoints:
- POST /auth/signup/
- POST /auth/login/
- GET /auth/me/
