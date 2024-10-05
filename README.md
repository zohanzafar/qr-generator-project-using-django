# qr-generator-project-using-django

# QR Code Generator Django App

This project implements a **QR Code Generator** using Django and Tailwind CSS. The app allows users to generate high-quality 4K QR codes from URLs, with features including user authentication (login, register, logout, change password) and QR code download functionality.

## Features

- User Authentication (Register, Login, Logout, Change Password)
- Generate 4K QR Codes from URLs
- Download generated QR Codes
- Responsive design using Tailwind CSS
- Secure implementation with best practices

## Project Setup

Follow these steps to set up and run the project.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
```

### 2. Create and Activate a Virtual Environment

Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root and add the following:

```
SECRET_KEY=your_secret_key_here
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

## Usage

1. Register a new account or login with existing credentials.
2. On the home page, enter a URL to generate a QR code.
3. Click "Generate QR Code" to create the QR code.
4. Use the "Download QR Code" button to save the generated QR code.

## API Endpoints

- `/`: Home page and QR code generation
- `/register/`: User registration
- `/accounts/login/`: User login
- `/accounts/logout/`: User logout
- `/change-password/`: Change user password