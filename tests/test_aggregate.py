from webagent_trajectory_lab.aggregate import aggregate_runs


def test_aggregate_runs() -> None:
    runs = [
        [{"type": "action", "name": "a"}, {"type": "stop", "success": True}],
        [{"type": "action", "name": "b"}, {"type": "stop", "success": False}],
    ]
    out = aggregate_runs(runs)
    assert out["runs"] == 2.0
    assert out["success_rate"] == 0.5
