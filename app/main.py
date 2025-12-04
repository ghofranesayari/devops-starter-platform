from flask import Flask, jsonify

def create_app():
    """
    Application factory.
    This function creates and configures the Flask app.
    Using a factory makes the project easier to extend and test later.
    """
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health():
        """
        Simple health check endpoint.
        Used to know if the service is alive.
        """
        return jsonify({"status": "ok"}), 200

    @app.route("/info", methods=["GET"])
    def info():
        """
        Basic info about the app and about you.
        Later you can add version, environment, etc.
        """
        data = {
            "app": "devops-starter-platform",
            "role": "Junior DevOps / Cloud Engineer",
            "location": "Tunisia",
            "message": "Hello from my CI/CD-ready API 👋"
        }
        return jsonify(data), 200

    return app


# This block is executed only when we run:
#   python app/main.py
if __name__ == "__main__":
    app = create_app()
    # host="0.0.0.0" makes it reachable from the browser on localhost
    app.run(host="0.0.0.0", port=8000, debug=True)
