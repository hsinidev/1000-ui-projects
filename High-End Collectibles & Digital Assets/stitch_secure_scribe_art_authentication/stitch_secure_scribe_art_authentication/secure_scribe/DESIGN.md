---
name: Secure-Scribe
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c6c5d4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#908f9d'
  outline-variant: '#454652'
  surface-tint: '#bdc2ff'
  primary: '#bdc2ff'
  on-primary: '#1b247f'
  primary-container: '#1a237e'
  on-primary-container: '#8690ee'
  inverse-primary: '#4c56af'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#c6c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#303030'
  on-tertiary-container: '#989898'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bdc2ff'
  on-primary-fixed: '#000767'
  on-primary-fixed-variant: '#343d96'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  mono-technical:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  margin-mobile: 20px
  gutter-mobile: 12px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  safe-area-bottom: 34px
---

## Brand & Style

This design system establishes a visual language of "Digital Provenance." It is designed to evoke the unwavering confidence of a high-security vault combined with the refined elegance of a premier art gallery. The aesthetic centers on high-trust authentication, utilizing technical precision and premium materials to reassure collectors and institutions of an object's legitimacy.

The style is a hybrid of **Minimalism** and **Glassmorphism**, leaning heavily into "Technical Luxury." It avoids decorative clutter in favor of functional, high-fidelity components that feel like precision instruments. Every interaction should feel deliberate, secure, and permanent.

## Colors

The palette is anchored in a default **Dark Mode** to emphasize the "vault" atmosphere. 

- **Deep Indigo (#1A237E):** Used for primary actions, structural depths, and "secure state" indicators. It provides a more sophisticated, intellectual alternative to standard tech-blue.
- **Platinum Silver (#E5E4E2):** Applied to typography and borders to simulate metallic finishes. It represents the "Scribe" element—precious and durable.
- **Black (#000000) & Neutral (#121212):** These form the base of the UI, creating infinite depth and high contrast for authentication data.
- **Metallic Gradients:** Linear gradients moving from `#BDBBB7` to `#E5E4E2` should be used on borders and "Tamper-Proof" components to simulate light reflecting off brushed metal.

## Typography

This design system utilizes **Hanken Grotesk** for its sharp, contemporary geometry that balances technical clarity with a premium feel.

- **Headlines:** Set with tight tracking to feel solid and "stamped." 
- **Body Text:** Optimized for high legibility against dark backgrounds using generous line heights.
- **Technical Labels:** Small, all-caps labels with wide tracking are used for metadata, serial numbers, and "Tamper-Proof" status indicators, mimicking archival cataloging.
- **Scanning UI:** For real-time scanning data, use the `mono-technical` variant to provide a sense of computational rigor.

## Layout & Spacing

As a mobile-first system, the layout relies on a **4-column fluid grid** with a 20px outer margin. 

The vertical rhythm is governed by a **4pt grid system**. 
- **Vault Alignment:** Use rigorous, left-aligned layouts to project order and stability.
- **Negative Space:** Generous vertical padding between sections (32px+) is essential to maintain the "premium" feel, preventing the technical data from feeling cluttered or overwhelming.
- **Scanning Context:** The central 60% of the screen is reserved as a "Focus Zone" for scanning interactions and art visualization.

## Elevation & Depth

Depth is not communicated through shadows, but through **Tonal Layering** and **Glassmorphism**.

- **Level 0 (Base):** True Black (#000000).
- **Level 1 (Plates):** Deep Indigo (#1A237E) at 10% opacity, used for background containers.
- **Level 2 (Glass Cards):** Surfaces using a `backdrop-filter: blur(20px)` and a 1px semi-transparent Platinum Silver border. This creates a "frosted glass" effect that feels like a protective casing over the art.
- **Level 3 (Interactive):** Active states use a subtle inner glow (Platinum Silver at 15% opacity) to suggest the element is illuminated from within.

## Shapes

The shape language is **Soft (0.25rem)**. 

Precision is key; therefore, large rounded corners are avoided as they feel too "consumer-grade." The slight 4px radius on buttons and cards provides just enough approachability while maintaining a crisp, architectural edge. 

- **Scanning Reticles:** Use sharp 90-degree corners for the viewfinder to emphasize technical precision.
- **Badges:** Use a "Hexagonal" or "Chipped-Corner" geometry for Tamper-Proof badges to distinguish them from standard UI elements.

## Components

### 1. Tamper-Proof Badges
These are high-priority status indicators. They feature a metallic linear gradient background, high-contrast black text, and a micro-pattern overlay (such as a 1px dot grid) to simulate holographic security features.

### 2. Scanning UI Patterns
The scanning interface utilizes a "Laser-Line" animation—a horizontal Platinum Silver stroke with a subtle Deep Indigo outer glow—that moves vertically across the viewfinder. Peripheral data (coordinates, ISO, Hash ID) should be displayed in `mono-technical` typography at the corners of the scan area.

### 3. Glass Action Buttons
Primary buttons use a Deep Indigo fill with a 1px Platinum Silver border. Secondary buttons use the Glassmorphism style: translucent background with a high-intensity backdrop blur.

### 4. Authentication Cards
Cards used to display art metadata must feature a "Certificate of Authenticity" layout. This includes a clear hierarchy: Artist Name (Headline-md), Provenance ID (Label-caps), and a "Verified" watermark integrated into the background blur.

### 5. Input Fields
Fields are "Underlined" rather than boxed, using a 1px Platinum Silver stroke. This mimics the appearance of a signature line on a physical certificate. On focus, the line glows with a Deep Indigo pulse.