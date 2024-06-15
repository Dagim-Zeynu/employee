# 🌟 Employee List

Employee List is a Django web application that allows an admin to manage a list of employees. The admin can add employees with their full name, email, phone number, and role at the company. The front end displays a list of employees, and clicking on an employee's name redirects to a detailed view of that employee.

## ✨ Features

- 🛠 **Admin Interface**: Add and manage employees with ease.
- 📜 **Employee List**: View a comprehensive list of all employees.
- 📋 **Employee Details**: Click on an employee to see detailed information.

## 📋 Requirements

- 🐍 Python 3.12.2
- 🌐 Django 5 or higher

## 🚀 Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/employee-list.git
    cd employee-list
    ```

2. **Create a virtual environment and activate it**:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations**:

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser to access the admin interface**:

    ```sh
    python manage.py createsuperuser
    ```

6. **Start the development server**:

    ```sh
    python manage.py runserver
    ```

7. **Open your browser and go to** `http://127.0.0.1:8000/admin` **to log in to the admin interface and start adding employees**.

## 🛠 Usage

1. **Log in** to the admin interface and add employees with their details.
2. **Visit the front end** at `http://127.0.0.1:8000/` to see the list of employees.
3. **Click on an employee's name** to view their details.


