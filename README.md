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
flask_web_app/
│
├── app.py
├── requirements.txt
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── index.html
│   └── layout.html
└── instance/
    └── config.py
```
**Highlights:**
- `templates/` for HTML files (Jinja2)
- `static/` for CSS, JS, images
- `app.py` is the entry point
- `instance/config.py` for environment-specific configuration

---

### 🔹 REST API Application Structure
```
flask_api_app/
│
├── app.py
├── requirements.txt
├── config.py
├── controllers/
│   ├── user_controller.py
│   └── product_controller.py
├── models/
│   ├── user.py
│   └── product.py
├── services/
│   ├── user_service.py
│   └── product_service.py
└── utils/
    └── helpers.py
```
**Highlights:**
- `controllers/` contains routes (API endpoints)
- `models/` for data structures / ORM models
- `services/` for business logic
- `utils/` for reusable helpers
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


## ✨ Code-base structure
The project has a super simple structure, represented as below:
```
< PROJECT ROOT >
   |
   |-- app/
   |    |
   |    |-- __init__.py                 # Initialization of app
   |    |-- config.py                   # Handlers for the front end routes
   |    |-- setup_security.py                      
   |    |-- auth/
   |    |
   |    |   |-- __init__.py
   |    |   |-- email.py
   |    |   |-- forms.py
   |    |   |-- models.py               # Database models for storing data
   |    |   |-- routes.py               # REST API hanlder
   |    |
   |    |-- static/                     # CSS files, Javascripts files
   |    |   
   |    |   |-- css/
   |    |   |
   |    |   |   |-- bootstrap.min.css
   |    |   |   |-- bootstrap.min.css.map
   |    |   |   |-- style.css
   |    |   |
   |    |   |-- js/
   |    |   |
   |    |   |   |-- bootstrap.min.js
   |    |   |   |-- jquery.min.js
   |    |   |
   |    |-- templates/
   |    |
   |    |    |-- auth/                    # Auth related pages login/register
   |    |    |
   |    |    |    |-- login.html
   |    |    |    |-- register.html
   |    |    |    |-- reset_password.html
   |    |    |    |-- reset_password_request.html
   |    |    |
   |    |    |-- bootstrap/
   |    |    |
   |    |    |    |-- bs5_base.html
   |    |    |
   |    |    |-- email/
   |    |    |  
   |    |    |    |-- reset_password.html
   |    |    |    |-- reset_password.txt
   |    |    |
   |    |    |-- forms/
   |    |    |
   |    |    |    |-- forms.html
   |    |    |
   |    |    |-- navbar/
   |    |    |  
   |    |    |    |-- messages.html
   |    |    |    |-- navbar.html
   |    |    |-- base.html
   |    |
   |    |-- utils/
   |    |
   |    |    |-- __init__.py
   |    |    |-- app_logger.py
   |    |    |-- decorators.py
   |    |    |-- mailer.py
   |    |
   |-- requirements.txt
   |-- run.py
   |
   |-- ************************************************************************
```


