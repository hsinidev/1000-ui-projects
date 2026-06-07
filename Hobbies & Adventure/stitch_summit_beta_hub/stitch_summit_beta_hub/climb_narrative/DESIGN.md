---
name: Climb Narrative
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c9ac'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9379'
  outline-variant: '#444933'
  surface-tint: '#abd600'
  primary: '#ffffff'
  on-primary: '#283500'
  primary-container: '#c3f400'
  on-primary-container: '#556d00'
  inverse-primary: '#506600'
  secondary: '#ffb59c'
  on-secondary: '#5c1900'
  secondary-container: '#fa5c1c'
  on-secondary-container: '#511500'
  tertiary: '#ffffff'
  on-tertiary: '#2f3131'
  tertiary-container: '#e2e2e2'
  on-tertiary-container: '#636565'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c3f400'
  primary-fixed-dim: '#abd600'
  on-primary-fixed: '#161e00'
  on-primary-fixed-variant: '#3c4d00'
  secondary-fixed: '#ffdbcf'
  secondary-fixed-dim: '#ffb59c'
  on-secondary-fixed: '#390c00'
  on-secondary-fixed-variant: '#832700'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  button:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  base: 8px
  gutter: 24px
  margin-page: 40px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system targets an audience of high-performance athletes and outdoor enthusiasts who value technical precision and raw energy. The aesthetic is rooted in a mix of **Brutalism** and **High-Contrast Modernism**, reflecting the physical grit of rock climbing through a digital lens. 

The brand personality is aggressive, reliable, and unapologetic. It avoids soft gradients and rounded corners in favor of a "carved" look that mimics the sheer faces of a cliff. The UI should evoke a sense of adrenaline and focus, utilizing high-density layouts and stark visual departures between surface and accent. Subtle noise overlays and monochromatic topographical line-art should be used sparingly in backgrounds to ground the industrial elements in the natural world.

## Colors

The palette is anchored by **Granite Grey** and **Chalk White**, providing a high-contrast foundation that ensures maximum readability in high-glare outdoor environments. 

- **Granite Grey (#333333)**: The primary surface color, acting as the "rock" upon which all elements are built.
- **Chalk White (#F5F5F5)**: Used for primary body text and high-visibility icons, providing a clean, utilitarian contrast.
- **Neon Green (#CCFF00)**: The "Action" color. Reserved for primary CTAs, success states, and critical navigation paths. It represents growth and safety.
- **Neon Orange (#FF5F1F)**: The "Energy" color. Used for warnings, interactive highlights, and status indicators like "Current Difficulty" or "Live Occupancy."

A deeper black (#1A1A1A) is used for background layers to provide depth behind the Granite Grey surfaces.

## Typography

This design system utilizes a dual-font strategy to balance technical industrialism with athletic readability.

- **Headlines (Space Grotesk)**: Chosen for its geometric, slightly eccentric terminal strokes that feel engineered and precise. All major headings should be set in Bold or Medium weights with tight letter spacing to create a high-impact, "poster-like" feel.
- **Body & Interface (Lexend)**: Designed specifically for readability and athletic contexts. Its generous spacing and clear character definitions ensure that data (like climbing grades or weather conditions) is digestible at a glance.
- **Data Labels**: Use Space Grotesk in all-caps for labels and metadata to maintain a technical, "instrument cluster" appearance.

## Layout & Spacing

The layout philosophy follows a **Fixed-Grid System** within a 12-column container for desktop and a 4-column container for mobile. 

Spacing is governed by an 8px rhythmic scale, but emphasis is placed on "negative tension"—using large gaps (64px+) between sections to allow the high-contrast elements room to breathe. Components should be stacked with tight vertical rhythm (16px or 32px) to emphasize the verticality of the sport. Padding within containers should be generous to ensure that "Chalk White" text never feels cramped against "Granite Grey" edges.

## Elevation & Depth

In line with the rugged, industrial theme, this design system rejects soft shadows and ambient blurs. Depth is achieved through **Tonal Layers** and **Hard Strokes**.

- **Surfaces**: The base background is the darkest shade, with cards and containers using Granite Grey (#333333).
- **Hard Borders**: Instead of shadows, use 1px or 2px solid strokes in Chalk White (at 10% opacity) or Neon accents to define edges.
- **Inverted Layers**: For interactive elements, use "Negative Space" elevation where the element appears cut out of the surface, achieved through darker inner borders.
- **Overlays**: Any modal or overlay must be 100% opaque or use a very subtle grain texture; avoid soft glassmorphism.

## Shapes

The shape language is strictly **Sharp (0px)**. There are no rounded corners in this design system. 

Every button, input field, card, and image container must have 90-degree angles. This reinforces the "industrial" and "rugged" brand pillars, suggesting stability and uncompromising strength. For specific decorative elements, 45-degree chamfered corners (clipped corners) may be used to evoke technical gear and carabiner designs, but the default state is always a hard rectangle.

## Components

- **Buttons**: Rectangular with no radius. Primary buttons use a Neon Green fill with black text. Secondary buttons use a Granite Grey fill with a 2px Neon Orange stroke. Hover states should "invert"—the fill swaps with the border color.
- **Chips/Badges**: Small, sharp-edged tags used for climbing grades (e.g., V5, 5.12a). Use Neon Orange for high difficulty and Neon Green for beginner/intermediate.
- **Input Fields**: Chalk White 1px bottom-border only, or full Granite Grey boxes with no border. Placeholder text should be low-opacity Chalk White. Focus state triggers a 2px Neon Green border.
- **Cards**: Large, blocky containers with a subtle "rock texture" background image at 5% opacity. Headers within cards should use the "Label-Caps" typography style.
- **Progress Bars/Metrics**: Use thick, chunky bars. The "track" is Granite Grey, and the "fill" is Neon Green. No rounded caps on the bars.
- **Specialized Component - "The Grade Scale"**: A vertical or horizontal stepped component that highlights the difficulty of a climb, using the Neon Orange to indicate the specific grade on a spectrum.