from pathlib import Path


def token() -> str:
    return (Path(__file__).parent / ".token").read_text().strip()


def icons() -> Path:
    return Path(__file__).parent / ".overrides" / ".icons" / "fontawesome"


def kit(mode: str) -> str:
    return f"https://kit.fontawesome.com/{(token())}.{mode}"
