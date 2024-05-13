import azure.functions as func
from Flaskapp import app as flask_app  # Import the Flask app

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Redirect HTTP requests to the Flask app."""
    return func.WsgiMiddleware(flask_app.wsgi_app).handle(req, context)
