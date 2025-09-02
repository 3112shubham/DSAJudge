# import os
# import json
# import firebase_admin
# from firebase_admin import credentials, firestore, auth

# # Get the path from environment variable
# firebase_key_path = os.environ.get("FIREBASE_KEY_JSON")
# if not firebase_key_path:
#     raise ValueError("FIREBASE_KEY_JSON environment variable not set")

# # Read JSON file from path
# with open(firebase_key_path, "r") as f:
#     cred_dict = json.load(f)

# # Initialize Firebase
# cred = credentials.Certificate(cred_dict)
# firebase_admin.initialize_app(cred)

# db = firestore.client()

import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Get the JSON string from environment variable
firebase_key_json = os.environ.get("FIREBASE_KEY_JSON")
if not firebase_key_json:
    raise ValueError("FIREBASE_KEY_JSON environment variable not set")

# Convert string to dict
cred_dict = json.loads(firebase_key_json)

# Initialize Firebase
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)

db = firestore.client()