---
name: WealthLogic
colors:
  surface: '#fcf9f5'
  surface-dim: '#dcdad6'
  surface-bright: '#fcf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f0'
  surface-container: '#f0edea'
  surface-container-high: '#eae8e4'
  surface-container-highest: '#e5e2df'
  on-surface: '#1b1c1a'
  on-surface-variant: '#434843'
  inverse-surface: '#30302e'
  inverse-on-surface: '#f3f0ed'
  outline: '#737973'
  outline-variant: '#c3c8c1'
  surface-tint: '#4d6453'
  primary: '#061b0e'
  on-primary: '#ffffff'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#b4cdb8'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#161817'
  on-tertiary: '#ffffff'
  tertiary-container: '#2a2c2b'
  on-tertiary-container: '#929392'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e3e1'
  tertiary-fixed-dim: '#c6c7c5'
  on-tertiary-fixed: '#1a1c1b'
  on-tertiary-fixed-variant: '#454746'
  background: '#fcf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e5e2df'
typography:
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-lg:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
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
  gutter: 24px
  margin: 48px
  container-max-width: 1280px
---

## Brand & Style

The design system is anchored in the concept of "Quiet Luxury"—a philosophy that prioritizes substance, stability, and intelligence over flashy trends. It targets high-net-worth individuals and institutional users who demand the precision of AI with the gravitas of traditional private banking. 

The visual style is a blend of **Minimalism** and **Modern Corporate**. It utilizes generous whitespace to create a sense of calm and clarity, while the "sturdy" aesthetic is reinforced through structured grids and intentional alignment. The emotional response is one of absolute security and sophisticated guidance; the UI feels less like a software tool and more like a high-end digital concierge.

## Colors

The palette is derived from classic symbols of wealth and endurance. **Forest Green** serves as the primary anchor, representing growth and institutional permanence. **Gold** is used sparingly as a high-contrast accent for interactive elements, status indicators, and premium call-to-actions, signaling value and achievement. 

The foundation is an **Off-White** canvas, which softens the visual experience and prevents the high-contrast green from feeling overly aggressive. For text and UI borders, a deep neutral charcoal is employed to maintain legibility without the harshness of pure black. Semantic colors (success, error, warning) should be desaturated to match the earthy, sophisticated tone of the primary palette.

## Typography

This design system employs a dual-font strategy to balance authority with modern utility. **Noto Serif** is reserved for headlines and editorial moments; its classic proportions convey the "sturdy" and "authoritative" nature of wealth management. It should be used to ground the page and guide the user's eye to key sections.

**Manrope** is used for all body text, data visualizations, and interface labels. Its geometric yet refined construction ensures that complex financial data remains legible and accessible. Large numerical values and AI-generated insights should utilize the medium or semi-bold weights of Manrope to stand out within the layout.

## Layout & Spacing

The layout utilizes a **Fixed Grid** system to establish a sense of architectural permanence. A 12-column grid is standard for desktop views, with wide margins and generous gutters to prevent information density from feeling overwhelming. 

The spacing rhythm is built on an 8px base unit. Component internal padding should favor larger values (e.g., 24px or 32px) to reinforce the high-end, spacious feel. Sections of content are separated by significant vertical whitespace to allow the "Off-White" background to act as a visual breather, emphasizing the quality of the data presented.

## Elevation & Depth

Depth in this design system is communicated through **Tonal Layers** and **Ambient Shadows**. Surfaces do not "float" aggressively; instead, they sit with a heavy, grounded presence. 

Shadows are exceptionally soft, using a multi-layered approach with very low opacity (3-5%) and a slight color tint derived from the Forest Green primary color (#1B3022). This creates a "natural" depth that feels like physical paper or cardstock. Refined, 1px borders in a desaturated version of the primary green or a light gold are used to define boundaries without relying solely on shadows, maintaining a clean, structured appearance.

## Shapes

To support the "sturdy" and "sophisticated" narrative, this design system uses **Soft** roundedness. A radius of 0.25rem (4px) is the standard for most interactive elements like buttons and input fields, providing a slight hint of modern approachability without losing the rigor of a traditional financial institution. 

Larger containers and cards may use `rounded-lg` (8px) to soften the overall composition, but the system generally avoids pill shapes or high-radius curves, which can feel too casual for wealth management.

## Components

### Buttons
Primary buttons are solid Forest Green with Gold text or high-contrast White. They feature subtle 1px Gold borders on hover to indicate interactivity. Secondary buttons use a "Ghost" style—a thin Forest Green border with an Off-White background.

### Cards
Cards are the primary vessel for AI insights. They should have a pure White or very light gray background, a 1px border (#E5E5E1), and the signature soft ambient shadow. Headline serif text within cards should be centered or left-aligned with ample padding.

### Input Fields
Inputs are minimalist, featuring only a bottom border or a very light 4-sided stroke. On focus, the border transitions to Gold. Labels use the `label-sm` Manrope style in all-caps with increased letter spacing for a premium, technical feel.

### Data Displays & Chips
Financial metrics and AI tags use small, rectangular chips with solid Forest Green backgrounds and Gold text. Data visualizations (charts/graphs) should prioritize Forest Green and Gold as the primary data points, using desaturated neutrals for secondary axes and grids.

### Lists
Transaction and portfolio lists use horizontal dividers with 0.5px thickness in a soft neutral. Hover states should subtly darken the background color of the row rather than changing the border, maintaining the horizontal flow of the page.