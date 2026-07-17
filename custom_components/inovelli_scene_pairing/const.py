"""Constants for the Inovelli Scene Pairing integration."""

from __future__ import annotations

DOMAIN = "inovelli_scene_pairing"

# Home Assistant event fired by ZHA for device scene/button actions.
ZHA_EVENT = "zha_event"

# --- Actions and the (configurable) gesture -> action map -----------------------
# On Inovelli Blue over ZHA: button_3 = config button, button_1/button_2 = down/up
# paddle. Each action can be bound to one or more zha_event commands (comma-separated
# in options), so e.g. double-tap can replace hold for arming.
ACTION_ARM = "arm"  # arm pairing / add a switch to the group
ACTION_COLOR = "color"  # cycle the group LED color (while anchor)
ACTION_REMOVE = "remove"  # remove a switch from its group
ACTION_EXIT = "exit"  # exit pairing early (while anchor)

CONF_CMD_ARM = "cmd_arm"
CONF_CMD_COLOR = "cmd_color"
CONF_CMD_REMOVE = "cmd_remove"
CONF_CMD_EXIT = "cmd_exit"

DEFAULT_CMD_ARM = "button_3_hold"
DEFAULT_CMD_COLOR = "button_3_press"
DEFAULT_CMD_REMOVE = "button_3_double"
DEFAULT_CMD_EXIT = "button_1_press, button_2_press"

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
    CONF_CMD_ARM: DEFAULT_CMD_ARM,
    CONF_CMD_COLOR: DEFAULT_CMD_COLOR,
    CONF_CMD_REMOVE: DEFAULT_CMD_REMOVE,
    CONF_CMD_EXIT: DEFAULT_CMD_EXIT,
}
