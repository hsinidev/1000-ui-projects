---
name: Clinical-Kinetic
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#424752'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#727784'
  outline-variant: '#c2c6d4'
  surface-tint: '#115cb9'
  primary: '#003f87'
  on-primary: '#ffffff'
  primary-container: '#0056b3'
  on-primary-container: '#bbd0ff'
  inverse-primary: '#acc7ff'
  secondary: '#006b5f'
  on-secondary: '#ffffff'
  secondary-container: '#8ef5e3'
  on-secondary-container: '#007165'
  tertiary: '#404242'
  on-tertiary: '#ffffff'
  tertiary-container: '#575959'
  on-tertiary-container: '#cfd0d0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#acc7ff'
  on-primary-fixed: '#001a40'
  on-primary-fixed-variant: '#004491'
  secondary-fixed: '#8ef5e3'
  secondary-fixed-dim: '#71d8c7'
  on-secondary-fixed: '#00201c'
  on-secondary-fixed-variant: '#005047'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  section-gap: 80px
---

## Brand & Style

The design system establishes a high-performance environment for elite sports medicine. The "Clinical-Kinetic" aesthetic bridges the gap between sterile medical precision and the dynamic energy of human movement. The brand personality is authoritative and expert-led, yet technologically progressive, designed to evoke a sense of rapid, data-backed recovery.

The visual style utilizes **Soft-UI Neomorphism** to create tactile, interactive surfaces that feel ergonomic and responsive. This is balanced by a **Minimalist** layout structure that prioritizes high-resolution medical imagery—specifically musculoskeletal renderings and athletes in motion—to ground the digital experience in physical reality. The overall emotional response is one of "Technical Trust": the user should feel they are in a state-of-the-art facility where recovery is engineered.

## Colors

The palette is anchored by **Medical Blue (#0056B3)**, providing a foundation of institutional trust and clinical depth. This is accented by **Mint (#98FFED)**, used sparingly to signify "Kinetic Energy," vitality, and successful rehabilitation milestones. 

**Sterile White (#FFFFFF)** serves as the primary canvas, ensuring a clean, hygienic atmosphere. A secondary neutral, a very cool-toned slate grey, is utilized for backgrounds to allow the white neumorphic elements to "pop" via subtle shadow play. High-contrast states should prioritize the Blue-on-White combination, while Mint is reserved for interactive highlights, progress indicators, and "active" recovery states.

## Typography

This design system uses **Lexend** for headlines to leverage its athletic, highly readable, and structured geometric qualities. It communicates forward momentum and clarity. For body copy and labels, **Manrope** provides a refined, modern, and trustworthy tone that remains legible even in dense medical data views.

Headlines should use tight letter-spacing to appear "compact" and engineered. Body text requires generous line-height to maintain a "breathable" clinical feel. Labels are frequently used in uppercase with slight tracking to differentiate data points from narrative text.

## Layout & Spacing

The system employs a **Fixed Grid** on desktop (12 columns) and a **Fluid Grid** on mobile devices. The layout philosophy is "Spacious Precision," using an 8px base unit to ensure all elements align to a rigorous mathematical rhythm. 

Large margins and significant vertical gaps between sections are intentional, mimicking the organized, uncluttered environment of a premium rehabilitation clinic. Imagery should often break the grid or use "Bleed" layouts to convey kinetic energy and movement, while data-heavy medical information remains strictly contained within cards.

## Elevation & Depth

Elevation is the primary driver of the "Soft-UI" aesthetic. Rather than traditional floating shadows, this design system uses **Neumorphic Extrusion**. Surfaces appear to be molded from the background material.

- **Raised Elements (Buttons, Cards):** Achieved using two shadows—a light shadow (White, top-left) and a dark shadow (Soft Blue-Grey, bottom-right).
- **Sunken Elements (Input Fields, Progress Wells):** Achieved using inner shadows to create an "etched" or "carved" appearance.
- **Interactive Depth:** When pressed, buttons transition from a raised state to a sunken state, providing tactile physical feedback.
- **Glassmorphism:** Reserved exclusively for high-level navigation overlays or floating medical charts to maintain visual hierarchy without breaking the "physical" mold of the UI.

## Shapes

The shape language is **Rounded (Level 2)**. This balance avoids the "aggressiveness" of sharp corners and the "juvenile" feel of full pills. A 0.5rem (8px) base radius is applied to standard components, while larger containers like cards use 1.5rem (24px) to emphasize the soft, molded nature of the Neumorphic surfaces. Circular shapes are reserved strictly for iconography backgrounds and user avatars to represent "joint rotation" and fluid motion.

## Components

### Buttons
Primary buttons use the Medical Blue background with white text, featuring a subtle raised neumorphic effect. Secondary buttons are White with Blue text. The "Active" state for buttons must use an inner shadow to simulate being pressed into the surface.

### Cards
Cards are the primary container for medical data. They should have no visible border; depth is defined entirely by the dual-shadow neumorphic technique. Padding within cards should be generous (min 24px) to maintain the clinical feel.

### Input Fields
Inputs are "sunken" into the UI using inner shadows. The focus state is indicated by a 2px Mint (#98FFED) glow, symbolizing a "connection" or "activation."

### Chips & Tags
Used for identifying injury types or muscle groups. These should be flat with a 1px Blue border or a light Mint tint to distinguish them from the interactive raised buttons.

### Kinetic Progress Bars
Progress bars for rehabilitation goals use a "well" (sunken) background with a Mint (#98FFED) fill. The fill should have a slight outer glow to suggest energy and vitality.

### Medical Imagery Containers
Imagery should be framed with Soft-UI "frames" or use organic, mask-like shapes that mimic anatomical structures rather than simple rectangles.