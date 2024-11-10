from pathlib import Path

QUERY_DIR = Path(__file__).parent / "queries" / "graphql"
QUERY_DIR.mkdir(parents=True, exist_ok=True)
