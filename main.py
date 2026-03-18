from datetime import datetime
from str_slices import str1, str2, str3, str4, str5, str6, str7


def app(environ, start_response):
    time = datetime.now()
    data = bytes(f'''
                Hello, Python!
                The time is {time:%b %d %H:%M:%S}
                ---------------------------------
                String Slices Exampl:
                Source str = 'code-basics'. 
                Get slice:
                    'sic': {str1}
                    from first to 3 char: {str2}
                    from 4 to last: {str3}
                    'sic' another way: {str4}
                    'oebs': {str5}
                    revese: {str6}
                    'cisab': {str7}
                ---------------------------------
                String method Example:
                Source str = 'Hexlet'
                
                 
                
                ''', "utf-8")
    # data = bytes(f"Hello, Python!\nThe time is {time:%b %d %H:%M:%S}", "utf-8")
    start_response(
        "200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
    )
    return iter([data])
