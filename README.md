# Medichip - Nursing Home Management System

A comprehensive web application for managing nursing home operations including admin staff, doctors, patients, appointments, and medical records.

## Tech Stack

**Backend:**
- Django REST Framework (Python)
- SQLite Database
- JWT Authentication (djangorestframework-simplejwt)

**Frontend:**
- React with TypeScript
- Vite (build tool)
- Axios (HTTP client)
- localStorage for JWT token persistence

## Project Structure

```
medichip/
├── backend/              # Django REST Framework API
│   ├── medichip_backend/ # Django project settings
│   ├── api/              # Main API app
│   ├── manage.py
│   └── requirements.txt
├── frontend/             # React + TypeScript + Vite
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
└── README.md
```

## Features

### Current Phase
- User authentication with JWT tokens
- Three user roles: Admin Staff, Doctor, Patient
- Automatic role assignment on registration
- User login/logout functionality
- Role-based access control

### Future Features
- Admin staff management
- Doctor scheduling and appointments
- Patient records management
- Prescription handling
- Appointment booking/cancellation/rescheduling

## Getting Started

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Authentication

All API requests are authorized with JWT tokens. Include the token in the `Authorization` header:
```
Authorization: Bearer <your-token>
```

## License
MIT
