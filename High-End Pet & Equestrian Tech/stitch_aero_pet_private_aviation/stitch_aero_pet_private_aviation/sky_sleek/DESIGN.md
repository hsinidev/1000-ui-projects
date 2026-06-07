---
name: Sky-Sleek
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#43474e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#476083'
  primary: '#000613'
  on-primary: '#ffffff'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#afc8f0'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#040607'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c1f20'
  on-tertiary-container: '#848688'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-xl:
    fontFamily: Montserrat
    fontSize: 64px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Montserrat
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
    lineHeight: '1.6'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin-desktop: 80px
  margin-mobile: 24px
  section-padding: 120px
---

## Brand & Style

This design system embodies the "Sky-Sleek" aesthetic, a fusion of high-altitude tranquility and elite hospitality. The brand personality is aspirational, serene, and meticulously attentive, targeting ultra-high-net-worth individuals who view their pets as family members deserving of first-class travel.

The visual style leans into **Minimalism** with a touch of **Glassmorphism**. It prioritizes vast white space (representing the open sky), ultra-thin architectural lines, and a composition that feels weightless. Every interaction should evoke the hushed, exclusive atmosphere of a private jet cabin.

## Colors

The palette is anchored by **Deep Navy Blue**, providing a sense of authority, safety, and the infinite night sky. **Gold** is used sparingly as a high-contrast accent for interactive elements and iconography, signaling premium value and bespoke service. 

**Cloud White** serves as the primary canvas color, ensuring the interface feels airy and expansive. For text, a soft charcoal (#4A4A4A) is used against Cloud White to maintain readability without the harshness of pure black, while Cloud White text is used against Deep Navy backgrounds for a striking, high-contrast "night mode" feel within specific components.

## Typography

The typographic hierarchy is designed for effortless scanning and a sense of architectural structure. **Montserrat** is the voice of the brand for headings, utilizing lighter weights (300-400) for large display text to maintain an "airy" feel, and medium weights for smaller headings to ensure hierarchy.

**Inter** provides a highly legible, neutral foundation for all body copy and functional labels. Wide line-heights (1.6) are mandatory for body text to reinforce the feeling of space. Labels should frequently use uppercase with increased letter-spacing to mimic luxury brand tagging.

## Layout & Spacing

The design system employs a **Fixed Grid** on desktop and a **Fluid Grid** on mobile. On large screens, content is centered within a 1280px container with generous 80px side margins to isolate the content and create a "gallery" effect.

Vertical spacing is intentionally oversized. Sections should be separated by at least 120px to prevent the UI from feeling cluttered. The layout relies on "Negative Space as a Feature," allowing high-resolution imagery of pets and aircraft to breathe. Elements should align to a strict 8px baseline grid to maintain structural integrity amidst the wide margins.

## Elevation & Depth

Depth is handled through **Ambient Shadows** and **Tonal Layers**. Instead of heavy shadows, this design system uses extremely soft, long-range shadows (Blur: 40px, Opacity: 4%) with a slight Deep Navy tint to lift cards off the Cloud White background.

To simulate the glass partitions of a private jet, certain overlays and navigation bars use a **Backdrop Blur** (20px) with a 70% opaque Cloud White tint. This creates a sense of physical layers without introducing visual noise. Thin 1px Gold borders are used on elevated elements to define boundaries with precision.

## Shapes

The shape language is **Soft (0.25rem)**. While the overall aesthetic is modern and sleek, sharp corners are avoided to maintain a sense of "comfort" and "safety" associated with pet care. 

Primary containers and image carousels use a slightly larger radius (rounded-lg: 0.5rem) to feel more approachable. Interactive elements like buttons and input fields stay consistent with the 0.25rem radius to look precise and engineered.

## Components

### Buttons
Primary buttons feature a transparent background with a 1.5pt **Gold border** and Gold text. On hover, they transition to a solid Deep Navy fill with white text. Secondary buttons are "Ghost" style with no border, using only Gold text and an underline on hover.

### Cards
Cards are the primary content vessel, featuring generous padding (40px) and a subtle 1px border in a very light grey (#E0E0E0). Imagery within cards should always be top-aligned and full-bleed to the card's top and side edges.

### Icons
All icons must be **Thin-line vectors** (1pt stroke) in Gold. They should be geometric and minimalist, avoiding filled shapes.

### Input Fields
Inputs are minimal: a single bottom border (1px) in Deep Navy. Upon focus, the border transitions to Gold with a subtle upward float animation for the label.

### Specialized Components
- **The "Flight Path" Stepper:** A thin Gold line connecting circular nodes to track a pet's journey in real-time.
- **Pet Profile Badges:** Small, circular avatars with a Gold ring indicating "Elite" or "Frequent Flyer" status.