---
name: Zenith-Watchroll
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#bfc9c4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#89938f'
  outline-variant: '#3f4945'
  surface-tint: '#94d3c1'
  primary: '#94d3c1'
  on-primary: '#00382e'
  primary-container: '#004d40'
  on-primary-container: '#7ebdac'
  inverse-primary: '#29695b'
  secondary: '#ffb596'
  on-secondary: '#581e00'
  secondary-container: '#76320f'
  on-secondary-container: '#fd9d71'
  tertiary: '#f7bd48'
  on-tertiary: '#412d00'
  tertiary-container: '#593f00'
  on-tertiary-container: '#dea833'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#afefdd'
  primary-fixed-dim: '#94d3c1'
  on-primary-fixed: '#00201a'
  on-primary-fixed-variant: '#065043'
  secondary-fixed: '#ffdbcd'
  secondary-fixed-dim: '#ffb596'
  on-secondary-fixed: '#360f00'
  on-secondary-fixed-variant: '#76320f'
  tertiary-fixed: '#ffdea6'
  tertiary-fixed-dim: '#f7bd48'
  on-tertiary-fixed: '#271900'
  on-tertiary-fixed-variant: '#5d4200'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system embodies the heritage and precision of elite horology. The brand personality is **authoritative, timeless, and bespoke**, catering to discerning collectors who value craftsmanship over trends. The UI should evoke the emotional response of entering a private members' club or opening a custom-made leather trunk.

The aesthetic leans heavily into **Tactile / Skeuomorphic** elements mixed with **Minimalism**. We avoid the "flatness" of modern SaaS, instead favoring physical metaphors: surfaces that look like grain leather, borders that resemble fine saddle-stitching, and interactive elements that carry the weight and luster of antique brass. High-contrast transitions between deep greens and rich tans create a visual rhythm that is both luxurious and highly legible.

## Colors

The palette is anchored by **Deep Emerald Green**, which serves as the primary canvas, providing a sense of depth and stability. **Rich Tan Leather** is utilized for primary calls-to-action and navigational highlights, offering a warm, organic contrast to the cool green.

**Antique Brass** is reserved for accents, iconography, and decorative borders, acting as the "metal hardware" of the interface. The background remains a deep, near-black neutral to ensure the high-contrast luxury feel is maintained. 

- **Primary:** Deep Emerald Green (#004D40) for main backgrounds and containers.
- **Secondary:** Rich Tan Leather (#A0522D) for active states and primary buttons.
- **Tertiary:** Antique Brass (#B8860B) for accents, strokes, and specialized icons.
- **Neutral:** Deep Charcoal (#1A1A1A) for secondary backgrounds and structural shadows.

## Typography

The typographic scale emphasizes hierarchy and editorial elegance. **Noto Serif** provides a traditional, authoritative voice for all headings. For long-form text and technical specifications, **Work Sans** offers a clean, grounded counterpoint that ensures readability across all devices.

Use "label-caps" for small metadata, categories, or overlines to add a touch of watch-dial sophistication. Headlines should never be purely white; use a very light cream or silver-tinted white to maintain the "antique" feel.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model. Content is centered within a 12-column grid to create a focused, "boutique" browsing experience. Large margins on the periphery suggest exclusivity and prevent the interface from feeling cluttered.

Spacing follows a strict 8px rhythmic unit. Horizontal whitespace should be generous, mimicking the "breathability" of a high-end luxury catalog. Avoid dense information layouts; instead, allow each product or feature to occupy its own defined section.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Metallic Accents** rather than aggressive drop shadows. 

1.  **Base Layer:** Deep Emerald Green (#004D40).
2.  **Raised Surfaces:** Subtle inner-glows on Tan Leather containers to simulate the curvature of a leather roll.
3.  **Depth Accents:** Use a 1px solid stroke of Antique Brass (#B8860B) to define the edges of high-priority cards or "hardware" elements like buttons.
4.  **Shadows:** When used, shadows should be thin, sharp, and high-opacity (simulating a direct spotlight) rather than soft and ambient.

## Shapes

The shape language is primarily **Soft (0.25rem)**. We avoid overly round "pill" shapes, as they feel too casual for an elite horology brand. The slight rounding mimics the natural edge of a hand-cut leather strap.

A signature "Stitch Detail" should be applied to the borders of primary cards and hero sections—a dashed 1px Antique Brass line positioned 4px inside the container edge.

## Components

**Buttons:**
Primary buttons are Tan Leather (#A0522D) with Noto Serif text in white. They feature a 1px Antique Brass bottom border to simulate a metallic base. Hover states involve a slight deepening of the leather tone.

**Input Fields:**
Fields should be dark (#1A1A1A) with a subtle 1px border. On focus, the border transitions to Antique Brass. Use Work Sans for input text to ensure clarity.

**Cards:**
Luxury product cards utilize a "Leather-Inlay" style: a Deep Emerald background, a Tan Leather header, and a 1px Antique Brass stitch detail running vertically along the left edge.

**Chips:**
Used for watch specifications (e.g., "Automatic," "Swiss Made"). These should be ghost-styled with an Antique Brass outline and Work Sans uppercase labels.

**Lists:**
Inventory lists should be separated by thin Antique Brass dividers (0.5px opacity) to maintain a refined, ledger-like appearance.

**Additional Component - "The Vault Toggle":**
A bespoke switch component designed to look like a mechanical watch crown or a brass latch, used for high-security actions or switching between "Collection" and "Store" views.