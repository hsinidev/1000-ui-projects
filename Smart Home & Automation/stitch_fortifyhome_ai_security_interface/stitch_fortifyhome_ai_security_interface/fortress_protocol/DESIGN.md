---
name: Fortress Protocol
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#373a3b'
  surface-container-lowest: '#0c0f10'
  surface-container-low: '#191c1d'
  surface-container: '#1d2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#323536'
  on-surface: '#e1e3e4'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e1e3e4'
  inverse-on-surface: '#2e3132'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#bdc8ce'
  on-secondary: '#283237'
  secondary-container: '#404b50'
  on-secondary-container: '#afbac0'
  tertiary: '#ffb4aa'
  on-tertiary: '#690003'
  tertiary-container: '#470001'
  on-tertiary-container: '#fa3d33'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#d9e4ea'
  secondary-fixed-dim: '#bdc8ce'
  on-secondary-fixed: '#131d22'
  on-secondary-fixed-variant: '#3e484d'
  tertiary-fixed: '#ffdad5'
  tertiary-fixed-dim: '#ffb4aa'
  on-tertiary-fixed: '#410001'
  on-tertiary-fixed-variant: '#930007'
  background: '#111415'
  on-background: '#e1e3e4'
  surface-variant: '#323536'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  status-display:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.03em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  margin-mobile: 20px
  gutter: 12px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
  action-height: 64px
---

## Brand & Style

The design system is engineered to evoke feelings of absolute safety, impenetrable protection, and professional-grade reliability. The target audience includes homeowners and property managers who prioritize functional clarity and rapid response over aesthetic fluff. 

The visual style is **Corporate / Modern** with a lean toward **High-Contrast Precision**. It utilizes a "Utility-First" philosophy where every pixel serves a functional purpose. The interface avoids unnecessary decorative elements, favoring a robust, industrial aesthetic that mirrors high-end security hardware. Surfaces are matte, transitions are snappy and intentional, and the overall atmosphere is one of disciplined vigilance.

## Colors

The design system employs a **Dark Mode** default to minimize eye strain during night-time monitoring and to reinforce the "night watch" metaphor. 

- **Primary (Navy Blue):** Used for the primary app environment and structural headers, providing a deep, authoritative foundation.
- **Secondary (Gunmetal):** Used for component backgrounds, cards, and secondary surfaces to create subtle depth against the navy background.
- **Tertiary (Alert Red):** Reserved exclusively for active alarms, critical errors, and "Disarm" functions. It must be used sparingly to maintain its psychological impact.
- **Neutrals:** High-contrast whites and cool grays are used for maximum text legibility and icon clarity against the dark canvases.
- **Functional Colors:** Bright green for "Secure" status and amber for "System Warning" are utilized for immediate glanceability.

## Typography

This design system utilizes **Inter** for its exceptional legibility on mobile screens and its neutral, systematic character. The type scale is biased toward larger sizes for critical status information to ensure readability in high-stress situations.

- **Headlines:** Use Bold weights to establish clear information hierarchy.
- **Status Display:** An extra-large, extra-bold style specifically for the primary system state (e.g., "ARMED", "READY").
- **Labels:** Use uppercase with increased letter spacing for technical metadata and small UI controls to maintain a professional, instrumentation-like feel.
- **Body:** Standard weight for descriptions and logs, ensuring a comfortable reading rhythm.

## Layout & Spacing

The design system uses a **Fluid Grid** based on a 4px baseline unit. The layout is optimized for one-handed operation, placing critical controls within easy reach of the thumb.

- **Margins:** A generous 20px side margin ensures content does not feel cramped against the bezel.
- **Quick-Action Grid:** A 2-column layout for primary controls (Lights, Locks, Cameras) with 12px gutters.
- **Safe Areas:** Significant vertical padding is used around status indicators to create a "focal zone" in the upper third of the screen.
- **Touch Targets:** Minimum height for action elements is 64px to accommodate rapid, high-pressure interaction.

## Elevation & Depth

To maintain a sense of "Robustness," this design system avoids soft, floating shadows. Instead, it uses **Tonal Layers** and **Low-Contrast Outlines**.

- **Level 0 (Base):** Navy Blue (#001F3F).
- **Level 1 (Cards/Sections):** Gunmetal (#2A3439).
- **Level 2 (Active Controls):** Secondary color with a 1px solid border (Light Gray at 20% opacity).
- **Indication of Depth:** Subtle inner-shadows are used on "pressed" states of large buttons to simulate a physical, tactile membrane switch.
- **Focus:** Active states are indicated by high-saturation borders rather than drop shadows, maintaining the "flat-and-sturdy" aesthetic.

## Shapes

The design system uses **Soft (0.25rem)** roundedness to strike a balance between modern software design and industrial hardware. 

- **Primary Buttons:** Utilize `rounded-lg` (0.5rem) to differentiate from the more rigid layout containers.
- **Status Shields:** Occasional use of circular or "shield" shapes for the central system status to provide a psychological anchor of protection.
- **Input Fields:** Strict 0.25rem corners to maintain the architectural feel of the grid.

## Components

- **Quick-Action Buttons:** Large, square or slightly rectangular blocks with centered icons and labels. Backgrounds use Gunmetal (#2A3439) when off, and Primary Navy or Accent Red when active.
- **Status Indicators:** High-visibility bars at the top of the screen or large central icons. They must use the functional color palette (Green, Amber, Red) for instant recognition.
- **Event Timeline (Lists):** A vertical feed of security events. Each item features a timestamp in `label-md` and a high-contrast icon indicating the event type (e.g., motion, door open).
- **Control Sliders:** Used for dimming lights or volume. Thick tracks with large, easy-to-grab handles.
- **Camera Feed Cards:** 16:9 aspect ratio containers with a subtle 1px border. Status overlays (REC, LIVE) should appear in the top-right corner using Alert Red.
- **Keypad Component:** A 3x4 grid of high-contrast digits with significant haptic feedback and "Secure" masking for PIN entry.