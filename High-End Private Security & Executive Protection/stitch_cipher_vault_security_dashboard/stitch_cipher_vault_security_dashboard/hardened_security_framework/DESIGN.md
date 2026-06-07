---
name: Hardened Security Framework
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1c1b1d'
  surface-container: '#201f21'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e1e3'
  on-surface-variant: '#c7c5cd'
  inverse-surface: '#e5e1e3'
  inverse-on-surface: '#313032'
  outline: '#919097'
  outline-variant: '#46464d'
  surface-tint: '#c2c5e0'
  primary: '#c2c5e0'
  on-primary: '#2b2f44'
  primary-container: '#1a1e32'
  on-primary-container: '#82859e'
  inverse-primary: '#595d74'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#c9c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#1f1f1f'
  on-tertiary-container: '#888686'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dee1fc'
  primary-fixed-dim: '#c2c5e0'
  on-primary-fixed: '#161a2e'
  on-primary-fixed-variant: '#42465c'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131315'
  on-background: '#e5e1e3'
  surface-variant: '#353436'
typography:
  display-lg:
    fontFamily: IBM Plex Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: IBM Plex Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  title-sm:
    fontFamily: IBM Plex Serif
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.5'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  border-thick: 3px
  border-standard: 2px
---

## Brand & Style

The design system is engineered to evoke a sense of absolute permanence and impenetrable security. Drawing inspiration from high-security architecture and physical vault engineering, the brand personality is defensive, elite, and unwavering. It prioritizes the feeling of "hardened" software—digital interfaces that feel as solid as the reinforced steel they control.

The aesthetic follows a **Structural Brutalist** approach mixed with **Tactile Industrialism**. It avoids superficial decorations in favor of thick structural lines, visible mechanical logic, and high-contrast states. The experience is designed for high-net-worth individuals who demand discretion and reliability; every interaction must feel deliberate, heavy, and secure.

## Colors

This design system utilizes a high-contrast, low-chroma palette to reinforce a sense of technical sophistication and "black-site" privacy.

- **Deep Indigo (#1A1E32):** Used as the primary foundation for structural elements and deep-space backgrounds, providing a more sophisticated depth than pure black.
- **Platinum Silver (#E5E4E2):** The secondary color, used for high-visibility text, iconography, and "metallic" surfaces. It represents the physical hardware of the vault.
- **Matte Black (#0A0A0A):** The terminal background color, used to create "void" spaces where data is obscured or hidden.
- **Functional Accents:** A secure green is used sparingly for "Armed/Safe" states, while a deep oxidized red is reserved for "Breach/Warning" alerts.

## Typography

Typography in this design system is split between structural authority and technical precision.

- **Headlines:** Set in **IBM Plex Serif** to provide a sturdy, established, and architectural feel. These should feel "stamped" into the interface.
- **Body Text:** **Inter** provides maximum legibility for privacy policies and technical specifications.
- **Technical UI & Data:** **JetBrains Mono** is used for all readouts, timestamps, sensor data, and masked states. This reinforces the "hardened" technical nature of the system. All labels should be uppercase with slightly increased tracking to mimic industrial labeling.

## Layout & Spacing

The layout philosophy is based on a **Rigid Grid** system, emphasizing verticality and containment. On mobile, a single-column stack is used with heavy margins (24px) to ensure no accidental edge-touches.

Spacing follows an 8px rhythmic scale. However, unlike traditional fluid systems, this system uses "contained blocks." Elements do not float; they are housed within visible, heavy-bordered containers. Padding within containers should be generous (24px+) to prevent the technical data from feeling cluttered, maintaining a premium, "calm" security posture.

## Elevation & Depth

This design system rejects ambient soft shadows in favor of **Mechanical Depth**. 

1.  **Inset Shadows:** Surfaces should use inner shadows (1-4px offset, 0 blur) to appear recessed into the frame, like panels in a control room.
2.  **Raised States:** Active elements (like primary buttons) use a "Plinth" effect—no blur, 3px solid offsets in Matte Black to appear physically raised.
3.  **Industrial Textures:** Backgrounds should utilize a subtle grain or "brushed metal" CSS noise filter (3-5% opacity) to eliminate the flat digital feel.
4.  **Tonal Stacking:** Surfaces deeper in the hierarchy become darker (Matte Black), while interactive top-level panels use Deep Indigo.

## Shapes

The shape language is strictly **Sharp (0px)**. To convey defensive strength, the system avoids rounded corners entirely. Every container, button, and input field is a perfect rectangle. This geometric rigidity mimics the literal corners of a vault and the precision of industrial engineering. 

Small chamfered corners (45-degree cuts) may be used on primary action buttons to give them a "machined" appearance, but standard radius curves are prohibited.

## Components

- **Buttons:** Large, full-width blocks with a 3px solid border. The "Default" state is an inset shadow; the "Active" state reverses the shadow to an offset plinth.
- **Masked Data:** Sensitive information (codes, vault status) should be displayed using "Masked Blocks"—solid rectangles of Platinum Silver that only reveal the JetBrains Mono data upon a "Hold to Reveal" tactile interaction.
- **Input Fields:** Thick 2px Matte Black borders with a Platinum Silver background. On focus, the border color shifts to Deep Indigo with a subtle interior glow.
- **Cards:** Referred to as "Modules," these have 3px borders and a mandatory "header bar" in a contrasting color (e.g., Platinum Silver header on a Deep Indigo body).
- **Status Indicators:** Use square "LED" pips rather than circular ones. A pulse animation is only permitted for critical alarms; all other states must remain static and solid.
- **Tactile Sliders:** For high-security confirmations (like "Seal Vault"), use a heavy-duty track slider that requires a continuous swipe-and-hold, mimicking the physical turning of a bolt.