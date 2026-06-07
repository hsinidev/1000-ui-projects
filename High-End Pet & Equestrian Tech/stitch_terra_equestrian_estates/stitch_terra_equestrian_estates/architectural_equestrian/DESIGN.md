---
name: Architectural Equestrian
colors:
  surface: '#fbf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#4e453e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#80756d'
  outline-variant: '#d2c4bb'
  surface-tint: '#705a49'
  primary: '#322214'
  on-primary: '#ffffff'
  primary-container: '#4a3728'
  on-primary-container: '#bba08c'
  inverse-primary: '#dec1ac'
  secondary: '#8e4c32'
  on-secondary: '#ffffff'
  secondary-container: '#ffa989'
  on-secondary-container: '#793c23'
  tertiary: '#0c2833'
  on-tertiary: '#ffffff'
  tertiary-container: '#243e49'
  on-tertiary-container: '#8ea9b6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#fbddc7'
  primary-fixed-dim: '#dec1ac'
  on-primary-fixed: '#28180b'
  on-primary-fixed-variant: '#574333'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb59a'
  on-secondary-fixed: '#380d00'
  on-secondary-fixed-variant: '#71361d'
  tertiary-fixed: '#cbe7f5'
  tertiary-fixed-dim: '#afcbd8'
  on-tertiary-fixed: '#021f29'
  on-tertiary-fixed-variant: '#304a55'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 72px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

The design system is rooted in the concept of "Architectural Grounding"—a philosophy that mirrors the permanence of elite estates and the precision of competitive polo. It targets a high-net-worth audience that values legacy, land stewardship, and understated luxury. 

The aesthetic is a fusion of **High-End Minimalism** and **Modern Architectural** principles. It avoids the clutter of traditional real estate platforms in favor of a gallery-like experience. The UI should evoke an emotional response of tranquility, stability, and exclusivity. Key visual drivers include expansive full-bleed imagery of landscapes, a rigid adherence to alignment, and a "less is more" approach to functional elements. Every interaction is designed to feel deliberate, quiet, and sophisticated.

## Colors

The palette is derived from the natural elements of a world-class estate: umber soil, terracotta stables, and slate skies.

- **Primary (Umber):** Used for primary navigation, high-level headers, and core brand moments. It represents the "grounded" nature of the brand.
- **Secondary (Terracotta):** Reserved for subtle accents, interactive states, or highlighting specific "Land Data" features. It adds warmth to the architectural coolness.
- **Tertiary (Slate Blue):** Used for secondary utility elements, data visualizations, and map interfaces to provide a sophisticated contrast to the earth tones.
- **Neutral (Charcoal/White):** Deep charcoal is used for body text to ensure readability without the harshness of pure black. Crisp whites and off-whites (Bone) form the canvas, providing the necessary whitespace for a minimalist feel.

## Typography

This design system utilizes a high-contrast typographic pairing to balance heritage with modernity.

- **Headings:** **EB Garamond** provides a literary, authoritative, and timeless feel. Large-scale display sizes should use tight letter-spacing to emphasize the high-contrast strokes of the serif.
- **Body & UI:** **Metropolis** offers a geometric, structured counterpoint. Its clean lines and open apertures ensure maximum readability for technical land data and property specifications.
- **Labels:** Small labels and captions are always rendered in Metropolis with increased letter-spacing and uppercase styling to evoke an architectural blueprint aesthetic.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop, centered within the viewport to create a "boutique" feel. 

- **Grid:** A 12-column grid with generous 32px gutters. 
- **Rhythm:** A strict 8px baseline grid governs all vertical rhythm.
- **Whitespace:** High-end appeal is achieved through "Section Gaps" (128px+), allowing full-bleed imagery to breathe. 
- **Alignment:** Elements are often offset or asymmetrical to mirror modern architectural plans, but they must always snap to the underlying grid lines.

## Elevation & Depth

This design system eschews heavy shadows in favor of **Tonal Layering** and **Low-Contrast Outlines**. 

- **Layering:** Depth is communicated by stacking surfaces of slightly different neutral tones (e.g., a Bone card on a White background).
- **Outlines:** Use 1px "Hairline" borders in Slate or Umber at 10-20% opacity. This creates a "blueprint" or "drafting" effect that feels precise and architectural.
- **Focus:** Interactive elements may use a very subtle, diffused ambient shadow (Blur 20px, Opacity 5%, Tinted with Umber) only upon hover to signify lift without breaking the minimalist plane.

## Shapes

The shape language is **Sharp (0)**. 

To maintain an "Architectural" and "Grounded" aesthetic, the design system utilizes 0px border radii for all primary components (buttons, input fields, cards, and images). This reinforces the feeling of structural integrity and precision. Softness is introduced through photography and organic serif typography rather than the UI framework itself.

## Components

### Buttons & Inputs
- **Primary Action:** Sharp-edged, solid Umber fill with white Metropolis caps. No gradients.
- **Secondary Action:** 1px Umber outline, transparent background.
- **Forms:** Input fields are minimal, consisting of a bottom border only (Hairline Slate) until focused, at which point they transition to a full 1px box.

### Cards
- **Property Cards:** Minimalist frames with full-bleed imagery. Typography is placed either in a high-contrast white overlay at the bottom or in a structured white block below the image. No shadows; use 1px hairlines for separation.

### Land-Data Visualizations
- **Topography:** Use thin, Slate Blue vector lines for contour maps.
- **Interactive Layers:** Overlays for soil quality or parcel boundaries should use 20% opacity fills in Terracotta or Slate, maintaining the visibility of the underlying land.

### Inquiry Forms
- **Sleek Layout:** Multi-step forms with significant padding. Each step focuses on a single category (e.g., "Land Requirements") to prevent cognitive overload. Use Metropolis for all form labels to maintain a professional, data-driven feel.