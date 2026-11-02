# MediCare Management System

A healthcare management web application developed using Python, FastAPI, MySQL, HTML, CSS and Jinja2.

## About the Project

MediCare Management System is a web-based application designed to simplify healthcare appointment management.

The application allows patients to explore doctors, book medical appointments and share feedback about their healthcare experience. It also provides appointment management functionality.

## Features

- View doctors and their specialisations.
- Book medical appointments.
- View all patient appointments.
- Confirm and cancel appointments.
- Delete appointments.
- Submit patient feedback.
- Rate healthcare services on a scale of 1–5.
- Store application data in MySQL.
- User-friendly dashboard interface.

## Technologies Used

- Python
- FastAPI
- MySQL
- SQLAlchemy
- HTML5
- CSS3
- Jinja2
- Uvicorn

## Project Structure

```text
Medicare_management/
├── app/
│   ├── main.py
│   ├── database.py
│   └── __init__.py
├── templates/
├── static/
│   └── style.css
├── .gitignore
├── requirements.txt
└── README.md
```

## Database

Database Name: `medicare_db`

The application uses three main tables:

1. **Doctors:** Stores doctor details, education, specialisation and experience.
2. **Appointments:** Stores patient details, appointment date, time and status.
3. **Reviews:** Stores patient feedback, ratings and review dates.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/pranavvv752/Medicare-Management-System.git
```

### 2. Navigate to the project folder

```bash
cd Medicare-Management-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment (Windows)

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure the database

- Create a MySQL database named `medicare_db`.
- Create the doctors, appointments and reviews tables.
- Configure your database credentials in a `.env` file in the project root.

### 7. Run the application

```bash
python -m uvicorn app.main:app --reload
```

### 8. Open the application

Visit:

http://127.0.0.1:8000


## Future Improvements

- Patient and administrator authentication.
- Search and filter appointments.
- Edit appointment details.
- View all submitted patient reviews.
- Display average patient ratings.
- Email appointment notifications.
- Enhanced security and validation.

## Author

**Pranav** and **ChatGPT**

GitHub: [pranavvv752](https://github.com/pranavvv752)

---

This project was developed as a practical learning project to explore Python backend development, database integration and web application development.
