# Tontine Contribution Tracking System

This is a Django-based web application for tracking contributions in a tontine system.

## Features

-   Custom User Model with JWT Authentication
-   Group and Member Management
-   Contribution and Payout Tracking
-   Cycle Management
-   Audit Logging

## Tech Stack

-   Django 4.x
-   Django REST Framework (DRF)
-   SQLite
-   djangorestframework-simplejwt (for JWT auth)
-   django-cors-headers
-   python-decouple

## Project Structure

```
tontine/
├── manage.py
├── tontine/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── apps/
│   ├── accounts/
│   ├── groups/
│   ├── cycles/
│   ├── contributions/
│   ├── payouts/
│   └── audit/
├── requirements.txt
├── .env.example
└── README.md
```

## Setup Instructions

### 1. Create and Activate a Virtual Environment

**On macOS and Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
.\\venv\\Scripts\\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file by copying the example file:

```bash
cp .env.example .env
```

Open the `.env` file and add a `SECRET_KEY`. You can generate one using the following command:

```bash
python -c 'import secrets; print(secrets.token_hex(24))'
```

Your `.env` file should look like this:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account.

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

-   **Register:** `POST /api/auth/register/`
-   **Login:** `POST /api/auth/login/`
-   **Refresh Token:** `POST /api/auth/refresh/`
-   **Current User:** `GET /api/auth/me/`

The admin panel is available at `/admin/`.
