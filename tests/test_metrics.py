from webagent_trajectory_lab import compute_metrics


def test_metrics() -> None:
    events = [
        {"type": "action", "name": "click"},
        {"type": "action", "name": "click"},
        {"type": "stop", "success": True},
    ]
    out = compute_metrics(events)
    assert out["steps"] == 2.0
    assert out["success"] == 1.0
    assert out["repeat_ratio"] == 0.5
