# Scissor Project Documentation

# Introduction
Scissor is a URL shortener project that allows users to create shortened versions of long URLs. It provides a simple and convenient way to generate short URLs that can be easily shared and accessed.

# Features
- URL Shortening: Users can enter a long URL and generate a shortened version of it.
- Redirect: Shortened URLs automatically redirect to the original long URL when accessed.
- Analytics: Basic analytics are provided, such as the number of clicks and the creation date of the shortened URLs.
- User Authentication: Users can create an account, log in, and manage their shortened URLs.

# Technologies Used
- Backend Framework: Flask
- Database: SQLite (can be replaced with other databases like PostgreSQL)
- Frontend: HTML, CSS, JavaScript
- Version Control: Git

# Installation and Setup
- Clone the repository: git clone https://github.com/walescript/scissor.git
- Navigate to the project directory: cd scissor
- Create a virtual environment: python3 -m venv env
- Activate the virtual environment:
- On macOS and Linux: source env/bin/activate
- On Windows: .\env\Scripts\activate
- Install the project dependencies: pip install -r requirements.txt
- Run database migrations: python manage.py migrate
- Start the development server: python3 app.py

# Configuration
- Database Configuration: The project is configured to use SQLite by default. If you want to use a different database, update the database settings in the settings.py file.
- Environment Variables: The project uses environment variables to store sensitive information such as the secret key. Set these variables in a .env file in the project root directory. Refer to the .env.example file for the required variables.

# Usage
- Access the application in your web browser: http://taglio.site
- Register an account or log in if you already have one.
- On the homepage, enter a long URL in the input field and click the "Shorten" button.
- The shortened URL will be generated and displayed on the page.
- Copy the shortened URL and share it with others.

# Acknowledgements
This project was created as a learning exercise. Some code and concepts may have been adapted or inspired by online tutorials and resources. Feel free to customize this documentation to fit the specific details and structure of your Scissor project.


