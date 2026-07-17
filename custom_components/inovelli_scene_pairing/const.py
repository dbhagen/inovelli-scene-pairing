"""Constants for the Inovelli Scene Pairing integration."""

from __future__ import annotations

DOMAIN = "inovelli_scene_pairing"

# Home Assistant event fired by ZHA for device scene/button actions.
ZHA_EVENT = "zha_event"

# --- Gestures (Inovelli Blue button map over ZHA) -------------------------------
# button_3 = config button, button_1 = down paddle, button_2 = up paddle.
CMD_HOLD = "button_3_hold"  # arm pairing / add a switch (add-only)
CMD_TAP = "button_3_press"  # while anchor: cycle the group LED color
CMD_LEAVE = "button_3_double"  # remove a switch from its group
CMD_EXIT_DOWN = "button_1_press"  # paddle down: exit pairing early
CMD_EXIT_UP = "button_2_press"  # paddle up: exit pairing early

HANDLED_COMMANDS = frozenset({CMD_HOLD, CMD_TAP, CMD_LEAVE, CMD_EXIT_DOWN, CMD_EXIT_UP})

# --- Zigbee cluster ids we bind for the bidirectional mirror --------------------
CLUSTER_ONOFF = 0x0006  # 6
CLUSTER_LEVEL = 0x0008  # 8
GROUP_MEMBER_ENDPOINT = 1  # the load endpoint (group membership / receiver side)
BINDING_ENDPOINT_FALLBACK = 2  # Inovelli Blue controller (client) endpoint

# --- Inovelli manufacturer cluster for LED bar effects --------------------------
INOVELLI_MFG_CLUSTER = 0xFC31  # 64561
INOVELLI_MFG_ID = 0x122F  # 4655
LED_EFFECT_CMD = 1  # led_effect command id
LED_FX_FAST_BLINK = 2  # fast-blink effect
LED_FX_CLEAR = 0  # clear/stop effect

# LED bar color hues (0-255). Orange is the idle "ungrouped" color and is
# deliberately excluded from the palette so grouped/ungrouped stay distinct.
LED_IDLE_HUE = 21  # orange
PALETTE_DEFAULT = [0, 42, 85, 127, 170, 212, 234]  # red,yellow,green,cyan,blue,purple,pink

# LED number-entity suffixes exposed by the ZHA Inovelli quirk.
LED_ON_COLOR_SUFFIX = "_default_all_led_on_color"
LED_OFF_COLOR_SUFFIX = "_default_all_led_off_color"

# --- Group naming ---------------------------------------------------------------
GROUP_NAME_PREFIX_DEFAULT = "Inovelli Link"

# --- Pairing window -------------------------------------------------------------
WINDOW_SECONDS_DEFAULT = 20

# --- Options keys ---------------------------------------------------------------
CONF_WINDOW_SECONDS = "window_seconds"
CONF_PALETTE = "palette"
CONF_PAIR_PREFIX = "pair_prefix"

DEFAULT_OPTIONS = {
    CONF_WINDOW_SECONDS: WINDOW_SECONDS_DEFAULT,
    CONF_PALETTE: PALETTE_DEFAULT,
    CONF_PAIR_PREFIX: GROUP_NAME_PREFIX_DEFAULT,
}
