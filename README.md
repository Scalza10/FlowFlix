# Sample Flask App with SQL Database Integration

## Overview

This is a sample Flask application that integrates with an SQL database and includes data models. The app's main feature is generating access codes that users can redeem to access content for a limited time. The application is hosted on Azure Web App, includes a microservice for emailing codes, and has a Vue.js front end for an enhanced user experience.

## Features

- **SQL Database Integration**: The app uses SQLAlchemy for database operations.
- **Data Models**: Well-defined data models to manage user data and access codes.
- **Code Generation**: The app generates codes that expire after a certain period.
- **User Access**: Users can redeem codes to access content within a specified time frame.
- **Microservice for Emailing Codes**: A microservice sends codes to users via email.
- **Vue.js Integration**: Vue.js is integrated to enhance the front-end experience.
- **Cloud Hosting**: The app is deployed on Azure Web App.

## Future Enhancements

- **Advanced Analytics**: Implement analytics to track code usage and user engagement.
- **User Management**: Add features for user registration, login, and profile management.
- **Enhanced Security**: Implement OAuth for secure authentication and authorization.

## Prerequisites

- Python 3.x (3.12 preferred)
- Flask
- SQLAlchemy
- SQL Server (or any other SQL Database)
- Vue.js
- Axios
- SendGrid (for emailing codes)
- Azure Account (for hosting)

## Setup Instructions

### Backend Setup

1. **Clone the repository**:
   sh
   git clone https://github.com/your-repo/sample-flask-app.git
   cd sample-flask-app
2. **Create virtual Env**:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**:
    pip install -r requirements.txt

4. **Set up environment variables**: Create a .env file in the root directory and add the following:

DB_SERVER= DB Server Name
DB_DATABASE=DB Name
DB_USERNAME= Authorized UserName
DB_PASSWORD= Password for said User
SENDGRID_API_KEY= Sendgrid Api Key
SENDGRID_TEMPLATE_ID= needed only if using templates from sendgrid, can be modified to use plain HTML
SENDGRID_FROM_EMAIL= verified From email for sendgrid

5. **Run the flask App**

### Frontend Setup

1. **Navigate to the frontend directory:**
    cd frontend

2. **Install dependencies:**
    npm install

3. **Run the Vue.js development server:**
    npm run serve

## Deployment

The application is deployed on Azure Web App. Follow the Azure documentation for deploying Flask and Vue.js applications.

## Usage

- **Access the application**: Navigate to the deployed URL on Azure.
- **Generate and redeem codes**: Use the application to generate access codes and redeem them to access content.
- **Send codes via email**: Use the microservice to send access codes to users via email.

## License

This project is licensed under the MIT License.
