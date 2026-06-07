---
name: Serene Bio-Acoustics
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#434843'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#737872'
  outline-variant: '#c3c8c1'
  surface-tint: '#506354'
  primary: '#334537'
  on-primary: '#ffffff'
  primary-container: '#4a5d4e'
  on-primary-container: '#c0d5c2'
  inverse-primary: '#b7ccb9'
  secondary: '#5c5d6e'
  on-secondary: '#ffffff'
  secondary-container: '#e1e1f5'
  on-secondary-container: '#626374'
  tertiary: '#004c14'
  on-tertiary: '#ffffff'
  tertiary-container: '#00671e'
  on-tertiary-container: '#83e584'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8d5'
  primary-fixed-dim: '#b7ccb9'
  on-primary-fixed: '#0e1f13'
  on-primary-fixed-variant: '#394b3d'
  secondary-fixed: '#e1e1f5'
  secondary-fixed-dim: '#c5c5d8'
  on-secondary-fixed: '#191b29'
  on-secondary-fixed-variant: '#444655'
  tertiary-fixed: '#96f996'
  tertiary-fixed-dim: '#7adc7d'
  on-tertiary-fixed: '#002105'
  on-tertiary-fixed-variant: '#005316'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Bodoni Moda
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: Bodoni Moda
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style

This design system centers on the intersection of rigorous biological science and deep restorative wellness. The brand personality is authoritative yet gentle, evoking the feeling of a high-end research laboratory located within a primordial forest. It aims to evoke a sense of "auditory sanctuary"—where users feel safe, grounded, and scientifically supported.

The visual style is a sophisticated blend of **Glassmorphism** and **Tactile Minimalism**. It utilizes translucent layers to mimic the cellular structures of life, paired with organic, non-linear shapes that suggest fluid movement and sound waves. The UI should feel "alive"; elements do not simply appear but rather emerge through soft blurs and rhythmic "breathing" animations (subtle scaling and opacity shifts) that mirror human respiration.

## Colors

The palette is anchored by **Deep Moss Green**, providing a foundation of scientific authority and earthiness. This is contrasted by **Soft Lavender** and **Pale Violet**, which introduce a dreamlike, ethereal quality associated with soundscapes and relaxation. 

**Secondary Tones:**
- **Sage:** Used for interactive states and supportive backgrounds to bridge the gap between moss and white.
- **Pale Violet:** Used for subtle highlights and secondary gradients to enhance the bio-acoustic theme.

**Gradients & Transparency:**
Gradients should be used sparingly, primarily as background "auras" or within glass containers. Use a "Living Gradient" style: a soft transition from Soft Lavender to a transparent Sage, mimicking the dispersal of sound in a natural environment. Use high transparency (40-60%) for glass layers to maintain legibility while suggesting depth.

## Typography

This design system utilizes a high-contrast typographic pairing to balance scientific credibility with modern accessibility.

- **Headings (Bodoni Moda):** This high-contrast serif brings an editorial, authoritative feel. It should be used for all primary titles and significant callouts. The verticality of the font mirrors the peaks of a sound wave.
- **Body & Interface (Manrope):** A clean, geometric sans-serif that ensures maximum readability. The open apertures and balanced proportions provide a "breathable" feel to dense information.

**Styling Rules:**
Use generous line heights to prevent visual claustrophobia. For labels and small data points, use Manrope with increased letter spacing and uppercase styling to denote a "clinical" or "data-driven" precision.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** with wide, airy margins to reinforce the "Serene" brand pillar. Content should never feel cramped; the design system mandates significant "Negative Space Pockets" to allow the user’s eyes to rest.

**Grid Architecture:**
- **Desktop:** 12-column grid with a 1280px max-width. Gutters are fixed at 24px, while margins expand fluidly.
- **Tablet:** 8-column grid with 24px margins.
- **Mobile:** 4-column grid with 16px margins.

**Rhythm:**
Spacing follows an 8px incremental scale. However, for major section breaks, use "Atmospheric Spacing" (80px, 120px, or 160px) to create a sense of vastness and calm.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and **Ambient Shadows** rather than traditional heavy dropshadows. 

- **Surface Tiers:** Backgrounds are Crisp White or very Pale Violet. Floating elements (cards, menus) use a semi-transparent blur (Backdrop Filter: blur(20px)) to simulate a biological membrane.
- **Shadows:** Use "Leaf Shadows"—extremely diffused, low-opacity shadows (#4A5D4E at 5-10% opacity) with a large spread. This makes components appear as if they are floating gently on a surface rather than being pinned to it.
- **Interaction Depth:** When an element is hovered, the blur intensity increases slightly, and the "breathing" animation pauses, suggesting the system is "listening" to the user.

## Shapes

The shape language is strictly **Organic and Biological**. Avoid harsh 90-degree angles.

- **Containers:** Use a base radius of 1rem (16px) for standard cards. Large sections or hero containers should utilize "Squircle" or irregular "Blob" masks to mimic cellular forms.
- **Active States:** Interactive elements (buttons, toggles) should use rounded or pill-shaped geometries.
- **Sound Wave Elements:** Use continuous, smooth Bézier curves for all data visualizations. Lines should have rounded caps to maintain the soft aesthetic.

## Components

**Buttons:**
Primary buttons are Deep Moss Green with Crisp White text. They feature a unique "Pulse" state where a soft Lavender glow expands from the center when active, mimicking a sonar ping.

**Cards:**
Constructed with blurred glass backgrounds and subtle 1px inner borders in Soft Lavender. This creates a "specimen" look—as if the content is suspended in a clear medium.

**Input Fields:**
Minimalist design with no bottom border, only a soft-tinted background fill. On focus, the field expands slightly with a "breathing" transition and the label shifts to the Bodoni Moda typeface.

**Interactive Sound Waves:**
A signature component of this design system. These are live-reactive SVG patterns that animate based on user hover speed or audio playback. They should use a Sage-to-Lavender gradient stroke.

**Progress Indicators:**
Instead of linear bars, use "Circular Expansion" rings that grow and shrink in rhythm, resembling ripples in water or expanding lungs.