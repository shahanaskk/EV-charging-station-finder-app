# ⚡ EV Charging Station Finder App

A web application built using **Python, Django, and MySQL** that helps electric vehicle (EV) users locate nearby charging stations and book charging slots online. The system includes separate dashboards for administrators, users, and workers, making station and booking management simple and efficient.

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
- User dashboard
- Detect current location using browser geolocation
- Find nearby EV charging stations based on current location
- Calculate distance between the user and charging stations
- Display charging stations sorted by nearest distance
- View charging station details
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
- GeoPy

### Database

- MySQL

### Frontend

- HTML
- CSS
- JavaScript
- Bootstrap

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

## 📍 Location-Based EV Station Finder

The application allows users to find nearby EV charging stations using their current location.

When the user selects **Use My Location**:

1. The browser's Geolocation API obtains the user's latitude and longitude.
2. The coordinates are sent to the Django backend.
3. GeoPy calculates the distance between the user and each EV charging station.
4. Charging stations are sorted from nearest to farthest.
5. The results are displayed as responsive station cards.

The application stores the latitude and longitude of each EV charging station and uses these coordinates for distance calculation.

---

## 📸 Screenshots

Screenshots will be added soon.

---

## 🚧 Project Status

**In Progress**

### Completed

- User Authentication (Login & Registration)
- Role-based Dashboards (Admin, User & Worker)
- Admin Dashboard
- EV Charging Station Management (CRUD)
- Image Upload Support
- User Dashboard
- Worker Dashboard
- MySQL Database Integration
- Secure Configuration using Environment Variables (`.env`)
- Git & GitHub Version Control
- Charging Slot Management
- Add, Edit and Delete Charging Slots
- Current Location Detection
- Location-Based EV Station Search
- Place-name based EV Station Search
- Distance Calculation using GeoPy
- Nearest Station Sorting
- Nearest EV Station Cards

### Planned Improvements

- Booking System Enhancement
- Booking History
- View detailed station information
- Improved UI/UX
- Responsive Design
- Search and Filter Stations
- Enhanced Validation and Error Handling

---

## 📚 Learning Outcomes

This project has helped me gain practical experience with:

- Django project structure
- Django Models and ORM
- User Authentication
- CRUD Operations
- Template Rendering
- MySQL Integration
- File Uploads
- Browser Geolocation API
- Latitude and Longitude
- GeoPy distance calculation
- JSON communication between JavaScript and Django
- Git & GitHub
- Environment Variables using `.env`

---

## 👩‍💻 Author

**Shahanas K K**

Python Django Developer
