"""Shared entity helpers for TTLock Local."""

from __future__ import annotations

from typing import Any

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import TTLockLocalCoordinator
from .const import DOMAIN


class TTLockLocalCoordinatorEntity(CoordinatorEntity[TTLockLocalCoordinator]):
    """Base class for coordinator-backed TTLock Local entities."""

    def _managed_locks(self) -> list[dict[str, Any]]:
        if not self.coordinator.data:
            return []

        data = self.coordinator.data
        merged: dict[str, dict[str, Any]] = {}

        for item in data.get("managed_locks", []):
            address = str(item.get("address", "")).upper()
            if not address:
                continue
            merged[address] = dict(item)

        target_mac = str(data.get("target_mac", "")).upper()
        if target_mac:
            target_state = {
                "address": target_mac,
                "name": data.get("status") or f"TTLock {target_mac}",
                "active": True,
                "connected": data.get("connected"),
                "is_locked": data.get("is_locked"),
                "battery": data.get("battery"),
                "rssi": data.get("rssi"),
                "last_action": data.get("last_action"),
                "updated_at": data.get("updated_at"),
            }
            current = merged.get(target_mac, {})
            merged[target_mac] = {
                **current,
                **{key: value for key, value in target_state.items() if value is not None},
                "address": target_mac,
                "name": current.get("name") or target_state["name"],
                "active": True,
                "last_action": data.get("last_action") or current.get("last_action"),
                "updated_at": data.get("updated_at") or current.get("updated_at"),
            }

        return list(merged.values())

    def _lock_state(self, address: str) -> dict[str, Any] | None:
        normalized = address.upper()
        for item in self._managed_locks():
            if str(item.get("address", "")).upper() == normalized:
                return item
        return None

    @staticmethod
    def lock_display_name(lock_state: dict[str, Any]) -> str:
        return str(lock_state.get("name") or lock_state.get("address") or "TTLock")

    def build_device_info(self, address: str, name: str) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, address.upper())},
            manufacturer="TTLock",
            model="Local BLE Lock",
            name=name,
        )
