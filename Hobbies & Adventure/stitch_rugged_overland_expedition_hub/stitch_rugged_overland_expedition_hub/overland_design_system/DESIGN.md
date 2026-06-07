---
name: Overland Design System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cdc6b7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#969083'
  outline-variant: '#4b463b'
  surface-tint: '#d6c692'
  primary: '#decd99'
  on-primary: '#3a3009'
  primary-container: '#c2b280'
  on-primary-container: '#4f441c'
  inverse-primary: '#6a5e33'
  secondary: '#c8c6c5'
  on-secondary: '#303030'
  secondary-container: '#474746'
  on-secondary-container: '#b6b5b4'
  tertiary: '#ffc0ab'
  on-tertiary: '#5c1a00'
  tertiary-container: '#ff9873'
  on-tertiary-container: '#7f2700'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f3e2ac'
  primary-fixed-dim: '#d6c692'
  on-primary-fixed: '#231b00'
  on-primary-fixed-variant: '#51461e'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#ffdbcf'
  tertiary-fixed-dim: '#ffb59c'
  on-tertiary-fixed: '#380c00'
  on-tertiary-fixed-variant: '#822800'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0.05em
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1280px
---

## Brand & Style
This design system is engineered for resilience, mirroring the heavy-duty hardware used in off-road exploration. The brand personality is rugged, utilitarian, and uncompromisingly functional. It targets overlanding enthusiasts who value durability over aesthetics, evoking the feeling of a field-tested piece of equipment rather than a digital interface.

The design style is a fusion of **Industrial Brutalism** and **Tactile Skeuomorphism**. It utilizes heavy structural lines, raw material textures, and physical metaphors—such as toggle switches and machined plates—to create a "dashboard" experience. Every element is designed to feel like it was bolted onto the frame, prioritizing clarity and immediate feedback under harsh conditions.

## Colors
The palette is derived from the environments where overlanding thrives: desert sands, volcanic rock, and oxidized metal.

- **Khaki (#C2B280):** Used for primary navigation and high-level structural framing.
- **Charcoal (#2B2B2B) & Neutral (#1A1A1A):** The foundation of the UI, providing a low-glare, dark-mode-first environment suitable for night-time navigation.
- **Rusty Orange (#B7410E):** Reserved for critical actions, warnings, and active states. It mimics the look of industrial primers and weathered steel.
- **Tactical Green (#4B5320):** Used for secondary status indicators, success states, and subtle environmental accents.

Textures of brushed steel should be applied to headers, while a faint, weathered topographic map pattern should be used as a low-opacity overlay (approx. 5%) on large background surfaces to add depth without sacrificing readability.

## Typography
The typography strategy separates "Information" from "Instruction."

**Space Grotesk** is used for all headlines and labels. Its technical, geometric construction echoes the precision of GPS readouts and industrial stamping. For headlines, a high-contrast weight is required, often paired with an all-caps treatment to simulate etched serial numbers or stencil markings.

**Public Sans** serves as the workhorse for body text. Its neutral, institutional clarity ensures that gear lists and route descriptions are legible in low-light or vibrating environments. It provides a formal, "manual-style" aesthetic that reinforces the system's focus on utility.

## Layout & Spacing
The layout follows a **Rigid Fixed Grid** model. Elements are locked into a 12-column system that feels structured and mechanical. 

- **Gutter & Margins:** Wide gutters (24px) prevent the UI from feeling cramped, ensuring that "tactile" elements have enough clearance for touch interaction.
- **Rhythm:** A 4px baseline grid governs all vertical spacing.
- **Visual Structure:** Containers should be separated by heavy, 2px borders rather than whitespace alone. This design system treats screen real estate like a tool chest—every item has a dedicated, reinforced compartment.

## Elevation & Depth
In this design system, depth is communicated through **Bold Borders and Hard Offsets** rather than soft ambient shadows. 

- **Hard Shadows:** Use 100% opacity shadows with 0 blur, offset by 3px or 4px to the bottom right, using the Charcoal color. This creates a "stamped" or "raised plate" effect.
- **Inset Depth:** For input fields and inactive states, use an inner shadow (inset) to simulate a recessed physical housing.
- **Tonal Layering:** Different tiers of Charcoal and Khaki are used to stack elements. Higher-priority "modules" use a lighter charcoal or a brushed-steel texture background to appear closer to the user.

## Shapes
The shape language is strictly **Sharp (0)**. There are no rounded corners in the design system, reflecting the machined edges of overlanding gear, roof racks, and recovery tools. 

- **Corners:** All containers, buttons, and inputs must have 90-degree angles.
- **Angled Accents:** For a more technical feel, occasional 45-degree "dog-ear" or chamfered cuts can be applied to the top-right corner of cards or buttons to mimic military-spec identification plates.

## Components
Components are designed to be "field-ready," emphasizing high click-confidence and physical presence.

- **Buttons:** Styled as heavy-duty physical switches. They feature a 2px solid border, a "hard" offset shadow, and use all-caps labels. The `active` state should remove the shadow and shift the element 2px down/right to simulate a physical press.
- **Inputs:** Recessed boxes with a 2px Charcoal border. Include a "Label Plate" in the top-left using the `label-caps` typography style on a Khaki background.
- **Chips/Badges:** Designed to look like small metal tags or dymo-tape labels. Use the Tactical Green or Rusty Orange for status, with high-contrast text.
- **Cards:** Heavy containers with a 2px border and a subtle topographic map overlay. Cards can include "bolt" icons in the four corners to reinforce the industrial aesthetic.
- **Toggle Switches:** Modeled after cockpit flip-switches. Avoid standard iOS-style sliders; use two-state toggle buttons with a visible "mechanical" arm or indicator.
- **Progress Bars:** Segmented bars that look like battery indicators or mechanical gauges rather than smooth continuous lines.