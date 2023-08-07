import os
from typing import Optional


def str_default(value: Optional[str], default: str) -> str:
    if not value:
        return default
    try:
        return str(value)
    except ValueError:
        return default


OPENAI_API_KEY = str_default(os.getenv("OPENAI_API_KEY"), "")

if OPENAI_API_KEY == "":
    # warn user that OPENAI_API_KEY is not set
    print("OPENAI_API_KEY is not set")

Q_SUMMARY = "Summarize the paper’s claimed primary contributions: In 10-15 \
        sentences, describe the key ideas, results, findings, and \
        significance as claimed by the paper’s authors"
