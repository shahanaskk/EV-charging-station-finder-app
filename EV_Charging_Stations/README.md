# ⚡ EV Charging Station Finder App

A web application built using **Python, Django, and MySQL** that helps electric vehicle (EV) users locate charging stations and book charging slots online. The system includes separate dashboards for administrators, users, and workers, making station and booking management simple and efficient.

---

## 🚀 Features

### 👨‍💼 Admin

- Secure admin login
- Add new EV charging stations
- View all charging stations
- Edit station details
- Delete charging stations
- Manage charging slots

### 👤 User

- User registration and login
- Browse available EV charging stations
- View station details
- Book available charging slots
- View booking status

### 👷 Worker

- Worker registration and login
- Dedicated worker dashboard

---

## 🛠️ Technologies Used

### Backend

- Python
- Django

### Database

- MySQL

### Frontend

- HTML
- CSS
- JavaScript

### Tools

- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```text
EV-charging-station-finder-app/
│
├── EV_Charging_Stations/
├── MyApp/
├── manage.py
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/shahanaskk/EV-charging-station-finder-app.git
```

### 2. Navigate to the project folder

```bash
cd EV-charging-station-finder-app
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Add your Django secret key:

```env
DJANGO_SECRET_KEY=your_secret_key
```

### 5. Configure the MySQL database

Update the database settings in `settings.py` with your local MySQL credentials.

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

---

## 📸 Screenshots

Screenshots will be added soon.

---

## 🚧 Project Status

**In Progress**

### Completed

- User Authentication(Log in & Registration)
- Role-based Dashboards (Admin, User & Worker)
- Admin Dashboard
- EV Charging Station Management (CRUD)
- Image Upload Support
- User Dashboard
- Worker Dashboard
- MySQL Database integration
- Secure Configuration using Environment Variables (.env)
- Git & GitHub version control

### Planned Improvements

- Charging Slot Management
- Booking System
- Location (Latitude & Longitude) Management
- Improved UI/UX
- Responsive Design
- Search and Filter Stations
- Booking History
- Enhanced Validation and Error Handling

---

## 📚 Learning Outcomes

This project helped me gain practical experience with:

- Django project structure
- Django Models and ORM
- User Authentication
- CRUD Operations
- Template Rendering
- MySQL Integration
- File Uploads
- Git & GitHub
- Environment Variables using `.env`

---

## 👩‍💻 Author

**Shahanas K K**

Python Django Developer
