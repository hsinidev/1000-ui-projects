---
name: Kinetic Tech
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
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#0a0a0a'
  on-primary-container: '#7b7979'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#cac6c3'
  on-tertiary: '#32302f'
  tertiary-container: '#0b0a09'
  on-tertiary-container: '#7c7977'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e6e1df'
  tertiary-fixed-dim: '#cac6c3'
  on-tertiary-fixed: '#1d1b1a'
  on-tertiary-fixed-variant: '#484645'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  display-lg:
    fontFamily: spaceGrotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: spaceGrotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: spaceGrotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 64px
---

## Brand & Style

This design system is engineered for the intersection of high-end industrial design and digital fluidity. It targets a sophisticated, tech-literate audience that values precision and performance. The visual language aims to evoke a sense of "invisible power"—technology that is both robust and ethereal.

The aesthetic combines **Glassmorphism** with a **High-Contrast Dark** foundation. It leverages "liquid" motion principles to ensure transitions feel organic rather than mechanical, softening the hard edges of the hardware-focused environment. The presence of x-ray imagery and internal component visuals suggests transparency and engineering excellence. The overall emotional response should be one of quiet awe and tactile satisfaction.

## Colors

The palette is anchored in **Carbon Black**, providing a void-like depth that allows hardware products to stand out. The **Electric Blue** accent acts as a functional signal, used exclusively for interactive elements, data visualization, and "live" states.

**Silver/Chrome** is utilized for structural elements, borders, and iconography to mimic physical metallic finishes. Backgrounds should not be flat; use subtle linear gradients (45-degree angles) to simulate light hitting brushed metal or polished obsidian. Neon glows in Electric Blue must be used sparingly to highlight active states and draw the user's eye to primary touchpoints.

## Typography

The typography strategy prioritizes a technical, engineered feel. **Space Grotesk** is the choice for headers, providing a geometric and futuristic personality that remains legible at large display scales. Its idiosyncratic letterforms reinforce the "high-performance" narrative.

For body and technical data, **Geist** offers a mono-influenced clarity that feels like developer-grade precision. It is used for descriptions, specifications, and UI labels. Use wide letter-spacing on "label-caps" to create a premium, architectural feel in navigation and metadata. Headlines should always favor heavy weights (Medium to Bold) to maintain authority against the deep background.

## Layout & Spacing

The design system utilizes a **12-column fluid grid** for pedestal displays, optimized for large-format touch interaction. Generous margins (64px+) are mandatory to ensure content does not feel cramped and to maintain the "luxury showroom" aesthetic.

The rhythm is based on an **8px linear scale**. Use "XL" spacing between major sections to allow the eye to rest. For interactive zones, use tighter "MD" spacing to group related controls. In mobile/tablet orientations, the grid collapses to 4 or 6 columns, with margins reduced to 24px, while maintaining the 8px spacing increments for internal component logic.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** and light-based hierarchy rather than traditional drop shadows.

1.  **Base Layer:** Solid Carbon Black (#0A0A0A).
2.  **Surface Layer:** Semi-transparent dark grays with a 20px - 40px backdrop blur. This creates a "frosted" effect that allows background imagery to bleed through softly.
3.  **Edge Definition:** Instead of shadows, use 1px "Silver/Chrome" inner-borders with 20% opacity. This simulates the chamfered edge of a physical product.
4.  **Active Elevation:** When an element is interacted with, apply an Electric Blue "underglow"—a soft, diffused outer glow (0px 0px 15px) with a 30% opacity to suggest the element is powered on.

## Shapes

The shape language is **Technical-Soft**. The primary radius is 4px (`roundedness: 1`), providing a sharp, precise look that avoids the "playfulness" of highly rounded corners. This mimics the precision machining found in high-end electronics.

Large containers or modal overlays may use a slightly more pronounced 8px (rounded-lg) radius to differentiate from smaller UI components like buttons or input fields. Interactive buttons should never be pill-shaped; they must remain rectangular with the standard 4px radius to maintain the structural integrity of the grid.

## Components

### Buttons
Primary buttons feature a "Chrome" 1px border and a subtle glass background. Upon hover or touch, the border transitions to "Electric Blue" and triggers a faint neon glow. Text is always uppercase "label-caps" for a professional look.

### Product Cards
Cards utilize x-ray or internal component imagery as a background at 20% opacity. They feature a 1px silver border. Information is revealed using a "liquid" upward slide animation when a user approaches or touches the pedestal.

### Data Chips
Chips are small, dark-gray pills with no background blur, used for technical specs. They feature a monospaced "Geist" font to emphasize the technical nature of the specs.

### Input Fields
Fields are represented by a single silver bottom-border (underline style). When focused, the line turns Electric Blue and "glows," and the label floats upward using a smooth, eased transition.

### Interactive Overlays
Overlays use maximum glassmorphism (60% background blur) and cover the full width of the screen, creating a focused "immersive mode" for detailed product exploration.