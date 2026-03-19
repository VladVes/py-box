from datetime import datetime
from str_slices import str1, str2, str3, str4, str5, str6, str7
from str_methods import data 

def app(environ, start_response):
    # data = bytes(f"Hello, Python!\nThe time is {time:%b %d %H:%M:%S}", "utf-8")
    start_response(
        "200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
    )
    return iter([data])
