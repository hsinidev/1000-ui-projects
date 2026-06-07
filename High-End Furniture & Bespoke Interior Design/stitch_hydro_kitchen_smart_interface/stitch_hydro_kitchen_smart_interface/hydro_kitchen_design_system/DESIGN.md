---
name: Hydro-Kitchen Design System
colors:
  surface: '#f9f9f7'
  surface-dim: '#dadad8'
  surface-bright: '#f9f9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f2'
  surface-container: '#eeeeec'
  surface-container-high: '#e8e8e6'
  surface-container-highest: '#e2e3e1'
  on-surface: '#1a1c1b'
  on-surface-variant: '#444748'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f1ef'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#006875'
  on-secondary: '#ffffff'
  secondary-container: '#00e3fd'
  on-secondary-container: '#00616d'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#281900'
  on-tertiary-container: '#af7a00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#9cf0ff'
  secondary-fixed-dim: '#00daf3'
  on-secondary-fixed: '#001f24'
  on-secondary-fixed-variant: '#004f58'
  tertiary-fixed: '#ffdeac'
  tertiary-fixed-dim: '#ffba38'
  on-tertiary-fixed: '#281900'
  on-tertiary-fixed-variant: '#604100'
  background: '#f9f9f7'
  on-background: '#1a1c1b'
  surface-variant: '#e2e3e1'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  data-metric:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: -0.01em
spacing:
  unit: 8px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  max-width: 1440px
---

## Brand & Style

The brand personality is rooted in high-performance engineering, quiet luxury, and culinary precision. It targets affluent homeowners and professional chefs who demand professional-grade hardware integrated with seamless digital intelligence. 

The design style is a hybrid of **Minimalism** and **Tactile Modernism**. It avoids unnecessary ornamentation in favor of structural integrity and material honesty. The digital interface should feel like an extension of the physical hardware—cool to the touch, responsive, and indestructible. The emotional response is one of absolute control and calm, achieved through vast whitespace, strict alignment, and "active-state" glows that mimic physical heating elements or flowing water.

## Colors

The palette is anchored by the "Carrara" spectrum—ultra-clean whites and stone greys that provide a neutral canvas. "Brushed Steel" silvers function as structural dividers and secondary surfaces.

- **Primary (Charcoal Plate):** Used for typography and high-contrast structural elements.
- **Secondary (Electric Glow):** Reserved for liquid-based controls (induction cooling, water flow, sous-vide timers).
- **Tertiary (Thermal Amber):** Strictly for active heating zones, oven indicators, and safety warnings.
- **Surface Strategy:** Backgrounds utilize subtle gradients from Marble White to Carrara Grey to simulate light hitting a stone surface.

## Typography

Typography functions as a tool of precision. 
- **Hanken Grotesk** provides a sophisticated, modern architectural feel for headlines.
- **Inter** ensures maximum legibility for body text and instructions.
- **JetBrains Mono** is utilized for technical readouts, metrics, and labels to evoke the feeling of high-end kitchen hardware engraving and engineering documentation.

All labels should be uppercase with increased tracking to enhance the "luxury equipment" aesthetic.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy on desktop and a **Fluid Grid** on mobile. 

- **Desktop:** 12-column grid with a 1440px max-width. Spacing is generous to prevent the UI from feeling cluttered. Content modules are separated by significant "breathing room" (64px+).
- **Mobile:** 4-column fluid grid. Margins compress to 20px, but vertical rhythm remains strict to the 8px baseline.
- **Alignment:** Elements must align to the grid edges. Asymmetrical layouts are permitted for hero images of stone/metal, but functional UI controls must be strictly rectilinear.

## Elevation & Depth

This design system uses **Tonal Layers** and **Low-contrast Outlines** rather than traditional drop shadows.

- **Base Layer:** Carrara Marble texture or solid white.
- **Tier 1 (Surface):** Slightly recessed or elevated surfaces use 1px "Brushed Steel" borders with 5% opacity charcoal fills.
- **Interactive Depth:** When an element is active, it does not lift with a shadow; instead, it emits an inner glow (Electric Blue or Thermal Amber) that appears to illuminate the surrounding "stone" surface.
- **Glassmorphism:** Used sparingly for "Steam/Mist" overlays, utilizing a high-diffusion backdrop blur (20px) to simulate frosted glass lids.

## Shapes

The shape language is **Sharp (0px)**. To reflect precision engineering and the way stone is cut, all buttons, cards, and input fields utilize 90-degree corners. 

The only exception to this rule is for circular dial controls (emulating physical stove knobs) and circular status indicators. Any structural container or button must maintain a sharp, architectural edge.

## Components

- **Buttons:** Rectangular with no border-radius. Primary buttons use Charcoal Plate backgrounds with white text. Secondary buttons use 1px Brushed Steel borders.
- **The "Glow" State:** Active buttons or toggles do not change color entirely; they gain a 2px outer-glow or "neon-strip" underline in the accent color.
- **Data Visualizations:** Circular progress rings for temperature and timers. Use thin (1px or 2px) strokes.
- **Input Fields:** Minimalist bottom-border only (1px Brushed Steel). When focused, the border transitions to Electric Glow.
- **Cards:** Defined by whitespace and thin 1px dividers rather than background color changes. 
- **The "Control Dial":** A signature digital component—a large, high-contrast circle that users slide to adjust heat or water pressure, mimicking the physical Hydro-Kitchen hardware.
- **Tactile Feedback:** Icons should be line-art based (thin 1.5pt strokes), mimicking laser-etched metal markings.