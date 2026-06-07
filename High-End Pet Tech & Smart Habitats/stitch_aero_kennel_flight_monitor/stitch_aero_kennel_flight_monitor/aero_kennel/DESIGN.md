---
name: Aero-Kennel
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#44464e'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#75777f'
  outline-variant: '#c5c6cf'
  surface-tint: '#4c5e86'
  primary: '#00081e'
  on-primary: '#ffffff'
  primary-container: '#0a1f44'
  on-primary-container: '#7687b2'
  inverse-primary: '#b4c6f4'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#050910'
  on-tertiary: '#ffffff'
  tertiary-container: '#1b2128'
  on-tertiary-container: '#838891'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9e2ff'
  primary-fixed-dim: '#b4c6f4'
  on-primary-fixed: '#041a3f'
  on-primary-fixed-variant: '#34466d'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#dee3ed'
  tertiary-fixed-dim: '#c1c7d0'
  on-tertiary-fixed: '#161c23'
  on-tertiary-fixed-variant: '#42474f'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-readout:
    fontFamily: Space Grotesk
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
  unit: 8px
  gutter: 24px
  margin: 48px
  container-max: 1280px
---

## Brand & Style

The brand personality is engineered, elite, and vigilant. This design system communicates the precision of aerospace engineering with the warmth of high-end hospitality. It targets affluent pet owners and professional logistics partners who demand uncompromising safety and real-time transparency.

The visual style is **Aerospace-Sleek**, a hybrid of **Glassmorphism** and **Corporate Modern**. It utilizes semi-transparent layers to suggest the depth of a cockpit interface, while maintaining the crystalline clarity of a sterile, high-tech environment. The emotional response should be one of absolute trust—evoking the feeling of a private jet cabin combined with a state-of-the-art medical monitoring suite.

## Colors

This design system utilizes a palette rooted in **Deep Navy Blue**, signifying stability, depth, and institutional trust. The background is a **Crisp White**, emphasizing cleanliness and the clinical precision required for live animal transport. 

**Metallic Gold** is reserved for premium touchpoints, high-level certifications, and subtle border accents to signify the "Gold Standard" of care. For technical monitoring, the system employs high-chroma status colors against the navy and white backgrounds to ensure that critical environmental data (temperature, oxygen, humidity) is instantly legible and actionable.

## Typography

The typographic hierarchy prioritizes rapid information processing. **Montserrat** is used for primary headings to provide a geometric, confident, and modern structural feel. **Inter** handles the bulk of the user interface and body text, chosen for its exceptional legibility at small scales and neutral, professional tone.

A third font, **Space Grotesk**, is introduced specifically for labels and data readouts. Its technical, slightly futuristic character reinforces the "aerospace" narrative and distinguishes live monitoring data (like temperature fluctuations) from standard UI text. Use All-Caps for labels to create a "dashboard" aesthetic.

## Layout & Spacing

This design system employs a **Fixed Grid** model to mirror the structured environment of aviation logistics. A 12-column grid is used for desktop layouts, ensuring that monitoring panels and telemetry data stay in consistent, predictable locations.

The spacing rhythm is based on an **8px linear scale**, promoting a sense of mathematical order. Large margins (48px+) are used to isolate critical data components, preventing visual clutter and ensuring that the user's focus remains on the pet's safety and environmental status.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** and layering rather than heavy shadows. 

1.  **Backdrop Blurs:** Use a 20px blur with a 60% white opacity for "Surface Layers" that sit above the navy primary background.
2.  **Inner Glows:** Apply a 1px soft white inner border to glass elements to simulate light hitting the edge of a cockpit display.
3.  **Subtle Gradients:** Use linear gradients (Top-Left to Bottom-Right) on primary buttons and headers, moving from the primary Deep Navy to a slightly lighter Navy (#162E5A) to suggest the curvature of aerospace hull materials.
4.  **Shadows:** When necessary, use extremely diffused, low-opacity navy-tinted shadows (e.g., `rgba(10, 31, 68, 0.08)`) to lift cards off the crisp white background.

## Shapes

The shape language reflects **Precision Engineering**. A "Soft" (0.25rem) base roundedness is used for most UI components (inputs, small buttons) to maintain a clean, technical edge. Larger containers, such as pet profile cards or monitoring modules, use a slightly larger radius (0.5rem) to provide a modern, approachable feel without becoming "playful." Pill-shaped elements are strictly reserved for status badges (e.g., "In-Flight," "Optimal") to make them stand out from the rectangular grid.

## Components

### Buttons & Controls
- **Primary Action:** Deep Navy background with a subtle gradient and Gold text or a 1px Gold border.
- **Secondary Action:** Transparent background with a 1px Navy border and Navy text.
- **Micro-interactions:** Buttons should have a slight "inner glow" on hover to simulate an illuminated physical switch.

### Monitoring Cards
- Use glassmorphic surfaces with a 1px Metallic Gold top-border to indicate "Premium Tier" transport.
- Data readouts within cards must use the `data-readout` typographic style for high-visibility monitoring.

### Alert Badges
- High-contrast, solid fill backgrounds (Red, Amber, Green).
- Use white text for critical/optimal and navy text for warning.
- Alerts should include a subtle "pulse" animation if the data point (e.g., Temperature) is outside of safe thresholds.

### Input Fields
- Crisp White background with a 1px light grey border (#E2E8F0).
- On focus, the border transitions to Deep Navy with a 2px outer glow in Metallic Gold.

### Additional Components
- **Telemetry Timeline:** A vertical or horizontal stepper showing the pet's journey, utilizing gold-topped pins for major milestones (Departure, Cruising, Arrival).
- **Environment Gauges:** Circular progress indicators for humidity and oxygen levels, using the system's status colors.