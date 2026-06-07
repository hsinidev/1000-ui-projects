---
name: Desert Mirage
colors:
  surface: '#fff9ec'
  surface-dim: '#e0dac7'
  surface-bright: '#fff9ec'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf3e0'
  surface-container: '#f4eedb'
  surface-container-high: '#efe8d5'
  surface-container-highest: '#e9e2d0'
  on-surface: '#1e1c10'
  on-surface-variant: '#56423e'
  inverse-surface: '#333024'
  inverse-on-surface: '#f7f0dd'
  outline: '#89726d'
  outline-variant: '#ddc0ba'
  surface-tint: '#9f402d'
  primary: '#9f402d'
  on-primary: '#ffffff'
  primary-container: '#e2725b'
  on-primary-container: '#5a0d02'
  inverse-primary: '#ffb4a5'
  secondary: '#006a62'
  on-secondary: '#ffffff'
  secondary-container: '#5ef6e6'
  on-secondary-container: '#006f66'
  tertiary: '#8d4f11'
  on-tertiary: '#ffffff'
  tertiary-container: '#cb8241'
  on-tertiary-container: '#462200'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad3'
  primary-fixed-dim: '#ffb4a5'
  on-primary-fixed: '#3e0500'
  on-primary-fixed-variant: '#802918'
  secondary-fixed: '#61f9e9'
  secondary-fixed-dim: '#3adccc'
  on-secondary-fixed: '#00201d'
  on-secondary-fixed-variant: '#005049'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#ffb77d'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#6e3900'
  background: '#fff9ec'
  on-background: '#1e1c10'
  surface-variant: '#e9e2d0'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
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
  label-caps:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  stack-gap: 12px
  section-margin: 64px
---

## Brand & Style

The brand personality is grounded, artisanal, and serene. It targets travelers, architectural enthusiasts, and lifestyle-oriented users who value authenticity and tactile experiences. The design system evokes the emotional response of a high-end desert retreat—calm, sun-drenched, and naturally sophisticated.

The design style is a hybrid of **Tactile/Skeuomorphic** and **Minimalism**. It avoids the harshness of digital-first interfaces in favor of "Adobe Architecture" principles: thick walls, soft edges, and organic imperfections. Surfaces appear as hand-plastered clay rather than flat pixels. This is achieved through subtle noise textures and volumetric layering, creating a UI that feels physically present and warm.

## Colors

The palette is derived from the high desert at golden hour. **Terracotta** serves as the primary action color, providing warmth and energy. **Turquoise** is used sparingly as a high-contrast accent for success states or highlights, mimicking inlaid stones. **Sand** acts as a supportive mid-tone for secondary UI elements.

The "Earth-Toned" variation shifts the experience toward a muted, autumnal palette, replacing the vibrant turquoise with sage greens and deep ochres to emphasize a more rugged, naturalistic mood.

**Backgrounds & Textures:**
- Base surfaces use a "Stucco" finish: a subtle #FAF3E0 with a low-opacity grain overlay (2-4%).
- Text is rendered in deep charcoal (#2D2926) rather than pure black to maintain the organic feel.

## Typography

This design system utilizes **Plus Jakarta Sans** for headings to provide a soft, welcoming, and modern geometric feel that complements the rounded architecture. **Be Vietnam Pro** is used for body copy and labels, offering exceptional legibility with a contemporary, friendly tone that remains approachable across long-form content.

**Editorial Touches:**
- Display headings should be set in "Sentence case" to feel more personal.
- Labels use "All Caps" with generous tracking to create a sense of navigational clarity against the organic shapes.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to create centered, intentional compositions reminiscent of gallery layouts. A 12-column grid is used for desktop, but margins are intentionally wide (64px+) to prevent the content from feeling "crowded" by the edges of the screen.

Spacing is governed by an 8px rhythmic scale. However, "Architectural Spacing" is applied to major sections—using larger, odd-numbered intervals (e.g., 80px or 120px) to create the breathing room found in open desert landscapes.

## Elevation & Depth

Depth is communicated through **Ambient Shadows** that are tinted with the primary terracotta or sand hues, rather than neutral grays. Shadows are extremely diffused (high blur radius, low opacity) to mimic the way sunlight hits soft adobe corners.

- **Level 1 (Surface):** Flat stucco texture.
- **Level 2 (Cards):** 20px blur, 4% opacity shadow tinted #E2725B.
- **Level 3 (Modals/Floating):** 40px blur, 8% opacity shadow with a slight vertical offset to simulate high-noon sun.

Avoid sharp drops; every elevation change should feel like a molded protrusion from the base wall.

## Shapes

The shape language is the core differentiator of this design system. It avoids sharp 90-degree angles entirely. 

- **Primary Radius:** 16px (`rounded-lg`) is the standard for cards and containers.
- **Extreme Radius:** 24px+ (`rounded-xl`) is used for buttons and highlight sections to mimic hand-rolled clay edges.
- **Inner Radii:** Must be smaller than outer radii to maintain visual harmony (nested rounding).

All containers should feel "thick." Use a subtle 2px inner border (inset shadow) that is slightly lighter than the surface color to give the appearance of a bevel.

## Components

**Buttons:**
Primary buttons are heavily rounded (24px) with a subtle bottom-heavy shadow to make them feel "pressed" into the surface. Use Terracotta with white text.

**Input Fields:**
Fields should have a thick 2px border in Sand (#F4A460) and a soft cream background. Labels are always floating above the field in uppercase.

**Chips:**
Use the Turquoise (#40E0D0) color for active chips. They should resemble smooth river stones—fully pill-shaped with significant horizontal padding.

**Cards:**
Cards are the primary layout vehicle. They must feature a 1px soft-wheat border and a very light grain texture. Header images within cards should also inherit the large 16px border radius.

**Selection Controls:**
Checkboxes and Radios should feel tactile. When selected, they should look like an indent in the clay rather than a flat digital checkmark.

**Additional Component - "The Alcove":**
A specific container style used for featured content that uses a "negative" inner shadow to appear recessed into the page, like a built-in shelf in an adobe wall.