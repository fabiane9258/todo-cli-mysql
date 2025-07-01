# 📝 CLI To-Do List App (Python + MySQL)

A simple and modular command-line To-Do list application built with **Python** and **MySQL**, designed to demonstrate full-stack backend logic, database operations, and clean CLI interaction.

---

## 🚀 Features

- Add new tasks ✅
- List all tasks 📋
- Delete tasks 🗑️
- Persistent storage using MySQL
- Clean separation of logic and interface (MVC-style)

---

## 🧱 Tech Stack

- **Python 3**
- **MySQL**
- `mysql-connector-python` for DB connection
- `virtualenv` (recommended for environment isolation)

---

## 📁 Project Structure

todo/
├── cli.py # CLI interface (menu & input)
├── todo.py # Task logic (add, list, delete)
├── database.py # MySQL connection module
├── pycache/ # (Ignored) Compiled Python files
└── .gitignore # Ignoring pycache and venv