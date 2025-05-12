import sys
import os

# This line is crucial for running the app from within the src directory or if main.py is the entry point.
# It adds the parent directory of 'src' (i.e., the project root 'campus_bet') to the Python path.
# This allows Python to find the 'src' package for imports like 'from src import create_app'.
# The create_flask_app template includes a similar line.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import create_app

app = create_app()

if __name__ == "__main__":
    # Note: For deployment, a production WSGI server like Gunicorn or uWSGI should be used.
    # The debug=True mode is suitable for development only.
    # The host='0.0.0.0' makes the server accessible externally if needed (e.g., within a Docker container or LAN).
    app.run(host="0.0.0.0", port=5000, debug=True)

