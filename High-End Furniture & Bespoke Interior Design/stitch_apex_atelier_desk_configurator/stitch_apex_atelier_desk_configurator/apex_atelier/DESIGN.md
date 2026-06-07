---
name: Apex-Atelier
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1a1a1a'
  on-primary-container: '#848282'
  inverse-primary: '#5f5e5e'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#dec1af'
  on-tertiary: '#3f2c20'
  tertiary-container: '#26170c'
  on-tertiary-container: '#977e6e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#fbddca'
  tertiary-fixed-dim: '#dec1af'
  on-tertiary-fixed: '#28180d'
  on-tertiary-fixed-variant: '#574335'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
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
  margin-desktop: 64px
  margin-tablet: 32px
  margin-mobile: 20px
  max-width: 1440px
---

## Brand & Style

This design system embodies "Architectural Luxe," a philosophy that merges the structural integrity of high-end physical spaces with the fluidity of digital interfaces. It targets a discerning, elite clientele who values artisanal craftsmanship as much as technological precision. 

The visual style is **Soft-UI / Neumorphism**, reimagined through a lens of luxury. Instead of plastic-like surfaces, the UI mimics high-end materials: matte metals, treated wood, and precision-milled stone. The interface feels "carved" rather than assembled, utilizing subtle shadows and highlights to create a sense of tactile depth. The atmosphere is quiet, confident, and bespoke, evoking the feeling of a private gallery or an architect's studio.

## Colors

The palette is anchored in a sophisticated dark mode. **Matte Black (#1A1A1A)** serves as the monolithic base, providing a void-like depth for other elements to inhabit. **Brushed Brass (#D4AF37)** is used sparingly for high-contrast call-to-actions and interactive focal points, suggesting precious metal inlays. 

**Deep Walnut (#3D2B1F)** provides organic warmth, used primarily for structural containers and backgrounds that require a sense of "material" weight. Neumorphic shadows utilize two specific tones: a subtle highlight (#252525) and a deep recession (#0F0F0F) to simulate 3D relief on the Matte Black surfaces.

## Typography

Typography establishes a dialogue between the classical and the contemporary. **Playfair Display** provides an editorial, high-fashion authority for headlines. It should be used with generous leading and occasional negative letter-spacing for large display titles to emphasize its sharp serifs.

**Inter** handles all functional UI and body text. It is chosen for its mathematical precision and exceptional legibility against dark backgrounds. Labels should be set in uppercase with increased letter-spacing to mimic the engraving found on architectural blueprints.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy, reminiscent of structured architectural drafts. A 12-column system is used for desktop, centered within a max-width container to maintain focus. Spacing is governed by a strict 8px rhythmic scale.

Negative space is treated as a luxury material. Surfaces should have expansive internal padding (minimum 40px for cards) to prevent the "recessed" Neumorphic effects from feeling cluttered. On mobile, the grid collapses to 4 columns, and margins are tightened, but vertical breathing room remains high to preserve the "Elite" brand feel.

## Elevation & Depth

Hierarchy is achieved through "Tactile Relief" rather than traditional layering. 

1.  **Recessed (Inset):** Used for input fields, search bars, and toggles. This creates the illusion that the UI has been milled out of a solid block of Matte Black. Use an inner shadow (top-left: dark, bottom-right: light).
2.  **Extruded (Raised):** Used for cards and primary containers. This uses a dual drop shadow (top-left: light/soft, bottom-right: dark/hard) to lift the surface toward the user.
3.  **Floating:** Reserved for global navigation and Brushed Brass CTAs. These use a more traditional, highly diffused ambient shadow to suggest they are suspended above the architectural base.

## Shapes

The shape language is "Softened Geometry." While the brand is architectural, hard 0px corners feel too aggressive for a "luxe" experience. A **Soft (0.25rem)** base radius is applied to standard components, providing a precision-milled look. Large containers use **rounded-lg (0.5rem)** to emphasize the tactile, organic nature of the Neumorphic shadows. Interaction states should never transition to full circles (pills) unless used for small status indicators; maintaining the "rectangle" preserves the architectural integrity.

## Components

### Buttons
- **Primary:** Solid Brushed Brass (#D4AF37) with black text. No Neumorphic effect; it should sit "above" the system as a high-contrast beacon.
- **Secondary:** Neumorphic "Extruded" style on Matte Black. The text is white or brass. On press, the button transitions to a "Recessed" state.

### Tactile Material Swatches
Interactive elements used for selection. These should look like physical tiles of Deep Walnut or Brass. They feature a heavy 3D "extrusion" and use a subtle grain texture overlay to enhance the artisanal feel.

### Recessed Tech Toggles
Form controls must appear "milled" into the surface. The track is an inset well, and the thumb is a precision-machined metal disc that appears to slide within the groove.

### Input Fields
Inputs are always "Recessed." Use a subtle inner shadow to define the boundary. Focused states are signaled by a thin 1px Brushed Brass border and a soft outer glow.

### Cards
Cards do not use borders. Depth is defined entirely by the soft light/dark shadow pair. The background of the card should be slightly lighter than the global background (#2A2A2A) to enhance the 3D effect.