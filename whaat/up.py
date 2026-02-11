# up.py
def set_timer(seconds):
    """Run a countdown timer for the given number of seconds."""
    try:
        seconds = int(seconds)
        if seconds <= 0:
            print("Please enter a positive number of seconds.")
            return

def run_useless():
    print("Useless Program!")

if __name__ == "__main__":
    run_useless()