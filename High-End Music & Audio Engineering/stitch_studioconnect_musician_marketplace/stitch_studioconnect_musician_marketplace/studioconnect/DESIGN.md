---
name: StudioConnect
colors:
  surface: '#f8fafa'
  surface-dim: '#d8dada'
  surface-bright: '#f8fafa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f4'
  surface-container: '#eceeee'
  surface-container-high: '#e6e8e9'
  surface-container-highest: '#e1e3e3'
  on-surface: '#191c1d'
  on-surface-variant: '#3e4949'
  inverse-surface: '#2e3131'
  inverse-on-surface: '#eff1f1'
  outline: '#6e7979'
  outline-variant: '#bdc9c8'
  surface-tint: '#006a6a'
  primary: '#006565'
  on-primary: '#ffffff'
  primary-container: '#008080'
  on-primary-container: '#e3fffe'
  inverse-primary: '#76d6d5'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#4d5d5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#657676'
  on-tertiary-container: '#ebfdfd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#93f2f2'
  primary-fixed-dim: '#76d6d5'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#d4e6e6'
  tertiary-fixed-dim: '#b8caca'
  on-tertiary-fixed: '#0e1e1f'
  on-tertiary-fixed-variant: '#3a4a4a'
  background: '#f8fafa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e3'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  button:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  container-padding: 20px
  gutter: 16px
---

## Brand & Style
The design system is built to bridge the gap between creative artistry and professional reliability. It establishes a high-trust environment for musicians and producers through a "Corporate Modern" aesthetic that prioritizes clarity, precision, and collaborative energy. 

The visual narrative is anchored by the concept of "The Perfect Take"—clean, intentional, and polished. This is achieved through expansive whitespace that allows artist portfolios to breathe, paired with rhythmic "Waveform" patterns that subtly reinforce the musical nature of the marketplace. The emotional response should be one of confidence and streamlined productivity.

## Colors
The palette utilizes **Deep Teal** as the primary driver for brand presence and critical actions, symbolizing depth and professional integrity. **Slate Grey** provides a grounded secondary layer, used for supporting UI elements and readable body text to reduce eye strain.

White is the foundational background color, ensuring a "clean studio" feel. A tertiary **Light Teal** is introduced for subtle highlights and active states, while the neutral off-white is reserved for section backgrounds to create soft separation between content blocks without using harsh lines.

## Typography
This design system employs **Inter** for its exceptional legibility and neutral, systematic character. The hierarchy is strictly enforced to ensure complex musician profiles and session data remain scannable. 

Headlines use tighter letter spacing and heavier weights to command attention, while body text maintains a generous line height for long-form descriptions. Small labels utilize an uppercase style with increased tracking to differentiate metadata (e.g., "INSTRUMENT," "BPM," "GENRE") from standard UI text.

## Layout & Spacing
The design system follows a mobile-first, fluid grid approach. On mobile devices, a 4-column grid is used with 20px outer margins to ensure content doesn't feel cramped against the screen edges. 

The spacing rhythm is based on an 8px base unit. Generous vertical padding (32px+) is encouraged between major sections to emphasize the "Modern" aesthetic and prevent visual noise. Content cards and list items should use a consistent 16px gutter to maintain a clean, rhythmic flow similar to a musical measure.

## Elevation & Depth
Depth is conveyed through **ambient shadows** and **tonal layers**. Shadows are extremely soft, utilizing the Primary Deep Teal color at a very low opacity (e.g., 4-8%) to tint the shadow, making it feel integrated with the brand rather than a generic grey.

To signify hierarchy, the design system uses:
1.  **Level 0 (Base):** Clean White background.
2.  **Level 1 (Cards):** Slightly elevated with a soft, diffused shadow (12px blur) to draw attention to session offers or artist profiles.
3.  **Level 2 (Modals/Overlays):** Stronger elevation to focus the user on a specific collaborative task.

A unique "Waveform" visual treatment is applied as a background texture on primary cards, using low-contrast, semi-transparent lines to create a sense of depth and movement without distracting from the text.

## Shapes
The shape language is defined as **Rounded**, utilizing a 0.5rem (8px) base radius. This creates an approachable and collaborative feel while maintaining a professional edge. 

Buttons and input fields follow this standard, while larger containers like "Artist Spotlight" cards may use a more pronounced 1rem (16px) radius to soften the layout. Avatars for musicians should be strictly circular to contrast against the geometric grid, symbolizing the individual at the heart of the tech.

## Components
-   **Buttons:** Primary buttons are solid Deep Teal with white text. Secondary buttons use a Slate Grey outline with a 1px border.
-   **Cards:** Musician cards feature a subtle Waveform pattern in the bottom third, acting as a decorative footer that holds "Rate" and "Availability" info.
-   **Inputs:** Form fields use a Slate Grey 1px border that shifts to Deep Teal on focus. Error states use a muted crimson that complements the teal palette.
-   **Chips/Tags:** Used for musical genres and skills. These should be low-contrast (Light Teal background) with Deep Teal text to remain legible but non-intrusive.
-   **Audio Player Bar:** A persistent mobile footer component for previewing session reels. It uses a frosted glass effect (Glassmorphism) with a 20px blur to allow the background content to subtly show through while maintaining focus on the playback controls.
-   **Trust Badges:** Small, circular icons with Deep Teal fills, used to denote "Verified Pro" or "Top Rated" musicians.