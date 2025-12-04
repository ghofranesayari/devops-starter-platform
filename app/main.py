import os
from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    @app.route("/info", methods=["GET"])
    def info():
        """
        Static info about the service.
        """
        return jsonify(
            {
                "service": "devops-starter-platform",
                "language": "python",
                "framework": "flask",
            }
        ), 200

    @app.route("/config", methods=["GET"])
    def config():
        """
        Return config values coming from environment variables.
        This is typical in real services (Dev/Prod, versions, etc.).
        """
        env = os.environ.get("APP_ENV", "local")
        version = os.environ.get("APP_VERSION", "1.0.0")

        return jsonify({"env": env, "version": version}), 200

    return app


if __name__ == "__main__":
    # Run the app for local development
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
