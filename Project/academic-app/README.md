# Academic Application

This is a minimal academic application built in Python. The application includes classes for managing users, students (Mahasiswa), lecturers (Dosen), and courses (Matakuliah).

## Project Structure

```
academic-app
├── src
│   ├── main.py          # Entry point of the application
│   └── models           # Contains model classes
│       ├── __init__.py  # Initializes the models package
│       ├── user.py      # User class definition
│       ├── mahasiswa.py  # Mahasiswa class definition
│       ├── dosen.py     # Dosen class definition
│       └── matakuliah.py # Matakuliah class definition
├── tests                # Contains unit tests
│   └── test_models.py   # Tests for the model classes
├── pyproject.toml       # Project configuration
├── requirements.txt      # Project dependencies
├── .gitignore           # Files to ignore in version control
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd academic-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
  # run the console example
  python src/main.py
  # or run the web server
  # from project root (academic-app):
  python -m src.app
  # or
  python src\app.py
  ```

## Run as Web App

- Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

- Start the Flask server:

```powershell
python -m src.app
```

Open your browser at `http://127.0.0.1:5000/` to view the app.

## Usage Examples

- Create a new user, student, or lecturer by instantiating the respective classes.
- Use the methods defined in each class to manage user information, course details, etc.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.