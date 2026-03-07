import os
import requests

CALMKEEP_ENDPOINT = "https://diargallop--calmkeep-service-calmkeep-service.modal.run/runtime"

def run(prompt):

    calmkeep_key = os.environ.get("CALMKEEP_API_KEY")
    anthropic_key = os.environ.get("CLAUDE_API_KEY")

    response = requests.post(
        CALMKEEP_ENDPOINT,
        headers={
            "calmkeep-key": calmkeep_key,
            "anthropic-api-key": anthropic_key
        },
        json={
            "prompt": prompt,
            "params": {}
        }
    )

    data = response.json()

    return data
