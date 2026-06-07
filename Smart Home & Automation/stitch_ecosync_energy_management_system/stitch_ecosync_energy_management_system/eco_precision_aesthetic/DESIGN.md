---
name: Eco-Precision Aesthetic
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
  on-surface-variant: '#42493e'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#72796e'
  outline-variant: '#c2c9bb'
  surface-tint: '#3b6934'
  primary: '#154212'
  on-primary: '#ffffff'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#a1d494'
  secondary: '#516169'
  on-secondary: '#ffffff'
  secondary-container: '#d2e2ec'
  on-secondary-container: '#55656d'
  tertiary: '#333b32'
  on-tertiary: '#ffffff'
  tertiary-container: '#4a5248'
  on-tertiary-container: '#bdc5b8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#d5e5ef'
  secondary-fixed-dim: '#b9c9d3'
  on-secondary-fixed: '#0e1d25'
  on-secondary-fixed-variant: '#3a4951'
  tertiary-fixed: '#dde5d8'
  tertiary-fixed-dim: '#c1c9bc'
  on-tertiary-fixed: '#161d15'
  on-tertiary-fixed-variant: '#41493f'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  code:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system embodies the intersection of environmental consciousness and high-performance engineering. The brand personality is authoritative yet optimistic, catering to a target audience of engineers, sustainability officers, and tech-forward consumers. 

The design style is **Minimalism with a Technical Edge**. It leverages generous whitespace to symbolize clarity and clean energy, while utilizing precise alignment and geometric rigor to evoke a sense of high-tech reliability. The emotional response should be one of "calm efficiency"—the user should feel they are interacting with a sophisticated tool that is inherently grounded in nature.

## Colors

The color palette is built on the foundation of **Forest Green (#2D5A27)**, used primarily for action states and brand-heavy elements to represent growth and sustainability. **Slate (#2F3E46)** provides a technical, grounded contrast, used for primary typography and structural UI elements.

The background is predominantly **Clean White (#FFFFFF)** to maintain a high-contrast, airy feel. A secondary neutral, a soft sage/grey, is used for subtle background divisions to prevent visual fatigue. Use the primary green sparingly for high-impact moments to maintain its significance.

## Typography

This design system utilizes a dual-font strategy to balance technicality with readability. **Space Grotesk** is used for headlines to provide a geometric, slightly futuristic character that aligns with the "tech" aspect of the aesthetic. **Inter** serves as the workhorse for body text and labels, ensuring maximum legibility across data-heavy interfaces.

Maintain tight tracking for large headlines and increased letter spacing for small caps labels. Use Slate for all primary text and Forest Green for emphasized links or interactive labels.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop (1280px max-width) to ensure precision and controlled information density. It employs a 12-column system with 24px gutters. 

The spacing rhythm is based on a **4px baseline grid**. For internal component padding, use 16px (sm) or 24px (md) to maintain the "approachable" feel. Vertical rhythm between sections should be generous (lg or xl) to emphasize the minimalist philosophy and allow the "sustainable" aesthetic room to breathe.

## Elevation & Depth

This design system uses **Ambient Shadows** and **Tonal Layers** to create depth without sacrificing its clean, technical look. Shadows should be highly diffused and soft, using a slight Slate tint (#2F3E46 at 8-12% opacity) instead of pure black to maintain color harmony.

- **Level 0 (Floor):** White or subtle grey background.
- **Level 1 (Cards/Inputs):** 1px border in a very light Slate tint or a soft, 4px-blur shadow.
- **Level 2 (Hover/Modals):** A more pronounced 12px-blur shadow to indicate interactivity or focus.

Avoid heavy gradients; depth is primarily achieved through hair-line strokes (1px) and subtle shifts in neutral values.

## Shapes

The shape language is defined by **Rounded (Level 2)** corners. Standard components like buttons and cards use an 8px radius, while larger containers or feature cards may scale up to 16px. This specific range (8-12px) is critical; it is soft enough to feel "approachable" and "organic" (referencing nature), yet sharp enough to remain "precise" and "professional."

Icons must follow a consistent **2px line-weight** with slightly rounded terminals to match the component corner radius.

## Components

### Buttons
Primary buttons use a solid Forest Green background with White text. Secondary buttons use a 1px Slate border with Slate text. Hover states should involve a subtle shift in luminosity rather than a color change.

### Cards
Cards are White with a 1px border (#E5E9EB) and a soft Level 1 shadow. Use a 12px corner radius for cards to distinguish them from smaller UI elements.

### Inputs & Selects
Inputs use a 1px Slate border at 20% opacity. Upon focus, the border transitions to Forest Green with a subtle 2px outer glow (glow color: Forest Green at 10% opacity).

### Chips & Tags
Use for filtering data. These should have a pill-shape (100px radius) to contrast against the more structured 8px radius of buttons, signaling they are metadata rather than primary actions.

### Icons
Line-art style only. Use Forest Green for icons that represent "active" energy or "green" status. Use Slate for utility icons (settings, profile, navigation). Symbols should focus on sustainability: leaves, lightning bolts, circular arrows, and solar grids.

### Data Visualization
Charts should utilize a palette derived from Forest Green, Slate, and an auxiliary Sage. Use thin lines and circular data points to maintain the technical aesthetic.