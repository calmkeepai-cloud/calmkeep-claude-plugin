# Calmkeep Continuity Layer

This skill allows Claude Code to use the Calmkeep continuity layer during long multi-step development or reasoning workflows.

Use this skill when tasks involve:

- building APIs across many prompts
- evolving complex software architectures
- maintaining consistent system definitions
- long-form legal or analytical reasoning
- iterative refactoring of large codebases

The Calmkeep client preserves structural continuity across multiple turns.
Environment variable required:

CALMKEEP_API_KEY

Users obtain a Calmkeep API key from: Calmkeep.ai

https://calmkeep.ai

Example usage:

```python
from calmkeep import CalmkeepClient
import os

client = CalmkeepClient(
    calmkeep_key=os.getenv("CALMKEEP_API_KEY"),
    claude_key=os.getenv("ANTHROPIC_API_KEY")
)

response = client.complete(
    prompt="Continue evolving the multi-tenant API while preserving earlier architectural decisions."
)

print(response)
