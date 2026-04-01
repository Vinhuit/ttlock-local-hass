# TTLock Local Integration

Home Assistant custom integration for the local TTLock backend.

Backend and Web UI documentation live in:

- [`Vinhuit/ttlock-local-server`](https://github.com/Vinhuit/ttlock-local-server)

## Summary

This integration:

- talks to the backend over HTTP
- does not access BLE directly
- creates Home Assistant entities from the backend state

## Backend Required

You must run the backend from:

- [`ttlock-local-server`](https://github.com/Vinhuit/ttlock-local-server)

Make sure these work before adding the integration:

- `http://<backend-ip>:8990/api/healthz`
- `http://<backend-ip>:8990/api/status`

## Entities

Per lock:

- lock entity
- battery sensor
- RSSI sensor
- connected sensor
- last action sensor
- updated sensor

Global:

- refresh monitor button
- reconnect active lock button

## Install

### HACS

Install `TTLock Local` from HACS, then restart Home Assistant.

### Manual

Copy:

```text
custom_components/ttlock_local
```

into your Home Assistant config and restart.

## Configure

In Home Assistant:

1. `Settings -> Devices & Services`
2. `Add Integration`
3. search for `TTLock Local`
4. enter backend host, port, and poll interval

## Notes

- the backend is the source of truth for selected lock and BLE state
- the integration selects the target lock before sending `lock` or `unlock`
- lock control cards in Home Assistant usually show only the main lock action; extra details are exposed via sensors and attributes

## Related Files

- [manifest.json](./manifest.json)
- [api.py](./api.py)
- [coordinator.py](./coordinator.py)
- [lock.py](./lock.py)
- [sensor.py](./sensor.py)
