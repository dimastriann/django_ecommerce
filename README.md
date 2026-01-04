# Django E-Commerce Project

A modern, fully-functional e-commerce platform built with Django 6.0 and Tailwind CSS. This project features a robust product management system, a user-friendly shopping cart, secure user authentication, and an order processing flow.

## 🚀 Features

- **Product Catalog**: Browse products by categories with detailed view pages.
- **Shopping Cart**: Add, remove, and update products in the cart without losing session data.
- **User Authentication**: Secure sign-up, login, and profile management using a custom user model.
- **Order Management**: Streamlined checkout process with address details and order history.
- **Responsive Design**: Beautifully styled with Tailwind CSS for a premium look on all devices.
- **Real-time Development**: Integrated with `django-browser-reload` for a seamless developer experience.

## 🛠️ Tech Stack

- **Backend**: [Django 6.0](https://www.djangoproject.com/) (Python)
- **Frontend Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Database**: PostgreSQL (configured via `django-environ`)
- **Environment Management**: `django-environ`
- **Linting & Formatting**: [Ruff](https://github.com/astral-sh/ruff) & [djLint](https://www.djlint.com/)

## 💻 Local Development Setup

Follow these steps to get the project running locally:

### 1. Clone the repository
```bash
git clone <repository-url>
cd django_ecommerce
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install dependencies
*Note: Ensure you have Python and Node.js installed.*
```bash
pip install -r requirements.txt  # If requirements.txt exists
# OR
pip install django django-environ django-tailwind django-browser-reload psycopg2-binary
```

### 4. Setup environment variables
Create a `.env` file in the root directory and add the following:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://user:password@localhost:5432/db_name
```

### 5. Setup Tailwind CSS
```bash
python manage.py tailwind install
python manage.py tailwind build
```

### 6. Run migrations and start the server
```bash
python manage.py migrate
python manage.py runserver
```

## 📁 Project Structure

- `accounts/`: Custom user model and authentication logic.
- `store/`: Product and category management.
- `cart/`: Shopping cart logic and context processors.
- `orders/`: Checkout and order processing.
- `theme/`: Tailwind CSS configuration and assets.
- `templates/`: Global and app-specific HTML templates.

## 📜 License

This project is licensed under the MIT License.
