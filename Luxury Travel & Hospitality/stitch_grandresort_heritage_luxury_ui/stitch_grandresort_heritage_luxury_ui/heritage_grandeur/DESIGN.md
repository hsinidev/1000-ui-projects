---
name: Heritage Grandeur
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#444650'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#6a5f00'
  on-secondary: '#ffffff'
  secondary-container: '#f2e176'
  on-secondary-container: '#6f6300'
  tertiary: '#131515'
  on-tertiary: '#ffffff'
  tertiary-container: '#272929'
  on-tertiary-container: '#8f9090'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#f5e479'
  secondary-fixed-dim: '#d8c860'
  on-secondary-fixed: '#201c00'
  on-secondary-fixed-variant: '#504700'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin-edge: 64px
  section-gap: 120px
---

## Brand & Style

This design system is built upon the pillars of "Heritage Luxury" and "Prestigious Hospitality." It targets an affluent, discerning clientele who values tradition, architectural precision, and bespoke service. The visual language evokes the feeling of a historic five-star manor—permanent, authoritative, yet welcoming.

The style is a fusion of **Minimalism** and **Tactile Luxury**. It utilizes heavy whitespace (the "Airy" quality) to signify exclusivity, while employing metallic accents and high-contrast color blocking to establish a sense of modern prestige. Every element should feel curated, avoiding unnecessary decorative flourishes in favor of structural elegance and material honesty.

## Colors

The palette is anchored by **Royal Navy**, used to convey depth, stability, and authority. This is contrasted against **Marble White**, which serves as the primary canvas to ensure the interface feels breathable and expansive. **Brass** is reserved for interactive elements, highlights, and delicate borders, mimicking the physical hardware found within a luxury estate.

- **Primary (Royal Navy):** Used for primary navigation backgrounds, hero typography, and deep-state surfaces.
- **Secondary (Brass):** Used for call-to-action borders, iconography, and decorative dividers.
- **Tertiary (Marble White):** The foundational background color for all pages to maintain a high-light, airy environment.
- **Neutral:** A rich charcoal (#1A1A1A) is used for body text to maintain legibility without the harshness of pure black.

## Typography

This design system employs a classic typographic pairing to balance heritage with modern readability. 

**Noto Serif** is used for all headlines and display text. It should be set with generous leading and, for larger sizes, a slight negative letter-spacing to create a dense, "editorial" feel. 

**Work Sans** provides a functional, grounded counterpoint for body copy and UI labels. The contrast between the organic curves of the serif and the geometric clarity of the sans-serif reinforces the "Traditional Elegance" theme. Always prioritize legibility and generous line heights to maintain the airy aesthetic.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to mirror the structured symmetry of classical architecture. Content is housed within a 12-column grid with wide gutters (32px) to prevent visual clutter.

Spacing is aggressive in its use of "negative space." Large vertical gaps (Section Gaps) are used between major content blocks to allow the user's eye to rest, signaling that the content is premium and not rushed. Elements should frequently utilize asymmetrical offsets to create a modern, high-end editorial look while remaining anchored to the 8px baseline grid.

## Elevation & Depth

This design system rejects heavy, fuzzy shadows in favor of **Tonal Layers** and **Low-Contrast Outlines**. Depth is communicated through the physical stacking of Marble White surfaces on top of slightly darker off-white backgrounds, or through the use of 1px Brass borders.

When a surface must feel elevated (such as a modal), use a "Ghost Shadow"—a very large blur (32px+) with extremely low opacity (3-5%) tinted with Royal Navy. This creates a subtle ambient lift rather than a digital drop-shadow. Background blurs may be used sparingly behind navigation bars to maintain the airy feel while scrolling over content.

## Shapes

The shape language is strictly **Sharp (0px)**. Rectilinear forms are a hallmark of traditional prestige and architectural integrity. Every card, button, and input field should feature crisp 90-degree angles. This severity is softened not by rounding corners, but by the use of delicate borders and generous internal padding. 

The only exception to the "sharp" rule is for purely circular elements, such as specific icon containers or image masks used in a gallery context to break the rhythm of the grid.

## Components

### Buttons
Buttons are the primary expression of the "Gold-Rimmed" aesthetic. 
- **Primary:** Royal Navy background with a 1px Brass border and Brass text. 
- **Secondary:** Transparent background with a 1px Brass border and Navy text.
- **Hover State:** Background fills with Brass, text shifts to Marble White.

### Refined Cards
Cards should not have shadows. Instead, use a 1px hairline border in a muted version of Brass or a subtle tonal shift in the background. Content inside cards must have at least 32px of padding to maintain the "prestigious" feel.

### Delicate Dividers
Dividers are 1px lines using the Brass color at 40% opacity. They should never span the full width of a container unless they are separating major navigation sections; instead, use centered, shorter dividers to separate headlines from body text.

### Polished Navigation
The navigation bar is expansive. Links are styled using the `label-caps` typography. The active state is indicated by a 2px Brass underline that does not touch the text, maintaining a "hovering" elegance.

### Inputs & Selection
Text inputs feature a bottom-border only (1px Brass) to mimic high-end stationery. Checkboxes and radio buttons are sharp-edged squares and diamonds, respectively, maintaining the architectural shape language.