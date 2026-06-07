---
name: CyberExam Defensive-Tech
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e4e2e4'
  on-surface-variant: '#e9bcb9'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#b08784'
  outline-variant: '#5f3e3d'
  surface-tint: '#ffb3af'
  primary: '#ffb3af'
  on-primary: '#68000e'
  primary-container: '#ff5357'
  on-primary-container: '#5c000b'
  inverse-primary: '#bf0024'
  secondary: '#c6c6cb'
  on-secondary: '#2f3034'
  secondary-container: '#46464b'
  on-secondary-container: '#b5b4ba'
  tertiary: '#6ed4f1'
  on-tertiary: '#003641'
  tertiary-container: '#2b9db9'
  on-tertiary-container: '#002e39'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3af'
  on-primary-fixed: '#410006'
  on-primary-fixed-variant: '#930019'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#b1ecff'
  tertiary-fixed-dim: '#6ed4f1'
  on-tertiary-fixed: '#001f27'
  on-tertiary-fixed-variant: '#004e5e'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#353437'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
spacing:
  unit: 4px
  container-margin: 20px
  gutter: 12px
  section-gap: 32px
  element-gap: 16px
---

## Brand & Style

This design system is engineered for the high-stakes environment of cybersecurity certification. The brand personality is authoritative, vigilant, and high-performance, mirroring the intensity of a Security Operations Center (SOC). It targets professionals who value precision over decoration.

The visual style is a fusion of **Technical Minimalism** and **Industrial Brutalism**. It utilizes a "black-site" aesthetic—matte surfaces, raw technical textures like micro-grids and scanlines, and high-contrast signaling. The emotional response is one of focused urgency; the UI does not just host content, it monitors progress. Every element is designed to feel like a mission-critical instrument where "Laser Red" represents active threats, critical errors, or the pulse of a live exam environment.

## Colors

The palette is anchored in a deep **Matte Black** (#0A0A0A) to eliminate peripheral distraction and reduce eye strain during long study sessions. **Laser Red** (#FF0033) is the primary action color, used sparingly for critical data points, active states, and "hot" interactive zones. 

Secondary information is rendered in a spectrum of technical **Greys**. Use lower-opacity greys for structural elements like borders and grid lines to maintain a "ghosted" UI feel. Avoid any blues or soft tones; the interface must remain strictly monochromatic except for the surgical application of red.

## Typography

This design system utilizes **Space Grotesk** for headlines and labels to evoke a futuristic, technical atmosphere. Its geometric construction provides the "hard-edged" look required for the Defensive-Tech aesthetic. Headlines should be tightly tracked to appear more aggressive and structured.

**Inter** is the workhorse for all body copy and exam questions, selected for its clinical neutrality and exceptional readability at small sizes on mobile displays. For data readouts, progress percentages, and technical identifiers, use the **label-caps** style to create a distinct hierarchy between "reading" and "monitoring."

## Layout & Spacing

The layout follows a strict **Fluid Grid** model optimized for mobile-first interaction. Content is contained within 20px side margins, with a vertical rhythm based on a 4px baseline unit. 

The spacing philosophy is "High Density." Elements are packed to reflect a professional data-heavy terminal, but grouped logically with clear 32px gaps between different functional blocks. Use 12px gutters for internal card layouts. Technical textures (like a subtle 8px dot-grid background) should be used to visually anchor elements to the layout, reinforcing the "instrument" feel.

## Elevation & Depth

This design system avoids traditional soft shadows. Instead, it uses **Tonal Layers** and **Bold Borders** to define depth. 

1. **Base Layer:** The Matte Black background.
2. **Surface Layer:** Dark grey (#1A1A1A) containers with 1px solid borders (#2C2C2E).
3. **Active Layer:** Elements that are being interacted with should feature a "Laser Red" outer glow (0px 0px 8px) to simulate a light-emitting diode.
4. **Overlay:** Use 40% opacity black overlays for modals, maintaining the visibility of the "system" underneath to ensure the user never feels disconnected from the exam flow.

## Shapes

The shape language is **Sharp (0)**. To maintain a gritty, professional, and military-grade aesthetic, avoid rounded corners on buttons, cards, and input fields. Sharp 90-degree angles communicate rigor and precision. 

Occasional 45-degree "clipped" corners (chamfers) may be used on primary action buttons or decorative elements to further lean into the industrial/tech aesthetic. All progress bars and sliders must be rectangular blocks.

## Components

- **Buttons:** Primary buttons are solid Laser Red with black text (Space Grotesk, Uppercase). Secondary buttons use a 1px Grey outline with no fill.
- **Trend Lines:** Integrated into cards, these use thin (1.5px) Laser Red strokes with a subtle drop-shadow glow to indicate exam performance over time.
- **Cards:** Simple 1px bordered boxes. Use a background texture of faint horizontal scanlines (2% opacity) to distinguish cards from the base background.
- **Input Fields:** Bottom-border only, or 1px Grey stroke. Focus state switches the border to Laser Red and activates a subtle red "glitch" or glow effect.
- **Chips/Status:** Rectangular blocks. "Critical" statuses use a pulsing red dot icon. "Neutral" uses a static grey outline.
- **Additional Component - "The HUD":** A persistent top-bar on the mobile device displaying exam time remaining and "Threat Level" (current score), using the **mono-data** type style for a real-time monitoring feel.