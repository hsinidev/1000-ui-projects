---
name: Lumière Heritage
colors:
  surface: '#fff8ef'
  surface-dim: '#e3d9c3'
  surface-bright: '#fff8ef'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fdf3db'
  surface-container: '#f7edd6'
  surface-container-high: '#f1e7d0'
  surface-container-highest: '#ece2cb'
  on-surface: '#201b0d'
  on-surface-variant: '#444748'
  inverse-surface: '#353021'
  inverse-on-surface: '#faf0d9'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#695d45'
  on-secondary: '#ffffff'
  secondary-container: '#efdebf'
  on-secondary-container: '#6e6149'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#271902'
  on-tertiary-container: '#97805e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#f2e0c2'
  secondary-fixed-dim: '#d5c5a7'
  on-secondary-fixed: '#231a08'
  on-secondary-fixed-variant: '#51452f'
  tertiary-fixed: '#fbdeb7'
  tertiary-fixed-dim: '#dec39c'
  on-tertiary-fixed: '#271902'
  on-tertiary-fixed-variant: '#564426'
  background: '#fff8ef'
  on-background: '#201b0d'
  surface-variant: '#ece2cb'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 80px
  section-gap: 120px
---

## Brand & Style

This design system is built upon the concept of "The Alchemist’s Archive." It targets discerning photographers and collectors who view equipment not as tools, but as vessels of history. The aesthetic is **Nostalgic-Editorial**, blending the structured layouts of mid-century photography journals with the tactile premium of artisanal craftsmanship. 

The UI should evoke a sense of quiet reverence—reminiscent of a darkroom or a high-end gallery. Visual storytelling is prioritized over rapid-fire interaction, encouraging users to linger on high-resolution archival imagery and technical narratives. The style utilizes a **Minimalist-Tactile** hybrid approach: clean, intentional whitespace paired with the perceived "weight" of aged paper and the precision of mechanical optics.

## Colors

The palette is anchored in the physical materials of early cinematography and photography. 

- **Aged Parchment (#F1E7D0):** This serves as the primary canvas, replacing stark whites with a warmer, more organic background that reduces eye strain and suggests longevity.
- **Warm Sepia (#E2D1B3):** Used for subtle layering, secondary containers, and accents that bridge the gap between the background and the dark text.
- **Obsidian Black (#1A1A1A):** The color of ink and camera bodies. This provides the high-contrast necessary for the editorial serif typography.
- **Muted Bronze (#A68E6B):** A tertiary accent reserved for interactive highlights, reminiscent of the brass components in vintage lens housings.

## Typography

This design system employs a strict typographic hierarchy to maintain its editorial authority. 

**Noto Serif** is the primary voice for brand storytelling and titles. It should be used with generous leading and occasional italicization for emphasis, mimicking the titling of vintage cinema. **Manrope** provides a functional, modern counterpoint for technical specifications and body copy, ensuring that while the aesthetic is vintage, the usability remains contemporary. 

Key instructions:
- Use `display-lg` for hero sections with tight tracking.
- Use `label-caps` for all navigational elements and small metadata to create an "archival tag" look.
- Body text should always prioritize readability with a line height of at least 1.6x.

## Layout & Spacing

The layout philosophy is a **Fixed-Editorial Grid**. On desktop, content is contained within a 12-column grid that mimics the proportions of a large-format photo book. On mobile, the system shifts to a single-column storytelling flow with intentional "pauses" created by vertical whitespace.

Rhythm is maintained through a 4px baseline, but macro-spacing (the gaps between sections) should be aggressive. This design system uses "Negative Space as Luxury," where the distance between elements signals the premium nature of the service.

## Elevation & Depth

This design system avoids traditional drop shadows in favor of **Tonal Layering** and **Structural Overlays**. 

- **Tonal Layers:** Depth is created by placing #E2D1B3 (Sepia) elements on #F1E7D0 (Parchment) surfaces. 
- **Framing:** Use thin, 1px solid borders in #1A1A1A with low opacity (10-15%) to define boundaries without breaking the "flat paper" aesthetic.
- **Lens Flare Overlays:** Subtle, non-intrusive light-leak textures may be applied as fixed-position background elements to simulate optical glass.
- **Archival Imagery:** Photos should appear as "tipped-in" plates, using crisp edges and no rounding to look like physical prints.

## Shapes

The shape language is **Strictly Geometric (Sharp)**. 

To reinforce the archival, printed-matter aesthetic, the `roundedness` is set to 0. Every button, image container, and input field must have sharp 90-degree corners. This mimics the precision of technical drawings and the clean cut of heavy cardstock. Avoid circles unless they are functional representations of camera lenses or apertures.

## Components

### Buttons
Primary buttons are solid Obsidian Black (#1A1A1A) with Parchment text, using the `label-caps` style. Secondary buttons use a 1px border with no fill. All hover states should involve a subtle color shift to Muted Bronze (#A68E6B) or an underline transition for text links.

### Input Fields
Fields consist of a single 1px bottom border (#1A1A1A). Labels sit above the line in `label-caps`. The focus state thickens the bottom border to 2px.

### Cards (The "Exhibit" Component)
Cards are used for showcasing lenses or services. They feature a full-width image at the top with a sharp 0px radius, followed by a wide margin and centered text. There is no background fill or shadow for cards; they are defined by their relationship to the grid.

### Chips & Tags
Metadata (e.g., "Leica", "Restored", "1950s") should be styled as small, bordered rectangles. They should look like physical labels found in a museum drawer.

### Interactive "Lens" Viewer
A custom component for this design system: an image gallery that utilizes a circular "aperture" mask for transitions, reinforcing the firm's focus on glass and optics.