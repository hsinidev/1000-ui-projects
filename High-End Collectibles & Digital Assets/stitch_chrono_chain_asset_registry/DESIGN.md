---
name: Horological Ledger
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2b2a2a'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1a1a1a'
  on-primary-container: '#848282'
  inverse-primary: '#5f5e5e'
  secondary: '#b5c8df'
  on-secondary: '#203243'
  secondary-container: '#36485b'
  on-secondary-container: '#a4b7cd'
  tertiary: '#cac6c4'
  on-tertiary: '#31302f'
  tertiary-container: '#1b1a19'
  on-tertiary-container: '#858281'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#d1e4fb'
  secondary-fixed-dim: '#b5c8df'
  on-secondary-fixed: '#091d2e'
  on-secondary-fixed-variant: '#36485b'
  tertiary-fixed: '#e6e2df'
  tertiary-fixed-dim: '#cac6c4'
  on-tertiary-fixed: '#1c1b1a'
  on-tertiary-fixed-variant: '#484645'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  headline-display:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: 0.08em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  technical-label:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  grid_margin: 20px
  grid_gutter: 12px
  unit_xs: 4px
  unit_sm: 8px
  unit_md: 16px
  unit_lg: 24px
  unit_xl: 48px
---

## Brand & Style

This design system is built upon the intersection of high-end horology and cryptographic certainty. The visual language evokes the feeling of an engineering blueprint for a masterpiece—precise, immutable, and exclusive. 

The aesthetic is **Technical Luxury**. It moves away from the "soft" nature of modern SaaS and instead adopts the rigid, disciplined world of watchmaking. Every pixel is treated as a component in a movement, utilizing **Engineering-grade Minimalism** with a **Tactile** overlay. The goal is to make the user feel they are interacting with a "digital twin" of their physical timepiece, where the UI serves as a protective vault and a certificate of authenticity.

Key visual pillars include:
- **Precision alignment:** Every element is locked to a strict technical grid.
- **Materiality:** Use of brushed metal textures and metallic light-refractions.
- **Trust-Architecture:** Heavy use of technical callouts (serial numbers, timestamps, block heights) to reinforce the blockchain foundation.

## Colors

The palette is anchored in **Charcoal (#1A1A1A)** and **Slate (#2C3E50)**, providing a deep, low-light environment that allows the watch photography and metallic accents to pop.

- **Foundational Neutrals:** Surfaces use Charcoal for the base and Slate for elevated containers to create a sense of depth without relying on traditional light-source logic.
- **The Accents:** **Champagne Gold** is used sparingly for primary actions and "Prestige" markers. **Brushed Steel** is the workhorse for borders, dividers, and secondary icons, mimicking the 316L stainless steel often found in luxury sport watches.
- **Semantic Feedback:** Verification is represented by **Emerald**, appearing as a faint "glow" or steady indicator. Stolen or lost status is flagged with **Ruby**, signifying an immediate breach of the registry.

## Typography

The typography system balances technical character with Swiss-style legibility.

- **Headlines:** Use **Space Grotesk** with wide tracking and uppercase styling. This mimics the engravings found on watch casebacks and high-end technical manuals.
- **Body:** **Inter** is used for all descriptive text. Its neutral, functional design ensures that information about provenance and specs is easily digestible.
- **Technical Metadata:** **JetBrains Mono** is introduced for blockchain hashes, serial numbers, and "digital twin" telemetry. This monospaced font reinforces the engineering-grade nature of the platform.

## Layout & Spacing

This design system utilizes a **4-column fluid grid** for mobile, designed to feel like a technical schematic.

- **The Micro-Border System:** Elements are separated by 0.5pt lines in **Brushed Steel**. These lines often extend to the edges of the screen, creating a "blueprint" effect.
- **Technical Callouts:** Margins are often used to house "Technical Callouts"—small, monospaced labels that indicate the X/Y coordinates of a section or the "Layer ID" of a component.
- **Rhythm:** A strictly linear 8px vertical rhythm is maintained. White space is used as a luxury commodity; large gaps between sections emphasize the importance of the individual asset being viewed.

## Elevation & Depth

Depth in this design system is achieved through **Material Layering** rather than traditional drop shadows.

- **Skeuomorphic Surfaces:** Secondary containers utilize a subtle linear gradient (from #2C3E50 to #1A1A1A) at a 135-degree angle to simulate the sheen of brushed titanium or steel.
- **Precision Shadows:** When shadows are used, they are "High-Fidelity"—meaning they have a very large blur radius (30px+) but extremely low opacity (10-15%). This simulates a heavy physical object sitting on a matte surface.
- **Etched Elements:** Dividers and some input fields use a "1px Highlight" technique—a light 0.5px line on the bottom edge and a dark 0.5px line on the top—to make elements appear etched into the metal surface.

## Shapes

The shape language reflects **Precision Machining**. 

- **Radius:** A consistent **4px (Soft)** radius is used for primary containers and buttons. This provides a "finished" edge that mimics a chamfered watch case rather than a sharp, dangerous blade or a soft, bubbly consumer app.
- **Clipping:** Images of watches should never be clipped into circles; they should maintain their original aspect ratio or be housed in the standard 4px rounded rectangular containers to preserve their architectural integrity.

## Components

- **The "Vault" Button:** Primary actions feature a subtle horizontal brushed-metal gradient with Champagne Gold text. On tap, the button slightly "depresses" via an inner shadow.
- **Asset Cards:** Use a "Digital Twin" aesthetic. The card features a micro-border, a JetBrains Mono "Reference Number" in the top-left corner, and a high-resolution, shadow-heavy image of the timepiece.
- **Verification Badge:** A small, Emerald-tinted capsule with a "Verified" icon. It should have a faint 2px outer glow to simulate an LED status indicator.
- **Technical Scanners:** For QR or serial scanning, the UI should use a "Crosshair" overlay with technical coordinates at each corner of the viewfinder.
- **Timeline/Provenance:** A vertical line component using the Brushed Steel color, with "Nodes" representing ownership transfers. Each node is a small hexagonal shape, referencing a screw-down case back.
- **Input Fields:** Flat Charcoal backgrounds with 1px Brushed Steel bottom-borders only. Labels are in `technical-label` style, positioned above the field.