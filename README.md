Calmkeep Claude Plugin

Calmkeep is a continuity layer for Claude that preserves architectural and reasoning stability across long multi-turn workflows.

This plugin enables Claude Code to route development tasks through the Calmkeep runtime, allowing complex systems to evolve across extended sessions without losing structural consistency.

Calmkeep maintains framework stability across long builds, preventing subtle regressions such as reintroducing earlier design patterns, conflicting libraries, or weakened validation logic.

What This Plugin Does

The Calmkeep Claude plugin routes Claude Code prompts through the Calmkeep runtime before they reach the Claude API.

This allows Calmkeep to maintain architectural continuity across long development workflows.

Typical use cases include:

• backend system design
• large refactor projects
• multi-tenant architecture
• RBAC-heavy systems
• long-form analytical reasoning
• multi-document legal analysis

Installation

Add the Calmkeep plugin marketplace:

/plugin marketplace add calmkeepai-cloud/calmkeep-claude-plugin

Install the Calmkeep continuity plugin:

/plugin install calmkeep-continuity
API Key Configuration

After installing the plugin, configure your API keys.

Set your Calmkeep subscription key:

export CALMKEEP_API_KEY=YOUR_CALMKEEP_SUBSCRIPTION_KEY

Set your Claude API key:

export CLAUDE_API_KEY=YOUR_CLAUDE_API_KEY

Your Claude usage is billed directly through Anthropic.

Calmkeep does not proxy or resell Claude tokens.

How It Works

When the plugin is active, Claude Code routes prompts through the Calmkeep runtime:

Claude Code
    ↓
Calmkeep Runtime
    ↓
Claude API
    ↓
Structured Response

Calmkeep enforces structural continuity across long sessions by stabilizing frameworks, preserving earlier constraints, and reducing architectural drift.

The runtime operates as an external orchestration layer and does not modify model weights or training data.

Obtaining a Calmkeep API Key

You can create a Calmkeep subscription and obtain an API key at:

https://calmkeep.ai

New accounts include a 14-day free trial.

Additional Resources

Calmkeep Documentation
https://calmkeep.ai/documentation

Calmkeep Runtime Test Reports
https://calmkeep.ai/codetestreport

License

MIT License

Maintained By

Calmkeep Systems
External Continuity Layer for Structured AI Workflows
