---
name: Sky-Sleek
colors:
  surface: '#121316'
  surface-dim: '#121316'
  surface-bright: '#38393c'
  surface-container-lowest: '#0d0e11'
  surface-container-low: '#1a1c1e'
  surface-container: '#1f2022'
  surface-container-high: '#292a2c'
  surface-container-highest: '#343537'
  on-surface: '#e3e2e5'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e3e2e5'
  inverse-on-surface: '#2f3033'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c5c7c8'
  on-tertiary: '#2e3132'
  tertiary-container: '#1c1f20'
  on-tertiary-container: '#848688'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#121316'
  on-background: '#e3e2e5'
  surface-variant: '#343537'
typography:
  display-lg:
    fontFamily: metropolis
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: 0.15em
  headline-lg:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  headline-md:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.08em
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: jetbrainsMono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.2em
  headline-lg-mobile:
    fontFamily: metropolis
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 32px
  margin-desktop: 80px
  margin-mobile: 24px
  section-gap: 120px
---

## Brand & Style

This design system embodies the intersection of elite aerospace engineering and acoustic tranquility. The brand personality is authoritative yet understated—prioritizing the "whisper-quiet" nature of advanced aviation technology. It targets high-net-worth stakeholders and aerospace executives who value technical precision as much as aesthetic refinement.

The UI style leverages a **Minimalist-Glassmorphic** hybrid. It utilizes expansive whitespace (air) to signify luxury, while thin-line vectors and metallic accents reflect the structural integrity of aircraft components. The emotional response is one of calm confidence, safety, and cutting-edge sophistication. Every element must feel intentional, light, and aerodynamically efficient.

## Colors

The palette is anchored in a deep-space navy to provide a high-contrast foundation for technical data. Metallic Silver is used for structural elements and iconography, evoking the sheen of polished aluminum and titanium. Cloud White is reserved for critical information and high-level hierarchy, ensuring maximum legibility against the dark background.

Glassmorphism is employed through a "Sub-Zero" translucent layer style, using the Metallic Silver at low opacities to create depth without visual noise. This maintains the "whisper-quiet" aesthetic by avoiding harsh solid blocks of color in the mid-ground.

## Typography

Typography focuses on "breathable" layouts. Headlines utilize **Metropolis** for its geometric, architectural quality, paired with generous letter spacing to evoke the feeling of vast horizons. **Inter** provides a highly legible, neutral foundation for body copy and technical descriptions. 

For data-heavy engineering specs and labels, **JetBrains Mono** is introduced to signal technical precision and monospaced accuracy. All headings should be treated with light font weights (300-400) to maintain a premium, non-aggressive presence.

## Layout & Spacing

The layout follows a **Fixed-Width Adaptive Grid** with extreme internal padding. A 12-column system is used for desktop, but content is often constrained to the center 8 columns to ensure "wide margins" that suggest exclusivity. 

Breakpoints:
- **Desktop (1440px+):** 80px margins, 32px gutters.
- **Tablet (768px - 1439px):** 40px margins, 24px gutters.
- **Mobile (<768px):** 24px margins, 16px gutters.

The "rhythm of silence" is maintained by utilizing a 120px vertical gap between major sections, allowing the eye to rest and emphasizing the importance of the technical content that follows.

## Elevation & Depth

Depth in this design system is achieved through light and transparency rather than shadow. 

1.  **Base Layer:** Deep Navy Blue (#001F3F) solid.
2.  **Glass Layers:** Components like cards and navigation bars use a backdrop-blur (minimum 20px) with a subtle #C0C0C0 10% opacity fill.
3.  **Outlines:** Instead of drop shadows, surfaces are defined by 1px "Ghost Borders"—thin, Metallic Silver lines at 20% opacity. 
4.  **Z-Index Logic:** Higher-level elements (modals, tooltips) increase the backdrop blur intensity and add a faint, ultra-diffused silver glow (0px 10px 40px rgba(192, 192, 192, 0.05)) to simulate light reflecting off cold metal.

## Shapes

The shape language is "Soft-Technical." We avoid fully sharp corners to prevent a cold, aggressive feel, but keep radii small (0.25rem) to maintain a sense of machined engineering precision. 

- **Primary Components:** 0.25rem (4px) corner radius.
- **Large Glass Cards:** 0.5rem (8px) corner radius.
- **Status Indicators:** 100% (Pill) for circularity in small technical readouts.

## Components

**Buttons:**
Primary actions are ghost-style buttons with a 1px Metallic Silver border and high letter spacing. Hover states introduce a subtle glass fill. There are no heavy, solid-colored buttons to ensure the UI remains "weightless."

**Thin-Line Icons:**
Icons must be 1px stroke weight, never filled. They should be custom-drawn to represent aeronautical components (e.g., stylized wing cross-sections, sound wave oscillations, or turbine silhouettes).

**Data Visualization:**
Charts use thin, glowing lines in Cloud White against the Navy background. No fills or gradients are allowed within charts; the focus is on the purity of the data line.

**Input Fields:**
Minimalist bottom-border-only fields with floating labels in JetBrains Mono. Focus states are indicated by the border transitioning from 20% to 100% Metallic Silver opacity.

**Technical Cards:**
Used for engineering specs. These feature the Glassmorphism effect with a 1px top-left "light-source" highlight to simulate the edge of a glass cockpit display.

**Sound Scrubber/Range:**
A custom component for acoustic analysis. A thin horizontal line with a vertical 1px silver needle, prioritizing extreme precision in movement and visual feedback.