---
name: Vault-Safe
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
  on-surface-variant: '#c6c5d5'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#908f9e'
  outline-variant: '#464653'
  surface-tint: '#bfc2ff'
  primary: '#bfc2ff'
  on-primary: '#181d8c'
  primary-container: '#000080'
  on-primary-container: '#777eea'
  inverse-primary: '#4b53bc'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#212121'
  on-tertiary-container: '#8a8888'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bfc2ff'
  on-primary-fixed: '#00006e'
  on-primary-fixed-variant: '#3239a3'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
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
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '700'
    lineHeight: '1.2'
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  container-max: 1280px
---

## Brand & Style

The design system is engineered to evoke a "hardened" luxury aesthetic, merging the impenetrable feel of a Swiss bank vault with high-end industrial engineering. It targets high-net-worth individuals and security-conscious enterprises who equate physical weight and structural density with digital safety.

The visual style is **Industrial Tactile**. It rejects the ephemeral nature of modern SaaS design in favor of "armored" UI elements that feel bolted-down and permanent. By combining brutalist structural integrity (thick borders, heavy shadows) with luxury finishes (metallic gradients, deep navy tones), the design system establishes an immediate psychological sense of "bank vault" chic—where every interaction feels like operating a precision-machined locking mechanism.

## Colors

The palette is anchored in **Deep Navy (#000080)**, representing institutional authority and heritage trust. **Matte Black** and near-black neutrals form the structural chassis of the UI, providing a high-contrast environment where **Platinum Silver** elements can shine.

Platinum is not merely a flat color but a metallic texture. Use the silver gradient for primary action triggers and "active" reinforced states. Functional colors (Success, Warning, Error) must be desaturated to maintain the "hardened" aesthetic; avoid neon tones. All backgrounds should lean toward Deep Navy or Matte Black to create a light-absorbing, secure atmosphere.

## Typography

This design system utilizes a tiered typographic approach to balance industrial technicality with premium readability. 

**Space Grotesk** is used for headlines to provide a geometric, machined appearance. Its tight apertures and bold weights suggest structural strength. **Inter** serves as the primary body face for its exceptional clarity and high-contrast rendering against dark backgrounds. For technical data, serial numbers, and "system status" readouts, **JetBrains Mono** is utilized to reinforce the software's "hardened" tech-stack origins. Headlines should always be set with reduced letter-spacing to feel more compact and solid.

## Layout & Spacing

The layout is governed by a **Fixed Grid** philosophy. Content is housed within "Containment Zones" that align to a strict 12-column grid on desktop. To emphasize the "armored" feel, the design system utilizes generous internal padding (safe zones) within components, surrounded by tight external gutters.

- **Desktop:** 12 columns, 24px gutters, 64px outer margins.
- **Tablet:** 8 columns, 16px gutters, 40px outer margins.
- **Mobile:** 4 columns, 12px gutters, 20px outer margins.

The spacing rhythm is based on a **4px base unit**. All structural elements should use multiples of 8px (8, 16, 24, 32, 48, 64) for padding and margins to maintain a rhythmic, engineered appearance.

## Elevation & Depth

Elevation in this design system is not achieved through soft, ethereal light, but through **physical layering and mechanical extrusion**. 

1.  **Reinforced Borders:** Every primary container uses a 3px or 4px solid border. Use Matte Black for the border on Platinum surfaces, and Platinum/Steel colors for borders on Navy surfaces.
2.  **Hard Shadows:** Shadows should be high-opacity and "heavy" (e.g., `offset: 4px 4px, blur: 0, color: rgba(0,0,0,1)`). This creates a "brutalist" shadow that suggests the element is physically thick and resting on a surface.
3.  **Inset Depressions:** Input fields and secondary wells should use inner shadows to appear as if they are milled into the interface's "armor plating."
4.  **Metallic Gradients:** Use subtle 45-degree linear gradients to simulate brushed metal on interactive surfaces, increasing the tactile "clickable" nature of buttons.

## Shapes

The design system employs a **Sharp (0px)** corner philosophy for its primary architecture. Right angles suggest the rigidity of steel plates. 

To introduce the "reinforced" look, use **chamfered corners** (angled 45-degree clips) or "bracketed" corners for primary action buttons. If a component must be rounded for ergonomic reasons, the radius must not exceed 2px. All UI elements should feel like they were cut from sheet metal or machined from a solid block.

## Components

### Buttons
Primary buttons feature a **Platinum Silver gradient** background with a 4px Matte Black bottom-border, creating a "plunger" effect. Labels are in **Space Grotesk Bold** all-caps. The hover state should invert the silver to a deep navy, maintaining the heavy border.

### Input Fields
Inputs are styled as "recessed wells." Use a 2px inset shadow with a dark background. The "active" focus state should be indicated by a 3px border glow in Navy, mimicking an energized circuit.

### Cards & Containers
Containers are "vault modules." They must have a 4px solid border and "rivet" details—small 4px square markers in the four corners—to simulate reinforced attachment.

### Progress Indicators
Avoid smooth, circular loaders. Use segmented, blocky bars that fill up like a mechanical physical gauge.

### Checkboxes & Radios
Square-only. No rounded corners. The "checked" state should use a heavy "X" mark or a solid block fill to represent a physical toggle engagement.

### Security Badges
A unique component for this system: High-contrast, metallic badges that house status info, using JetBrains Mono for a "certificate" feel.