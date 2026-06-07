---
name: Digital Trust Core
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fa'
  on-surface: '#111c2c'
  on-surface-variant: '#3e4850'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#6e7881'
  outline-variant: '#bdc8d1'
  surface-tint: '#00658d'
  primary: '#00658d'
  on-primary: '#ffffff'
  primary-container: '#00aeef'
  on-primary-container: '#003e58'
  inverse-primary: '#82cfff'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#5a5f62'
  on-tertiary: '#ffffff'
  tertiary-container: '#9fa3a7'
  on-tertiary-container: '#353a3d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c6e7ff'
  primary-fixed-dim: '#82cfff'
  on-primary-fixed: '#001e2d'
  on-primary-fixed-variant: '#004c6b'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#dfe3e7'
  tertiary-fixed-dim: '#c3c7cb'
  on-tertiary-fixed: '#171c1f'
  on-tertiary-fixed-variant: '#43474b'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

This design system is built on the pillars of **Digital Sovereignty, Transparency, and Soft-Security**. For a Decentralized Identity (DID) portal, the UI must act as a calm, authoritative steward of user data. The brand personality is "The Quiet Guardian"—professional and institutional, yet technologically forward-thinking.

The visual style is **Refined Soft-UI**. While it draws inspiration from neumorphism, it avoids the usability pitfalls of low contrast by utilizing crisp typography and intentional accent colors. It employs "tactile digital" surfaces that feel like precision-engineered hardware. The goal is to make intangible blockchain data feel physical, safe, and easily manageable.

## Colors

The palette is anchored by **Sky Blue**, representing clarity and the expansive nature of the open web. **Silver** provides a metallic, high-fidelity finish that evokes the security of a physical vault.

- **Primary (Sky Blue):** Used for primary actions, verification statuses, and brand accents.
- **Secondary (Silver):** Used for subtle borders, inactive states, and decorative "brushed metal" effects.
- **Surface (White):** The foundational color for all Soft-UI extrusions.
- **Functional Grays:** A cool-toned slate is used for text to maintain high readability without the harshness of pure black.

Maintain a light-source consistency where "light" always hits the top-left of elements, creating consistent soft highlights and shallow shadows.

## Typography

This design system utilizes **Manrope** for its exceptional balance between geometric modernism and humanistic warmth. It provides the professional rigor required for financial and identity sectors while remaining approachable.

- **Headlines:** Use tighter letter-spacing and heavier weights to establish a "bolted-down" feel.
- **Body Text:** Ample line-height is prioritized to ensure that complex identity strings and wallet addresses are legible.
- **Data Labels:** **Inter** is used for utility-based information, labels, and metadata to provide a systematic, neutral contrast to the more expressive Manrope.

## Layout & Spacing

The layout follows a **Fixed-Grid model** within a centered container to evoke a sense of focus and containment—mimicking a physical identity card or passport. 

- **Grid:** A 12-column grid with generous 24px gutters.
- **Rhythm:** An 8px base unit drives all padding and margins. 
- **Negative Space:** Use "Heavy Minimalism." Provide significant padding within containers (Level: LG) to prevent the Soft-UI shadows from overlapping and creating visual mud. Data-heavy tables should utilize alternating silver-tinted rows rather than heavy lines.

## Elevation & Depth

Depth is the primary communicator of hierarchy in this design system. We use a **Subtle Neumorphic** stack:

1.  **Base Surface:** Background color (`#F8FAFC`).
2.  **Raised State (Buttons/Cards):** A top-left highlight (White, 100% opacity) and a bottom-right shadow (Cool Gray, 12% opacity). Blur radius should be high (20px+) to keep the effect "soft."
3.  **Sunken State (Inputs/Active Buttons):** An inner shadow (inset) using the same logic to denote that a field is ready for data entry.
4.  **Verification Glow:** For high-security "Verified" states, a soft Sky Blue outer glow replaces the standard shadow, signaling a "live" and trusted status.

## Shapes

The shape language is defined by **Friendly Geometry**. We use a `roundedness` level of **2**, which translates to 0.5rem (8px) for standard components.

- **Standard Components:** 8px radius for buttons and input fields.
- **Identity Cards:** 24px (rounded-xl) to mimic the feel of a physical ID or credit card.
- **Status Pills:** Fully rounded (pill-shaped) to distinguish them from interactive buttons.

Edges should never be sharp, as rounded corners are perceived as more approachable and less "threatening" in the context of data security.

## Components

### Buttons
Primary buttons use the **Raised** Soft-UI state with Sky Blue text or background. Hover states should transition to a deeper "pressed" inset shadow. No heavy borders; let the depth define the edge.

### Cards (The "Identity Vault")
The central component of the portal. These are large white containers with `rounded-xl` corners and the standard dual-shadow elevation. They house the user's DID information, QR codes, and credentials.

### Input Fields
Inputs must use the **Sunken** (inset shadow) state. This provides a clear affordance that the area is "empty" and needs to be filled. Use a 1px Silver border only on focus to enhance accessibility.

### Trust Chips
Small pill-shaped labels used for "Verified," "Pending," or "Revoked." These should use low-saturation versions of green, amber, and red, but always accompanied by a Sky Blue "Security Seal" icon to maintain brand consistency.

### Navigation
A clean, horizontal top-bar with a Silver bottom-border (0.5px). Active links are indicated by a small Sky Blue dot below the label, rather than a heavy underline.