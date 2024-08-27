import json
from pathlib import Path

from webagent_trajectory_lab import compute_metrics


def load_events(path: str) -> list[dict]:
    events = []
    for line in Path(path).read_text().splitlines():
        if line.strip():
            events.append(json.loads(line))
    return events


def main() -> None:
    events = load_events("data/demo_trajectory.jsonl")
    print(compute_metrics(events))


if __name__ == "__main__":
    main()
