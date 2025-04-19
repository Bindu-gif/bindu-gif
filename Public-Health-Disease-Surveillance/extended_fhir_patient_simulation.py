import requests
import json
import random
from datetime import datetime, timedelta

# Base URL of your FHIR server
FHIR_SERVER_URL = "http://localhost:8080/fhir/Patient"

# Function to generate random birthdates
def random_birthdate(start_year=1960, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Sample names for generating random patients
first_names = ["John", "Jane", "Alice", "Bob", "Mary", "Tom"]
last_names = ["Smith", "Doe", "Johnson", "Lee", "Brown", "Davis"]
genders = ["male", "female", "other", "unknown"]

# Generate and send 5 FHIR Patient resources
for i in range(1, 6):
    first = random.choice(first_names)
    last = random.choice(last_names)
    gender = random.choice(genders)
    birth_date = random_birthdate()

    # Create the FHIR-compliant patient resource
    patient = {
        "resourceType": "Patient",
        "id": f"example-{i:03}",
        "name": [
            {
                "use": "official",
                "family": last,
                "given": [first]
            }
        ],
        "gender": gender,
        "birthDate": birth_date,
        "address": [
            {
                "use": "home",
                "line": ["123 Main St"],
                "city": "Houghton",
                "state": "MI",
                "postalCode": "49931",
                "country": "USA"
            }
        ],
        "telecom": [
            {
                "system": "phone",
                "value": f"555-01{i:02}",
                "use": "mobile"
            }
        ]
    }

    # Convert data to JSON and post it to the FHIR server
    headers = {"Content-Type": "application/fhir+json"}
    response = requests.post(FHIR_SERVER_URL, headers=headers, data=json.dumps(patient))

    # Print response status
    print(f"Uploading Patient {patient['id']}...")
    if response.status_code == 201:
        print("✅ Upload successful.")
    else:
        print(f"❌ Failed to upload. Status Code: {response.status_code}")
        print("Response:", response.text)
