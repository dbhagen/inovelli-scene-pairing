# Inovelli Scene Pairing

[![License: MIT](https://img.shields.io/github/license/dbhagen/inovelli-scene-pairing?color=blue)](LICENSE)
[![Release](https://img.shields.io/github/v/release/dbhagen/inovelli-scene-pairing?display_name=tag&sort=semver)](https://github.com/dbhagen/inovelli-scene-pairing/releases)
[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![Validate](https://github.com/dbhagen/inovelli-scene-pairing/actions/workflows/validate.yml/badge.svg)](https://github.com/dbhagen/inovelli-scene-pairing/actions/workflows/validate.yml)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=dbhagen&repository=inovelli-scene-pairing&category=integration)

> Pair Inovelli Blue switches into **bidirectionally-mirrored Zigbee groups** and set
> **per-group LED bar colors** — entirely from the switch's scene button, over **ZHA**.
> No hand-written automations, no hub round-trip: grouped switches mirror each other at
> the Zigbee level.

## Why

Inovelli Blue switches expose rich multi-tap/hold scene events over Zigbee. This
integration turns those gestures into a live "grouping" workflow: hold a switch to open a
group, hold others to add them, single-tap to color the group, double-tap to remove one,
paddle-tap to finish. Under the hood it creates ZHA groups and binds each switch's control
clusters to the group, so **operating any switch drives all of them** — even if Home
Assistant is offline.

## Supported devices

- **Inovelli Blue 2-in-1 Dimmer — VZM31-SN**
- **Inovelli Blue Fan Switch — VZM35-SN**
- Requires the **ZHA** (Zigbee Home Automation) integration. **Zigbee2MQTT is not supported.**

## Gestures

Use the small **config button** below the paddle (unless noted):

| Gesture | Action |
| --- | --- |
| **Hold** (config button) | Arm pairing / add this switch to the open group (add-only — a hold never removes) |
| **Single-tap** (while pairing) | Cycle the group's LED bar color through the palette |
| **Double-tap** (config button) | Remove this switch from its group |
| **Paddle up or down** (while pairing) | Exit pairing mode immediately |

To pair: **hold** switch A (its bar flashes for the pairing window), then **hold** switch B
within the window — they're now grouped and mirror each other. Keep holding more switches to
add a 3rd/4th. **Single-tap** the switch you're holding to pick a color. **Double-tap** any
switch to drop it from its group. A grouped switch's bar shows the group color; ungrouped is
orange.

## Requirements

- Home Assistant **2024.8.0** or newer
- The **ZHA** integration with Inovelli Blue switches paired
- [HACS](https://hacs.xyz/)

## Installation

1. In HACS → three-dot menu → **Custom repositories**.
2. Add `https://github.com/dbhagen/inovelli-scene-pairing`, category **Integration**
   (or click the **My Home Assistant** badge above).
3. Install **Inovelli Scene Pairing**, then **restart Home Assistant**.
4. **Settings → Devices & Services → Add Integration →** search "Inovelli Scene Pairing".

## Options

**Settings → Devices & Services → Inovelli Scene Pairing → Configure:**

- **Pairing window (seconds)** — how long a switch stays in pairing mode after a hold (default 20).
- **LED color palette** — comma-separated hues (0–255) cycled by a single tap. Orange (21) is
  reserved for ungrouped switches and is not in the default palette.
- **Group name prefix** — Zigbee groups are named `"<prefix> N"` (default `Inovelli Link`).

## How it works

- Listens to `zha_event` button events; no automations to write.
- Group membership = each switch's **endpoint 1** joins the ZHA group (receiver side).
- Bidirectional mirror = each switch's **endpoint 2** OnOff + LevelControl client clusters
  are bound to the group (sender side), so any switch drives the whole group.
- LED colors use the switch's `default_all_led_*_color` numbers; flashes use the Inovelli
  manufacturer cluster.

## Troubleshooting

- **Nothing happens on a hold** — this reads events from **ZHA**. If your switches are on
  **Zigbee2MQTT**, they are not supported. Confirm the model is VZM31-SN / VZM35-SN.
- **Enable debug logging:**
  ```yaml
  logger:
    logs:
      custom_components.inovelli_scene_pairing: debug
  ```
- This integration relies on ZHA internal APIs. If a Home Assistant upgrade breaks it, please
  open an issue with your HA version and a debug log.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). This repo uses
[Conventional Commits](https://www.conventionalcommits.org/) and automated semver releases.

## License

MIT — see [LICENSE](LICENSE).
