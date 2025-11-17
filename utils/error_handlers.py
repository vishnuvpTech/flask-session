from flask import jsonify


def register_error_handlers(app):


    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error="Bad Request"), 400


    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error="Not Found"), 404


    @app.errorhandler(429)
    def rate_limit(e):
        return jsonify(error="Too Many Requests"), 429