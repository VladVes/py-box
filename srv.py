from wsgiref.simple_server import make_server
from main import app

def server(wsgi_app):
    served = make_server("", 8000, wsgi_app)
    print("Serving HTTP on port 8000...")

    served.serve_forever()
    
if __name__ == "__main__":
    server(app)