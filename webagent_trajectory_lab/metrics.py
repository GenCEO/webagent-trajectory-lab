def compute_metrics(events: list[dict]) -> dict[str, float]:
    steps = [e for e in events if e.get("type") == "action"]
    stop = next((e for e in reversed(events) if e.get("type") == "stop"), None)
    success = float(bool(stop and stop.get("success", False)))

    action_names = [e.get("name", "") for e in steps]
    repeats = 0
    for idx in range(1, len(action_names)):
        if action_names[idx] == action_names[idx - 1]:
            repeats += 1

    return {
        "steps": float(len(steps)),
        "success": success,
        "repeat_ratio": (repeats / len(steps)) if steps else 0.0,
        "efficiency": (1.0 / len(steps)) if success and steps else 0.0,
    }
