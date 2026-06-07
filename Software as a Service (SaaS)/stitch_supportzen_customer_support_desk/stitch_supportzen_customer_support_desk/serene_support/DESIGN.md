---
name: Serene Support
colors:
  surface: '#f7faf8'
  surface-dim: '#d7dbd9'
  surface-bright: '#f7faf8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f3'
  surface-container: '#ebefed'
  surface-container-high: '#e6e9e7'
  surface-container-highest: '#e0e3e2'
  on-surface: '#181c1c'
  on-surface-variant: '#3e4947'
  inverse-surface: '#2d3130'
  inverse-on-surface: '#eef1f0'
  outline: '#6e7977'
  outline-variant: '#bec9c6'
  surface-tint: '#006a64'
  primary: '#006a64'
  on-primary: '#ffffff'
  primary-container: '#64b5ad'
  on-primary-container: '#004540'
  inverse-primary: '#84d5cc'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fd'
  on-secondary-container: '#57657b'
  tertiary: '#5c5f61'
  on-tertiary: '#ffffff'
  tertiary-container: '#a5a8aa'
  on-tertiary-container: '#3a3d3f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#a0f1e8'
  primary-fixed-dim: '#84d5cc'
  on-primary-fixed: '#00201e'
  on-primary-fixed-variant: '#00504b'
  secondary-fixed: '#d5e3fd'
  secondary-fixed-dim: '#b9c7e0'
  on-secondary-fixed: '#0d1c2f'
  on-secondary-fixed-variant: '#3a485c'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f7faf8'
  on-background: '#181c1c'
  surface-variant: '#e0e3e2'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  h2:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  code:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 20px
  container-max: 1440px
---

## Brand & Style

This design system is built to reduce the cognitive load of customer support agents. The brand personality is empathetic, composed, and efficient. It utilizes a refined **Neumorphic (Soft-UI)** style, moving away from flat design toward a tactile interface that feels responsive to the touch. By using subtle highlights and shadows, the UI mimics physical surfaces, creating a sense of calm and order. The aesthetic is "quiet"—it avoids loud alerts in favor of gentle state changes, ensuring that even in high-pressure support environments, the interface remains a steady, helpful partner.

## Colors

The palette is anchored in **Soft Teal**, providing a tranquil but professional primary action color. **White** is used not just as a background, but as a "light source" for neumorphic highlights. **Slate** provides high-contrast grounding for typography and iconography, ensuring accessibility. 

The background color is specifically tuned to a slightly cool grey-blue (#E0E5EC) to allow both white highlights and soft shadows to remain visible, creating the signature Soft-UI depth without straining the eyes.

## Typography

The typography system prioritizes legibility for long-form reading, such as support tickets and documentation. **Manrope** is used for its modern, balanced proportions, providing a friendly yet institutional feel. For utility-heavy elements like metadata, tags, and small labels, **Inter** is employed to maintain clarity at smaller scales. Paragraphs utilize a generous line height to prevent "wall of text" fatigue for agents.

## Layout & Spacing

This design system employs a **Fluid Grid** model with a soft 4px base unit. Layouts should prioritize "breathing room" to maintain the calm aesthetic. Containers and cards use dynamic padding that scales with the viewport. The primary workspace for agents is typically a three-pane layout: navigation on the left, ticket feed in the center, and user telemetry on the right. Spacing between major neumorphic containers should be significant (24px+) to allow the "extruded" shadows to be fully appreciated without visual clutter.

## Elevation & Depth

Depth is the core differentiator of this design system. Instead of traditional Z-index layering with drop shadows, we use **Dual-Shadow Neumorphism**:
- **Concave (Pressed):** Used for input fields and active button states. Created with a dark inner shadow on the top-left and a light inner shadow on the bottom-right.
- **Convex (Raised):** Used for cards and primary buttons. Created with a dark drop shadow on the bottom-right and a white highlight on the top-left.
- **Shadow specs:** Shadows should be highly diffused (Blur: 12px-20px) with low opacity (15-20%) using the Slate-tinted `shadow_hex`.

## Shapes

The shape language is organic and approachable. Sharp corners are avoided entirely. Standard UI elements utilize a **0.5rem (8px)** radius to balance softness with professional structure. Larger layout containers and primary cards use **1rem (16px)**. This consistent rounding complements the soft shadows, reinforcing the "molded" look of the interface.

## Components

- **Buttons:** Primary buttons appear "raised" from the surface in Soft Teal. On click, they transition to a "pressed" (inner shadow) state.
- **Input Fields:** Search bars and ticket replies should be "sunken" (concave) into the background surface to indicate where data entry is required.
- **Cards:** Ticket items in a list are individual "raised" tiles. Use a subtle Teal border (1px, 10% opacity) for high-priority tickets to differentiate without breaking the neumorphic style.
- **Chips/Status:** Tags for "Open," "Pending," and "Resolved" should use low-saturation versions of green, amber, and blue, appearing as flat insets within the raised cards.
- **Progress Indicators:** Use soft, rounded bars that appear "carved" into the UI, with the teal fill appearing to sit inside the groove.
- **Sidebar:** The navigation menu should be a single, large raised surface that spans the height of the screen, creating a distinct vertical plane.