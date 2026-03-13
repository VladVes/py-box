from datetime import datetime


def app(environ, start_response):
    time = datetime.now()
    data = bytes(f"Hello, Python!\nThe time is {time:%b %d %H:%M:%S}", "utf-8")
    start_response(
        "200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
    )
    return iter([data])
