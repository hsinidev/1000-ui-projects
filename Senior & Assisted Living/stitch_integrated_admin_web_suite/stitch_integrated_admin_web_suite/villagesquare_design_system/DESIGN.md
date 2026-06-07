---
name: VillageSquare Design System
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#414844'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#785a00'
  on-secondary: '#ffffff'
  secondary-container: '#ffc300'
  on-secondary-container: '#6d5200'
  tertiary: '#27261a'
  on-tertiary: '#ffffff'
  tertiary-container: '#3d3c2f'
  on-tertiary-container: '#a8a695'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#ffdf9a'
  secondary-fixed-dim: '#f8be00'
  on-secondary-fixed: '#251a00'
  on-secondary-fixed-variant: '#5a4300'
  tertiary-fixed: '#e6e3d0'
  tertiary-fixed-dim: '#c9c7b5'
  on-tertiary-fixed: '#1c1c11'
  on-tertiary-fixed-variant: '#48473a'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Public Sans
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 32px
  gutter: 24px
  touch-target-min: 48px
  section-gap: 64px
---

## Brand & Style

This design system is built on the concept of the "Modern Heritage Newsletter." It evokes the warmth of a community bulletin board and the clarity of a high-end editorial magazine. The brand personality is neighborly, dependable, and vital, focusing on the active lifestyle of independent seniors. 

The visual style blends **Minimalism** with **Tactile** elements. It prioritizes clarity and ease of use without feeling clinical. By using generous whitespace and a "Digital Newsletter" layout, the interface feels familiar to those accustomed to print media, while providing the interactive benefits of a modern application. The emotional goal is to make residents feel "at home" and "informed."

## Colors

The palette is rooted in nature and optimism. 
- **Forest Green (Primary):** Used for structural elements, navigation, and primary actions to convey stability and growth.
- **Sunny Yellow (Secondary):** Used sparingly for accents, highlights, and energy-driven notifications. It acts as a visual "spark" to draw attention to interactive elements.
- **Warm White & Cream (Surface):** The background is a crisp White, but secondary containers use a soft Cream to reduce eye strain and enhance the "newsletter" feel.
- **Charcoal (Neutral):** Used for text to ensure maximum WCAG AAA contrast against light backgrounds, avoiding the harshness of pure black.

## Typography

Typography is the cornerstone of this design system’s accessibility. We use **Noto Serif** for headings to provide a traditional, authoritative, and literary feel that aids in visual hierarchy. **Public Sans** is used for body text due to its institutional clarity and neutral tone, ensuring that long-form community updates are easy to scan.

To accommodate senior users, the base font size starts at 18px. Line heights are intentionally generous to prevent lines of text from blurring together. High contrast is maintained across all levels, with bold weights used frequently for emphasis rather than color shifts alone.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop to mimic the structured columns of a newspaper, transitioning to a simplified single-column stack on mobile. 

The spacing rhythm is governed by an 8px scale, but emphasizes "loose" density. Large margins (32px+) ensure the interface never feels cramped. Every interactive element must adhere to a minimum 48px touch target to accommodate users with varying degrees of fine motor control. Use wide gutters (24px) between content cards to clearly delineate separate pieces of information.

## Elevation & Depth

This design system uses **Tonal Layers** and **Ambient Shadows** to create a sense of physical presence. 
- **Base Layer:** The primary canvas is White or Cream.
- **Card Layer:** Content "articles" sit on white cards with very soft, diffused shadows (Blur: 20px, Opacity: 5%, Color: Forest Green mixed with Neutral).
- **Floating Layer:** Only reserved for primary action buttons or critical alerts. These use a slightly tighter, more pronounced shadow to indicate they are "above" the page.

Avoid heavy blurs or complex glassmorphism, as these can be visually confusing. Depth should feel like paper stacked on a desk.

## Shapes

The shape language is **Rounded**, using a 0.5rem (8px) base radius for standard components like input fields and small cards. Larger containers, such as community highlight sections, use 1rem (16px) to appear more welcoming and soft. 

Avoid sharp 0px corners, as they appear too aggressive and technical. The "Digital Newsletter" aesthetic is reinforced by using slightly rounded containers that resemble clipped newspaper segments or stationary.

## Components

### Buttons & Targets
Buttons must be high-contrast. Primary buttons use the Forest Green background with White text. Secondary buttons use a thick 2px Forest Green border. All buttons have a minimum height of 48px and use 20px Bold Public Sans labels.

### Cards (Newsletter Style)
The primary content vehicle. Each card should have a clear Noto Serif headline, a short snippet of body text, and a clearly defined "Read More" or "Join" action. Cards use a 1px soft border or a light shadow—never both.

### Iconography (Activity, Event, Chat)
Icons are thick-stroke (2pt) and always accompanied by a text label. 
- **Activity Filter:** Use a magnifying glass or funnel icon with a clear "Filter by Interest" label.
- **Event Calendar:** A classic grid calendar icon.
- **Community Chat:** A double-speech-bubble icon.

### Input Fields
Fields must have persistent labels (no disappearing placeholder text). Use a 2px border on focus using the Sunny Yellow color to provide a high-visibility focus state.

### Chips & Tags
Used for "Activity Categories" (e.g., Gardening, Bridge, Yoga). These are pill-shaped with Forest Green text on a light Cream background, ensuring they are easy to read and tap.