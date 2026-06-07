---
name: SkillMap
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
  on-surface-variant: '#414844'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#002d1c'
  on-tertiary: '#ffffff'
  tertiary-container: '#00452e'
  on-tertiary-container: '#75b393'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#b1f0ce'
  tertiary-fixed-dim: '#95d4b3'
  on-tertiary-fixed: '#002114'
  on-tertiary-fixed-variant: '#0e5138'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  h1:
    fontFamily: Work Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
  h2:
    fontFamily: Work Sans
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
  h3:
    fontFamily: Work Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Newsreader
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Newsreader
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1280px
  gutter: 24px
  margin: 32px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system is built to evoke the prestige of traditional academic institutions while maintaining the velocity of modern professional development. The brand personality is **authoritative, nurturing, and precise**. It targets high-achieving professionals and L&D administrators who value structured growth and measurable progress.

The visual style follows a **Corporate Modern** approach with **Minimalist** influences. It prioritizes clarity and information density through a disciplined use of whitespace and a refined color palette. The aesthetic is "New Academic"—replacing heavy wood and leather with deep greens and metallic accents to signal both heritage and innovation.

## Colors

The palette is anchored by **Deep Forest Green**, which serves as the primary brand color to represent stability, growth, and depth of knowledge. **Metallic Gold** is used sparingly as a high-prestige accent to denote achievement, certification, and premium features.

**Off-White** provides a soft, low-strain canvas for long-form reading and data analysis. Secondary greens are utilized for success states and interactive elements, while a curated range of slate-toned neutrals handles borders and secondary text to maintain a professional, high-contrast environment.

## Typography

This design system utilizes a sophisticated pairing of **Work Sans** and **Newsreader**. 

**Work Sans** is the primary typeface for headlines and interface labels. Its grounded, professional geometry ensures that the platform feels reliable and systematic. **Newsreader** is employed for body copy and editorial content, bringing an intellectual, literary quality to the learning experience that improves readability during deep focus sessions. 

Use heavier weights of Work Sans for navigation and data points to maintain a clear visual hierarchy against the more elegant, serif body text.

## Layout & Spacing

The layout philosophy is based on a **Fixed Grid** system to reinforce the "Structured" aesthetic. Content is housed within a 12-column grid with a maximum container width of 1280px. This constraint ensures that dashboards and learning modules remain readable on ultra-wide monitors.

A strict 4px baseline grid governs the vertical rhythm. Large "stack" increments are used between major sections to create a sense of breathing room, while tighter gutters are used within component groups to emphasize their logical relationships.

## Elevation & Depth

Hierarchy is established primarily through **Tonal Layers** and **Low-Contrast Outlines**. Instead of heavy drop shadows, this design system uses subtle 1px borders in a muted version of the primary green or a soft slate. 

When depth is required for modals or dropdowns, use "Ambient Shadows"—diffused, low-opacity shadows (4-8% opacity) with a slight tint of the primary forest green to keep the shadows from appearing "dirty." Surfaces should feel like high-quality matte paper, stacked cleanly on top of one another.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding takes the edge off the institutional aesthetic without becoming overly playful or casual. 

Buttons, input fields, and cards should adhere to this 4px (0.25rem) standard. For "Growth" metaphors, such as progress bars or data visualizations, use 100% pill-rounding on the bar ends to contrast against the otherwise rectangular, structured environment.

## Components

### Buttons
Primary buttons use a solid Deep Forest Green fill with white text. Secondary buttons utilize the Gold accent as a 1.5px border with a transparent background. Hover states should subtly darken the green or introduce a gold tint to the border.

### Cards
Cards are the cornerstone of the platform. They feature a white background, a 1px soft-slate border, and a **2px Gold top-border accent** to denote "Featured" or "In-Progress" courses. This subtle metallic hit creates a premium feel without overwhelming the content.

### Inputs & Selects
Form fields use the Off-White background for the input area to distinguish them from the white card surfaces. Labels use Work Sans Medium to ensure clarity. Focus states use a 2px Deep Forest Green ring.

### Progress & Badges
Badges for certifications and skill levels should use the Gold color as a background for "Expert" levels and Forest Green for "Standard" levels. Progress bars should be slim (4px to 8px) to maintain the platform's sophisticated, minimalist tone.

### Course Grids
A structured grid of cards should be used for course libraries, ensuring uniform height across card titles to maintain a clean horizontal line across the interface.