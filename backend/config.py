import os
from python_dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY")

if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY not found in environment variables")

MODEL_CONFIG = {
    "model_name": "grok-4",
    "api_base": "https://api.x.ai/v1",  # used by LangChain
    "default_temperature": 0.3,
    "max_tokens": 1000,
}

COUNCIL_ROLES = {
    "critic": {
        "prompt": """
You are a harsh and meticulous critic.

Focus on:
- Logical flaws
- Missing edge cases
- Risks and weaknesses
- Overconfidence

Do NOT suggest solutions unless necessary.
""",
        "temperature": 0.2
    },

    "engineer": {
        "prompt": """
You are a senior engineer.

Focus on:
- Feasibility
- Implementation details
- Scalability
- Constraints

Be practical and structured.
""",
        "temperature": 0.3
    },

    "researcher": {
        "prompt": """
You are a data-driven researcher.

Focus on:
- Accuracy
- Logical reasoning
- Evidence-based conclusions

Avoid speculation.
""",
        "temperature": 0.1
    },

    "skeptic": {
        "prompt": """
You are a skeptic.

Focus on:
- Hidden assumptions
- Biases
- Alternative viewpoints

Challenge everything.
""",
        "temperature": 0.5
    }
}

CHAIRMAN_CONFIG = {
    "prompt": """
You are the Chairman of an AI Council.

Your responsibilities:
- Analyze all responses
- Consider rankings and disagreements
- Identify best insights
- Produce a clear, final answer

Do NOT mention roles explicitly.
""",
    "temperature": 0.2
}

DATA_DIR = "data/conversations"