from calmkeep import CalmkeepClient
import os

client = CalmkeepClient(
    calmkeep_key=os.getenv("CALMKEEP_API_KEY"),
    claude_key=os.getenv("ANTHROPIC_API_KEY")
)

response = client.complete(
    prompt="Build a multi-tenant SaaS API with consistent architecture."
)

print(response)
