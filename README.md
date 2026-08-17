# ⚡ EV Charging Station Finder App

A web application built using **Python, Django, and MySQL** that helps electric vehicle (EV) users find charging stations and manage charging slots. The application includes role-based access for administrators, EV charging stations, customers, and workers.

---

## 🚀 Features

### 👨‍💼 Admin

- Secure admin login
- Add new EV charging stations
- View all charging stations
- Edit station details
- Delete charging stations
- Manage EV charging station information

### ⚡ EV Charging Station

- EV station registration
- Automatic user account creation for EV stations
- EV station login
- Role-based access using Django Groups
- Dedicated EV station dashboard
- Manage charging slots
- Add charging slots
- View charging slots
- Edit charging slots
- Delete charging slots
- Charging slots linked to their respective EV stations

### 👤 Customer

- Customer registration
- Customer login
- Dedicated customer dashboard

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

Add your Django secret key and database credentials:

```env
DJANGO_SECRET_KEY=your_secret_key
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```

### 5. Configure the MySQL database

Create a MySQL database and make sure the database settings in `settings.py` read the required credentials from the `.env` file.

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

Screenshots will be added after the main application features and UI are completed.

---

## 🚧 Project Status

**In Progress**

### ✅ Completed

- User authentication and registration
- EV station authentication
- Role-based access using Django Groups
- Admin dashboard
- EV station dashboard
- Customer dashboard
- Worker dashboard
- EV charging station CRUD operations
- EV station slot management
  - Add slots
  - View slots
  - Edit slots
  - Delete slots

- Station-specific slot ownership
- Image upload support
- MySQL database integration
- Environment variable configuration using `.env`
- Git & GitHub version control
- Responsive template structure

### 🔄 Upcoming

- Customer search for EV charging stations
- Station details and available-slot display for customers
- Charging slot booking system
- Booking history
- Google Maps-based station search
- Improved UI/UX
- Enhanced validation and error handling
- Additional authorization and security improvements

---

## 📚 Learning Outcomes

This project has helped me gain practical experience with:

- Django project structure
- Django Models and ORM
- Django Authentication
- Django Groups and role-based access
- CRUD operations
- Template rendering
- MySQL integration
- ForeignKey and OneToOne relationships
- File uploads
- Form handling
- Environment variables using `.env`
- Git & GitHub version control
- Building role-based web applications

---

## 👩‍💻 Author

**Shahanas K K**

Python Django Developer
