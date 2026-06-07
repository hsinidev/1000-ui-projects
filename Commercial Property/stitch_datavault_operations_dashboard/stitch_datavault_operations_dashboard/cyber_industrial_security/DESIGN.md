---
name: Cyber-Industrial Security
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
  on-surface-variant: '#baccb0'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#85967c'
  outline-variant: '#3c4b35'
  surface-tint: '#2ae500'
  primary: '#efffe3'
  on-primary: '#053900'
  primary-container: '#39ff14'
  on-primary-container: '#107100'
  inverse-primary: '#106e00'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#fdf9f9'
  on-tertiary: '#313030'
  tertiary-container: '#e0dddc'
  on-tertiary-container: '#626161'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#79ff5b'
  primary-fixed-dim: '#2ae500'
  on-primary-fixed: '#022100'
  on-primary-fixed-variant: '#095300'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 16px
---

## Brand & Style

The design system is engineered to evoke a sense of absolute security, technical precision, and futuristic infrastructure. It targets a specialized audience of data architects, security auditors, and IT infrastructure leads who require high-density information presented with zero ambiguity.

The aesthetic blends **Minimalism** with **Brutalism**. It utilizes a "Terminal-Plus" approach: the raw, functional feel of a command-line interface elevated by modern high-fidelity accents. The emotional response is one of controlled power—the UI should feel like a high-security vault door interface: heavy, immutable, and hyper-responsive. Visual interest is driven by functional accents rather than decorative elements, using "fiber-optic" glowing lines to guide the eye through complex data hierarchies.

## Colors

The palette is strictly functional, optimized for low-light data center environments. 

- **Matte Black (#121212):** The foundation. Used for the primary background to reduce eye strain and maximize the contrast of glowing elements.
- **Silver (#C0C0C0):** Used for primary UI text, icons, and structural borders. It provides a metallic, industrial feel that differentiates the interface from standard "flat" dark modes.
- **Neon Green (#39FF14):** The high-visibility accent. Reserved for "Active" states, successful certifications, and critical path highlights. This color is used for "Fiber Lines"—1px strokes with a subtle outer glow (0px 0px 8px).
- **Surface Tiers:** Use a slightly lighter neutral (#1A1A1A) for card backgrounds to create a subtle separation from the abyss of the primary background.

## Typography

This design system employs a dual-font strategy to balance character and clarity.

- **UI & Navigation:** **Space Grotesk** is used for headlines, labels, and buttons. Its geometric, slightly quirky apertures provide the "futuristic" edge required for a tech-industrial aesthetic.
- **Technical Specifications:** **Inter** is used for all long-form body text and descriptions. Its neutral, systematic nature ensures high readability for complex technical documentation and ISO standards.
- **Data Rendering:** For technical specifications, hardware IDs, and certification numbers, use **Space Grotesk** in Medium weight. While not a true monospace, its rhythmic spacing and technical letterforms serve the "data" aesthetic effectively. All labels for data points must be in uppercase with increased letter spacing.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop (1280px max-width) and a **Fluid** model on mobile. 

- **Grid:** A 12-column grid with narrow 16px gutters to maintain a "high-density" technical look. 
- **Mobile-First Certifications:** Certification cards (ISO/SOC2) are designed to span the full width of mobile screens, using tight 8px internal padding to maximize data density.
- **Rhythm:** All vertical spacing must be a multiple of 4px. Use larger gaps (40px+) to separate distinct hardware sections, but keep internal card elements tightly grouped (8-16px) to mimic the compact nature of server rack configurations.

## Elevation & Depth

Shadows are strictly prohibited. In this design system, depth is communicated through **Tonal Layering** and **Luminous Accents**.

- **Level 0 (Background):** #121212.
- **Level 1 (Cards/Panels):** #1A1A1A with a 1px solid #C0C0C0 (at 10% opacity) border.
- **Level 2 (Active/Focus):** Elements gain a 1px #39FF14 border and a matching "fiber-optic" glow.
- **Fiber-Optic Lines:** Use vertical or horizontal lines (1px) in Neon Green to connect related data points (e.g., a facility location connected to its active certifications). These lines should have a soft 4px blur applied to a secondary stroke layer to simulate light emission.

## Shapes

The shape language is **Sharp (0px)**. To maintain the industrial and high-security aesthetic, all buttons, input fields, cards, and containers must have 90-degree corners. This evokes the rigid structure of server enclosures and reinforced facility architecture. 

A "chamfered corner" effect may be used for primary action buttons (clip the top-right corner at a 45-degree angle) to reinforce the technical/military-grade UI style.

## Components

- **Buttons:** Primary buttons use a Matte Black background with a 1px Neon Green border and Neon Green text. On hover, the button fills with Neon Green and the text flips to Matte Black.
- **Chips (Certifications):** Small, rectangular blocks with a Silver border. "Valid" certifications feature a 4px Neon Green dot prefix.
- **Inputs:** Technical fields use a #1A1A1A background with a Silver bottom-border only. Labels are always positioned above the input in uppercase Space Grotesk.
- **Cards:** Data center facility cards feature a "Live Status" header. If the facility is operational, the top border of the card is a 2px Neon Green "fiber" line.
- **Data Visualization:** Use simple 1px line charts. Gradients are only permitted as vertical "scans" within charts, using Neon Green at 10% opacity.
- **Security Indicator:** A persistent "Security Status" component in the header, utilizing a pulse animation on a Neon Green circle to indicate a live, secure connection.