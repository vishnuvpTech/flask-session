from flask import Flask
from config import Config
from extensions.db import init_db
from extensions.limiter import init_limiter
from extensions.security_headers import set_security_headers
from utils.error_handlers import register_error_handlers
from blueprints.main import main_bp
from blueprints.auth import auth_bp




def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)


    # Initialize Extensions
    init_db(app)
    init_limiter(app)


    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")


    # Security Headers
    @app.after_request
    def secure_headers(response):
        return set_security_headers(response)


    # Error Handlers
    register_error_handlers(app)


    return app




app = create_app()


if __name__ == '__main__':
    app.run(debug=True)