---
name: Obsidian Protocol
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#c4c7c8'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c6c6c7'
  primary: '#ffffff'
  on-primary: '#2f3131'
  primary-container: '#e2e2e2'
  on-primary-container: '#636565'
  inverse-primary: '#5d5f5f'
  secondary: '#bfc7d2'
  on-secondary: '#29313a'
  secondary-container: '#3f4851'
  on-secondary-container: '#aeb6c1'
  tertiary: '#ffffff'
  on-tertiary: '#303031'
  tertiary-container: '#e5e2e3'
  on-tertiary-container: '#656465'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c7'
  on-primary-fixed: '#1a1c1c'
  on-primary-fixed-variant: '#454747'
  secondary-fixed: '#dbe3ef'
  secondary-fixed-dim: '#bfc7d2'
  on-secondary-fixed: '#141c24'
  on-secondary-fixed-variant: '#3f4851'
  tertiary-fixed: '#e5e2e3'
  tertiary-fixed-dim: '#c8c6c7'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474647'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
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
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max-width: 1280px
  gutter: 24px
  margin: 40px
  stack-xs: 4px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
  stack-xl: 80px
---

## Brand & Style

The brand personality is anchored in the intersection of high-stakes security and technical performance. This design system communicates "unbreakable" through a stealth-inspired, minimalist aesthetic that prioritizes clarity and precision. The target audience—elite digital nomads and security-conscious professionals—expects an interface that feels like a piece of high-end hardware: cold, calculated, and exceptionally durable.

The visual style merges **Minimalism** with **Glassmorphism**. By using translucent, layered surfaces, the interface mimics the complex internal construction of a premium tactical backpack. Every element serves a functional purpose, utilizing heavy whitespace to ensure that critical information is never obscured. The emotional response is one of total control, sophisticated calm, and technological superiority.

## Colors

The palette is strictly nocturnal, utilizing a "Stealth Dark" mode as the primary environment. **Deep Charcoal (#1A1A1B)** serves as the foundational base, providing a matte finish that reduces visual fatigue. **Midnight Blue (#101820)** is reserved for depth layers and container backgrounds, offering a subtle, oceanic chill that differentiates structural elements from the void.

**Crisp White (#FFFFFF)** is used exclusively for high-contrast typography and critical interactive points, ensuring immediate recognition. Accents are handled through desaturated blue-greys to maintain the monochromatic rigor. All colors must pass AAA accessibility standards when used against the dark backgrounds to ensure the "Security" aspect of the brand is reflected in the usability of the interface.

## Typography

The typography system relies entirely on **Inter** to project a systematic and utilitarian image. The hierarchy is designed for rapid scanning. Headlines utilize a bold weight and tight letter-spacing to feel impactful and grounded. 

Label styles are frequently set in uppercase with increased letter-spacing to mimic technical serial numbers and industrial markings. This reinforces the "tech-focused" narrative. Body text is prioritized for legibility with a generous line height, ensuring that even dense technical specifications are easily digestible.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop and a fluid model for smaller breakpoints. The structure is built on a 12-column grid with a strict 8px baseline rhythm. This mathematical precision mirrors the internal gear-organizers of the backpacks.

Spacing is used to create "breathing room" between high-security features. Wide margins (40px) ensure the content feels premium and exclusive, rather than cluttered. Vertical stacking follows a geometric progression, ensuring that related functional blocks are clearly grouped through proximity.

## Elevation & Depth

Depth is established through a combination of **Glassmorphism** and **Tonal Layering**. Instead of traditional drop shadows, this design system uses:

1.  **Backdrop Blurs:** Background surfaces use a 20px Gaussian blur with a semi-transparent Midnight Blue fill (opacity 60-80%). This creates a "frosted lens" effect that suggests sophisticated layering.
2.  **Inner Strokes:** Each elevated container features a 1px solid white inner border with a very low opacity (10-15%). This mimics the glint of light on a hard edge, reinforcing the "precise and durable" feeling.
3.  **Z-Index Hierarchy:** Higher-level elements (like modals or floating tooltips) use a more transparent fill and a sharper inner stroke to appear "closer" to the user.

## Shapes

The shape language is defined by **Soft (Level 1)** roundedness. While a 0px sharp corner feels aggressive, the 0.25rem radius used here suggests the "soft-goods" nature of high-end nylon and polymer materials. 

Buttons and input fields utilize this consistent 0.25rem radius to maintain a cohesive, industrial-design look. Larger cards and containers may scale to `rounded-lg` (0.5rem) to maintain visual proportion without losing the "stealth" edge.

## Components

**Buttons:** 
Primary buttons are solid White with Midnight Blue text, providing a "high-alert" contrast. Secondary buttons utilize the Glassmorphic style with a subtle 1px border. The hover state should include a subtle "glow" or increased border opacity rather than a color shift.

**Cards:** 
Constructed using the Glassmorphic specs. They should feature no external shadows, relying on the backdrop blur and internal stroke to separate them from the Charcoal base.

**Input Fields:** 
Dark, recessed containers with a 1px Midnight Blue border. On focus, the border transitions to White with a sharp transition, indicating an active security state.

**Status Chips:** 
Small, technical indicators using monochromatic fills (e.g., a dark grey for "Locked", a soft white for "Active"). They should look like physical LED indicators on hardware.

**Lists:** 
Clean, border-bottom separated items. Icons used in lists must be hairline-thin (1px stroke) to match the "Precise" design pillar.

**Additional Components:**
- **Security Meters:** Linear gauges showing "Vault Integrity."
- **Coordinate Tags:** Small, monospaced labels for geographical or technical data points.