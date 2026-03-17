import os
from calmkeep import CalmkeepClient


def main():

    calmkeep_key = os.getenv("CALMKEEP_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    if not calmkeep_key:
        raise RuntimeError("CALMKEEP_API_KEY environment variable not set")

    if not anthropic_key:
        raise RuntimeError("ANTHROPIC_API_KEY environment variable not set")

    client = CalmkeepClient(
        calmkeep_key=calmkeep_key,
        anthropic_key=anthropic_key
    )

    response = client.complete(
        prompt=(
            "Continue evolving a multi-tenant SaaS API architecture. "
            "Preserve earlier constraints including RBAC separation, "
            "tenant isolation, and consistent validation patterns."
        )
    )

    print(response)


if __name__ == "__main__":
    main()
