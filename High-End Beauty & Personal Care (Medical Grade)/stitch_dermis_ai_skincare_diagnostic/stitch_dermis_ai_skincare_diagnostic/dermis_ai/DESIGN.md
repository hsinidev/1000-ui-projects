---
name: Dermis-AI
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadc'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#434653'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#737784'
  outline-variant: '#c3c6d5'
  surface-tint: '#2559bd'
  primary: '#00327d'
  on-primary: '#ffffff'
  primary-container: '#0047ab'
  on-primary-container: '#a5bdff'
  inverse-primary: '#b1c5ff'
  secondary: '#4d6265'
  on-secondary: '#ffffff'
  secondary-container: '#d0e7ea'
  on-secondary-container: '#53686b'
  tertiary: '#34373a'
  on-tertiary: '#ffffff'
  tertiary-container: '#4b4e50'
  on-tertiary-container: '#bcbfc2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001946'
  on-primary-fixed-variant: '#00419e'
  secondary-fixed: '#d0e7ea'
  secondary-fixed-dim: '#b4cbce'
  on-secondary-fixed: '#091f21'
  on-secondary-fixed-variant: '#364a4d'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c4c7ca'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#44474a'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
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
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-point:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-padding: 24px
  stack-gap: 16px
  section-gap: 32px
  gutter: 12px
---

## Brand & Style

This design system embodies "Sterile-Chic," a sophisticated fusion of medical precision and high-end futuristic aesthetics. The personality is clinical, authoritative, and ultra-hygienic, targeting health-conscious users who value data-driven skincare. 

The visual movement centers on **Glassmorphism** and **Minimalism**. By utilizing translucent layers and frosted glass effects, the UI mimics the clarity of laboratory glassware and the purity of advanced dermatological environments. The emotional response is one of absolute trust, technological advancement, and personal care. The interface should feel like a premium medical instrument: precise, responsive, and impeccably clean.

## Colors

The palette is anchored by **Clinical Blue**, representing medical authority and scientific depth. **Frost White** serves as the primary canvas, ensuring a high-brightness, "clean-room" feel. 

**Glass-Cyan** is the signature accent, used exclusively for glassmorphic containers and subtle glows to suggest futuristic scanning and analysis capabilities. Neutral tones are kept cool-toned and near-black to maintain high contrast for data visualization and critical medical text. All interactions should leverage transparency and subtle blurs rather than flat fills to maintain the "Glass-Chic" aesthetic.

## Typography

This design system utilizes **Space Grotesk** for headlines to inject a technical, geometric, and futuristic edge. It suggests engineering and high-tech analysis. 

**Inter** is the workhorse for body copy and labels, providing the "clinical" readability required for medical instructions and skin reports. The contrast between the expressive, technical headlines and the neutral, functional body copy reinforces the brand's dual identity as both a medical tool and an advanced AI. Tracking is increased on small labels to maintain a sense of airy, premium space.

## Layout & Spacing

Designed for mobile, this design system follows a **fluid grid** model with significant breathing room to prevent visual clutter. A 4-column layout is standard for small screens. 

Margins are generous (24px) to emphasize the minimalist, "hygienic" feel. Vertical rhythm is strictly enforced using a 4px baseline, ensuring that data-heavy analysis screens remain organized and scannable. Alignment should feel architectural—sharp edges and clear vertical axes are preferred over centered, floating elements.

## Elevation & Depth

Hierarchy is established through **Backdrop Blurs** and **Tonal Layering** rather than traditional drop shadows. Surfaces are defined by their refractive properties:

1.  **Level 0 (Base):** Solid Frost White (#F5F7FA).
2.  **Level 1 (Cards):** Glass-Cyan at 40% opacity with a 20px backdrop blur and a 1px solid Clinical Blue border (10% opacity).
3.  **Level 2 (Modals/Popups):** Glass-Cyan at 60% opacity with a 40px backdrop blur, creating a sense of "clinical isolation" from the background content.

Ambient shadows are minimized, used only when a tactile button press is required, appearing as a soft, low-opacity Clinical Blue glow (#0047AB at 15% opacity).

## Shapes

The shape language is "Soft-Precision." While the system is modern, the roundedness is kept to a **Soft (0.25rem)** level to maintain a clinical, professional edge that avoids looking too "playful" or consumer-grade.

Corners are sharp enough to feel like surgical instruments but rounded enough to feel sophisticated. Larger containers like "Scan Result Cards" may use `rounded-lg` (0.5rem) to provide a subtle visual cushion, but the core DNA remains disciplined and geometric.

## Components

### Buttons
Primary buttons use solid Clinical Blue (#0047AB) with white text for maximum contrast and authority. Secondary buttons use the "Glass-Cyan" effect with a thin, 1px Clinical Blue border. All buttons have a high-contrast hover/active state where the border thickness increases.

### Chips & Tags
Used for skin types (e.g., "Oily," "Sensitive"). These use a semi-transparent Frost White background with Clinical Blue text. They are slightly more rounded than buttons to distinguish them as informational metadata.

### Input Fields
Minimalist 1px bottom-border fields. Upon focus, a subtle "Cyan Glow" (blur: 8px) appears behind the input area, suggesting the AI is "scanning" or "processing" the input.

### Analysis Cards
The core of the experience. These leverage the full glassmorphism stack: frosted Cyan background, thin borders, and high-readability Inter typography. They should appear to "float" above the base Frost White surface.

### Additional Components
- **Scanner Viewfinder:** A thin, animated Clinical Blue frame with "corner brackets" to guide the user's camera.
- **Progress Gauge:** A thin, circular ring using a gradient from Glass-Cyan to Clinical Blue to represent skin health percentages.
- **Micro-interactions:** Transitions should be instantaneous and crisp, utilizing "wipe" or "fade" animations that mimic medical imaging technology.