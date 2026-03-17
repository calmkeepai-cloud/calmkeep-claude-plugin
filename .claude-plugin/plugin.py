import os
import requests

CALMKEEP_ENDPOINT = "https://diargallop--calmkeep-service-calmkeep-service.modal.run/runtime"


def run(prompt: str):

    calmkeep_key = os.environ.get("CALMKEEP_API_KEY")

    anthropic_key = (
        os.environ.get("ANTHROPIC_API_KEY")
        or os.environ.get("CLAUDE_API_KEY")
    )

    if not calmkeep_key:
        raise RuntimeError(
            "CALMKEEP_API_KEY environment variable not set."
        )

    if not anthropic_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY (or CLAUDE_API_KEY) environment variable not set."
        )

    try:
        response = requests.post(
            CALMKEEP_ENDPOINT,
            headers={
                "calmkeep-key": calmkeep_key,
                "anthropic-api-key": anthropic_key,
                "Content-Type": "application/json",
            },
            json={
                "prompt": prompt,
                "params": {}
            },
            timeout=120
        )

    except requests.RequestException as e:
        raise RuntimeError(f"Failed to contact Calmkeep runtime: {e}")

    if response.status_code != 200:
        raise RuntimeError(
            f"Calmkeep runtime error {response.status_code}: {response.text}"
        )

    try:
        return response.json()
    except ValueError:
        raise RuntimeError("Invalid JSON response from Calmkeep runtime.")
