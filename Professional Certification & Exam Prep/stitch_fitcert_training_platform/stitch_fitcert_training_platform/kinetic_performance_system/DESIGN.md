---
name: Kinetic Performance System
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
  on-surface-variant: '#414754'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc0'
  primary: '#0059bb'
  on-primary: '#ffffff'
  primary-container: '#0070ea'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc7ff'
  secondary: '#904d00'
  on-secondary: '#ffffff'
  secondary-container: '#fd8b00'
  on-secondary-container: '#603100'
  tertiary: '#515d70'
  on-tertiary: '#ffffff'
  tertiary-container: '#697589'
  on-tertiary-container: '#fefcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc7ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#ffb77d'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6e3900'
  tertiary-fixed: '#d7e3fa'
  tertiary-fixed-dim: '#bbc7dd'
  on-tertiary-fixed: '#101c2c'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  h1:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '700'
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
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
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

The brand personality of this design system is high-octane, authoritative, and relentlessly motivating. It is designed for the aspiring fitness professional who values speed, efficiency, and high-performance results. The UI avoids static layouts in favor of an "active" aesthetic that suggests momentum and progress.

The design style is **High-Contrast / Bold** layered with **Modern** efficiency. It utilizes aggressive typography and vibrant color pops to maintain engagement during intense study sessions. The visual language mirrors the environment of a high-end gym: clean, functional, and technologically advanced, ensuring the platform feels like a professional tool rather than just a digital textbook.

## Colors

The palette is anchored by **Electric Blue**, representing focus and professional reliability, and **Orange**, used strategically to inject energy and highlight calls to action. 

A deep navy tertiary color (#051121) is introduced to provide necessary grounding and high-contrast legibility for text elements against the bright primary colors. Gradients should transition diagonally from Electric Blue to a slightly deeper indigo, or utilize a "vibrant glow" effect where Orange highlights interact with Blue backgrounds to create a sense of kinetic energy.

## Typography

This design system utilizes **Lexend** for all headlines and labels. Its athletic, wide stance evokes a sense of strength and clarity, making it ideal for a fitness prep environment. Headings should be styled with tight tracking and heavy weights to command attention.

**Inter** is used for body text and instructional content to ensure maximum legibility and a clean, systematic feel. The contrast between the expressive, geometric Lexend and the neutral, functional Inter reinforces the balance between energy and professional certification standards.

## Layout & Spacing

The layout follows a **Fluid Grid** model based on a 12-column system. To emphasize the "Kinetic" aesthetic, the spacing rhythm uses an 8px base unit but favors generous outer margins and tight inner gutters to create clusters of information that feel like "modules" of energy.

Vertical rhythm should be varied; use larger gaps (xl) between major content sections to allow the UI to "breathe" like an athlete, while keeping interactive elements tightly grouped (sm/md) to facilitate fast-paced navigation. Use asymmetrical layouts occasionally—such as off-center text blocks—to suggest movement.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Vibrant Gradients** rather than traditional heavy shadows. Surfaces use subtle, semi-transparent overlays (Glassmorphism) when appearing over brand-colored backgrounds to maintain a sense of depth without losing the energetic color play.

When shadows are necessary, they are highly diffused and tinted with the primary Electric Blue to avoid "dirty" grey tones. Use "inner glows" on buttons and active states to make elements appear energized or "charged." High-contrast outlines in White or Electric Blue are used for secondary elements to maintain a sharp, technical look.

## Shapes

The shape language centers on **Rounded (Level 2)** containers to provide a modern, approachable feel that softens the high-contrast color palette. 

However, a "mixed-radius" strategy is applied: interactive triggers like buttons and progress indicators use a **Pill-shaped (Level 3)** radius to suggest movement and aerodynamics. Containers for study content or data visualizations maintain the standard 0.5rem (Level 2) radius to maximize space efficiency and maintain professional structure.

## Components

**Buttons:** Primary buttons use a vibrant Electric Blue to Orange horizontal gradient with white uppercase Lexend text. Hover states should include a slight scale-up effect (1.02x) to reinforce the kinetic theme.

**Chips & Tags:** Use high-contrast fills (Electric Blue with White text) for status indicators. Use "ghost" versions (outlined) for categories to prevent visual clutter.

**Input Fields:** Fields feature a subtle light-grey fill with a 2px bottom border that transforms into a full Electric Blue focus ring when active.

**Cards:** Cards should utilize a subtle backdrop blur when placed over gradients. Study cards should feature a prominent "Progress Bar" at the very top of the card, using the Orange secondary color to signal completion.

**Progress Indicators:** Use thick, rounded strokes for circular progress rings and linear bars. These should animate with a "spring" physics feel to match the fast-paced, professional narrative of this design system.

**Study Modules:** Incorporate large, bold "Success" states using the Orange color to celebrate milestones, ensuring the emotional response is always one of high-energy achievement.