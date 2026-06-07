---
name: Marine-Industrial Interface
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1c'
  surface-container: '#1f1f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e3'
  on-surface-variant: '#bfc8c7'
  inverse-surface: '#e5e2e3'
  inverse-on-surface: '#303031'
  outline: '#899391'
  outline-variant: '#3f4948'
  surface-tint: '#95d1ce'
  primary: '#95d1ce'
  on-primary: '#003735'
  primary-container: '#004b49'
  on-primary-container: '#7ebab7'
  inverse-primary: '#2a6865'
  secondary: '#ffb693'
  on-secondary: '#561f00'
  secondary-container: '#fe6b00'
  on-secondary-container: '#572000'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#414343'
  on-tertiary-container: '#afafb0'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b1eeea'
  primary-fixed-dim: '#95d1ce'
  on-primary-fixed: '#00201f'
  on-primary-fixed-variant: '#084f4d'
  secondary-fixed: '#ffdbcc'
  secondary-fixed-dim: '#ffb693'
  on-secondary-fixed: '#351000'
  on-secondary-fixed-variant: '#7a3000'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131314'
  on-background: '#e5e2e3'
  surface-variant: '#353436'
typography:
  display-lg:
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
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-readout:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  container-max: 1440px
---

## Brand & Style

This design system is engineered for the high-stakes environment of marine hardware management. The aesthetic is **Nautical-Industrial**, merging the functional rigidity of maritime engineering with modern digital precision. It evokes a sense of "over-engineered" reliability, positioning the software as a piece of heavy-duty equipment rather than a mere application.

The visual style is **Tactile and Rugged**. It rejects the trend of ethereal, flat interfaces in favor of physical metaphors: milled metal, carbon fiber composites, and mechanical switches. The UI should feel substantial, as if every interaction requires intent and every readout is mission-critical. The target audience—mariners, engineers, and fleet managers—requires high legibility under harsh lighting and a layout that prioritizes functional hierarchy over decorative flair.

## Colors

The palette is anchored by the deep, atmospheric **Teal (#004B49)**, representing the marine environment and serving as the primary brand identifier. The foundation of the interface is **Carbon Fiber Grey/Black (#1A1A1B)**, utilized in dark mode to reduce eye strain during night-time navigation while providing a high-tech, industrial backdrop.

**Safety Orange (#FF6B00)** is reserved exclusively for high-priority alerts and emergency states. It must be used sparingly to maintain its psychological impact. **Crisp White (#FFFFFF)** provides high-contrast legibility for critical data readouts. Secondary accents use a vibrant "Liquid Aqua" for status indicators, mimicking the glow of marine instrumentation.

## Typography

The typographic system utilizes a trio of technical typefaces to delineate information types. **Space Grotesk** is used for headlines; its geometric, slightly "off-kilter" technicality matches the industrial aesthetic. **Inter** handles all body copy, ensuring maximum readability for complex documentation and logs.

For technical data, coordinates, and status labels, **JetBrains Mono** provides a monospaced structure that ensures numerical values align perfectly in tables and dashboards. All labels should be treated with uppercase styling and increased tracking to mimic stamped metal plates or engraved hardware tags.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy on desktop to ensure that critical controls remain in predictable locations—a necessity for hardware-adjacent software. A 12-column grid is used with generous 24px gutters to prevent visual clutter. 

On mobile and tablet, the layout shifts to a high-density fluid model, ensuring that large, tactile touch targets are prioritized for use in unstable environments (e.g., on a moving vessel). Spacing follows a strict 4px baseline rhythm, emphasizing a "tight" industrial fit. Elements should be grouped into logical "modules" that resemble physical rack-mounted equipment.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering** and physical texturing rather than soft, ambient shadows. 

1.  **Base Layer:** Solid Carbon Fiber Grey (#1A1A1B) with a subtle, diagonal 45-degree carbon weave pattern (low opacity).
2.  **Raised Surfaces:** Buttons and cards use a 1px "milled" inner highlight on the top edge and a 2px "machined" shadow on the bottom, creating a tactile, extruded effect.
3.  **Recessed Wells:** Input fields and data containers appear "etched" into the surface using inner shadows and darker backgrounds.
4.  **Liquid Indicators:** Status bars use a "glow-from-within" effect, mimicking backlit liquid crystal or fluid-filled gauges.

## Shapes

The shape language is **Soft (0.25rem)**, reflecting the chamfered edges of marine-grade metalwork. This slight rounding prevents the UI from feeling dangerously sharp while maintaining a professional, heavy-duty silhouette. Large components, such as primary action cards, may use a "notched corner" aesthetic to reinforce the industrial hardware metaphor. Icons should be stroke-based with consistent weights, avoiding thin lines that might disappear in high-glare environments.

## Components

### Buttons
Buttons are the primary tactile element. They feature a subtle gradient to suggest a convex surface. The "Emergency" button is Safety Orange with a striped "Caution" border. Active states should feel "pressed" via an inverted inner shadow.

### Status Indicators
Indicators should behave like "Liquid Gauges." Instead of flat bars, they use a subtle pulse and a slight blur to simulate glowing fluid or LEDs behind a glass panel.

### Input Fields
Fields are styled as "Recessed Ports." They use a darker shade of the neutral base and a high-contrast border when focused. Text entry uses the monospaced font for precision.

### Cards
Cards are modular "Chassis" units. They must have a defined header area, often separated by a thin horizontal line (1px) that looks like a seam between two metal plates.

### Toggle Switches
Toggles are styled as physical "Rockers." The "On" state uses the primary Deep Teal with a glowing indicator light, while the "Off" state remains a neutral, dark grey.

### Emergency Alerts
When an emergency state is triggered, the entire component or screen perimeter should utilize a high-contrast "Strobe" animation between Safety Orange and Black to ensure immediate user attention.