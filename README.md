# Notes App Full-Stack Web Application using Flask and Python

## 1 Introduction
The Notes Web Application is a Flask-based web application that allows users to create, store, and manage notes efficiently. 
It integrates with a database to store user information, notes, and authentication data. The app also supports basic user account operations, 
such as user registration, login, logout, and personalized note management. Developed using Flask, Flask-Login, and Flask-SQLAlchemy, the application 
ensures persistent storage of notes, allowing users to access their data after logging in.

## 2 Technologies Used
1. Flask: A lightweight web framework used to create the structure and handle HTTP requests.
2. Flask-Login: Manages user sessions, ensuring that each user's information is stored securely, and access is restricted based on authentication.
3. Flask-SQLAlchemy: A SQLAlchemy extension for Flask, used for database interactions, managing user information, and storing notes.
4. Werkzeug Security: For password hashing and verification.
5. HTML, CSS, and JavaScript: For front-end templates and interactivity.

## 3 Folder Structure
```
/Notes_App_Full-Stack_Web_Application
│
├── instance/
│   ├── database.db        # SQLite database storing user and notes data
│
├── website/
│   ├── static/            # Contains JavaScript files, CSS, and images
│   │   └── index.js       # JavaScript file for frontend logic
│   ├── templates/         # HTML templates for rendering pages
│   │   ├── base.html      # Base layout template
│   │   ├── home.html      # Homepage template (shows user's notes)
│   │   ├── login.html     # Login page template
│   │   ├── sign_up.html   # Sign-up page template
│   ├── __init__.py        # Initialize Flask app
│   ├── auth.py            # Handles authentication (login, sign up, logout)
│   ├── models.py          # Defines database models (User, Notes)
│   ├── views.py           # Contains routes and view logic for the app
│
├── main.py                # Main file to run the Flask application
├── requirements.txt       # Project dependencies (Flask, Flask-Login, Flask-SQLAlchemy, etc.)
├── Notes.txt              # General notes for the project
```

## 4 Application Functionality

### 4.1 User Authentication
The app allows users to register, log in, and manage sessions securely using Flask-Login and Werkzeug's password hashing functionalities.

1. Registration: New users can register by providing a username, email, and password. Passwords are securely hashed using generate_password_hash() from werkzeug.security.
2. Login: Users can log in using their email and password. Flask-Login's login_user() function is used to authenticate users and start their session.
3. Logout: Authenticated users can securely log out using logout_user().
4. Session Management: Flask-Login keeps track of authenticated users and ensures that only logged-in users can access certain routes (e.g., creating or viewing notes).

### 4.2 Notes Management
Once logged in, users can perform the following operations on their notes:

1. Create Notes: Users can create new notes. The notes are saved in the database, associated with the logged-in user.
2. View Notes: After login, the user can view all the notes they have created.
3. Delete Notes: Users have the ability to delete notes. This operation updates the database and removes the note from the UI.
4. This functionality ensures that user data is persistent and accessible across sessions.

### 4.3 Database Design
The application uses an SQLite database (database.db) for data persistence. The main entities stored in the database are users and notes. The models.py file defines two primary models: User and Note.
1. User Model: Stores user information, including an ID, email, password (hashed), and associated notes.
```
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    # creating an ID for all users to uniquely identify them.
    # because some of them may have the same email ID too.
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    # max 150 characters
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    # for relationship, your referencing name of class - it is capital.

    # yapindi - New Changes
    def is_active(self):
        return True
```

2. Note Model: Stores note content and links each note to a specific user via a foreign key relationship.
```
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
```

## 5 Authentication and Security
Security is critical in web applications, especially for user authentication. This app implements the following security measures:

1. Password Hashing: All passwords are hashed before storing in the database using generate_password_hash(). This ensures that even if the database is compromised, passwords remain secure.
2. Session Management: Only authenticated users can access note-related operations. The login_required decorator from Flask-Login restricts access to certain routes unless the user is logged in.
3. Flash Messages: Feedback messages (using flash()) are displayed for events like login failures, successful registration, or unauthorized access attempts.

## 6 Front-End and Templates
The app’s user interface is powered by HTML templates and rendered by Flask’s render_template() function. The templates folder consists of:

1. base.html: The master layout used by all pages (login, sign-up, home). It includes the navigation bar and imports necessary static files (CSS, JS).
2. home.html: Displays the list of notes created by the user. It provides a simple interface to add new notes and delete existing ones.
3. login.html: The login form where users authenticate themselves.
4. sign_up.html: The registration form for new users.

## 7 API Endpoints and Routing
Routes are handled by Flask using the views.py and auth.py files. These files contain the logic for different URLs the user can visit.

Authentication Routes (in auth.py):
/login: Handles user login.
/sign-up: Handles user registration.
/logout: Logs the user out.
App Routes (in views.py):
/: The homepage (accessible only after login) where the user can view, add, and delete notes.

## 8 Running the App
```
python main.py
```

## 9 Viewing the App
```
http://127.0.0.1:5000
```

## 10 Future Improvements
1. Deployment: The application is ready for deployment to platforms like Microsoft Azure.
2. Add Categories or Tags for Notes: Allow users to organize notes into categories or add tags for better management.
3. Share Notes: Add functionality to share notes with other users or export them as text or PDF files.
4. Search Functionality: Implement search capabilities so users can find specific notes based on keywords.
5. Enhanced Front-End: Improve the design and interactivity with frameworks like Bootstrap or Tailwind CSS.
