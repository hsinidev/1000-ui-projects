---
name: Dark Sea Design System
colors:
  surface: '#081421'
  surface-dim: '#081421'
  surface-bright: '#2e3a48'
  surface-container-lowest: '#040f1b'
  surface-container-low: '#101c29'
  surface-container: '#15202d'
  surface-container-high: '#1f2b38'
  surface-container-highest: '#2a3643'
  on-surface: '#d7e3f5'
  on-surface-variant: '#b9caca'
  inverse-surface: '#d7e3f5'
  inverse-on-surface: '#26313f'
  outline: '#849495'
  outline-variant: '#3a494a'
  surface-tint: '#00dce5'
  primary: '#e9feff'
  on-primary: '#003739'
  primary-container: '#00f5ff'
  on-primary-container: '#006c71'
  inverse-primary: '#00696e'
  secondary: '#4cd6fb'
  on-secondary: '#003642'
  secondary-container: '#00b2d6'
  on-secondary-container: '#003f4e'
  tertiary: '#e9fff9'
  on-tertiary: '#003731'
  tertiary-container: '#75f2e0'
  on-tertiary-container: '#006e63'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#63f7ff'
  primary-fixed-dim: '#00dce5'
  on-primary-fixed: '#002021'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#b3ebff'
  secondary-fixed-dim: '#4cd6fb'
  on-secondary-fixed: '#001f27'
  on-secondary-fixed-variant: '#004e5f'
  tertiary-fixed: '#7af7e5'
  tertiary-fixed-dim: '#5bdac9'
  on-tertiary-fixed: '#00201c'
  on-tertiary-fixed-variant: '#005048'
  background: '#081421'
  on-background: '#d7e3f5'
  surface-variant: '#2a3643'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
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
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system evokes the mysterious, tranquil, and high-tech nature of deep-sea exploration. The brand personality is authoritative yet immersive, positioning the consultancy as a bridge between advanced marine biology and luxury lifestyle. It targets high-end hobbyists and commercial entities who value precision and aesthetic excellence.

The visual style is a hybrid of **Glassmorphism** and **Minimalism**. By utilizing translucent layers and vibrant, glowing accents against a void-like background, the UI mimics the experience of looking through a high-end aquarium or a submersible viewport. The aesthetic relies on depth, fluidity, and the contrast between the dark "abyss" of the background and the "bioluminescent" interactive elements.

## Colors

The palette for this design system is anchored in the "Abyssal Zone." The primary background is a near-black midnight blue, providing the necessary contrast for the bioluminescent highlights. 

- **Primary (Neon Cyan):** Reserved for primary actions, critical data points, and "active" states. It should feel like a light source.
- **Secondary (Bioluminescent Teal):** Used for supporting interactive elements, hover states, and secondary information hierarchy.
- **Neutrals:** The background levels (#000814 and #001D3D) create the sense of water depth. Text is kept at high-contrast white or cool-tinted silver to ensure legibility.
- **Accents:** Use subtle gradients between Cyan and Teal to simulate fluid motion.

## Typography

Typography in this design system is clean and technical. **Space Grotesk** is used for headlines to provide a subtle futuristic, scientific edge that aligns with high-end aquarium technology. **Inter** is utilized for body copy and UI labels to ensure maximum readability and a systematic feel.

High contrast is non-negotiable. Headlines should typically be white (#FFFFFF), while body text can drop to a slightly desaturated blue-grey (#B0C4DE) to manage information hierarchy without sacrificing clarity. Letter spacing is slightly tightened on large headings for a premium feel and widened on small labels for legibility against dark, blurred backgrounds.

## Layout & Spacing

This design system employs a **fluid grid** model to mimic the expansive nature of the ocean. Layouts should feel breathable, with generous margins and large negative spaces that allow high-quality marine imagery to "breathe."

A 12-column grid is standard for desktop, with 24px gutters. Spacing follows an 8px rhythmic scale. Components and sections should use larger vertical padding (LG and XL units) to create a premium, editorial feel. Content should be grouped in floating "vessels" (cards) that appear to drift over the deep background.

## Elevation & Depth

Depth is the core of this design system's identity. Instead of traditional drop shadows, elevation is communicated through **Glassmorphism** and **Tonal Layering**:

1.  **Level 0 (The Abyss):** The base background (#000814).
2.  **Level 1 (Submerged Surface):** Secondary background (#001D3D) used for sectioning.
3.  **Level 2 (The Viewport):** Glassmorphic cards with a 15% white border, 10% white fill, and a 20px backdrop blur.
4.  **Level 3 (Bioluminescence):** Interactive elements that emit a "glow." Use a `box-shadow` with the Primary Cyan color, high blur (15-20px), and low opacity (0.3) to simulate light refracting through water.

Transitions between levels should be smooth and fluid, avoiding harsh cuts.

## Shapes

The shape language is **Rounded (Level 2)**. Sharp corners are avoided to maintain a fluid, organic "aquatic" feel. 

Standard components like buttons and input fields use a 0.5rem (8px) radius. Larger containers and glass cards use 1rem (16px) or 1.5rem (24px) for a softer, more modern appearance. This roundedness helps balance the technical feel of the typography with a more approachable, premium consumer aesthetic.

## Components

### Buttons
Primary buttons use a solid Neon Cyan fill with dark text. They must feature a subtle outer glow of the same color. Secondary buttons use a transparent background with a 1px Cyan border and cyan text.

### Glass Cards
Cards are the primary container. They feature heavy backdrop blurs (20px+) and thin, translucent borders. Content inside cards should be strictly aligned to the internal grid.

### Input Fields
Inputs are minimalist: a bottom-border only or a very subtle glass fill. On focus, the border and label should transition to Neon Cyan with a faint glow.

### Chips & Data Visualization
Used for "Fish Species" or "Water Parameters." Chips use a Bioluminescent Teal outline. Data visualizations (charts/graphs) should use the Cyan-to-Teal gradient, with lines appearing as "glowing filaments" against the dark background.

### Imagery
Images must be high-resolution, featuring deep-sea or high-contrast marine life. Apply a slight vignette to imagery to ensure it blends seamlessly into the dark UI background.