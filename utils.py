def read_wordlist(file_path):
    """Reads a wordlist file and returns a list of words."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Wordlist file not found: {file_path}")
        return []

def log_error(message):
    """Logs error messages."""
    print(message)

# Common configurations
REQUEST_TIMEOUT = 5  # Timeout for HTTP requests in seconds
