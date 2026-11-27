"""HTTP-приложение для практики по CI."""

from flask import Flask, jsonify


def create_app():
    """Создаёт приложение и регистрирует маршруты."""
    application = Flask(__name__)

    @application.get("/health")
    def health():
        """Возвращает состояние приложения."""
        return jsonify(status="unhealthy")

    @application.get("/")
    def index():
        """Возвращает сведения о приложении."""
        return jsonify(service="devops-ci-app", version="1.0.0", status="running")

    return application


app = create_app()
