---
name: Luxe-Layover
colors:
  surface: '#fbf8ff'
  surface-dim: '#d5d8f9'
  surface-bright: '#fbf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f2ff'
  surface-container: '#ececff'
  surface-container-high: '#e5e6ff'
  surface-container-highest: '#dee0ff'
  on-surface: '#161a32'
  on-surface-variant: '#474650'
  inverse-surface: '#2b2f48'
  inverse-on-surface: '#f0efff'
  outline: '#787681'
  outline-variant: '#c8c5d1'
  surface-tint: '#59579a'
  primary: '#59579a'
  on-primary: '#ffffff'
  primary-container: '#b8b5ff'
  on-primary-container: '#464485'
  inverse-primary: '#c3c0ff'
  secondary: '#46645f'
  on-secondary: '#ffffff'
  secondary-container: '#c8e9e2'
  on-secondary-container: '#4c6a65'
  tertiary: '#5d5e60'
  on-tertiary: '#ffffff'
  tertiary-container: '#bbbcbe'
  on-tertiary-container: '#4a4c4e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e3dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#150f53'
  on-primary-fixed-variant: '#413f80'
  secondary-fixed: '#c8e9e2'
  secondary-fixed-dim: '#adcdc7'
  on-secondary-fixed: '#01201c'
  on-secondary-fixed-variant: '#2f4c47'
  tertiary-fixed: '#e2e2e4'
  tertiary-fixed-dim: '#c6c6c8'
  on-tertiary-fixed: '#1a1c1d'
  on-tertiary-fixed-variant: '#454749'
  background: '#fbf8ff'
  on-background: '#161a32'
  surface-variant: '#dee0ff'
typography:
  display-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
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
  lg: 48px
  xl: 80px
  container-max: 1440px
  gutter: 32px
---

## Brand & Style

This design system is built for the modern, sophisticated traveler who views transit as an extension of their lifestyle. The brand personality is serene, premium, and tactile. By blending the organic feel of soft-UI with a high-end e-commerce editorial layout, the interface evokes a sense of calm and organization amidst the chaos of travel.

The visual style utilizes **Neumorphism**, moving away from flat design toward a world of extrusions and soft indentations. This creates a "soft-touch" digital experience that mimics premium physical packaging. The result is an interface that feels less like a screen and more like a physical dashboard of travel essentials.

## Colors

The palette is anchored by **Silk White**, a slightly desaturated off-white that serves as the essential canvas for neomorphic shadows. Pure white is reserved exclusively for the "light-source" highlights of UI elements.

**Soft Lavender** acts as the primary accent for calls to action and navigational highlights, while **Mint** is used sparingly for success states, badges, and secondary features to maintain a refreshing, airy feel. The typography utilizes a deep, muted navy-charcoal rather than true black to preserve the softness of the overall aesthetic.

- **Surface:** #F9F9FB (The foundational background)
- **Primary:** #B8B5FF (Lavender)
- **Secondary:** #D1F2EB (Mint)
- **Text:** #4A4E69 (Muted Charcoal)

## Typography

This design system utilizes **Plus Jakarta Sans** across all levels to maintain a contemporary, approachable, yet geometric look. The "Display" styles are tightly tracked to create a high-end editorial feel on desktop layouts. 

The hierarchy is structured to support long-form product descriptions and clear technical specs. Body copy is given generous line height to enhance readability and contribute to the "spacious" requirement of the brand.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop, centered within a 1440px max-width container. A 12-column system is used with generous 32px gutters to prevent the neomorphic shadows from overlapping or feeling cluttered.

Spacing follows an 8px rhythmic scale. To achieve the "spacious" high-end feel, section vertical padding is set to `xl` (80px), allowing product imagery and "Soft-UI" surfaces plenty of room to breathe. Components should use `md` (24px) internal padding to ensure the tactile "raised" edges are clearly visible.

## Elevation & Depth

Depth is the primary communicator of hierarchy in this design system. We use a dual-shadow approach to create the Neumorphic effect:

1.  **Raised Surfaces:** Elements appear to emerge from the background. This is achieved using a top-left shadow of white (#FFFFFF) and a bottom-right shadow of soft grey-lavender (#E2E4EB).
2.  **Sunken Surfaces:** Used for input fields and active button states. This is achieved using inner shadows with the same directional logic (top-left dark, bottom-right light).
3.  **Floating Elements:** For high-priority cards or modals, a third "ambient" shadow layer is added—a very diffused, low-opacity charcoal shadow to lift the element further off the page.

Shadow blurs should be high (20px+) and offsets should remain subtle (4px to 10px) to keep the look "chic" rather than "dated."

## Shapes

The shape language is consistently **Rounded**. Sharp corners are avoided as they break the liquid-like illusion of neomorphic surfaces. 

Standard components use a 0.5rem (8px) radius, while larger product cards and feature containers use `rounded-xl` (1.5rem / 24px) to emphasize the soft, premium nature of the brand. Interactive elements like "Add to Cart" may occasionally use pill-shapes to draw the eye.

## Components

### Buttons
Primary buttons are "Raised" surfaces. In the default state, they feature the dual-shadow neomorphic effect. On hover, the shadow intensity increases slightly. On click/active, the button transitions to a "Sunken" state using inner shadows, providing immediate tactile feedback.

### Cards
Cards are the primary container for products. They should have no visible border; instead, their "lift" from the Silk White background defines their boundaries. Padding inside cards should be generous (32px) to maintain the high-end feel.

### Input Fields
Inputs are styled as "Sunken" wells. This creates a clear mental model that these are areas to be "filled." The focus state highlights the inner shadow with a Soft Lavender tint.

### Chips & Tags
Used for product categories (e.g., "TSA Approved," "Lightweight"). These are flat surfaces with a very thin Silk White border or a soft Mint background to distinguish them from the interactive raised buttons.

### Additional Components
- **Progress Steppers:** For checkout, using soft-extruded circles.
- **Product Magnifier:** A floating, glassmorphic circular lens used to inspect fabric textures.
- **Cart Drawer:** A slide-out panel that uses a large-radius "Raised" surface treatment on its left edge to appear as if it sits above the main content.