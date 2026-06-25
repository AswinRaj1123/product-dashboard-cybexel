# Product Dashboard API

## Python Django REST Framework Assessment

### Objective
Develop a Product Dashboard API using Django REST Framework (DRF) following an API-First Architecture.

---

## Table of Contents
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [Features](#features)
- [Testing the API](#testing-the-api)

---

## Tech Stack
- **Backend**: Python 3.x, Django
- **API Framework**: Django REST Framework (DRF)
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (Development)
- **Filtering/Search**: django-filter
- **Environment Management**: python-dotenv

---

## Project Structure
`
product-dashboard-cybexel/
├── product_dashboard/
│   ├── accounts/             # User authentication and profile management
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── products/             # Product management
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── product_dashboard/    # Project configuration
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── .gitignore
├── LICENSE
└── README.md
`

---

## Setup Instructions

### Prerequisites
- Python 3.x
- pip

### Installation
1. Clone or download the project
2. Navigate to the project root directory:
   `ash
   cd product-dashboard-cybexel
   `
3. Create a virtual environment:
   `ash
   python -m venv venv
   `
4. Activate the virtual environment:
   - Windows (PowerShell):
     `powershell
     .\venv\Scripts\Activate.ps1
     `
   - Windows (Command Prompt):
     `cmd
     venv\Scripts\activate.bat
     `
   - macOS/Linux:
     `ash
     source venv/bin/activate
     `
5. Install the project dependencies:
   `ash
   cd product_dashboard
   pip install django djangorestframework djangorestframework-simplejwt django-filter python-dotenv
   `
6. Create a .env file in the product_dashboard directory with the following content:
   `env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   `
7. Apply database migrations:
   `ash
   python manage.py migrate
   `
8. Create a superuser (admin):
   `ash
   python manage.py createsuperuser
   `
9. Run the development server:
   `ash
   python manage.py runserver
   `

The API will now be available at http://127.0.0.1:8000/

---

## API Documentation

### Authentication Endpoints
| Method | URL                          | Description                          | Authentication Required |
|--------|------------------------------|--------------------------------------|-------------------------|
| POST   | /api/register/             | User registration                    | No                      |
| POST   | /api/token/                | Obtain JWT access and refresh tokens | No                      |
| POST   | /api/token/refresh/        | Refresh JWT access token             | No                      |
| GET    | /api/profile/              | Retrieve user profile                | Yes                     |
| PUT    | /api/profile/              | Update user profile                  | Yes                     |
| PATCH  | /api/profile/              | Partially update user profile        | Yes                     |

### Product Endpoints
| Method | URL                          | Description                          | Authentication Required | Admin Only |
|--------|------------------------------|--------------------------------------|-------------------------|------------|
| GET    | /api/products/             | List all products                    | Yes                     | No         |
| POST   | /api/products/             | Create a new product                 | Yes                     | Yes        |
| GET    | /api/products/<id>/        | Retrieve a single product            | Yes                     | No         |
| PUT    | /api/products/<id>/        | Update a product                     | Yes                     | Yes        |
| PATCH  | /api/products/<id>/        | Partially update a product           | Yes                     | Yes        |
| DELETE | /api/products/<id>/        | Delete a product                     | Yes                     | Yes        |

---

## Features

### Authentication & Authorization
1. **User Registration**
   - Fields: Name, Email, Password, Confirm Password
   - Passwords are securely hashed using Django's built-in password hashing system
   - Validation to ensure password and confirm password match

2. **JWT Authentication**
   - Access Token (valid for 60 minutes)
   - Refresh Token (valid for 1 day)
   - Token rotation enabled
   - Custom JWT serializer includes user's name and email in the token payload

3. **Role Management**
   - Admin: Can create, update, delete, and view products
   - Authenticated Users: Can only view products and their own profile

### Product Management
1. **Product Model**
   - Title
   - Description
   - Price
   - Product Image
   - Created At
   - Updated At
   - Created By (auto-set to authenticated user on creation)

2. **Product Features**
   - Search products by title using ?search=<query>
   - Sort products by price or creation date using ?ordering=<field>
     - Example: ?ordering=price (ascending) or ?ordering=-created_at (descending)

### Admin Profile
- Fields: Name, Email, Profile Image (Optional)
- Endpoint: /api/profile/

---

## Testing the API

### Using Postman
1. Start the Django development server
2. Use the API endpoints as documented above
3. For authenticated endpoints, include the JWT access token in the Authorization header:
   - Header Key: Authorization
   - Header Value: Bearer <your-access-token>

### Using Django Admin
- Access the Django admin interface at http://127.0.0.1:8000/admin/
- Log in with the superuser credentials created during setup
- Manage users and products through the admin panel

---

## License
This project is licensed under the terms specified in the LICENSE file.
