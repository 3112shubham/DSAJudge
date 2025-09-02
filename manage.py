#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webcheck.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# set FIREBASE_KEY_JSON=C:\D\Dev-Projects\TP\DSAJudge\firebase_key.json

# {
#   "type": "service_account",
#   "project_id": "dsa-evaluation",
#   "private_key_id": "a4afefb1deaf5c65464e8212b755be9097bf6d12",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCw7L5xr7Iua05l\nF7QbtlBUgSujKk7YwC/lGzSuHKsECvV06iHs9/qdvg7c7mEnCV/rMMGBLPh41xA7\na/ZVTtglmEfOl+jV5LnCHl6GpZpoM1boVfxDlngSc/9M2912mVrNclrVqyVRG2YC\niVTLc4qrwmQPon1crx5bGWt0aUOik+ryxn8UTxLlpVbWT2dSxuPyg1i+s2Oq4+Ms\nub0U6mSzvYEvhWD6dVGaCamQE6qAnDMGdL1rRlcIG7ABywpoujBPMdYzeo+lysRl\nvPVVwtdTEAZgEw5bX/K84pyyuPVcqARlY8iCcDvtWqe1IEXATnMI4fXOtCC/TWdN\n9p1CBe3tAgMBAAECggEACwH3yV/6kIvJmV2TraO2tMNCoUi5FiBC+piqOuj6tOov\nomIM0U8ObzELgLBuJ/0b1Ci46V4QaYhL8L6DWYRpy1EBqrdl26T677pu/CaiiDgl\ngJgU9WmPt+oyqKgHS+E3to+WWjPnQvgW7TJ5LZ1XM9+I1TYxYYpds6JNvrTr6dn6\nU9GoUMljEcNiy8FUzoauJYxDDUYQrNoe4bw23xZNHgwiTGlG0Q40vl3ifl+lMg0U\nY+RnaERdZKZYT5fjp+0ri2xIiOLdNYnLNtAfzcKxgo0zAJRuAcR1kkpxDHWtEDb3\nIWs/pi0kDEmY6YJT09cyFwJ/6UvFeYahdzymTK/wqwKBgQD5Ype/RqOtip75WE4v\nePYRp+oP7TbvE3vMShttg69eEsnHgMqd3YxKm6b5Nc1qaAcNeoj0E2QwvEkcCUyd\nT3UmkmY7SlrwuUU6v4haz589tnaDatQANjpHltcwWoPv0a4gXYY2P84f0AipRTol\nS0J7JFPmZuHwab+4H3/wEMMR2wKBgQC1nh8bkKmdmad+2lHsLJi+sEhRmxOsQReO\nBq54i8n4ozJMf8NBSXw0YbN3/Pgkrb00zgN/+E9J7MjhYv5dCaXCCGXF2A2ActjN\n42XxtMmVM5S8k2cC9Q6bD3EUdCnAJHrrspTlI6mpQamwpD7RnzRXsAfliq+T/AR4\nqYskRY591wKBgQDCK7zBJiv8zAi5VcMSfVkCKD47BlSWUxI53p16aGSbl39aAXJA\n9iXsVULtmLGGntaW7QhDGfIRbBh0Zt0rQpmRXb2RfnROJ8K6WjS9mBiBgVbHPd8x\nBwfbg5uqv18o05aDBq6gAI/p/x0vRoJeVTm/DWrx4rsaaAvpPUVs0nA/rwKBgGZr\nOyOyWtSTeA9jUtua8rBmfQH4MAnt0zi2r+EvA8EBVzYovpWsuSxZBHpf4BffGloS\n64pZH22S6F2iE8unyyA22B3QDx0mpvjEihLaXuuS4QfPIEJcq9XpyV09fOXsLJ2K\nYckuaVkXvHfux7Yyz7O7g1iA8y7C6kqZYewchZSVAoGBAObt5U5Pf59bMLR7eRrK\nrI3UHRZU/fbj5Pvp85lRw2G6YWhEla6FdVn7XjoOWhpzChXNvs9b3CHdAIaAcZZf\nS/55TULXClTIhLxiY6hNNoQvub69gOkOGWRcOza/06QbWdg4cqYy8eKCk3XQ4jAc\nbf8YJEuJ0qujp4BT48zUm2J7\n-----END PRIVATE KEY-----\n",
#   "client_email": "firebase-adminsdk-fbsvc@dsa-evaluation.iam.gserviceaccount.com",
#   "client_id": "117623841900845295435",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40dsa-evaluation.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }



