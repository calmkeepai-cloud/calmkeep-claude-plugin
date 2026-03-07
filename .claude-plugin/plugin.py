import os
import requests

CALMKEEP_ENDPOINT = "https://diargallop--calmkeep-service-calmkeep-service.modal.run/complete"

def run(prompt):

    api_key = os.environ.get("CALMKEEP_API_KEY")

    response = requests.post(
        CALMKEEP_ENDPOINT,
        json={
            "prompt": prompt,
            "calmkeep_key": api_key
        }
    )

    data = response.json()

    return data["response"]
