---
name: AeroGarden Logic
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
  on-surface-variant: '#3f4a3d'
  inverse-surface: '#2e3131'
  inverse-on-surface: '#eff1f1'
  outline: '#6f7a6c'
  outline-variant: '#becab9'
  surface-tint: '#006e20'
  primary: '#006e20'
  on-primary: '#ffffff'
  primary-container: '#98ff98'
  on-primary-container: '#007924'
  inverse-primary: '#77dc7a'
  secondary: '#29695b'
  on-secondary: '#ffffff'
  secondary-container: '#acedda'
  on-secondary-container: '#2e6d5f'
  tertiary: '#516161'
  on-tertiary: '#ffffff'
  tertiary-container: '#d9ebea'
  on-tertiary-container: '#5a6b6a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#93f993'
  primary-fixed-dim: '#77dc7a'
  on-primary-fixed: '#002105'
  on-primary-fixed-variant: '#005316'
  secondary-fixed: '#afefdd'
  secondary-fixed-dim: '#94d3c1'
  on-secondary-fixed: '#00201a'
  on-secondary-fixed-variant: '#065043'
  tertiary-fixed: '#d4e6e5'
  tertiary-fixed-dim: '#b8cac9'
  on-tertiary-fixed: '#0e1e1e'
  on-tertiary-fixed-variant: '#3a4a49'
  background: '#f8fafa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e3'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
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
  container-padding: 2rem
  gutter: 1.5rem
  stack-sm: 0.5rem
  stack-md: 1.5rem
  stack-lg: 3rem
---

## Brand & Style

The design system is engineered for the modern indoor horticulturalist, blending the organic vitality of botany with the precision of smart technology. The personality is optimistic, clinical yet inviting, and exceptionally clear. It aims to evoke a sense of "digital oxygen"—a UI that feels as fresh and life-giving as a well-tended greenhouse.

The aesthetic follows a **High-Tech Minimalism** approach with a touch of **Glassmorphism**. It prioritizes a spacious, airy layout to prevent cognitive load, reflecting the restorative nature of gardening. Visual interest is generated through subtle depth and high-quality negative space rather than heavy ornamentation.

## Colors

The palette is anchored by **Mint Green (#98FF98)**, used intentionally for primary actions and status indicators of health and growth. **White (#FFFFFF)** serves as the primary canvas color to maximize the "breath of fresh air" vibe.

- **Primary:** Mint Green is used for growth metrics, "on" states, and primary CTAs.
- **Secondary:** Deep Forest Green (#004D40) provides high-contrast legibility for text and grounding elements.
- **Tertiary:** Soft Mint Wash (#E0F2F1) is used for subtle background containers and hover states.
- **Neutral:** A cool-toned off-white (#F7F9F9) differentiates background layers from pure white cards.

## Typography

This design system utilizes **Space Grotesk** for headlines to inject a tech-forward, geometric, and futuristic personality. Its slightly idiosyncratic letterforms mirror the intersection of nature and engineering.

For functional text and data readout, **Inter** provides maximum clarity and a neutral, systematic feel. Use uppercase for `label-sm` styles to denote technical metadata (e.g., pH levels, Lux, Temperature). All body text should maintain generous line heights to preserve the airy aesthetic.

## Layout & Spacing

The system uses a **Fixed Grid** on desktop (1280px max-width) and a fluid layout on mobile. The spacing rhythm is based on an 8px modular scale, emphasizing large "safety margins" to ensure the UI never feels cramped.

Elements are grouped in logical "pods" with 24px gutters between them. Padding within cards and containers should be aggressive (minimum 32px) to reinforce the spacious atmosphere. White space is treated as a functional element that guides the eye toward critical growth data.

## Elevation & Depth

Depth is achieved through **Ambient Shadows** and **Tonal Layers** rather than heavy borders.

- **Level 1 (Base):** Pure White (#FFFFFF) surfaces on top of a Neutral (#F7F9F9) background.
- **Level 2 (Active Cards):** Use a very soft, highly diffused shadow (e.g., `0px 10px 30px rgba(0, 77, 64, 0.04)`) to make elements appear as if they are floating gently above the surface.
- **Level 3 (Overlays):** Modals and dropdowns utilize a backdrop blur (Glassmorphism) with 15px saturation to maintain context of the underlying "garden" data.

Avoid solid black shadows; always tint shadows with the secondary Forest Green to keep them feeling organic.

## Shapes

The shape language is defined by **Rounded** corners (0.5rem base) that soften the tech-heavy data. Large containers and main dashboard cards should use `rounded-xl` (1.5rem) to evoke a friendly, modern consumer hardware feel. Buttons and input fields use a consistent `rounded-lg` (1rem) for a comfortable, ergonomic touch target.

## Components

### Buttons
Primary buttons use a Mint Green background with Deep Forest Green text. They should have a subtle glow effect on hover rather than a color darken. Secondary buttons are outlined with a 1px Mint Green stroke.

### Chips & Tags
Used for plant status (e.g., "Hydrated," "Needs Light"). These use a semi-transparent version of the status color with a thin-line icon prefix.

### Lists & Data Rows
Data rows are separated by whitespace rather than lines. Each row should feel like a "floating slat" with subtle rounded corners.

### Input Fields
Inputs are borderless with a very light Mint Wash (#E0F2F1) background. The focus state is signaled by a 2px Mint Green bottom-border and a subtle lift in elevation.

### Icons
Use 1.5pt thin-line icons. Avoid solid fills. Icons should represent biological and technical concepts (e.g., a stylized leaf, a Wi-Fi signal, a water droplet).

### Specialized Components
- **Growth Gauge:** A circular progress ring using a gradient from Mint Green to White.
- **Environment Cards:** Large, airy cards displaying temperature and humidity with oversized typography.