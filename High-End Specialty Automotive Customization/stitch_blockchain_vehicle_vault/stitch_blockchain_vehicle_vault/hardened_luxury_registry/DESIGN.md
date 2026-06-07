---
name: Hardened Luxury Registry
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a29'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e918e'
  outline-variant: '#444845'
  surface-tint: '#c7c6c4'
  primary: '#ffffff'
  on-primary: '#303130'
  primary-container: '#e3e2e0'
  on-primary-container: '#646463'
  inverse-primary: '#5e5e5d'
  secondary: '#c2c2f2'
  on-secondary: '#2b2d53'
  secondary-container: '#44456e'
  on-secondary-container: '#b4b4e4'
  tertiary: '#ffffff'
  on-tertiary: '#303030'
  tertiary-container: '#e2e2e2'
  on-tertiary-container: '#646464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3e2e0'
  primary-fixed-dim: '#c7c6c4'
  on-primary-fixed: '#1b1c1b'
  on-primary-fixed-variant: '#464746'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c2c2f2'
  on-secondary-fixed: '#16173d'
  on-secondary-fixed-variant: '#42436b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
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
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  border-thick: 3px
  border-thin: 1px
---

## Brand & Style

This design system is engineered to evoke the sensation of an impenetrable digital vault. It targets ultra-high-net-worth individuals and collectors who require more than a database; they require a high-security visual confirmation of ownership. The brand personality is authoritative, mechanical, and uncompromising.

The aesthetic direction is **Hardened Industrialism**—a fusion of Neo-Brutalism and high-end technical interfaces. It eschews soft gradients and organic shapes for rigid structures, thick borders, and heavy-duty interactive elements. Every interface element is designed to feel "bolted down," reinforcing the immutability of the Soulbound NFT assets being managed. The emotional goal is to provide the user with absolute confidence in the permanence and security of their luxury vehicle records.

## Colors

The palette is strictly limited to high-contrast, industrial tones to maintain a serious, high-end security atmosphere.

- **Primary (Platinum Silver):** Used for typography, key iconography, and highlighting the "metallic" edges of the interface. It represents the value and rarity of the assets.
- **Secondary (Deep Indigo):** Acts as the primary surface color for containers and depth. It provides a more sophisticated alternative to pure black, suggesting a high-tech obsidian or deep-sea military coating.
- **Tertiary (Black):** Reserved for the deep background and voids. It creates the "void" into which the vault modules are set.
- **Surface Treatments:** High-contrast borders are always used to separate these colors. Texture overlays (noise or subtle brushed metal) should be applied to the Platinum and Indigo surfaces to increase the tactile feel.

## Typography

The typography in this design system emphasizes technical precision and structural integrity. 

- **Headings:** **Space Grotesk** is used for all primary headlines. Its geometric but slightly idiosyncratic characters provide a "high-tech future" look that avoids standard corporate tropes.
- **Body:** **Geist** provides a clean, neutral, and hyper-legible experience for descriptions and narrative text. It feels engineered rather than drawn.
- **Data & Labels:** **JetBrains Mono** is utilized for all "Soulbound" identifiers, blockchain hashes, and technical specifications. The monospaced nature reinforces the feeling of a terminal or a direct-from-ledger output.

All labels should be treated as functional indicators, often appearing in all-caps with generous letter spacing to mimic engraved serial numbers.

## Layout & Spacing

This design system employs a **Fixed Module Grid**. Elements do not simply "float"; they are locked into heavy-duty containers.

- **Grid Logic:** A 12-column grid for desktop, 6-column for tablet, and 2-column for mobile.
- **Rhythm:** An 8px base unit (with 4px for fine-tuning) ensures all elements align to a rigid technical standard.
- **Compartmentalization:** Every content block must be enclosed within a defined border. Spacing between modules should be consistent (24px) to create "channels" of negative space that feel like structural joints.
- **Alignment:** Use hard-left alignment for all data points. Indentation should be used sparingly, primarily to indicate a hierarchy of "nested" security levels.

## Elevation & Depth

Standard shadows are strictly prohibited. Depth is instead conveyed through **Structural Layering** and **Tonal Insets**.

1.  **Bold Borders:** Every interactive or containing element uses a 3px "Hardened" border. Use the Platinum Silver color against the Deep Indigo background to create a "lit edge" effect.
2.  **Tonal Stacking:** Surfaces do not "float" above each other with shadows. Instead, background surfaces are the darkest (#000000), and foreground "vault panels" are slightly lighter (#1A1B41). 
3.  **The 'Soulbound' Inset:** Active or "locked" items should use an inner shadow (inset) to look as if they have been physically stamped into the interface. 
4.  **Verification Layers:** Use a scan-line texture or a very subtle 5% opacity "dot grid" on the primary background to suggest a digital screen or a heads-up display (HUD).

## Shapes

The shape language is defined by **Zero-Radius Geometry**. 

All buttons, inputs, cards, and containers must have 0px corner radii. Sharp corners communicate a "Hardened" security posture and industrial manufacturing. The only exceptions are circular icons or specific "Soulbound" seals, which should appear as perfectly circular "stamps" to contrast against the rigid rectangular grid of the interface.

To add visual interest without using curves, use "clipped" corners (45-degree chamfers) on primary action buttons or the main header of the "vault" modules to reinforce the military-grade hardware aesthetic.

## Components

### Primary Action Buttons
Large, sharp-edged rectangles with a 3px Platinum Silver border. On hover, the button should invert colors (Background: Platinum, Text: Black). The "active" state should move the button 2px down and right to simulate a heavy physical click.

### Soulbound Identity Cards
The center-piece of the UI. These cards house the vehicle registry data. They must feature:
- A "Status: Locked" indicator using the `label-caps` style.
- A technical watermark of the vehicle's VIN or Blockchain ID.
- High-contrast, thick-bordered containers for image assets.

### Input Fields
Inputs should look like data entry terminals. Deep black background, 1px Platinum border. Use the `data-display` (JetBrains Mono) font for user input. Include a blinking block cursor (`_`) to maintain the technical theme.

### Data Chips
Used for vehicle features (e.g., V12, Carbon Fiber). These are small, sharp rectangles with a semi-transparent Deep Indigo fill and a Platinum border.

### Status Indicators
Security levels (Verified, Pending, Locked) should use high-saturation functional colors (Green/Red) but only in small doses (e.g., a glowing square icon) to ensure the interface remains dominated by the neutral metallic palette.