---
name: Arboreal Stewardship
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#414844'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#0e6c4a'
  on-secondary: '#ffffff'
  secondary-container: '#a0f4c8'
  on-secondary-container: '#19724f'
  tertiary: '#411c02'
  on-tertiary: '#ffffff'
  tertiary-container: '#5c3113'
  on-tertiary-container: '#d79973'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#a0f4c8'
  secondary-fixed-dim: '#85d7ad'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdbc8'
  tertiary-fixed-dim: '#fab890'
  on-tertiary-fixed: '#321300'
  on-tertiary-fixed-variant: '#693b1d'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Work Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Work Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Work Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Newsreader
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Newsreader
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  button:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  section-gap: 80px
---

## Brand & Style

The design system is rooted in the philosophy of conservation and public service. It balances the rugged durability required for land management with the sophisticated clarity of a modern administrative tool. The aesthetic blends **Tactile Skeuomorphism** with **Minimalism**, using high-fidelity wood textures and organic patterns to ground the digital experience in the physical world of parks and recreation. 

The emotional response should be one of "Structured Serenity"—the user should feel the reliability of a government institution and the tranquility of a forest. Design elements take inspiration from nature's geometry, moving away from rigid squares toward pebble-like silhouettes and soft, flowing transitions.

## Colors

The palette is derived from a deep forest canopy. **Deep Forest Green** serves as the primary anchor for navigation and high-emphasis actions, ensuring a sturdy, authoritative presence. **Sage Green** is utilized for secondary interactions, success states, and progress indicators, providing a softer contrast that prevents the UI from feeling overly heavy.

**Off-White** acts as the primary canvas color, reducing eye strain and providing a crisp backdrop for photography. **Warm Wood tones** are reserved for decorative accents, specific call-to-action containers, and "Physical Touchpoints" (like header bars or sidebar textures) to evoke the feeling of park signage and outdoor infrastructure.

## Typography

This design system employs a sophisticated pairing to balance institutional trust with narrative warmth. **Work Sans** provides a sturdy, utilitarian foundation for headings and UI labels; its low stroke contrast ensures legibility across digital kiosks and mobile devices in high-glare outdoor environments.

**Newsreader** is used for body copy and long-form descriptions. Its literary qualities suggest a sense of history and storytelling, making park descriptions and ecological reports feel personal and engaging. All serif text should maintain generous line height (1.6) to enhance readability against off-white backgrounds.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** approach for desktop views to maintain a curated, editorial feel, transitioning to a flexible fluid model for tablet and mobile. A 12-column grid is used, but content is often centered in a "reading-width" column (8 columns wide) to keep information digestible.

Spacing is generous, favoring "air" over density to mirror the openness of public lands. Vertical rhythm is established using leaf-patterned SVG dividers that break up large sections of text, providing a thematic visual pause rather than a rigid line.

## Elevation & Depth

Hierarchy is achieved through **Tonal Layers** and subtle physical metaphors rather than intense shadows. Surfaces are stacked to look like overlapping leaves or layered earth.

1.  **Base Layer:** Off-White (#F8F9FA) canvas.
2.  **Mid Layer:** Light Sage or subtle wood-grain textures used for cards and containers, featuring a soft, 2px stroke in a slightly darker shade rather than a shadow.
3.  **Top Layer:** High-priority modals or floating action buttons use a "Deep Earth" shadow—a low-opacity, wide-blur shadow tinted with #1B4332 to make elements feel like they are floating just above the forest floor.
4.  **Inset Depth:** Input fields use a subtle inner shadow to appear carved into the surface.

## Shapes

The design system moves away from perfect circles and squares. While standard buttons use a **Rounded (0.5rem)** base, "Feature Cards" and primary "Hero Imagery" utilize **Pebble Shapes**—asymmetric border radii that mimic river stones. 

Dividers are never simple lines; they are either decorative leaf-trails or soft, undulating "horizon" curves. This organic approach softens the technical nature of the management software, making it feel more integrated with the environment it serves.

## Components

### Buttons
Primary buttons are solid Deep Forest Green with white text, featuring a subtle "wood grain" overlay at 5% opacity for texture. Hover states shift the background to a slightly lighter Sage Green. Secondary buttons use a Sage Green outline with an organic, slightly irregular stroke width.

### Cards
Cards are the primary organizational unit. They feature "Pebble" corners and a very thin, #9C6644 (Wood) border. Headers within cards may feature a small leaf icon or a wood-textured top-bar to signify different categories (e.g., Trail Data vs. Revenue).

### Input Fields
Inputs are styled with an Off-White fill and a 2px Sage Green bottom border. On focus, the border expands into a soft green glow. The corners remain rounded to match the system's "Soft" shape profile.

### Chips & Tags
Used for land designations (e.g., "National Park," "Restricted Access"). These are pill-shaped with background colors drawn from the earth-tone palette. They should feel like physical wooden or plastic trail markers.

### Leaf Dividers
Custom SVG components used to separate sections. They should be responsive, stretching the "vine" of the divider while keeping the leaf clusters at the ends fixed.

### Data Visualization
Charts and graphs should use the Forest-to-Sage gradient. Avoid harsh reds for alerts; use the Wood/Earth tones for "Caution" and Deep Forest for "Active" states.