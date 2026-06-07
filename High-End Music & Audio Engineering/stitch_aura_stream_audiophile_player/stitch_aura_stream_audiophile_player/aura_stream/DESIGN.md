---
name: Aura-Stream
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e4'
  on-surface-variant: '#c6c6ce'
  inverse-surface: '#e5e2e4'
  inverse-on-surface: '#303032'
  outline: '#909098'
  outline-variant: '#46464d'
  surface-tint: '#bfc5e4'
  primary: '#bfc5e4'
  on-primary: '#292f48'
  primary-container: '#0a1128'
  on-primary-container: '#767c99'
  inverse-primary: '#575d78'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c5c7c8'
  on-tertiary: '#2e3132'
  tertiary-container: '#101314'
  on-tertiary-container: '#7c7e7f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#bfc5e4'
  on-primary-fixed: '#141a32'
  on-primary-fixed-variant: '#3f465f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#131315'
  on-background: '#e5e2e4'
  surface-variant: '#353436'
typography:
  headline-display:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
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
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  metadata-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 16px
  md: 32px
  lg: 64px
  xl: 128px
  gutter: 24px
  margin: 48px
---

## Brand & Style

The brand personality is authoritative yet understated, catering to an audience that values sonic precision and visual clarity. This design system is built on a **Minimalist Editorial** style, merging the high-end layout of luxury print magazines with the technical rigor of high-fidelity audio equipment.

The UI should evoke a sense of calm focus—like a quiet listening room. It utilizes vast whitespace (negative space) to allow high-resolution artist photography and album art to serve as the primary visual drivers. The emotional response is one of premium exclusivity; the interface does not compete with the art, it frames it. Subtle gradients and technical metadata overlays suggest a layer of professional-grade sophistication without cluttering the user experience.

## Colors

The palette is anchored in a dark-mode-first approach to emphasize the "audiophile" environment. **Deep Navy (#0A1128)** serves as the primary canvas, providing a depth that feels more sophisticated than pure black. **Silk White (#F8F9FA)** is used sparingly for high-contrast typography and essential icons to ensure legibility.

**Silver (#C0C0C0)** acts as the bridge, used for secondary metadata, borders, and technical details to evoke the brushed-metal texture of premium amplifiers. Subtle variations of the navy are used for "Aura" gradients—very soft radial glows that emanate from behind album art to create depth without defined shadows.

## Typography

Typography follows an editorial hierarchy. **Noto Serif** (the headline font) provides the "high-contrast" elegance required for artist names and editorial features. It should be typeset with generous leading and occasionally negative letter-spacing for large display sizes to maintain a tight, professional look.

**Inter** handles all functional UI elements. It is chosen for its exceptional legibility at small sizes, crucial for displaying technical audio bitrates, tracklists, and navigation. Use the "label-caps" style for section headers to provide a clear, technical structure to the page without the weight of a serif.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy for desktop (12 columns) and a fluid approach for mobile. The layout is intentionally "spacious," using the 'lg' and 'xl' spacing units to separate major editorial sections. 

Content should feel like a curated gallery; use wide margins (48px+) to prevent the UI from feeling "app-like" and instead feel "publication-like." Align technical metadata to a strict baseline grid to reinforce the sense of precision. Components like tracklists should use generous vertical padding (md) to give each composition its own breathing room.

## Elevation & Depth

Hierarchy is achieved through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows. 

1.  **Base Layer:** The Deep Navy (#0A1128) background.
2.  **Surface Layer:** Slightly lighter navy (#121F45) used for cards or containers, defined by a 1px Silver (#C0C0C0) border at 10-15% opacity.
3.  **Aura Layer:** For active elements (like the current playing track), use a very soft, large-radius radial gradient behind the imagery to create a "glow" effect that feels like light reflecting off hardware.

Avoid drop shadows. Depth should feel like physical layers of glass or metal stacked on top of one another.

## Shapes

The shape language is **Soft (0.25rem)**. While a minimalist aesthetic often leans toward sharp corners, this design system uses a subtle radius to prevent the UI from feeling overly aggressive or "brutalist." 

Album art should maintain a consistent 4px (0.25rem) radius. Only buttons and high-level containers should use the `rounded-lg` (8px) setting. The goal is to maintain a rectilinear, architectural feel while softening the points of interaction.

## Components

**Buttons:** Use "Ghost" styles as the default. A 1px Silver border with Silk White text. Primary actions (like 'Play') can use a solid Silk White background with Deep Navy text for maximum contrast.

**Chips:** Small, rectangular tags with 11px Inter metadata. Used for audio quality indicators (e.g., "MQA", "24-bit/192kHz"). These should have a Silver border at 20% opacity.

**Lists:** Tracklists should be minimalist. No background for rows; use a simple 1px divider in Silver (10% opacity) between items. Hover states should use a subtle shift in background color to the Accent Navy.

**Input Fields:** Minimalist underlines or 1px bordered boxes. No heavy fills. Labels should always use the "label-caps" typography style.

**Cards:** Editorial cards feature large-scale imagery. Typography should often be placed *below* the image or overlayed with a subtle bottom-to-top dark gradient for legibility.

**Additional Component - The Audio Gauge:** A custom visualizer or playback bar that uses thin, 1px lines to represent frequency or progress, echoing the aesthetic of high-end oscilloscope displays.