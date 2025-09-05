import json
from pathlib import Path

from webagent_trajectory_lab.aggregate import aggregate_runs


def load(path: str) -> list[dict]:
    return [json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]


def main() -> None:
    runs = [
        load("data/demo_trajectory.jsonl"),
        [
            {"type": "action", "name": "open_menu"},
            {"type": "action", "name": "click_help"},
            {"type": "stop", "success": False},
        ],
    ]
    print(aggregate_runs(runs))


if __name__ == "__main__":
    main()
