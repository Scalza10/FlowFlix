import os
import re
from flask import request, jsonify
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def is_valid_email(email):
    # Simple regex for email validation
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def send_email():
    email = request.args.get('email')
    
    if not email or not is_valid_email(email):
        return jsonify({"message": "Invalid email address"}), 400

    data = {
        "personalizations": [
            {
                "to": [{"email": email}],
            }
        ],
        "from": {"email": f"{os.getenv('SENDGRID_FROM_EMAIL')}"},
        "template_id": f"{os.getenv('SENDGRID_TEMPLATE_ID')}",
    }
    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error sending email"}), 400