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
  A virtual environment keeps project-specific Python packages separate so they don’t conflict with other projects.
- Pin dependency versions in `requirements.txt`.
  Specify exact versions (Flask==3.0.3) so the app behaves the same everywhere (dev, prod, CI/CD).
- Review and set security configs:
  - `MAX_CONTENT_LENGTH` → limits maximum request size (prevents large file attacks).
  - `MAX_FORM_MEMORY_SIZE` → limits data for form submissions.
  - `SESSION_COOKIE_SECURE` → forces cookies to be sent only over HTTPS.
- Use `SECRET_KEY_FALLBACKS` for safe key rotation.
  Allows safe rotation of old secret keys without breaking existing sessions.
- Keep Flask extensions modern and compatible.
  Use updated versions of extensions like Flask-JWT, SQLAlchemy, etc., to avoid security risks and bugs.
- Use Flask’s built-in test client for reliable unit tests.
  A stable and easy way to test routes without running a live server.
- Follow modular design using **Blueprints** for large apps.
  Break large apps into modules (auth, users, admin), making code clean and maintainable.
- Use environment-based config classes (Dev, Prod, Test).
  Each environment loads only the required config.
- Store secrets in environment variables (never commit secrets).
  Never commit secrets like API keys or database passwords into Git.
- Implement request validation using libraries like `marshmallow` or `pydantic`.
  Use marshmallow or pydantic to validate incoming JSON and form data.
- Add logging using Python’s `logging` module or `loguru`.
  Use Python’s logging module or loguru for clean logs (errors, warnings, info).
- Use `.env` files with `python-dotenv` for configuration management.
  Store configs (DB URL, SECRET_KEY) in .env and load with python-dotenv.
- Structure services and controllers separately for clean architecture.
  controllers → handle API routes
  services → handle business logic
  This improves clean architecture.
- Use pagination for large API responses.
  Helps avoid returning huge datasets in one response.
- Enable CORS properly when building APIs.
  Allows frontend apps (React/Next.js) to access your Flask API safely.
- Protect routes with authentication (JWT, OAuth, or Session-based).
  Use JWT, OAuth, or Session Auth to secure APIs.
- Employ rate limiting for public APIs using `Flask-Limiter`.
  Use Flask-Limiter to prevent abuse or DDoS-like behavior.
- Cache frequently accessed data using `Flask-Caching`.
  Use Flask-Caching to speed up API response time.
- Use `gunicorn` or `uwsgi` for production; avoid running `flask run`.
  Never use flask run in production; it's not safe or efficient.
- Implement graceful error handling using custom error handlers.
  Create custom error handlers for clean JSON responses.
- Add health-check routes for monitoring.
  Example: `/health` → returns simple "OK" for monitoring tools.
- Write unit tests for routes, services, and utilities.
  Catch bugs early and ensure features work as expected.
- Containerize the app using Docker for consistent deployment.
  Ensures same environment everywhere (dev, staging, prod).
- Maintain CI/CD pipelines for automatic testing and deployment.
  Automate testing and deployment for reliability.
- Use proper database connection management & connection pooling.
  Use pooled connections to avoid exhausting DB connections.
- Apply database migrations using `Flask-Migrate`.
  Safely update database schema across environments.
- Avoid long-running tasks inside Flask—use Celery or RQ.
  Move big tasks (email sending, reports) to Celery or RQ.
- Use Nginx as reverse proxy in production.
  Handles SSL, static files, load balancing before traffic reaches Flask.
- Monitor performance using APM tools (like New Relic, Datadog).
  Use tools like Datadog, New Relic to monitor errors, latency, and performance.
- Document APIs using Swagger/OpenAPI (`flasgger`, `apispec`).
  Use Swagger, Flasgger, or APISpec to generate API documentation.

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