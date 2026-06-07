---
name: Kinetic Grid
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
  on-surface-variant: '#5a4136'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#8e7164'
  outline-variant: '#e2bfb0'
  surface-tint: '#a04100'
  primary: '#a04100'
  on-primary: '#ffffff'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#ffb693'
  secondary: '#465f88'
  on-secondary: '#ffffff'
  secondary-container: '#b6d0ff'
  on-secondary-container: '#3f5881'
  tertiary: '#5b5f62'
  on-tertiary: '#ffffff'
  tertiary-container: '#95999c'
  on-tertiary-container: '#2d3134'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#aec7f6'
  on-secondary-fixed: '#001b3d'
  on-secondary-fixed-variant: '#2d476f'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c3c7ca'
  on-tertiary-fixed: '#181c1e'
  on-tertiary-fixed-variant: '#43474a'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style

This design system is built for the high-velocity world of startup incubation. The brand personality is ambitious, authoritative, and friction-less. It targets founders who need information quickly and mentors who require structured engagement. 

The aesthetic is a fusion of **Corporate Modern** and **High-Contrast Bold**. It leverages a "Bento-box" layout strategy to compartmentalize complex data—schedules, directories, and resources—into digestible, interactive modules. The emotional response should be one of "readiness to build": organized enough to be professional, but vibrant enough to feel like a high-energy workspace.

## Colors

The palette is driven by the tension between Vibrant Orange and Navy. Orange acts as the "action" color, reserved for primary CTAs, progress indicators, and highlight states. Navy provides the structural foundation, used for deep backgrounds, headers, and primary text to ensure the system feels grounded and institutional. 

A "Tertiary" cool gray (#F4F7FA) is utilized to define the Bento-box containers against the pure White background, creating a subtle layer of depth without relying on heavy shadows.

## Typography

This design system utilizes **Inter** exclusively to maintain a utilitarian, high-performance feel. Energy is injected through aggressive weight distribution—using "Extra Bold" for displays and "Bold" for section headers. 

Tight letter-spacing is applied to larger headlines to create a "compact" and modern editorial look. For mobile density, labels are often uppercase and bolded to remain legible at small sizes within crowded directory lists or schedule blocks.

## Layout & Spacing

The layout follows a **Strict Modular Grid (Bento-style)**. Content is housed in containers that snap to a 12-column grid on desktop and a 2-column grid on mobile. 

Spacing is governed by an 8px rhythm. To achieve the "Bento-box" look, use consistent 16px gutters between all modules. On mobile, padding inside modules is reduced to 12px (sm) to maximize information density, allowing users to see multiple schedule items or directory names without excessive scrolling.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and **Low-contrast Outlines** rather than traditional shadows. This maintains the high-energy, "flat" startup aesthetic.

- **Level 0 (Background):** Pure White (#FFFFFF).
- **Level 1 (Bento Modules):** Tertiary Gray (#F4F7FA) or Navy (#002147) for high-impact blocks.
- **Level 2 (Active States):** A 1px solid border using Navy at 10% opacity for light cards, or Orange for active focus.

Shadows are used sparingly, only on floating action buttons (FABs) or dropdown menus, using a very tight, 4px blur with 5% opacity Navy to prevent "muddiness."

## Shapes

This design system uses a **Rounded** shape language to balance the "Navy" corporate feel with "Orange" energy. Modules and primary containers use a 1rem (16px) corner radius. This significant rounding helps the Bento-box layout feel approachable and modern rather than industrial. Small components like tags, input fields, and "Quick Action" buttons use a 0.5rem (8px) radius to maintain precision.

## Components

### Buttons
Primary buttons are solid Vibrant Orange with White bold text. Secondary buttons use the Navy outline with a 2px stroke. Interaction states should involve a slight scale-up (1.02x) to reinforce the "High-Energy" theme.

### Bento Cards
The core of the system. Cards must have a consistent 16px internal padding. They can have different background fills (Navy, Orange, or Light Gray) depending on the content priority. Headline text within cards should never exceed 2 lines.

### High-Density Lists (Mobile)
For schedules and directories, use a "tight-row" format: 48px height minimum for touch targets, 12px horizontal padding, and a 1px divider. Use small, high-contrast avatars for the directory to add visual energy without wasting space.

### Chips & Tags
Used for "Industry" or "Stage" filters. These should be semi-pill-shaped with Navy text on a 10% Navy opacity background to keep the interface from becoming visually cluttered with too many colors.

### Status Indicators
Use small, glowing dots (CSS animation) for "Live" events or "Available" mentors to contribute to the "Collaborative" atmosphere.