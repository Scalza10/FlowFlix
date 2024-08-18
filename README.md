# Sample Flask App with SQL Database Integration

## Overview
This is a sample Flask application that integrates with an SQL database and includes data models. The app's main feature is generating access codes that users can redeem to access content for a limited time. The application currently runs locally, but future plans include cloud hosting, implementing a microservice for emailing codes, and integrating Vue.js for the front end.

## Features
- **SQL Database Integration**: The app uses SQLAlchemy for database operations.
- **Data Models**: Well-defined data models to manage user data and access codes.
- **Code Generation**: The app generates codes that expire after a certain period.
- **User Access**: Users can redeem codes to access content within a specified time frame.

## Future Enhancements
- **Cloud Hosting**: Plan to deploy the app on a cloud platform like AWS, Azure, or Heroku.
- **Microservice for Emailing Codes**: A microservice will send codes to users via email.
- **Vue.js Integration**: Vue.js will be integrated to enhance the front-end experience.

## Prerequisites
- Python 3.x
- Flask
- SQLAlchemy
- SQLite (or any other preferred SQL database)

