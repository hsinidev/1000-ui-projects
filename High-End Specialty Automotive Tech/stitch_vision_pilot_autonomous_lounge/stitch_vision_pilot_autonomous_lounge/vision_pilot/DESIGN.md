---
name: Vision-Pilot
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#4a463e'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#7b776d'
  outline-variant: '#ccc6bb'
  surface-tint: '#645e50'
  primary: '#645e50'
  on-primary: '#ffffff'
  primary-container: '#f4ebd9'
  on-primary-container: '#706a5b'
  inverse-primary: '#cec6b5'
  secondary: '#9d4228'
  on-secondary: '#ffffff'
  secondary-container: '#fd8c6b'
  on-secondary-container: '#74240c'
  tertiary: '#465f88'
  on-tertiary: '#ffffff'
  tertiary-container: '#e4ecff'
  on-tertiary-container: '#526b95'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#eae2d0'
  primary-fixed-dim: '#cec6b5'
  on-primary-fixed: '#1f1b10'
  on-primary-fixed-variant: '#4b4639'
  secondary-fixed: '#ffdbd1'
  secondary-fixed-dim: '#ffb5a0'
  on-secondary-fixed: '#3b0900'
  on-secondary-fixed-variant: '#7e2c13'
  tertiary-fixed: '#d6e3ff'
  tertiary-fixed-dim: '#aec7f6'
  on-tertiary-fixed: '#001b3d'
  on-tertiary-fixed-variant: '#2d476f'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  display-md:
    fontFamily: Metropolis
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  headline-lg:
    fontFamily: Metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0.03em
  headline-sm:
    fontFamily: Metropolis
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.15em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  margin-page: 64px
  gutter-grid: 32px
  padding-card: 24px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system is engineered for the sanctuary of a Level 4 autonomous vehicle—a transition from a cockpit to a mobile lounge. The brand personality is "Architectural-Chic," blending the permanence of modern interior design with the fluidity of motion. It targets high-net-worth individuals who value serenity, spatial awareness, and "Social-First" interaction models that prioritize passenger-to-passenger engagement over driver-to-road focus.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**, specifically curated to mimic a high-end architectural interior. It utilizes wide margins and soft-shadowed planes to create a sense of physical depth within the digital interface. The emotional response is one of calm confidence; the UI does not demand attention but remains elegantly available, much like a well-placed piece of designer furniture.

## Colors

The palette is derived from natural, tactile materials used in premium architecture. **Sand (#F4EBD9)** serves as the primary canvas, providing a warm, non-glare foundation that feels more like a textured wall than a digital screen. **Navy Blue (#002147)** is used for high-contrast typography and structural elements, ensuring legibility against the light background. 

**Terracotta (#D36B4D)** is the active accent, reserved for interactive states, notifications, and points of interest. For AR overlays and glass elements, use a semi-transparent white with high background blur to maintain the "Social-First" transparency, allowing the interior of the vehicle to bleed into the interface.

## Typography

This design system utilizes **Metropolis** for its geometric precision and architectural rhythm. The type scale is characterized by high contrast between massive display headings and functional body text. 

To achieve the "sophisticated" look, all headings must employ generous letter spacing (tracking), particularly in uppercase label styles. For mobile or smaller seat-back displays, use `headline-sm` in place of `display-lg` to maintain hierarchy without overwhelming the narrow viewport. Text color should predominantly be Navy Blue, with Terracotta used sparingly for calls-to-action.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** approach inspired by gallery layouts. It prioritizes "Social-First" viewing angles, meaning content is centered or biased toward passenger sightlines rather than a central dashboard.

- **Margins:** Ultra-wide 64px margins on all sides to create a "framed" effect, making the UI feel like a piece of art hanging in the lounge.
- **Grid:** A 12-column grid for widescreen lounge displays; a 4-column grid for individual passenger tablets.
- **Rhythm:** An 8px linear scale. Large interactive tiles should span multiple columns (typically 4 or 6) to ensure they are easily reachable from a reclined "lounge" position.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Glassmorphism**. Rather than traditional heavy shadows, the design system uses "Architectural Depth":

1.  **Base Layer:** The Sand (#F4EBD9) canvas, representing the "wall."
2.  **Surface Layer:** Soft-shadowed cards with a very large blur radius (40px+) and low opacity (10%), creating the illusion of panels floating slightly away from the surface.
3.  **Overlay Layer:** AR and navigation elements use a "Frosted Glass" effect—`backdrop-filter: blur(20px)` with a 70% white tint. This ensures that the vehicle's ambient lighting and movement are visible through the UI, reducing motion sickness and maintaining a connection to the environment.

## Shapes

The shape language is "Softly Geometric." While the grid is rigid and architectural, the components themselves feature a **Rounded (0.5rem to 1.5rem)** radius to mimic molded interior components like seat headrests and organic dashboard curves. 

- **Standard Tiles:** 1rem (rounded-lg) for a balanced, modern look.
- **Primary Buttons:** 1.5rem (rounded-xl) to make them feel more tactile and approachable.
- **Navigation Bars:** Often utilize a pill-shape for floating elements or sharp edges when docked to the frame of the screen.

## Components

### Large Interactive Tiles
The core of the interface. Tiles are used for route selection, media control, and climate. They feature a white surface with a 5% Navy Blue tint and a soft shadow. Icons within tiles should be "Thin-Stroke" Navy Blue.

### Glassmorphism AR Overlays
Used for "Points of Interest" labels appearing over the windows or main AR display. These must have a high-contrast Navy Blue text and a 1px white "inner-glow" border to ensure visibility against varying outdoor light conditions.

### Refined Navigation Bars
A floating bottom-docked bar. It should be semi-transparent with a glass effect. Active states are indicated by a Terracotta dot or subtle underline, avoiding heavy fills to keep the "spacious" feel.

### Buttons & Inputs
Buttons are "Social-First"—large enough for multi-user access. Primary buttons use a solid Terracotta fill with white text. Secondary buttons are ghost-style with a Navy Blue 1px border. Input fields are minimalist underlines with floating labels in uppercase `label-caps`.

### Lounge Lists
Lists used for music or destination history should have generous vertical padding (24px+) between items to prevent a "cluttered" digital look, maintaining the premium architectural aesthetic.