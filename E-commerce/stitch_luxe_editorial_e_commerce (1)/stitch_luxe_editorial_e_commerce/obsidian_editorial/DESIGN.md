---
name: Obsidian Editorial
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c8'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c6c6c7'
  primary: '#ffffff'
  on-primary: '#2f3131'
  primary-container: '#e2e2e2'
  on-primary-container: '#636565'
  inverse-primary: '#5d5f5f'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#ffffff'
  on-tertiary: '#342f2d'
  tertiary-container: '#eae1dd'
  on-tertiary-container: '#696360'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c7'
  on-primary-fixed: '#1a1c1c'
  on-primary-fixed-variant: '#454747'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#eae1dd'
  tertiary-fixed-dim: '#cec5c1'
  on-tertiary-fixed: '#1f1b19'
  on-tertiary-fixed-variant: '#4b4643'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  display-xl:
    fontFamily: Newsreader
    fontSize: 120px
    fontWeight: '300'
    lineHeight: 110px
    letterSpacing: -0.04em
  display-lg:
    fontFamily: Newsreader
    fontSize: 80px
    fontWeight: '300'
    lineHeight: 84px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 56px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 32px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 28px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.15em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-mobile: 24px
  margin-desktop: 64px
  section-gap: 160px
---

## Brand & Style

The design system is engineered for the high-end luxury fashion space, prioritizing an immersive, cinematic experience that mirrors the feeling of a physical coffee-table book. The brand personality is authoritative yet quiet, utilizing extreme minimalism and high-contrast visuals to let high-resolution photography command attention.

The aesthetic follows a **Minimalist-Cinematic** movement. It relies on dramatic shifts in scale and generous "negative space" (deep obsidian) to create a sense of exclusivity and prestige. Every interaction is designed to feel deliberate and weighted, moving away from the frantic pace of traditional web interfaces toward a curated, slow-consumption editorial flow.

## Colors

The palette is strictly limited to maintain a focused, high-contrast environment. 

- **Obsidian (#050505):** The base surface. It provides a deeper-than-black foundation that makes images pop and ensures the "paper white" text feels luminous.
- **Charcoal (#1a1a1a):** Used for structural containers, cards, and subtle sectioning. This provides enough contrast against the obsidian base to define shape without introducing jarring lines.
- **Paper White (#f5f5f5):** The primary ink. It is slightly softened from pure white to prevent eye strain while maintaining a crisp, editorial clarity.
- **Muted Accents:** A secondary tier of grays (#404040) is used for tertiary information and borders to ensure the hierarchy remains sophisticated.

## Typography

This design system utilizes a high-contrast typographic pairing to establish editorial authority. 

**Newsreader** is the voice of the system. It should be used for all large-scale headlines and pull quotes. For "Display" levels, use a lighter weight (300) and tighter letter spacing to achieve a sophisticated, modern serif look.

**Inter** provides the functional backbone. It is used for body copy, navigational elements, and UI labels. By utilizing a clean, utilitarian sans-serif for functional text, the system maintains a contemporary feel that balances the traditionalism of the serif headlines. Use uppercase labels with increased letter-spacing for category tags and small UI indicators.

## Layout & Spacing

The layout philosophy is based on a **Fixed Grid** with exaggerated vertical rhythm. 

- **The 12-Column Grid:** Desktop layouts follow a 1440px max-width grid. Use wide 32px gutters to give content room to breathe.
- **Editorial Breathing Room:** Section gaps are intentionally large (160px+) to force the user to focus on one piece of content at a time. 
- **Asymmetric Balance:** Align secondary text elements to the center or right-third of the grid to create dynamic, magazine-style layouts rather than standard centered stacks.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering** and **Sophisticated Shadows**. 

Avoid heavy dropshadows. Instead, use "Environment Shadows"—very large blur radii (60px-100px) with extremely low opacity (15-20%) black shadows to lift charcoal containers off the obsidian surface. 

To define sections without breaking the immersive dark feel, use **Subtle Borders**. Borders should be 1px solid and colored at #1a1a1a (on obsidian) or #2a2a2a (on charcoal). This creates a "hairline" effect common in luxury print media.

## Shapes

The design system employs a **Sharp (0)** shape language. All containers, buttons, and image frames must have 0px border radii. 

The use of 90-degree angles reinforces the architectural and "high-fashion" nature of the design. Roundness is perceived as "friendly" or "approachable," which contradicts the desired "exclusive" and "imposing" brand personality. Every element should feel carved and precise.

## Components

### Buttons
Primary buttons are solid Paper White (#f5f5f5) with Obsidian text, 0px border-radius, and uppercase Inter labels. Secondary buttons are Ghost-style with a 1px Paper White border and no fill.

### Cards
Cards use the Charcoal (#1a1a1a) fill with no visible border. Imagery within cards should fill the entire container. Text overlays should appear only on hover or be placed directly beneath the card with generous padding.

### Input Fields
Inputs are minimal: a single 1px bottom border (#404040). On focus, the border transitions to Paper White (#f5f5f5). Labels should be small, uppercase, and placed above the field.

### Editorial Components
- **The Hero Spread:** A full-viewport image container with an oversized Newsreader headline overlapping the imagery.
- **The Pull Quote:** Center-aligned Newsreader Medium text, italicized, with 1px horizontal dividers above and below.
- **Navigation:** A persistent, minimal top-bar with ultra-thin hairlines. Use a "hidden" drawer for secondary links to maintain a clean visual field.