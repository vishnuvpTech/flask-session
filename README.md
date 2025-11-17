<div align="center"><img src="https://raw.githubusercontent.com/pallets/flask/refs/heads/stable/docs/_static/flask-name.svg" alt="" height="150"></div>

# Flask

Flask is a lightweight [WSGI] web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around [Werkzeug]
and [Jinja], and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

[WSGI]: https://wsgi.readthedocs.io/
[Werkzeug]: https://werkzeug.palletsprojects.com/
[Jinja]: https://jinja.palletsprojects.com/


Key points:
- Micro‑framework with no mandatory ORM or tools.
- Easy to learn and ideal for rapid prototyping.
- Used in production systems at scale.

---

## 🚀 Why Choose Flask?
- Minimal boilerplate.
- Large ecosystem of extensions.
- Great documentation and community.
- Highly flexible for small and large applications.
- Clear architecture and easier onboarding for teams.

---


## 🏷️ Latest Version
- **Flask 3.1.2** (Released: Aug 19, 2025)
- Previous major release: **3.1.0** (Nov 13, 2024)

Python compatibility:
- Requires **Python 3.9+**

---

## A Simple Example

```python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

```
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## 📂 Simple Flask Project Structure

### 🔹 Web Application Structure
```
myflaskapp/
  ├── app/
  │   ├── __init__.py
  │   ├── config.py
  │   ├── extensions.py
  │   ├── models.py
  │   ├── auth/                       # blueprint: authentication
  │   │   ├── __init__.py
  │   │   ├── routes.py
  │   │   ├── forms.py
  │   │   └── templates/auth/
  │   │       └── login.html
  │   ├── main/                       # blueprint: app main pages / api
  │   │   ├── __init__.py
  │   │   ├── routes.py
  │   │   └── templates/main/
  │   ├── api/                        # optional: REST API blueprint
  │   │   ├── __init__.py
  │   │   └── routes.py
  │   ├── templates/
  │   │   ├── base.html
  │   │   └── 404.html
  │   ├── static/
  │   │   ├── css/
  │   │   ├── js/
  │   │   └── images/
  │   └── tasks.py                    # optional celery tasks
  ├── migrations/                     # Alembic/Flask-Migrate files (gitignored)
  ├── tests/
  │   ├── conftest.py
  │   ├── test_basic.py
  │   └── ...
  ├── .env
  ├── .flaskenv
  ├── Dockerfile
  ├── docker-compose.yml
  ├── requirements.txt
  ├── manage.py                        # cli entry (migrate, shell)
  ├── wsgi.py                          # production entrypoint for gunicorn
  ├── README.md
  └── .gitignore

```
**Highlights:**
- `app/` contains application package (blueprints keep code modular).
- `extensions.py` centralizes objects like db, login_manager, migrate, mail.
- `config.py` holds environment-specific configuration classes.
- `manage.py` or `wsgi.py` used for running and deployment.
- `migrations/` created by Flask-Migrate (Alembic).
- `tests/` for unit/integration tests with pytest.
- `Dockerfile/` & `docker-compose.yml` for containerized deployment.

---

### 🔹 REST API Application Structure
```
flask_api_app/
  ├── app/
  │   ├── __init__.py
  │   ├── config.py
  │   ├── extensions.py
  │   ├── models/
  │   │   ├── __init__.py
  │   │   └── user.py
  │   ├── api/
  │   │   ├── __init__.py
  │   │   ├── v1/
  │   │   │   ├── __init__.py
  │   │   │   ├── routes.py
  │   │   │   ├── schemas.py    # marshmallow / pydantic validation
  │   │   │   └── controllers/  # business logic
  │   │   │       ├── __init__.py
  │   │   │       └── user_controller.py
  │   ├── services/
  │   │   └── user_service.py
  │   ├── utils/
  │   │   ├── helpers.py
  │   │   └── exceptions.py
  │   ├── middlewares/
  │   │   └── auth_middleware.py
  │   └── tasks/
  │       └── celery_tasks.py
  ├── migrations/
  ├── tests/
  │   ├── test_user.py
  │   ├── conftest.py
  │   └── ...
  ├── requirements.txt
  ├── manage.py
  ├── wsgi.py
  ├── .env
  ├── docker-compose.yml
  ├── Dockerfile
  └── README.md

```
**Highlights:**
- `api/`	API versions & route handlers
- `api/v1/routes.py`	All endpoints of API v1
- `api/v1/schemas.py`	Marshmallow/Pydantic validation
- `api/v1/controllers/`	Business logic for routes
- `models/`	SQLAlchemy models
- `services/`	Complex logic (DB ops, external API calls)
- `utils/`	Helper functions and custom exceptions
- `middlewares/`	Auth, Rate limit, etc.
- `extensions.py`	Initialize db, migrate, jwt, cache, etc.
- `config.py`	Config classes (dev, prod)
- `manage.py`	Run commands (flask db migrate etc.)
- `wsgi.py`	Gunicorn entrypoint
- `migrations/`	Alembic migrations
- `tests/`	Unit tests using pytest
- Clean layering → scalable API design

---


## 🧠 Best Practices
- Always use a virtual environment.
- Pin dependency versions in `requirements.txt`.
- Review and set security configs:
  - `MAX_CONTENT_LENGTH`
  - `MAX_FORM_MEMORY_SIZE`
  - `SESSION_COOKIE_SECURE`
- Use `SECRET_KEY_FALLBACKS` for safe key rotation.
- Keep Flask extensions modern and compatible.
- Use Flask’s built-in test client for reliable unit tests.
- Follow modular design using **Blueprints** for large apps.
- Use environment-based config classes (Dev, Prod, Test).
- Store secrets in environment variables (never commit secrets).
- Implement request validation using libraries like `marshmallow` or `pydantic`.
- Add logging using Python’s `logging` module or `loguru`.
- Use `.env` files with `python-dotenv` for configuration management.
- Structure services and controllers separately for clean architecture.
- Use pagination for large API responses.
- Enable CORS properly when building APIs.
- Protect routes with authentication (JWT, OAuth, or Session-based).
- Employ rate limiting for public APIs using `Flask-Limiter`.
- Cache frequently accessed data using `Flask-Caching`.
- Use `gunicorn` or `uwsgi` for production; avoid running `flask run`.
- Implement graceful error handling using custom error handlers.
- Add health-check routes for monitoring.
- Write unit tests for routes, services, and utilities.
- Containerize the app using Docker for consistent deployment.
- Maintain CI/CD pipelines for automatic testing and deployment.
- Use proper database connection management & connection pooling.
- Apply database migrations using `Flask-Migrate`.
- Avoid long-running tasks inside Flask—use Celery or RQ.
- Use Nginx as reverse proxy in production.
- Monitor performance using APM tools (like New Relic, Datadog).
- Document APIs using Swagger/OpenAPI (`flasgger`, `apispec`).
- Always use a virtual environment.
- Pin dependency versions in `requirements.txt`.
- Review and set security configs:
  - `MAX_CONTENT_LENGTH`
  - `MAX_FORM_MEMORY_SIZE`
  - `SESSION_COOKIE_SECURE`
- Use `SECRET_KEY_FALLBACKS` for safe key rotation.
- Keep Flask extensions modern and compatible.
- Use Flask’s built‑in test client for reliable unit tests.

---

## 💡 Example Configuration (3.1.x Features)
```python
from flask import Flask, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "current-key"
app.config["SECRET_KEY_FALLBACKS"] = ["old-key-1", "old-key-2"]
app.config["SESSION_COOKIE_PARTITIONED"] = True

@app.route('/')
def index():
    session['user'] = 'alice'
    return "Hello, Flask!"
```

---

## 🔐 Security Best Practices
- Always set a strong `SECRET_KEY` and rotate using `SECRET_KEY_FALLBACKS`.
- Enable `SESSION_COOKIE_SECURE`, `SESSION_COOKIE_HTTPONLY`, and `SESSION_COOKIE_SAMESITE`.
- Validate and sanitize all input; use schemas (`marshmallow`/`pydantic`).
- Use HTTPS everywhere; redirect HTTP to HTTPS in production.
- Avoid exposing sensitive error messages — use custom error handlers.
- Rate‑limit sensitive endpoints (login, OTP, password reset) using `Flask-Limiter`.
- Protect against CSRF using `Flask-WTF` for forms or manual CSRF tokens.
- Use parameterized queries for DB operations to avoid SQL injection.
- Implement authentication using JWT or OAuth with proper token expiry.
- Restrict file uploads and validate file types; store outside webroot.
- Set `CONTENT_SECURITY_POLICY` headers to mitigate XSS and clickjacking.
- Use `trusted_hosts` to prevent Host‑header injection.
- Periodically update dependencies to patch vulnerabilities.
- Run security scans (Bandit, pip‑audit) regularly.

## 🙌 Further Reading
- Flask Documentation: https://flask.palletsprojects.com

---


## 👍 Pros and 👎 Cons of Flask

### **Pros**
- Lightweight and minimalistic; gives full control to developers.
- Flexible architecture — choose your own ORM, auth system, and tools.
- Easy learning curve and great for beginners.
- Large ecosystem of extensions for any feature.
- Simple to scale from small apps to enterprise-level systems.
- Clean routing and modularization using Blueprints.
- Perfect for microservices and REST API development.
- Fast development cycle — ideal for prototypes and MVPs.
- Excellent documentation and active community.

### **Cons**
- No built‑in ORM, authentication, or form handling (must add manually).
- Can become unstructured in large teams if not following best practices.
- Requires manual decisions for architecture (not opinionated).
- Not as feature-rich out of the box compared to Django.
- Extensions may vary in quality and long‑term maintenance.
- Might require more setup for production‑ready deployments.

---
---