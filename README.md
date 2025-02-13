# FinanceApp

FinanceApp is a Django-based web application designed to manage and track various bills and expenses. Users can add bills, set due dates, and monitor payments efficiently.

## Features
- User authentication (Login/Register)
- Add and manage bills (Water, Internet, Garbage, Electricity, etc.)
- Track due dates and amounts
- Responsive UI using HTML & CSS

## Installation & Setup

### Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.8)
- pip (Python package manager)
- Virtual environment support (`venv`)
### **Setting Up the Project**

#### **Step 1: Clone the Repository**
```sh
# Navigate to your desired directory and clone the repository
$ git clone https://github.com/yourusername/financeApp.git
$ cd financeApp
```

#### **Step 2: Create a Virtual Environment**
##### **On Linux/macOS:**
```sh
$ python3 -m venv myworld
$ source myworld/bin/activate
```
##### **On Windows:**
```sh
$ python -m venv myworld
$ myworld\Scripts\activate
```

#### **Step 3: Install Dependencies**
```sh
$ pip install -r requirements.txt
```

#### **Step 4: Apply Migrations**
```sh
$ python manage.py migrate
```

#### **Step 5: Run the Development Server**
```sh
$ python manage.py runserver
```
Now, open your browser and go to `http://127.0.0.1:8000/` to access the application.

## File Structure Overview
```
financeApp/
│── manage.py          # Django project manager
│── db.sqlite3         # Database (SQLite by default)
│── requirements.txt   # Project dependencies
│── financeApp/        # Main project settings
│   ├── settings.py    # Configuration file
│   ├── urls.py        # URL routing
│   ├── wsgi.py        # WSGI entry point
│── members/           # Core app for bill management
│   ├── models.py      # Database models
│   ├── views.py       # Application logic
│   ├── templates/     # HTML templates for frontend
│   │   ├── add_bill.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   ├── register.html
```
---
### **Contributing**
Feel free to submit a pull request if you'd like to contribute!
