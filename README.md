# Repo Description
WIP to explore how to build an alerting pipeline for processing noise-sensor data.

```shell
python run_demo.py
```

### Dev. Notes
#### Core Flow
- Simulate timeseries stream
- Read stream
- Checks
  - Data length
  - missingness
  - anomaly?
  - read JSON stored decibel limit
- Assert-logic for dB breach (2min frequency?)
- Log breach
- Trigger event-related alert (monitor alert cooldown & decide channels)
