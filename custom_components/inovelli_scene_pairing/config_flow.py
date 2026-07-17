"""Config and options flow for Inovelli Scene Pairing."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
)
from homeassistant.core import callback
import voluptuous as vol

from .const import (
    CONF_CMD_ARM,
    CONF_CMD_COLOR,
    CONF_CMD_EXIT,
    CONF_CMD_REMOVE,
    CONF_PAIR_PREFIX,
    CONF_PALETTE,
    CONF_WINDOW_SECONDS,
    DEFAULT_CMD_ARM,
    DEFAULT_CMD_COLOR,
    DEFAULT_CMD_EXIT,
    DEFAULT_CMD_REMOVE,
    DEFAULT_OPTIONS,
    DOMAIN,
    GROUP_NAME_PREFIX_DEFAULT,
    PALETTE_DEFAULT,
    WINDOW_SECONDS_DEFAULT,
)


def _palette_to_str(palette: list[int]) -> str:
    return ", ".join(str(x) for x in palette)


def _palette_from_str(value: str) -> list[int]:
    parts = [p.strip() for p in str(value).replace(";", ",").split(",")]
    return [int(p) for p in parts if p != ""]


class InovelliScenePairingConfigFlow(ConfigFlow, domain=DOMAIN):
    """Single-instance UI setup."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()
        if user_input is not None:
            return self.async_create_entry(title="Inovelli Scene Pairing", data={})
        return self.async_show_form(step_id="user")

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow:
        return InovelliScenePairingOptionsFlow()


class InovelliScenePairingOptionsFlow(OptionsFlow):
    """Tune window seconds, LED palette, and group-name prefix."""

    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        if user_input is not None:
            return self.async_create_entry(
                title="",
                data={
                    CONF_WINDOW_SECONDS: user_input[CONF_WINDOW_SECONDS],
                    CONF_PALETTE: _palette_from_str(user_input[CONF_PALETTE]),
                    CONF_PAIR_PREFIX: user_input[CONF_PAIR_PREFIX],
                    CONF_CMD_ARM: user_input[CONF_CMD_ARM],
                    CONF_CMD_COLOR: user_input[CONF_CMD_COLOR],
                    CONF_CMD_REMOVE: user_input[CONF_CMD_REMOVE],
                    CONF_CMD_EXIT: user_input[CONF_CMD_EXIT],
                },
            )

        current = {**DEFAULT_OPTIONS, **self.config_entry.options}
        schema = vol.Schema(
            {
                vol.Required(
                    CONF_WINDOW_SECONDS,
                    default=current.get(CONF_WINDOW_SECONDS, WINDOW_SECONDS_DEFAULT),
                ): vol.All(vol.Coerce(int), vol.Range(min=3, max=120)),
                vol.Required(
                    CONF_PALETTE,
                    default=_palette_to_str(current.get(CONF_PALETTE, PALETTE_DEFAULT)),
                ): str,
                vol.Required(
                    CONF_PAIR_PREFIX,
                    default=current.get(CONF_PAIR_PREFIX, GROUP_NAME_PREFIX_DEFAULT),
                ): str,
                vol.Required(CONF_CMD_ARM, default=current.get(CONF_CMD_ARM, DEFAULT_CMD_ARM)): str,
                vol.Required(
                    CONF_CMD_COLOR, default=current.get(CONF_CMD_COLOR, DEFAULT_CMD_COLOR)
                ): str,
                vol.Required(
                    CONF_CMD_REMOVE, default=current.get(CONF_CMD_REMOVE, DEFAULT_CMD_REMOVE)
                ): str,
                vol.Required(
                    CONF_CMD_EXIT, default=current.get(CONF_CMD_EXIT, DEFAULT_CMD_EXIT)
                ): str,
            }
        )
        return self.async_show_form(step_id="init", data_schema=schema)
