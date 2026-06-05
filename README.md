# danish-shehjehan_final_code  

A **Django‑based Electronic Voting System (EVS)** that leverages a lightweight blockchain to guarantee vote immutability and auditability. The repository contains the core `evs` app, migrations, admin configuration, forms, and a custom blockchain implementation.

---

## Overview  

The EVS provides a web interface for creating elections, registering candidates, and casting votes. Each vote is stored as a block in a simple proof‑of‑work chain, ensuring that once a vote is recorded it cannot be altered without breaking the chain’s hash integrity. The project is structured as a reusable Django app (`evs`) that can be integrated into any Django project.

---

## Features  

| Feature | Description |
|---------|-------------|
| **Blockchain‑backed voting** | Every vote is encapsulated in a `Block` object; the chain is validated on each new vote. |
| **Admin dashboard** | Full CRUD for elections, candidates, and blocks via Django admin. |
| **Custom forms & validation** | Secure voting forms with server‑side validation to prevent duplicate or malformed submissions. |
| **Database migrations** | 16 incremental migrations handling schema evolution (candidates, elections, block fields, etc.). |
| **Reusable Django app** | The `evs` app can be added to any Django project via `INSTALLED_APPS`. |
| **Extensible architecture** | Clear separation of models, views, forms, and blockchain logic for easy extension. |

---

## Tech Stack  

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.9+ |
| **Web framework** | Django 4.x |
| **Database** | SQLite (default) – can be swapped for PostgreSQL, MySQL, etc. |
| **Blockchain** | Custom proof‑of‑work implementation (`evs/blockchain.py`) |
| **Front‑end** | Django templates (Bootstrap optional) |
| **Testing** | Django’s built‑in test runner (extendable with pytest) |

---

## Installation  

> **Prerequisite:** Python 3.9 or newer and Git installed on your machine.

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/danish-shehjehan_final_code.git
cd danish-shehjehan_final_code

# 2️⃣ Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# 3️⃣ Install dependencies
pip install --upgrade pip
pip install -r requirements.txt   # If a requirements file is not present, install Django manually:
# pip install Django==4.*

# 4️⃣ Apply database migrations
python manage.py migrate

# 5️⃣ (Optional) Create a superuser for the admin interface
python manage.py createsuperuser
```

*If the project uses environment variables (e.g., secret keys), create a `.env` file and replace any placeholder values with your own, e.g.:*  

```dotenv
DJANGO_SECRET_KEY=YOUR_OWN_API_KEY
```

---

## Usage  

```bash
# Start the development server
python manage.py runserver
```

1. Open a browser and navigate to `http://127.0.0.1:800