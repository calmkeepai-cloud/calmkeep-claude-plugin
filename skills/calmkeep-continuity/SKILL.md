# Calmkeep Continuity Layer

This skill allows Claude Code to use the Calmkeep continuity layer during long multi-step development or reasoning workflows.

Calmkeep preserves structural and architectural continuity across long prompt chains.

Use this skill when tasks involve:

- building APIs across many prompts
- evolving complex software architectures
- maintaining consistent system definitions
- long-form legal or analytical reasoning
- iterative refactoring of large codebases

---

# Required Environment Variables

Users must configure the following environment variables:

CALMKEEP_API_KEY  
CLAUDE_API_KEY

A Calmkeep API key can be obtained from:

https://calmkeep.ai

Claude API keys are issued through Anthropic.

---

# Calmkeep Runtime Endpoint

Calmkeep is accessed through the hosted runtime endpoint:

POST https://diargallop--calmkeep-service-calmkeep-service.modal.run/runtime

Headers:

calmkeep-key: $CALMKEEP_API_KEY  
anthropic-api-key: $CLAUDE_API_KEY  
Content-Type: application/json

Body:

```json
{
  "prompt": "<user request>",
  "params": {}
}
```

The response returned from this endpoint contains the structured output produced through the Calmkeep orchestration layer.

---

# Python SDK Example

Developers can also access Calmkeep through the Python SDK.

```python
from calmkeep import CalmkeepClient
import os

client = CalmkeepClient(
    calmkeep_key=os.getenv("CALMKEEP_API_KEY"),
    claude_key=os.getenv("CLAUDE_API_KEY")
)

response = client.complete(
    prompt="Continue evolving the multi-tenant API while preserving earlier architectural decisions."
)

print(response)
```

---

# When to Use Calmkeep

Activate the Calmkeep continuity layer when:

- sessions extend beyond a few prompts
- architectural consistency must be preserved
- earlier design constraints must remain enforced
- reasoning must compound across multiple responses
- development workflows span many iterative prompts

Calmkeep helps prevent structural drift across extended development or analytical sessions.
