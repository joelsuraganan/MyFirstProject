from datetime import datetime

def get_greeting():
    """Returns a greeting based on the current time of day."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

if __name__ == "__main__":
    print(get_greeting())
