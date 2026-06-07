---
name: Organic Minimalist
colors:
  surface: '#f5fbf3'
  surface-dim: '#d6dcd4'
  surface-bright: '#f5fbf3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff5ed'
  surface-container: '#eaefe8'
  surface-container-high: '#e4eae2'
  surface-container-highest: '#dee4dd'
  on-surface: '#171d18'
  on-surface-variant: '#434843'
  inverse-surface: '#2c322d'
  inverse-on-surface: '#edf2eb'
  outline: '#737872'
  outline-variant: '#c3c8c1'
  surface-tint: '#506354'
  primary: '#334537'
  on-primary: '#ffffff'
  primary-container: '#4a5d4e'
  on-primary-container: '#c0d5c2'
  inverse-primary: '#b7ccb9'
  secondary: '#725a41'
  on-secondary: '#ffffff'
  secondary-container: '#ffdcbd'
  on-secondary-container: '#796046'
  tertiary: '#42413d'
  on-tertiary: '#ffffff'
  tertiary-container: '#5a5954'
  on-tertiary-container: '#d2cfc9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8d5'
  primary-fixed-dim: '#b7ccb9'
  on-primary-fixed: '#0e1f13'
  on-primary-fixed-variant: '#394b3d'
  secondary-fixed: '#ffdcbd'
  secondary-fixed-dim: '#e1c1a2'
  on-secondary-fixed: '#291805'
  on-secondary-fixed-variant: '#59422b'
  tertiary-fixed: '#e5e2db'
  tertiary-fixed-dim: '#c9c6c0'
  on-tertiary-fixed: '#1c1c18'
  on-tertiary-fixed-variant: '#474742'
  background: '#f5fbf3'
  on-background: '#171d18'
  surface-variant: '#dee4dd'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
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
  margin-desktop: 64px
---

## Brand & Style

This design system is built for the intentional dweller. The brand personality is **grounded, sustainable, and serene**, evoking the feeling of a quiet morning in a forest clearing. It targets environmentally conscious individuals seeking freedom through architectural efficiency.

The design style is a blend of **Organic Minimalism** and **Tactile Functionalism**. It prioritizes heavy whitespace to reflect the 'minimalist' lifestyle and utilizes high-quality photography where the architecture interacts with natural environments. UI elements feel like physical objects—smoothly sanded wood and soft fabrics—rather than cold digital components. The interface remains functional and "invisible," allowing the tiny homes to be the focal point.

## Colors

The palette is derived from the natural world to create an immediate sense of sustainability.

- **Primary (Moss Green):** Used for primary actions and brand presence. It represents growth and environmental stewardship.
- **Secondary (Warm Oak):** A tactile accent used for highlights, interactive elements, and providing a sense of warmth against the cooler greens.
- **Tertiary (Sand/Bone):** A soft off-white used for container backgrounds to reduce the harshness of pure white while maintaining a clean aesthetic.
- **Neutral:** A deep, desaturated charcoal-green used for body text to ensure high legibility without the starkness of pure black.
- **Background (Crisp White):** The canvas of the system, providing the "breathable" space essential to the minimalist narrative.

## Typography

This design system employs a sophisticated typographic pairing to balance heritage with modernity. 

**Noto Serif** is used for all headings. Its classic proportions feel grounded and literary, conveying the "home" aspect of the product. **Inter** is the functional workhorse for all UI elements, body copy, and data-heavy inputs. It provides the "modern" and "clean" clarity required for technical specifications and marketplace navigation. Large headlines should use tighter tracking, while labels benefit from subtle letter-spacing to improve scanability at small sizes.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy on desktop to ensure content feels contained and "composed," much like a tiny house floor plan. A 12-column grid is utilized with generous 24px gutters.

The spacing rhythm is based on an 8px base unit. To reflect the minimalist lifestyle, vertical padding should be aggressive—allowing sections to breathe. Elements should be grouped tightly when functionally related but separated by significant "white space" to prevent visual clutter. Margin-heavy layouts are preferred over border-heavy ones.

## Elevation & Depth

Depth in this design system is achieved through **Ambient Shadows** and **Tonal Layering**. 

Shadows are extremely soft, with a large blur radius and low opacity (approx. 4-8%), often tinted with a hint of Moss Green to feel organic rather than synthetic. This mimics the way natural light hits a surface. 

- **Level 0:** Base surface (Crisp White).
- **Level 1:** Secondary containers (Tertiary Sand color) with no shadow.
- **Level 2:** Floating cards and interactive inputs with a subtle ambient shadow.
- **Level 3:** Overlays and Modals with a deeper, more diffused shadow to focus attention.

Avoid harsh outlines; use subtle color shifts in backgrounds to define boundaries.

## Shapes

The shape language is **Rounded**, reflecting the soft edges of natural materials and ergonomic furniture. 

Standard components (buttons, inputs) use a 0.5rem radius. Large cards and "exploded-view" containers use a 1rem radius to feel approachable. Photography should also feature rounded corners to integrate seamlessly with the UI. The use of circles is reserved for avatars and specific status indicators to maintain a balanced, structured appearance without becoming overly "bubbly."

## Components

- **Buttons:** Primary buttons use the Moss Green background with white text. Secondary buttons use a "Warm Oak" ghost style with a subtle 1px border. 
- **Exploded-View Containers:** Used for architectural diagrams. These containers feature a Tertiary background and dashed Moss Green lines to connect labels to specific parts of a diagram.
- **Interactive Calculators:** Inputs are large and tactile with clear 16px padding. Active states are indicated by a 2px "Warm Oak" bottom border rather than a full-box glow.
- **Minimalist Navigation:** A simple, center-aligned text menu with high tracking and no background container. Scroll-triggered transitions should make the nav background blur slightly over content.
- **Cards:** Houses are displayed in cards with full-bleed photography at the top. Descriptions are brief, prioritizing "Body-LG" typography for price and location.
- **Chips/Tags:** Used for sustainability certifications (e.g., "Solar Powered"). These are pill-shaped with a light tint of the Primary color and small icons.