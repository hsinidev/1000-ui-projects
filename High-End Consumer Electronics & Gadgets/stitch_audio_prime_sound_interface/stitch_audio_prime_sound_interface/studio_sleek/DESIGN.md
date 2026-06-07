---
name: Studio Sleek
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
  on-surface-variant: '#d8c3b4'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#a08d80'
  outline-variant: '#524439'
  surface-tint: '#ffb77b'
  primary: '#ffb77b'
  on-primary: '#4d2700'
  primary-container: '#c8803f'
  on-primary-container: '#432100'
  inverse-primary: '#8c4f10'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcc2'
  primary-fixed-dim: '#ffb77b'
  on-primary-fixed: '#2e1500'
  on-primary-fixed-variant: '#6d3a00'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Montserrat
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
    lineHeight: '1.6'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-viz:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.0'
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
  margin-mobile: 20px
  container-max: 1280px
---

## Brand & Style

The brand personality is authoritative, precision-engineered, and unapologetically premium. It targets the discerning audiophile who values technical excellence as much as industrial aesthetics. The UI must evoke the sensation of handling high-end studio equipment—cold to the touch, heavy, and perfectly calibrated.

The design style is **Tactile Industrial**. It bridges the gap between digital interface and physical hardware. By utilizing subtle metallic gradients, micro-textures (mimicking brushed aluminum and leather grain), and high-fidelity macro photography, the system establishes a "Studio Sleek" atmosphere. Every interaction should feel like adjusting a physical knob or sliding a weighted fader. The aesthetic is dark, focused, and immersive, stripping away unnecessary embellishments to highlight the raw beauty of the hardware and the precision of the audio data.

## Colors

The palette is rooted in industrial materials. **Deep Charcoal (#1A1A1A)** serves as the foundational "obsidian" surface, providing a high-contrast backdrop for technical data. **Brushed Copper (#B87333)** is used as the functional accent color—reserved for active states, playback progress, and critical interactive elements, mimicking the internal wiring and premium accents of the headphones. **Metallic Silver (#C0C0C0)** provides structural highlights and secondary information.

The design system operates exclusively in a **Dark Mode** environment to maintain the studio aesthetic. Gradients should transition from Deep Charcoal to slightly lighter ash tones (#2A2A2A) to simulate 3D curvature on surfaces. Functional alerts (errors) should use a desaturated red, while success states utilize a muted moss green to keep the focus on the primary copper accent.

## Typography

Typography is used to reinforce the industrial hierarchy. **Montserrat** is the display typeface, utilized in high-contrast weights to create a sense of architectural strength. **Inter** handles body copy and functional text, chosen for its unparalleled legibility in technical contexts. **JetBrains Mono** is introduced for labels and data visualizations to provide a "spec sheet" feel, emphasizing the precision of the audio metrics.

Use "label-caps" for all technical headers and metadata categories. Headlines should lean into tight tracking and heavy weights to feel like etched metal. Body text should maintain generous line heights for readability against the dark, textured backgrounds.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for desktop to maintain a cinematic, composed feel, while transitioning to a fluid model for mobile. A 12-column grid is standard, but technical panels often utilize a nested 4-column layout for modularity.

Spacing is governed by an 8px base unit. Visual groups are separated by wide margins to allow the macro photography and textures to breathe. In technical dashboards (like the EQ or frequency response views), the layout should feel dense and informative, using tighter 16px gutters to connect related data points. On mobile, elements reflow into a single-column stack, prioritizing the interactive "dial" and "slider" controls at the thumb-zone.

## Elevation & Depth

Elevation in this design system is achieved through **Tonal Sculpting** and **Material Stacking**. Rather than generic shadows, use:
1.  **Inner Glows/Shadows:** To create "recessed" areas for sliders and input fields, making them look like they are carved into a metal chassis.
2.  **Metallic Bevels:** A 1px highlight (Metallic Silver at 20% opacity) on the top edge of components and a 1px shadow on the bottom edge to simulate physical depth.
3.  **Backdrop Blurs:** Use heavy blurs (20px+) behind overlays to maintain the dark atmosphere while separating navigation from content.
4.  **Textural Layering:** Apply a subtle grain or "brushed metal" SVG filter to primary container surfaces to give them a tactile, non-digital quality.

## Shapes

The shape language is **Soft Industrial**. It avoids overly rounded, "friendly" corners in favor of tight, precise radii that suggest machined precision. 

Standard components (buttons, input fields) use a 4px (0.25rem) radius. For large cards or featured sections, a 12px (0.75rem) radius is used. Circularity is reserved strictly for functional audio metaphors: EQ dials, volume rings, and frequency orbiters. This contrast between the predominantly rectilinear grid and perfectly circular controls helps the user instinctively identify interactive audio parameters.

## Components

### Interactive Sliders
Designed as "Weighted Faders." The track is a recessed groove (inner shadow) in Deep Charcoal. The thumb is a Brushed Copper rectangle with a subtle vertical metallic texture.

### Circular EQ Dials
The centerpiece of the interface. Dials use a conical gradient to simulate a knurled metal texture. Active values are indicated by a glowing Brushed Copper ring segment.

### Technical Data Visualizations
Frequency response graphs use a single-pixel Copper line with a subtle outer glow. Background grids are rendered in Metallic Silver at 10% opacity, utilizing JetBrains Mono for axis labels.

### Buttons
- **Primary:** Solid Brushed Copper with black text. On hover, a subtle metallic sheen animation passes across the surface.
- **Secondary:** Ghost style with a 1px Metallic Silver border.
- **Tertiary:** Text-only in JetBrains Mono with an underline that expands from the center on hover.

### Cards
Cards are containers with a subtle gradient from #222222 to #1A1A1A. They feature a 1px top border in Silver (15% opacity) to catch the "studio light."

### Inputs
Fields are dark, recessed boxes. The cursor and focus state glow in Copper. Labels always sit above the field in "label-caps" style.