from pathlib import Path


def to_markdown(summary: dict[str, float], title: str = "Trajectory Report") -> str:
    lines = [f"# {title}", "", "| Metric | Value |", "|---|---:|"]
    for k, v in summary.items():
        lines.append(f"| {k} | {v:.4f} |")
    return "\n".join(lines)


def write_report(path: str, summary: dict[str, float], title: str = "Trajectory Report") -> None:
    Path(path).write_text(to_markdown(summary, title=title))
