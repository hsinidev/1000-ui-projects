---
name: UnicornHunt Brand Identity
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#4c4452'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#7e7383'
  outline-variant: '#cfc2d4'
  surface-tint: '#803abd'
  primary: '#500088'
  on-primary: '#ffffff'
  primary-container: '#6b21a8'
  on-primary-container: '#d7a8ff'
  inverse-primary: '#dfb7ff'
  secondary: '#8127cf'
  on-secondary: '#ffffff'
  secondary-container: '#9c48ea'
  on-secondary-container: '#fffbff'
  tertiary: '#531b62'
  on-tertiary: '#ffffff'
  tertiary-container: '#6d337b'
  on-tertiary-container: '#e8a3f4'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f1dbff'
  primary-fixed-dim: '#dfb7ff'
  on-primary-fixed: '#2d0050'
  on-primary-fixed-variant: '#661aa3'
  secondary-fixed: '#f0dbff'
  secondary-fixed-dim: '#ddb7ff'
  on-secondary-fixed: '#2c0051'
  on-secondary-fixed-variant: '#6900b3'
  tertiary-fixed: '#fcd6ff'
  tertiary-fixed-dim: '#f3aeff'
  on-tertiary-fixed: '#340042'
  on-tertiary-fixed-variant: '#682f76'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  caption:
    fontFamily: Inter
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  container-max: 1280px
---

## Brand & Style

This design system is engineered to capture the high-velocity spirit of venture-backed startups and the elite talent seeking them. The brand personality is ambitious, tech-forward, and relentlessly energetic. By blending **High-Contrast Boldness** with **Modern Corporate** precision, the interface communicates both the excitement of a "Unicorn" opportunity and the professional reliability of a top-tier recruitment platform.

The visual direction avoids the clinical coldness of traditional job boards, instead opting for a high-fidelity aesthetic characterized by vibrant saturation, generous white space, and a confident "tech-maximalist" attitude. The goal is to evoke a sense of momentum and "the next big thing" for every user interaction.

## Colors

The palette is anchored by a commanding **Royal Purple**, chosen for its associations with ambition and premium quality. This is supported by a range of Greys that move from deep charcoals for text to airy silvers for UI scaffolding.

- **Primary (Royal Purple):** Used for key actions, brand moments, and active states.
- **Secondary (Electric Violet):** Used for highlights, accents, and interactive hover states to maintain high energy.
- **Neutrals:** A sophisticated slate-grey scale provides the professional backdrop necessary for a recruitment portal, ensuring content remains the focus.
- **Surface:** Pure White (#FFFFFF) is the primary surface color to maintain a clean, high-fidelity look, while a very light Grey (#F8FAFC) is used to differentiate card sections and background containers.

## Typography

This design system utilizes a dual-font strategy to balance character with utility. 

**Space Grotesk** is the voice of the brand. Its geometric, technical quirks and bold weights are used for headlines and display text to signal innovation and confidence. It should be set with tight letter-spacing at larger sizes to emphasize its "high-energy" impact.

**Inter** serves as the workhorse for all functional content. Its neutral, systematic nature ensures that job descriptions, candidate bios, and complex data tables remain highly legible and professional. This distinction in typography creates a clear information hierarchy: Space Grotesk tells the story, while Inter delivers the details.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop to ensure a curated, high-end editorial feel, transitioning to a fluid model for tablet and mobile devices. A standard 12-column grid is used with generous 24px gutters to give the high-energy elements room to breathe.

The spacing rhythm is based on an 8px scale. Large vertical spacing (48px to 80px) should be used between major sections to prevent the UI from feeling cluttered. Content density should be kept moderate: tight enough to feel "fast," but loose enough to feel "premium."

## Elevation & Depth

Depth in this design system is achieved through **Ambient Shadows** and **Tonal Layering**. 

1.  **The Base:** All primary page backgrounds reside at the lowest level.
2.  **The Canvas:** Cards and content containers use a subtle, semi-transparent grey border (1px) combined with a soft, diffused shadow.
3.  **The Interaction:** Shadows should have a slight purple tint (#6B21A8 at 5-8% opacity) to create a "glow" effect rather than a traditional dark drop shadow. This reinforces the high-energy brand color.
4.  **Floating Elements:** Modals and dropdowns use a higher blur radius (24px+) to signify their position at the top of the stack.

Avoid heavy black shadows; the goal is a "light-as-air" high-fidelity feel where elements seem to vibrate with energy.

## Shapes

The shape language for this design system is **Rounded (Level 2)**. This strikes a balance between the "friendly" approachable nature of modern startups and the "structured" professional nature of recruitment.

- Standard buttons and input fields use a 0.5rem (8px) radius.
- Large containers and job cards use a 1rem (16px) radius to create a soft, modern frame for content.
- Small decorative elements, like skill tags or status indicators, should use a pill-shape (full radius) to add a dynamic, "bubbly" energy to the interface.

## Components

### Buttons
Primary buttons are high-energy: solid Royal Purple with white text and a subtle upward shadow. On hover, they should scale slightly (1.02x) and increase shadow depth. Secondary buttons use a ghost style with a 2px purple border.

### Job Cards
Cards are the core unit of the portal. They feature a white background, 16px corner radius, and a subtle purple-tinted shadow. Typography within the card must be strictly hierarchical: Company name in Inter (Bold), Job Title in Space Grotesk (Medium), and Salary/Location in Inter (Caption).

### Chips & Tags
Used for "Tech Stack" or "Benefits." These should be pill-shaped with a very light purple background (#F5F3FF) and Royal Purple text. They provide a splash of brand color without overwhelming the layout.

### Input Fields
Clean and professional. They use a 1px Grey-200 border that transitions to a 2px Royal Purple border on focus. Labels are always visible in Inter (Label-Bold) above the field.

### Status Indicators
Use high-saturation colors for status (e.g., "Hiring," "Closed," "Interviewing") but keep the indicator small—either a dot or a subtle pill tag—to maintain the clean, high-fidelity aesthetic.