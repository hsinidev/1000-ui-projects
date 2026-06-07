---
name: Digital Film Festival
colors:
  surface: '#faf9f7'
  surface-dim: '#dadad8'
  surface-bright: '#faf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeec'
  surface-container-high: '#e9e8e6'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1b'
  on-surface-variant: '#444748'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f1ef'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#5f5e5b'
  on-secondary: '#ffffff'
  secondary-container: '#e5e2dd'
  on-secondary-container: '#656460'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1d1b17'
  on-tertiary-container: '#87837d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#e5e2dd'
  secondary-fixed-dim: '#c9c6c1'
  on-secondary-fixed: '#1c1c19'
  on-secondary-fixed-variant: '#474743'
  tertiary-fixed: '#e7e2db'
  tertiary-fixed-dim: '#cbc6bf'
  on-tertiary-fixed: '#1d1b17'
  on-tertiary-fixed-variant: '#494641'
  background: '#faf9f7'
  on-background: '#1a1c1b'
  surface-variant: '#e3e2e0'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 84px
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
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

This design system is built upon the concept of the "Digital Gallery"—a space where the interface recedes to allow the cinematic art to breathe. The brand personality is archival, curated, and intellectual, targeting a discerning audience of cinephiles and independent creators. 

The style utilizes **Minimalism** with an **Editorial** layout influence. It prioritizes the "void" (whitespace) as a functional element to create a sense of prestige and focus. Transitions are intentionally slowed to mimic the deliberate pace of a film projector, ensuring the user experience feels like a journey through a physical exhibition rather than a frantic digital browse.

## Colors

The palette for this design system is anchored by "Gallery White" (#F9F8F6), a warm, sophisticated neutral that avoids the sterility of pure white. Text and primary structural elements use "Deep Charcoal" (#1A1A1A) to provide a high-contrast, legible ground that mimics the ink of a prestige broadsheet.

While the UI remains monochromatic, the "Primary Color" is conceptually dynamic, derived from the dominant hues of the film posters currently on screen. When no film is featured, the system defaults to the Deep Charcoal for all interactive cues. Accents and dividers utilize a "Warm Gray" (#E5E2DD) to provide soft structure without disrupting the minimalist flow.

## Typography

Typography in this design system functions as both information and ornament. **Noto Serif** is used for headlines to convey a literary, classic cinematic feel. It should be typeset with generous leading and occasional italicization for emphasis.

**Manrope** serves as the functional workhorse for body copy and UI elements. Its clean, geometric proportions provide a contemporary counterpoint to the serif headers. To maintain the editorial aesthetic, use the "label-caps" style for metadata (e.g., duration, year, genre) to create a distinct visual hierarchy that separates narrative content from technical data.

## Layout & Spacing

This design system employs a **Fixed Grid** with an emphasis on **Asymmetry**. Layouts are built on a 12-column grid, but components often offset or overlap to break the "standard" web feel and mimic modern magazine spreads.

Extreme whitespace is a core requirement; a "Section Gap" of 128px is used to separate distinct cinematic collections. Negative space is not "empty" here—it is used to frame the film posters, which should vary in size across the layout to create a rhythmic, gallery-like browsing experience. Avoid centering all content; instead, use left-aligned blocks with wide right-side margins to guide the eye.

## Elevation & Depth

To maintain the sophisticated, flat-art aesthetic, this design system rejects traditional shadows. Instead, it uses **Low-contrast outlines** and **Tonal layers**. 

Depth is communicated through hairline borders (1px) in a slightly darker gray than the background. For interactive states or "hovered" film cards, use a subtle "scale-up" transition (1.02x) rather than a shadow. This keeps the interface feeling like paper or a physical wall rather than a digital stack of windows. Overlays (like navigation or search) should use a high-opacity "Gallery White" background with no blur, maintaining the crispness of the editorial direction.

## Shapes

The shape language of this design system is strictly **Sharp (0)**. Square corners reflect architectural precision and the rectangular nature of film frames. 

Buttons, image containers, and input fields must all maintain 90-degree angles. This rejection of modern "softness" reinforces the high-end, gallery-like atmosphere and ensures the focus remains on the organic shapes within the film imagery itself.

## Components

### Buttons
Primary actions are represented by "Ghost Buttons"—rectangular outlines with centered text in the Label Caps style. Secondary actions are text-only with a simple 1px underline that disappears on hover.

### Film Cards
Cards are the primary vehicle for cinematic imagery. They feature no visible borders or backgrounds; the image itself is the container. Title and metadata appear in a sophisticated Serif-Sans stack only upon hover or as a caption below the image, never as an overlay that obscures the artwork.

### Navigation
The navigation is a minimalist horizontal bar at the top with wide spacing between links. It should feel like a directory in a museum—functional, unobtrusive, and secondary to the exhibits.

### Inputs & Forms
Form fields consist of a single bottom-border (Deep Charcoal). Labels are placed above the line in the Manrope Sans-Serif font at a reduced size. There are no box-style inputs.

### Refined Borders
Use 1px vertical and horizontal lines to separate different "wings" of the gallery. These lines should not span the full width of the container, but rather act as "anchors" for the asymmetrical grid.