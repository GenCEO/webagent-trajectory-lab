from .metrics import compute_metrics


def aggregate_runs(runs: list[list[dict]]) -> dict[str, float]:
    if not runs:
        return {"runs": 0.0, "success_rate": 0.0, "avg_steps": 0.0, "avg_repeat_ratio": 0.0}

    metrics = [compute_metrics(r) for r in runs]
    n = len(metrics)
    return {
        "runs": float(n),
        "success_rate": sum(m["success"] for m in metrics) / n,
        "avg_steps": sum(m["steps"] for m in metrics) / n,
        "avg_repeat_ratio": sum(m["repeat_ratio"] for m in metrics) / n,
    }
