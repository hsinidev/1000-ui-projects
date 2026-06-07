---
name: CultureCloud Design System
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
  on-surface-variant: '#3e4850'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#6e7881'
  outline-variant: '#bec8d2'
  surface-tint: '#006591'
  primary: '#006591'
  on-primary: '#ffffff'
  primary-container: '#0ea5e9'
  on-primary-container: '#003751'
  inverse-primary: '#89ceff'
  secondary: '#a43073'
  on-secondary: '#ffffff'
  secondary-container: '#fc79bd'
  on-secondary-container: '#76014e'
  tertiary: '#4953bc'
  on-tertiary: '#ffffff'
  tertiary-container: '#8792fe'
  on-tertiary-container: '#17228f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#89ceff'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#004c6e'
  secondary-fixed: '#ffd8e7'
  secondary-fixed-dim: '#ffafd3'
  on-secondary-fixed: '#3d0026'
  on-secondary-fixed-variant: '#85145a'
  tertiary-fixed: '#e0e0ff'
  tertiary-fixed-dim: '#bdc2ff'
  on-tertiary-fixed: '#000767'
  on-tertiary-fixed-variant: '#2f3aa3'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  title-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Plus Jakarta Sans
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
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The brand personality is optimistic, celebratory, and connective. This design system is built to transform corporate recognition into a vibrant social experience, moving away from stiff HR tools toward an interface that feels as intuitive and engaging as a modern social feed. The target audience is a diverse, digital-native workforce that values transparency and instant feedback.

The chosen style is **Minimalism infused with Glassmorphism**. By prioritizing heavy whitespace and "Airy" layouts, we allow the content—employee achievements and peer stories—to breathe. Translucent layers and subtle background blurs create a sense of depth without adding visual weight, while micro-interactions provide a tactile, "squishy" response that makes the act of giving recognition feel rewarding.

## Colors
The palette is centered on a "Morning Sky" concept. **Sky Blue** serves as the primary driver for actions and brand presence, evoking clarity and trust. **Soft Pink** is used strategically for emotional highlights, such as "likes," heart reactions, and celebratory milestones. 

The color application relies heavily on gradients between the primary and secondary colors to signify "momentum" and "growth." Backgrounds remain almost entirely white or very light gray to maintain the airy aesthetic, using the primary and secondary colors only as high-chroma accents or soft glow effects behind cards.

## Typography
**Plus Jakarta Sans** is the sole typeface for this design system. Its modern, rounded terminals perfectly mirror the friendly and approachable brand personality. 

Headlines use heavy weights (700-800) with tight tracking to create a rhythmic, editorial feel in the social feed. Body copy is set with generous line height (1.6) to ensure legibility during long scrolling sessions. We utilize "Display" sizes specifically for milestone numbers (e.g., "Years of Service" or "Points Earned") to celebrate achievement with scale.

## Layout & Spacing
This design system utilizes a **fluid grid** model with a mobile-first philosophy. The layout centers on a primary vertical feed, optimized for single-hand interaction on mobile devices.

A strict 8px linear scale governs all padding and margins to maintain a consistent visual rhythm. Elements within the feed—recognition cards, user stories, and comment threads—use generous internal padding (stack-lg) to emphasize the "Airy" feel. On desktop, the layout expands to a 12-column grid, but the core feed remains centered and constrained to a readable width, flanked by secondary utility widgets (e.g., Leaderboards, Upcoming Birthdays).

## Elevation & Depth
Depth is communicated through **ambient shadows** and **glassmorphism** rather than traditional hard borders. 

1.  **Level 0 (Surface):** The main background, using the neutral background color.
2.  **Level 1 (Cards):** Recognition cards use a high-spread, low-opacity shadow (Color: Sky Blue at 5% opacity) to feel as if they are floating gently above the surface.
3.  **Level 2 (Overlays):** Modals and bottom sheets utilize a backdrop blur (20px) and 80% white opacity to maintain context with the feed behind them.
4.  **Level 3 (Interactions):** Active states on buttons and "high-five" actions trigger a soft glow effect using the secondary pink or primary blue, creating a sense of digital illumination.

## Shapes
The shape language is defined by **Rounded (Level 2)** geometry. Standard components like cards and input fields use a 0.5rem (8px) radius, while buttons and high-frequency interaction points utilize a fully rounded "pill" shape (rounded-xl) to encourage clicking.

Avatars are always circular to emphasize the human, social element of the platform. Icons are contained within soft, rounded-square backgrounds with a subtle 10% tint of the primary color to keep the interface looking lightweight and modern.

## Components

### Buttons & Actions
Primary buttons feature a horizontal gradient from Sky Blue to Tertiary Indigo. They should have a "bouncy" hover state (scale 1.02) and a slight shadow increase. Secondary buttons are "ghost" style with a Sky Blue border and soft blue hover fill.

### Recognition Cards
These are the heart of the system. They feature a glassmorphic header, large emoji support for reactions, and a dedicated "Celebrate" button. The card should support rich media (photos/videos) with a 16:9 aspect ratio and rounded corners matching the system's Level 2 rounding.

### Chips & Tags
Used for skills or core values (e.g., "Leadership," "Innovation"). These are pill-shaped with low-contrast background tints and include a leading icon or emoji.

### Inputs & Forms
Input fields are "Social-style"—floating labels are avoided in favor of clear, rounded containers with subtle 1px borders that turn Sky Blue on focus. Emoji pickers are integrated directly into the text area for quick recognition replies.

### The "High-Five" Interaction
A unique component for peer recognition. A large, circular floating action button (FAB) that, when tapped, triggers a confetti burst micro-interaction using the system's palette.