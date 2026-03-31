# TTLock Local

Home Assistant custom integration for the `ttlock-sdk-js` local Web UI API.

This repository contains:

- `custom_components/ttlock_local`

The integration talks to an existing local TTLock backend and creates Home Assistant entities for:

- locks
- battery sensors
- RSSI sensors
- monitor buttons

## Requirements

- A running `ttlock-sdk-js` Web UI / `server.js` backend reachable from Home Assistant
- The backend must expose the local API endpoints used by this integration

## Supported API calls

- `GET /api/status`
- `POST /api/select-lock`
- `POST /api/unlock`
- `POST /api/lock`
- `POST /api/refresh`
- `POST /api/reconnect`

## Install with HACS

1. Add this repository as a custom repository in HACS.
2. Type: `Integration`
3. Install `TTLock Local`
4. Restart Home Assistant.
5. Add the integration from the Home Assistant UI.

## Notes

- This integration does not embed the BLE stack in Python.
- BLE control stays in the existing `ttlock-sdk-js` backend.
- Home Assistant communicates with that backend over HTTP on your local network.
