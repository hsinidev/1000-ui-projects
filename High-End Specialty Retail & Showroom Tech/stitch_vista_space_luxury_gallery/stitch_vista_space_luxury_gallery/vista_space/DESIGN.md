---
name: Vista-Space
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
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1a1a1a'
  on-primary-container: '#848282'
  inverse-primary: '#5f5e5e'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#181a1a'
  on-tertiary-container: '#818383'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Metropolis
    fontSize: 80px
    fontWeight: '300'
    lineHeight: 88px
    letterSpacing: -0.02em
  display-xl-mobile:
    fontFamily: Metropolis
    fontSize: 48px
    fontWeight: '300'
    lineHeight: 52px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Metropolis
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
    letterSpacing: 0.05em
  headline-lg-mobile:
    fontFamily: Metropolis
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 36px
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '300'
    lineHeight: 32px
    letterSpacing: 0.01em
  body-sm:
    fontFamily: Metropolis
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.2em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-desktop: 64px
  margin-tablet: 40px
  margin-mobile: 24px
  section-gap: 160px
---

## Brand & Style

This design system is engineered for the ultra-high-end architectural market, where the digital interface acts as a silent, sophisticated curator. The brand persona is **Authoritative**, **Cinematic**, and **Impeccable**, mirroring the experience of walking through a private contemporary art gallery. 

The visual style is **Minimalist-Galleria**. It prioritizes the architectural subject matter above all else, using full-bleed imagery and generous negative space to create a sense of breathability and scale. The interface employs precise geometry and extreme restraint, ensuring that every interactive element feels intentional and high-value. This system targets an elite demographic of investors and homeowners who value architectural integrity and quiet luxury over loud marketing.

## Colors

The palette is strictly monochromatic and achromatic to maintain an atmosphere of architectural permanence. 

- **Matte Black (#1A1A1A):** Used as the primary canvas color and for structural elements. It provides the "void" that allows photography to emerge with cinematic depth.
- **Stark White (#FFFFFF):** Reserved for high-contrast typography and critical UI markers. It creates a crisp, laser-etched aesthetic against dark backgrounds.
- **Platinum (#E5E4E2):** Utilized for secondary information, dividers, and subtle borders. It adds a metallic, premium texture that softens the transition between black and white.

The default mode is **Dark**, emphasizing the "Gallery" effect where lighting is focused on the "exhibits" (images) rather than the walls (UI).

## Typography

This design system utilizes **Metropolis** for its geometric precision and architectural skeleton. The typographic hierarchy relies on extreme scale and contrast.

- **Display & Headlines:** Set with light weights and slight negative letter-spacing for a sophisticated, editorial look. On desktop, display type should be used as a structural element of the page layout.
- **Body Text:** Set with generous line heights to ensure maximum legibility against dark backgrounds.
- **Labels:** Use all-caps with significant tracking (letter-spacing) to serve as navigational "markers," mimicking the small plaques found in galleries.

## Layout & Spacing

The layout philosophy is a **Fixed Grid with Fluid Voids**. It uses a strict 12-column grid on desktop, but emphasizes large vertical gaps between sections to allow content to "breathe."

- **Desktop:** 64px outer margins provide a luxurious frame for the content. Elements often span 6 or 8 columns to leave intentional "empty" space on the side.
- **Mobile:** Reflows to a single-column stack with 24px margins. Content density remains low.
- **Rhythm:** A 160px vertical gap between major sections creates a slow, deliberate scrolling experience, forcing the user to focus on one "architectural moment" at a time.

## Elevation & Depth

This design system rejects traditional shadows in favor of **Tonal Layering** and **Minimalist Outlines**. 

Hierarchy is established through:
- **Depth of Field:** Backgrounds use full-screen, high-resolution architectural renders. Overlays use a subtle background blur (10px) to indicate they are "hovering" over the space without obscuring it.
- **Ghost Borders:** Cards and containers use 1px solid borders in Platinum (#E5E4E2) at 20% opacity. They do not have shadows; they exist purely as geometric definitions.
- **Z-Index Precision:** Interactive overlays (drawers, modals) slide in with 100% opacity Matte Black backgrounds to completely focus the user's attention, treating the screen like a physical room transition.

## Shapes

The shape language is strictly **Rectilinear**. All corners are set to **0px (Sharp)**. 

This decision mirrors the hard edges of modern architecture and reinforces the "Authoritative" brand persona. Circular elements are only permitted for specific functional metaphors (e.g., a compass or a floorplan rotation tool) and should be rendered with ultra-thin 1px strokes.

## Components

- **Buttons:** Primary buttons are Stark White rectangles with Matte Black text in `label-caps`. Secondary buttons are "Ghost" style: 1px Platinum borders with no fill. On hover, the ghost button fills with Stark White and flips text to Matte Black.
- **Inputs:** Simple bottom-border lines (1px Platinum). Labels use `label-caps` and float above the line. Error states are indicated by a shift to a desaturated red, though color use is kept to a minimum.
- **Cards:** No background fill or shadows. 1px Platinum borders (low opacity) with images that zoom slightly on hover (scale 1.05) to provide a "lens" effect.
- **Navigation:** A persistent, ultra-thin top bar. Links use `label-caps`. Active states are indicated by a 1px underline that spans the full width of the text.
- **Gallery Viewer:** A custom component featuring a full-screen image with "Floating Controls" — minimalist White icons with no background containers, positioned in the corners of the viewport.
- **Floorplan Toggle:** A technical component using thin Platinum lines and monospaced-style labels to evoke architectural blueprints.