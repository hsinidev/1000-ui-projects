---
name: River Adventure Design System
colors:
  surface: '#111319'
  surface-dim: '#111319'
  surface-bright: '#373940'
  surface-container-lowest: '#0c0e14'
  surface-container-low: '#191b22'
  surface-container: '#1d1f26'
  surface-container-high: '#282a30'
  surface-container-highest: '#33343b'
  on-surface: '#e2e2eb'
  on-surface-variant: '#c3c6d5'
  inverse-surface: '#e2e2eb'
  inverse-on-surface: '#2e3037'
  outline: '#8d909e'
  outline-variant: '#434653'
  surface-tint: '#b1c5ff'
  primary: '#b1c5ff'
  on-primary: '#002c70'
  primary-container: '#0047ab'
  on-primary-container: '#a5bdff'
  inverse-primary: '#2559bd'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#ffb59a'
  on-tertiary: '#5b1b00'
  tertiary-container: '#8b2e01'
  on-tertiary-container: '#ffaa8a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001946'
  on-primary-fixed-variant: '#00419e'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdbcf'
  tertiary-fixed-dim: '#ffb59a'
  on-tertiary-fixed: '#380d00'
  on-tertiary-fixed-variant: '#802900'
  background: '#111319'
  on-background: '#e2e2eb'
  surface-variant: '#33343b'
typography:
  display-xl:
    fontFamily: Lexend
    fontSize: 80px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
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
    lineHeight: '1.6'
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  container-max: 1440px
---

## Brand & Style

This design system is engineered to capture the kinetic energy of whitewater rafting while maintaining a foundation of professional safety. The brand personality is **Exhilarating**, **Rugged**, and **Technical**. It targets adventure seekers who value high-performance gear and expert guidance.

The visual style is a hybrid of **High-Contrast Bold** and **Glassmorphism**. We utilize aggressive, oversized typography and high-saturation colors to evoke adrenaline, paired with translucent, blurred overlays that mimic the refractive properties of water. Motion is the primary driver of the experience—expect fluid transitions, liquid-masking effects, and "water-splatter" SVG organic shapes that break the grid to create a sense of spray and speed.

## Colors

The palette is anchored in a high-contrast dark mode to make the aquatic tones vibrate. **Cobalt Blue** serves as the primary brand driver, representing the power of the river. **Deep Navy** provides the structural background depth, while **White** is reserved for high-impact typography and essential clarity.

**Cyan** is used exclusively as a high-motion accent for interactive elements, data peaks, and "spray" effects. This neon-adjacent blue ensures visibility against the darker cobalt and navy depths. All secondary actions and safety-critical information utilize high-contrast pairings to ensure legibility in high-glare or outdoor environments.

## Typography

This design system utilizes **Lexend** for all headings and labels. Its athletic, wide proportions and geometric clarity resonate with the adventurous nature of the brand. Display type should use tight letter-spacing and heavy weights to create a "wall of sound" effect for impactful messaging.

**Inter** is the choice for body text, providing a neutral, highly readable counterpoint to the aggressive headings. This ensures that technical safety data and trip details remain legible even on smaller devices. Large-scale headings should frequently utilize "knockout" styles or gradients from Cyan to Cobalt to maintain the high-motion aesthetic.

## Layout & Spacing

The layout follows a **12-column fluid grid** that prioritizes dynamic asymmetry. Elements often break the vertical rhythm using "splatter" masks that extend beyond container boundaries. 

Spacing is generous, using an 8px base increment to ensure touch targets are accessible for users who may be outdoors or on the move. We utilize "Safe Zones" for critical text, while decorative "Water-Splatter" assets are permitted to bleed into the margins to create a sense of immersion. Section transitions should use organic, wave-like dividers rather than straight horizontal lines.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** rather than traditional shadows. Surfaces are treated as semi-transparent "ice" or "water" layers with heavy backdrop blurs (20px-40px). 

Higher-priority elements (like booking modals or safety alerts) utilize a brighter Cyan inner-glow (1px stroke) to simulate light catching the edge of a water droplet. We avoid heavy black shadows, preferring "Ambient Navy Glows" where the shadow color is a saturated version of the background (#050B18 at 40% opacity) to maintain color purity.

## Shapes

The shape language is a contrast between **Geometric Containers** and **Organic Fluidity**. Interactive components like buttons and cards use a `rounded-lg` (1rem) or `rounded-xl` (1.5rem) setting to feel friendly and safe. 

However, decorative background elements and image masks use "Blob" shapes and "Water-Splatter" paths. These organic shapes are never perfectly symmetrical, mimicking the unpredictable nature of river rapids. This creates a juxtaposition of professional reliability (the UI) and exhilarating nature (the brand assets).

## Components

### Buttons
Primary buttons are Cobalt Blue with white Lexend Bold text. The hover state initiates a "liquid fill" animation where Cyan color flows in from the bottom, accompanied by a subtle expansion in size.

### Glass Cards
Used for trip packages. These feature a 10% opacity white fill with a `backdrop-filter: blur(24px)` and a 1px translucent border. This ensures they remain readable over high-action photography.

### River Flow Chart
A custom data visualization component. It uses a thick, glowing Cyan polyline to represent CFS (Cubic Feet per Second) levels. The area beneath the line is filled with a Cobalt-to-Navy gradient. Data points pulse when hovered, simulating a ripple.

### Splatter Masks
Image containers that use SVG clip-paths to give photos of rafting a "splashed" edge. These are used sparingly for hero sections and testimonials to break the grid.

### Translucent Overlays
Used for "Safety Checklists." Full-screen blurs that darken the background to Deep Navy, allowing high-contrast white and cyan text to pop for maximum focus.