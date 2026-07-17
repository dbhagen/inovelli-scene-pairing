"""Inovelli Scene Pairing — pair Inovelli Blue switches into ZHA groups by gesture."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Event, HomeAssistant, callback

from .const import DEFAULT_OPTIONS, DOMAIN, ZHA_EVENT
from .engine import ScenePairingEngine

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the integration from a config entry."""
    options = {**DEFAULT_OPTIONS, **entry.options}
    engine = ScenePairingEngine(hass=hass, options=options)

    @callback
    def _on_zha_event(event: Event) -> None:
        data = event.data
        ieee = data.get("device_ieee")
        command = data.get("command")
        if not ieee or command not in engine.handled_commands:
            return
        hass.async_create_task(engine.handle_event(command, ieee))

    entry.async_on_unload(hass.bus.async_listen(ZHA_EVENT, _on_zha_event))
    entry.async_on_unload(engine.async_shutdown)
    entry.async_on_unload(entry.add_update_listener(_async_reload_entry))

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = engine
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry (bus unsub + timer cancel run via async_on_unload)."""
    hass.data.get(DOMAIN, {}).pop(entry.entry_id, None)
    return True


async def _async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload the entry when options change so the engine picks up new settings."""
    await hass.config_entries.async_reload(entry.entry_id)
