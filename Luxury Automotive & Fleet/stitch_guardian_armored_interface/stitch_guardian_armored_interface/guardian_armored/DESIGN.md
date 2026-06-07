---
name: Guardian-Armored
colors:
  surface: '#121315'
  surface-dim: '#121315'
  surface-bright: '#38393b'
  surface-container-lowest: '#0d0e10'
  surface-container-low: '#1a1c1d'
  surface-container: '#1e2022'
  surface-container-high: '#292a2c'
  surface-container-highest: '#343537'
  on-surface: '#e3e2e4'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e3e2e4'
  inverse-on-surface: '#2f3032'
  outline: '#8e9099'
  outline-variant: '#44474e'
  surface-tint: '#aec7f7'
  primary: '#aec7f7'
  on-primary: '#143057'
  primary-container: '#1b365d'
  on-primary-container: '#87a0cd'
  inverse-primary: '#465f88'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#c6c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#363636'
  on-tertiary-container: '#9f9f9f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f7'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2e476f'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#121315'
  on-background: '#e3e2e4'
  surface-variant: '#343537'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '900'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 600px
  armor-padding: 32px
---

## Brand & Style

The design system is engineered to evoke a sense of absolute invulnerability, catering to high-net-worth individuals and security-conscious clientele. The aesthetic is "Hardened Industrial"—a fusion of luxury craftsmanship and defensive architecture. It draws heavily from **Brutalism** for its uncompromising structure and **Tactile/Skeuomorphism** for its physical, vault-like presence.

The UI does not just sit on a screen; it feels bolted onto the hardware. Users should feel as though they are interacting with a high-security terminal inside an armored vehicle. Every interaction must feel deliberate, heavy, and authenticated. The visual narrative prioritizes privacy through intentional friction, ensuring that sensitive information is only revealed through active, secure gestures.

## Colors

The palette is anchored in a high-contrast, dark-mode environment to emphasize the "armored" feel. **Deep Black** serves as the foundation, representing the impenetrable void of a vault. **Platinum Silver** is used for structural elements, borders, and high-level accents, mimicking the sheen of reinforced steel.

**Deep Blue** acts as the primary signal color, representing authority, trust, and the "secured" state of the application. Metallic gradients are applied to the silver elements, moving from #E5E4E2 to #A9A9A9 to create a brushed-metal texture. Error states should utilize a desaturated oxide red, while success states use a high-visibility tactical green, though these are secondary to the primary authoritative blue.

## Typography

This design system utilizes **Inter** exclusively to maintain a utilitarian, high-precision industrial feel. The typographic hierarchy relies on extreme weight contrast. Headlines are set in "Black" or "Extra Bold" weights with tight tracking to mimic stamped metal or engraved serial numbers.

Body text maintains high readability with "Medium" weights to ensure clarity against dark, textured backgrounds. Labels and secure data points are rendered in all-caps with increased letter spacing, resembling tactical readouts or technical specifications.

## Layout & Spacing

The layout philosophy follows a **Rigid Fixed Grid**. On mobile, the interface is encased in "Armor Padding"—a thick outer margin that frames the content like a bulkhead. Content is organized into modular blocks that span the full width of the safe area, emphasizing a stacked, vertical fortress.

Spacing units are strictly derived from a 4px baseline. Gutters between elements are kept tight (16px) to maintain a sense of density and strength. Large vertical gaps are avoided to prevent the UI from feeling "airy" or "fragile."

## Elevation & Depth

Hierarchy is established through **Bold Borders** and **Heavy, Directional Shadows** rather than tonal elevation. Surfaces do not "float"; they are either recessed into the interface or extruded from it.

1.  **Recessed Layers:** Use inner shadows and a 2px Deep Black border to create "wells" for input fields and data displays.
2.  **Extruded Layers:** Primary cards and buttons use a 3px Platinum Silver border with a hard, 100% opacity shadow offset to the bottom-right (e.g., 6px 6px #000000) to create a physical, plate-like effect.
3.  **Security Overlays:** A fine 4px x 4px grid pattern is applied to secondary background layers, suggesting a screen-door effect or reinforced glass.

## Shapes

The design system strictly adheres to **Sharp Corners (0px)**. Any roundedness would compromise the "Hardened" aesthetic. Every button, card, input, and container must have 90-degree angles to reinforce the feeling of machined metal and architectural stability.

Where visual interest is needed, 45-degree "clipped" corners may be used for primary action buttons to mimic military-grade hardware tags, but these must be achieved through clip-paths rather than border-radius.

## Components

### Buttons
Buttons are heavy, rectangular slabs. The **Primary Action** button features a Deep Blue background, a 2px Platinum Silver top-left "highlight" border, and a 2px Deep Black bottom-right "shadow" border. The interaction state should involve a "press-in" effect where the shadow offset is reduced to zero.

### Data Masking & Inputs
To emphasize privacy, sensitive data (lat/long, payment info, passenger names) is masked by default with a "shattered glass" or "heavy block" pattern. A "Hold to Reveal" interaction cue is required, utilizing a progress bar that fills the button border as the user maintains contact.

### Cards & Containers
Cards are styled as "Armor Plates." They feature a subtle metallic linear gradient and a mandatory 1px grid overlay. Headers within cards are separated by a thick 3px horizontal divider.

### Security Patterns
Use tactical UI elements such as "Crosshair" corner markers on image containers and "Authenticating" pulse animations on all state transitions. All toggles and switches should resemble heavy-duty industrial rockers, using high-contrast "Active" (Deep Blue) and "Inactive" (Deep Black) states.

### Lists
List items are separated by heavy borders. Each item should feature a "Status Bolt"—a small square icon on the leading edge that changes color based on the security clearance or status of the item.