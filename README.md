# webagent-trajectory-lab

A focused toolkit to analyze trajectories from visual web agents.

## Why this exists
- Many multimodal agent benchmarks log rich trajectories but post-analysis is still ad hoc.
- This repo provides simple reusable metrics for step efficiency and action loops.

## Included metrics
- `steps`: number of action events
- `success`: terminal success flag
- `repeat_ratio`: repeated consecutive actions
- `efficiency`: successful trajectories rewarded for fewer steps

## Run
```bash
pip install -e .
python examples/analyze.py
```

## Batch mode
Use `python examples/batch_analyze.py` to summarize multiple runs.
