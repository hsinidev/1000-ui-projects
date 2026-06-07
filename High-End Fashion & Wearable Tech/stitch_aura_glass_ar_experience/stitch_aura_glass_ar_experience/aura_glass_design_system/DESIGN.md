---
name: Aura-Glass Design System
colors:
  surface: '#0b112e'
  surface-dim: '#0b112e'
  surface-bright: '#323756'
  surface-container-lowest: '#060b29'
  surface-container-low: '#141937'
  surface-container: '#181d3b'
  surface-container-high: '#232846'
  surface-container-highest: '#2e3352'
  on-surface: '#dee0ff'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dee0ff'
  inverse-on-surface: '#292e4d'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c1c4e6'
  on-secondary: '#2b2f49'
  secondary-container: '#414561'
  on-secondary-container: '#b0b3d4'
  tertiary: '#f7f8f8'
  on-tertiary: '#2f3131'
  tertiary-container: '#dbdbdb'
  on-tertiary-container: '#5e6060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#dee0ff'
  secondary-fixed-dim: '#c1c4e6'
  on-secondary-fixed: '#161a33'
  on-secondary-fixed-variant: '#414561'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0b112e'
  on-background: '#dee0ff'
  surface-variant: '#2e3352'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  data-mono:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  label-caps:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.2em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  safe-zone: 40px
  gutter: 16px
  component-gap: 8px
  hud-margin: 24px
---

## Brand & Style

This design system embodies "Futuristic-Chic," a fusion of high-fashion luxury and advanced spatial computing. The brand personality is sophisticated, precise, and visionary. It targets an affluent, tech-forward demographic that values both aesthetic elegance and technical performance. 

The UI follows a **Heads-Up Display (HUD)** glassmorphism style. It relies on extreme clarity, semi-transparent layered surfaces, and "light-as-air" visual weight to ensure the digital overlay enhances rather than obstructs the user's view of the physical world. The emotional response should be one of "effortless intelligence"—feeling like a high-end instrument that is both powerful and beautiful.

## Colors

The palette is anchored by **Deep Indigo (#0A0E27)**, which serves as the base for all optical overlays, providing necessary contrast for legibility in various lighting conditions. **Cyan Glow (#00F2FF)** is the primary functional color, used for data visualizations, active states, and "light-emissive" accents. **Crisp White (#FFFFFF)** is reserved for high-priority text and iconography to ensure maximum readability.

The system uses a dark default mode to minimize eye strain during AR projection. Use semi-transparent variants of the Indigo base (ranging from 40% to 80% opacity) to create the glassmorphic background layers.

## Typography

Typography is a mix of geometric modernism and technical precision. **Space Grotesk** is used for large headings to convey a futuristic, avant-garde feel. **Inter** handles all primary body copy for its exceptional legibility in transparent environments. 

For HUD-specific elements like coordinates, battery levels, and sensor data, **Space Mono** is utilized. All mono labels should be rendered in uppercase with generous letter spacing to mimic high-end technical instrumentation.

## Layout & Spacing

The layout philosophy follows a **Dynamic Safe-Area** model. Because this is an AR interface, content is weighted toward the periphery to keep the central field of view clear. 

We utilize an 8-column fluid grid for secondary menus, but primary HUD elements (like time or notifications) are anchored to the corners with a fixed 24px "HUD margin." Spacing follows a 4px base unit to maintain technical precision. Elements should feel "airy," with significant negative space between glass panels to prevent visual clutter.

## Elevation & Depth

Depth is conveyed through **Glassmorphism and Z-axis layering** rather than traditional shadows. 
1.  **Base Layer:** 40% opacity Deep Indigo with a 20px background blur.
2.  **Active Layer:** 60% opacity Deep Indigo with a 40px background blur and a 1px inner border of 20% White.
3.  **Floating Elements:** Elements "glow" into existence. Use a 0px spread, 8px blur outer glow in Cyan (#00F2FF) at 30% opacity for primary call-to-actions.

Avoid drop shadows. Use "inner glows" and "rim lighting" (thin 1px borders) to define the edges of surfaces against the real-world background.

## Shapes

The shape language is "Technical-Soft." While we use a **Soft (0.25rem)** base radius for standard containers to keep the look fashionable and approachable, we incorporate "clipped corners" or 45-degree angled accents on the outer edges of the primary HUD frame to reinforce the high-tech aesthetic. 

Borders must remain ultra-thin (1px) to maintain the "etched in glass" feel. Larger containers should feel like precision-cut crystal slabs.

## Components

**Buttons:** Primarily ghost-style with 1px Cyan borders. On hover, the background fills with a 10% Cyan tint and the border-glow intensifies. Text is always uppercase Space Mono.

**Chips/Tags:** Used for "System Status" indicators. These feature a small "pulse" dot icon next to the label to indicate real-time data streaming.

**Lists:** Items are separated by 1px Indigo-tinted dividers at 20% opacity. No containers around list items unless they are selected; selection triggers a full-width Cyan "scan-line" highlight.

**Input Fields:** Bottom-border only. When focused, the bottom border glows Cyan and a faint vertical "cursor" line appears at the edge of the field.

**Cards:** Semi-transparent glass panels with "bracket" corners—decorative L-shaped lines in the corners that frame the content, emphasizing the HUD feel.

**Additional HUD Elements:** 
- **Reticles:** Circular or crosshair-style focus points in Cyan.
- **Scanning Bars:** A horizontal 1px line that periodically moves down active glass panels to simulate "real-time processing."