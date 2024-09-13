from datetime import datetime, timedelta
import random
import string
from models import db, Code


def generate_code():
    new_code = Code(
        Code="".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
        ExpirationDate=datetime.now() + timedelta(hours=7),
    )
    db.session.add(new_code)
    db.session.commit()
    return new_code.Code
