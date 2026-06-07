---
name: Academic Heritage
colors:
  surface: '#fcf9f0'
  surface-dim: '#dddad1'
  surface-bright: '#fcf9f0'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ea'
  surface-container: '#f1eee5'
  surface-container-high: '#ebe8df'
  surface-container-highest: '#e5e2da'
  on-surface: '#1c1c17'
  on-surface-variant: '#554240'
  inverse-surface: '#31312b'
  inverse-on-surface: '#f4f1e8'
  outline: '#89726f'
  outline-variant: '#dcc0bd'
  surface-tint: '#9d4139'
  primary: '#210000'
  on-primary: '#ffffff'
  primary-container: '#4a0404'
  on-primary-container: '#d26a5f'
  inverse-primary: '#ffb4aa'
  secondary: '#465f88'
  on-secondary: '#ffffff'
  secondary-container: '#b6d0ff'
  on-secondary-container: '#3f5881'
  tertiary: '#110a00'
  on-tertiary: '#ffffff'
  tertiary-container: '#2e1f00'
  on-tertiary-container: '#a68440'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#7e2b23'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#aec7f6'
  on-secondary-fixed: '#001b3d'
  on-secondary-fixed-variant: '#2d476f'
  tertiary-fixed: '#ffdea5'
  tertiary-fixed-dim: '#e9c176'
  on-tertiary-fixed: '#261900'
  on-tertiary-fixed-variant: '#5d4201'
  background: '#fcf9f0'
  on-background: '#1c1c17'
  surface-variant: '#e5e2da'
typography:
  display-lg:
    fontFamily: notoSerif
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  base: 8px
  margin-page: 64px
  gutter: 24px
  section-gap: 128px
  grid-max-width: 1200px
---

## Brand & Style

This design system is engineered to evoke the gravitas of a centuries-old institution while maintaining the effortless clarity of modern digital standards. The brand personality is authoritative, intellectual, and exclusive, catering to a target audience of high-achieving scholars, distinguished faculty, and significant patrons. 

The style utilizes a **Modern-Traditionalist** approach. It borrows from Minimalism's use of generous whitespace and structural clarity, but incorporates Tactile elements—such as subtle textures reminiscent of heavy-stock paper and refined hairline borders—to suggest physical permanence. The UI should feel like a digital extension of a physical campus: marble halls, leather-bound volumes, and quiet, focused study environments. Every interaction is designed to feel "weighted," eschewing transient animations for deliberate, meaningful transitions.

## Colors

The palette is rooted in classical academia. The primary color, a Deep Burgundy, is used for core brand moments and primary actions to signify passion and power. Navy serves as the secondary anchor, providing a stabilizing, professional contrast for navigation and secondary UI elements. 

Parchment acts as the canvas for the entire system, replacing stark white to reduce eye strain and provide a "literary" feel. Gold is reserved for accents—honors, distinctions, and subtle highlights—representing excellence. Neutral grays are used sparingly, leaning into warm or cool tints derived from the primary and secondary colors to maintain a cohesive atmospheric temperature.

## Typography

Typography in this design system is the primary vehicle for prestige. The headlines utilize **notoSerif**, chosen for its timeless serif structure and high-contrast strokes that mirror traditional lithography. These should be set with generous leading to ensure an unhurried reading experience.

For utilitarian content, **inter** provides a clean, neutral balance. It ensures that complex information—such as course catalogs or financial data—remains highly legible and accessible. Labels and small metadata should be set in uppercase with increased letter-spacing to mimic the look of engraved plaques or architectural signage.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to mirror the structured nature of a printed manuscript or academic journal. Content is centered within a generous 1200px container, flanked by substantial margins that act as "breathing room" for the intellect.

A 12-column grid is used for internal page composition, but elements should frequently span multiple columns to maintain a sense of monumental scale. Spacing is governed by an 8px base unit, though the system favors "Macro-Spacing"—using large gaps between sections to signify a transition in thought or topic. Alignment must be rigorous; every element should feel anchored to a visible or invisible structural line.

## Elevation & Depth

In this design system, depth is communicated through **Tonal Layering and Refined Outlines** rather than aggressive shadows. Surfaces are distinguished by subtle value shifts—for example, a secondary container might be a slightly lighter or darker tint of Parchment.

Where shadows are used, they are "Ambient Shadows": extremely low opacity, wide blur radius, and tinted with the primary Burgundy or Navy to ensure they feel like part of the environment. Borders are the primary tool for hierarchy; 1px "Hairline" rules in Navy or Gold create a sense of containment and meticulous craft. Interactive states should feel like a physical depression or a subtle change in "ink" density rather than a floating effect.

## Shapes

The shape language is strictly **Sharp (0px)**. Roundness is perceived as too casual or modern for an institution of this stature. Right angles communicate stability, discipline, and architectural permanence. 

All buttons, cards, input fields, and containers must utilize perfectly square corners. This rigidity creates a "frame" effect for the content, focusing the user's attention on the elegant typography and rich color palette. Visual interest is generated through the proportion of these rectangles rather than the softening of their edges.

## Components

### Buttons
Primary buttons are solid Deep Burgundy with Gold or White text, utilizing a deliberate hover state that shifts to a slightly darker shade. Secondary buttons use a Navy "Ghost" style with a 1px border. All buttons have a minimum height of 48px to ensure a weighted, physical presence.

### Input Fields
Fields are characterized by a 1px bottom-border or a very thin perimeter border. Labels remain static or use a subtle "float" that maintains uppercase styling. The focus state is signaled by the border color shifting to Burgundy or Navy, never a neon glow.

### Cards
Cards are defined by their internal padding and a 1px Navy rule. They do not use shadows. The header of a card often uses a thin horizontal line to separate the title from the body content, mimicking academic formatting.

### Navigation
The main navigation should be prominent, using Noto Serif for top-level links. It acts as a lintel for the page, providing a sense of entry into the portal.

### Additional Components
- **The Seal:** A decorative brand mark used for certification or high-level section breaks.
- **The Rule:** An ornamental horizontal divider, sometimes featuring a small Gold diamond or crest in the center.
- **Status Badges:** Small, sharp-edged chips in muted academic tones (e.g., Forest Green for "Accepted", Slate for "Pending").