---
name: Cold-Tech Elite
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#bec8ca'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#889394'
  outline-variant: '#3f494a'
  surface-tint: '#85d3dc'
  primary: '#ffffff'
  on-primary: '#00363b'
  primary-container: '#a1eff8'
  on-primary-container: '#126f77'
  inverse-primary: '#026971'
  secondary: '#c1c7cf'
  on-secondary: '#2b3137'
  secondary-container: '#41474e'
  on-secondary-container: '#afb6bd'
  tertiary: '#ffffff'
  on-tertiary: '#00354a'
  tertiary-container: '#c4e7ff'
  on-tertiary-container: '#006c93'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#a1eff8'
  primary-fixed-dim: '#85d3dc'
  on-primary-fixed: '#002023'
  on-primary-fixed-variant: '#004f55'
  secondary-fixed: '#dde3eb'
  secondary-fixed-dim: '#c1c7cf'
  on-secondary-fixed: '#161c22'
  on-secondary-fixed-variant: '#41474e'
  tertiary-fixed: '#c4e7ff'
  tertiary-fixed-dim: '#7bd0ff'
  on-tertiary-fixed: '#001e2c'
  on-tertiary-fixed-variant: '#004c69'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  h1:
    fontFamily: spaceGrotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: spaceGrotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: spaceGrotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: jetbrainsMono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  metric-display:
    fontFamily: jetbrainsMono
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: -0.04em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-padding: 40px
  gutter: 24px
  section-gap: 80px
  component-padding-x: 20px
  component-padding-y: 16px
---

## Brand & Style

The design system is engineered to evoke the atmosphere of high-end thermal therapy: clinical precision meets premium hospitality. The "Cold-Tech" aesthetic centers on the concept of "Frost"—a sophisticated application of glassmorphism that suggests frozen surfaces and crystalline clarity. 

The target audience consists of elite athletes and wellness-focused professionals who demand technical excellence and measurable results. The UI must feel professional and trust-centric to validate the medical-grade nature of the services, while remaining futuristic enough to signal cutting-edge innovation. This is achieved through a meticulous balance of deep matte surfaces, shimmering metallic accents, and translucent layers that provide a sense of atmospheric depth.

## Colors

This design system utilizes a high-contrast dark mode foundation. **Matte Black** serves as the primary canvas, providing a "void" that allows technical elements to pop. **Ice Blue** is the core functional color, used for primary actions, success states, and indicating active thermal states. **Silver** acts as a structural accent, used for borders and secondary text to provide a metallic, premium sheen.

To maintain the "Frost" effect, use varying opacities of a cool-tinted white for overlays. Data visualizations should leverage the contrast between the deep background and the luminous Ice Blue to ensure clinical legibility.

## Typography

Typography in this design system is split between technical precision and modern readability. **Space Grotesk** is used for headlines, providing a geometric, futuristic character that aligns with the "Cold-Tech" aesthetic. **Manrope** is the workhorse for body copy, chosen for its balanced and professional tone to build user trust. 

For data points and recovery metrics, **JetBrains Mono** is employed to lend a scientific, monospaced look that suggests raw data processing. All labels should utilize uppercase JetBrains Mono with generous letter spacing to act as "technical identifiers" across the UI.

## Layout & Spacing

The layout philosophy is defined by "Precise Generosity." A 12-column fluid grid is used, but content is often constrained to a maximum width to maintain focus. Generous whitespace (negative space) is essential to prevent the "Frost" effects from feeling cluttered or muddy. 

Rhythms follow a 4px base unit. Margins are intentionally large (40px+) to frame the UI like a premium gallery. Internal component spacing must be consistent and tight, creating a sharp contrast between the expansive layout and the dense, data-rich cards.

## Elevation & Depth

Depth is communicated through "Thermal Layering" rather than traditional shadows. 

1.  **Base Layer:** Solid Matte Black (#0A0A0A).
2.  **Frost Layer:** Semi-transparent Ice Blue/White with a heavy backdrop blur (20px to 40px). This is the primary surface for cards and modals.
3.  **Light Catchers:** Instead of shadows, use 0.5px or 1px inner strokes in Silver or low-opacity white to simulate the edges of glass catching light.
4.  **Luminous Glow:** Primary interactive elements may have a soft Ice Blue outer glow (blur: 15px, opacity: 0.2) to suggest energy or activity.

## Shapes

The design system uses a "Soft Tech" shape language. Standard containers and buttons utilize a 0.25rem (4px) corner radius. This subtle rounding maintains a professional, architectural feel—avoiding the playfulness of highly rounded "pill" shapes while moving away from the aggressive sharpness of 0px corners. Large "Frost" panels may use a larger radius (0.75rem) to soften the transition between the background and the content.

## Components

### Buttons
Primary buttons are solid Ice Blue with black text, featuring a subtle inner "shiver" glow. Secondary buttons use a Silver "ghost" style with a backdrop blur.

### Frost Cards
The signature component. These containers must use a `backdrop-filter: blur(30px)` and a background color of `rgba(255, 255, 255, 0.05)`. A 1px solid border in Silver at 20% opacity is required.

### Recovery Metrics (Data Viz)
Charts use high-stroke weights in Ice Blue against the Matte Black background. Grid lines in the charts should be minimal and rendered in low-opacity Silver. "Critical" data points may use a sharp, high-contrast white.

### Membership Tiers
Premium tiers are distinguished by a vertical Silver-to-Ice-Blue gradient border and a higher backdrop-blur value, creating a more "dense" crystalline look than standard cards.

### Booking Interface
Calendar and time-slot pickers use a tight grid with JetBrains Mono for numbers. Selected states use a full Ice Blue flood with an inner shadow to suggest a "pressed into ice" effect.