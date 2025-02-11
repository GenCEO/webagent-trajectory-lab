import json
from pathlib import Path

from webagent_trajectory_lab import compute_metrics
from webagent_trajectory_lab.report import write_report


def load_events(path: str) -> list[dict]:
    events = []
    for line in Path(path).read_text().splitlines():
        if line.strip():
            events.append(json.loads(line))
    return events


def main() -> None:
    events = load_events("data/demo_trajectory.jsonl")
    summary = compute_metrics(events)
    print(summary)
    write_report("outputs/demo_report.md", summary, title="Demo Trajectory")


if __name__ == "__main__":
    main()
