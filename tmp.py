def get_status(status_code: int) -> str:
    match status_code:
        case 100:
            return "processing" 
        case 200:
            return "success"
        case 300:
            return "pending"
        case _:
            return "unknown status"

print(get_status(100))
print(get_status(200))
print(get_status(300))
print(get_status(00))