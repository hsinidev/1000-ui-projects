---
name: Vivid Pulse
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#4c4353'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#7e7384'
  outline-variant: '#cfc2d5'
  surface-tint: '#8234c6'
  primary: '#6100a4'
  on-primary: '#ffffff'
  primary-container: '#7b2cbf'
  on-primary-container: '#e4c2ff'
  inverse-primary: '#deb7ff'
  secondary: '#a03b56'
  on-secondary: '#ffffff'
  secondary-container: '#ff85a1'
  on-secondary-container: '#781b38'
  tertiary: '#6300a1'
  on-tertiary: '#ffffff'
  tertiary-container: '#7d2bbd'
  on-tertiary-container: '#e5c1ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f1dbff'
  primary-fixed-dim: '#deb7ff'
  on-primary-fixed: '#2d0050'
  on-primary-fixed-variant: '#680eac'
  secondary-fixed: '#ffd9df'
  secondary-fixed-dim: '#ffb1c0'
  on-secondary-fixed: '#3f0016'
  on-secondary-fixed-variant: '#81233f'
  tertiary-fixed: '#f2daff'
  tertiary-fixed-dim: '#e0b6ff'
  on-tertiary-fixed: '#2e004e'
  on-tertiary-fixed-variant: '#6a0baa'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  h1:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  h2:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  caption:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  xs: 0.25rem
  sm: 0.5rem
  md: 1rem
  lg: 1.5rem
  xl: 2.5rem
  gutter: 1.5rem
  max_container: 1440px
---

## Brand & Style

The design system is anchored in a "Creative & Human" aesthetic, specifically designed to bridge the gap between technical recruitment and personal storytelling. It leans into a **Modern-Glassmorphic** style, utilizing translucent layers and vibrant background blurs to create depth without losing the clean, professional air required of an ATS. 

The goal is to evoke a sense of optimism and approachability. By prioritizing video-first interactions, the UI treats candidates as people rather than data points. The visual language is high-energy yet soft, using significant whitespace to ensure the vibrant primary colors remain accents that guide the user's eye toward collaborative actions and human faces.

## Colors

The palette centers on a **Vibrant Purple** (#7B2CBF) for primary actions and brand presence, conveying professional authority with a creative edge. **Soft Pink** (#FF85A1) serves as the secondary accent, used for "Human" touchpoints like notifications, likes, or candidate highlights.

The interface maintains a high-contrast foundation with **Clean White** (#FFFFFF) backgrounds to ensure video content pops. Neutral shades are cool-toned to prevent the purple from feeling muddy, while a deep midnight purple is used for text to maintain better readability than pure black.

## Typography

This design system utilizes **Plus Jakarta Sans** for headlines to provide a soft, geometric, and welcoming first impression. Its rounded terminals mirror the UI's physical shape language. 

For body copy and functional labels, **Be Vietnam Pro** is used. It offers exceptional legibility at small sizes while maintaining a contemporary, friendly tone. Typography should always favor ample line-height to ensure the interface feels airy and less "cluttered" than traditional, data-heavy recruitment tools.

## Layout & Spacing

The layout follows a **Fluid Grid** model with a 12-column structure for dashboard views. Because this is a video-first platform, the spacing rhythm is generous to allow media thumbnails to breathe. 

Margins and gutters are set to a baseline of 24px (1.5rem) to create a clear separation between collaborative widgets and video feeds. Internal component padding should be "bubbly" (using the `lg` spacing unit) to reinforce the friendly aesthetic.

## Elevation & Depth

Visual hierarchy is achieved through **Ambient Shadows** and **Tonal Layers**. Shadows are specifically tinted with the primary purple (#7B2CBF) at a very low opacity (5-8%) to make elements feel like they are floating over a vibrant surface rather than a grey void.

Depth levels:
1.  **Level 0 (Surface):** The main application canvas.
2.  **Level 1 (Cards):** Low-offset, highly diffused shadows for candidate cards and sidebars.
3.  **Level 2 (Modals/Overlays):** Medium-offset shadows with a subtle backdrop blur (12px) to focus the user on video playback or rating tasks.

## Shapes

The shape language is overtly **Rounded**. This design system avoids sharp corners to maintain its "welcoming" tone. Standard buttons and input fields use a 0.5rem radius, while "Video Cards" and "Comparison Tables" use a more aggressive 1.5rem (`rounded-xl`) to feel like modern consumer hardware or high-end tablet interfaces.

## Components

### Buttons
Primary buttons are solid Purple with high-contrast White text, using a `pill` or `rounded-lg` shape. Secondary buttons should use a Soft Pink outline or a ghost style to keep the UI light.

### Video Cards
The hero component. These must feature a 16:9 aspect ratio with `rounded-xl` corners. Hover states should trigger a subtle scale-up effect and display a "Soft Pink" play icon overlay.

### Collaborative Rating Widgets
Star or heart ratings should utilize the Soft Pink palette. When multiple recruiters rate a candidate, use overlapping "avatar stacks" with a white border to show collaborative input.

### Human-Centric Form Fields
Fields should have thick, light-grey borders that turn Purple on focus. Labels should be phrased as questions (e.g., "Tell us about...") to maintain the conversational tone.

### Side-by-Side Comparison Tables
Unlike standard spreadsheets, these should use "Card-style columns." Each candidate is a vertical column with a video header, making the data feel like a profile comparison rather than a row of text.