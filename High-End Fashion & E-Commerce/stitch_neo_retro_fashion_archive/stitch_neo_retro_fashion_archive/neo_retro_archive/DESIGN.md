---
name: Neo-Retro Archive
colors:
  surface: '#fbf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#444748'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#5f5e58'
  on-secondary: '#ffffff'
  secondary-container: '#e5e2da'
  on-secondary-container: '#65645e'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#2e1500'
  on-tertiary-container: '#b07845'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#e5e2da'
  secondary-fixed-dim: '#c9c6bf'
  on-secondary-fixed: '#1c1c17'
  on-secondary-fixed-variant: '#474741'
  tertiary-fixed: '#ffdcc1'
  tertiary-fixed-dim: '#fbb980'
  on-tertiary-fixed: '#2e1500'
  on-tertiary-fixed-variant: '#693c0e'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  container-margin: 24px
  gutter: 16px
  section-gap: 64px
  timeline-track: 2px
---

## Brand & Style

This design system draws inspiration from high-end fashion editorial history, blending the intellectual rigor of a curated archive with the modern fluidity of mobile commerce. The aesthetic is "Neo-Retro"—a contemporary interpretation of mid-century print luxury. It is designed to evoke a sense of permanence, prestige, and meticulous curation.

The style is **Editorial Minimalism**. It prioritizes high-resolution archival photography as the primary narrative driver, supported by a structured, rhythmic layout. The emotional response is one of "quiet luxury": sophisticated, intentional, and authoritative. By using generous whitespace and a "Timeline" UX concept, the design system transforms simple browsing into a chronological journey through fashion history.

## Colors

The palette is rooted in the materials of vintage publishing: ink, aged paper, and sepia-toned photography.

- **Primary (Deep Black - #1A1A1A):** Represents the "Ink." Used for headings, primary icons, and structural borders to provide sharp definition.
- **Secondary (Parchment - #F5F2EA):** Represents the "Paper." This is the global background color, providing a warmer, more sophisticated alternative to clinical white.
- **Tertiary (Rich Sepia - #704214):** Represents the "Archive." Used for accents, timeline indicators, and secondary call-to-actions, evoking aged film and leather.
- **Neutral (Charcoal - #3C3C3C):** Used for body text and subtle metadata to ensure high legibility without the harshness of pure black.

## Typography

The typography strategy pairs the traditional authority of a high-end serif with the functional clarity of a modern sans-serif.

- **Headlines:** Use **Noto Serif**. This font carries the classic weight of vintage fashion mastheads. Display sizes should be set with tight tracking to mimic editorial headlines.
- **Body & Interface:** Use **Inter**. This provides a neutral, utilitarian balance to the expressive headlines, ensuring that long-form storytelling and archival data remain highly readable on mobile screens.
- **Labels:** Small caps and increased letter spacing are used for metadata (e.g., "COLLECTION 1994") to create a rhythmic, catalog-like feel.

## Layout & Spacing

This design system utilizes a **Fixed-Fluid Hybrid Grid**. On mobile, it adheres to a strict 4-column grid with generous 24px side margins to create an "enclosed" magazine feel. 

Spacing is intentionally oversized between sections (64px+) to allow the photography to breathe and to signify the transition between "eras" or "chapters" in the timeline. The layout philosophy is **Vertical Storytelling**, where the central axis of the page often acts as a literal timeline or anchor point for content blocks to stagger against.

## Elevation & Depth

To maintain the "archive" feel, the design system avoids modern drop shadows. Instead, it uses **Tonal Layering** and **Bold Outlines**.

- **Surfaces:** Depth is created by placing parchment-colored cards on slightly darker sepia-washed backgrounds, or deep black sections for high-impact photography.
- **Borders:** A 1px or 2px solid primary-colored border is used to define key archival containers, mimicking the look of framed photographs or boxed artifacts.
- **Imagery:** Photos are treated as physical objects. They should never be cropped with rounded corners; they should remain sharp and architectural, often overlapping grid lines to create a sense of dynamic editorial collage.

## Shapes

The shape language is strictly **Geometric and Sharp**. 

- **Corners:** A `roundedness` of 0 is enforced across all primary containers, buttons, and image frames to maintain a sophisticated, rigid architectural feel.
- **Accents:** Use circles and 45-degree diagonal lines as graphic accents to denote "stamps," "catalog markers," or "navigation nodes" along the timeline. These shapes serve as a nod to mid-century graphic design.

## Components

### Timeline Navigation
A persistent vertical line (2px, Sepia) that runs through the center or left-aligned margin. As the user scrolls, "Nodes" (geometric circles) highlight the current archival year or collection.

### Buttons
Primary buttons are solid Deep Black with Parchment text, featuring sharp 0px corners. Secondary buttons use a 1px Black outline. Text is always uppercase `label-sm` for an authoritative, "official" look.

### Archival Cards
Used for product or lookbook entries. These cards feature a hairline 1px border and excessive internal padding. Captions are placed in a "Table of Contents" style—left-aligned title with right-aligned date or serial number.

### Input Fields
Minimalist underlines (1px Black) rather than enclosed boxes. Labels sit above in uppercase `label-sm` weight to resemble vintage catalog forms.

### Interactive Nodes
Small, clickable geometric shapes (squares/triangles) used for pagination or revealing metadata, reinforcing the "Neo-Retro" technical-meets-classical aesthetic.