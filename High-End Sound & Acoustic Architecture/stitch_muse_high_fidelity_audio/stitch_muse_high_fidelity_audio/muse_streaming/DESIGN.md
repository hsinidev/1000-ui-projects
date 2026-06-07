---
name: Muse-Streaming
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d7c1c3'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9f8c8e'
  outline-variant: '#524345'
  surface-tint: '#ffb2bc'
  primary: '#ffb2bc'
  on-primary: '#551e29'
  primary-container: '#c77b86'
  on-primary-container: '#4c1722'
  inverse-primary: '#8c4b55'
  secondary: '#f3bd78'
  on-secondary: '#462a00'
  secondary-container: '#664105'
  on-secondary-container: '#e3af6c'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a29'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffd9dd'
  primary-fixed-dim: '#ffb2bc'
  on-primary-fixed: '#3a0915'
  on-primary-fixed-variant: '#70343e'
  secondary-fixed: '#ffddb6'
  secondary-fixed-dim: '#f3bd78'
  on-secondary-fixed: '#2a1800'
  on-secondary-fixed-variant: '#633f03'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  technical-data:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  max-width: 1440px
---

## Brand & Style

This design system is engineered to evoke the atmosphere of a private, high-end listening lounge. The brand personality is exclusive, sophisticated, and deeply immersive, catering to the discerning audiophile who views music as a cinematic experience rather than background noise. 

The visual style leverages **Glassmorphism** to create a sense of depth and airiness within a dark environment. By utilizing frosted glass surfaces, subtle background blurs, and razor-thin borders, the interface feels like high-end hardware. Full-bleed cinematic imagery of artists and album art serves as the primary "wallpaper" for the UI, with the interface layers floating delicately above it. The emotional response is one of reverence for the medium—premium, precise, and profoundly dark.

## Colors

The palette is anchored in the "Deepest Black" (#050505) to ensure maximum contrast and visual disappearance of the hardware frame, allowing cinematic imagery to pop. "Charcoal" (#121212) serves as the primary surface color for glass containers.

The accent strategy utilizes a "Luxurious Rose Gold" duo:
- **Primary Rose (#B76E79):** Used for primary actions, high-fidelity status indicators, and critical interactive states.
- **Champagne Gold (#E0AC69):** Used for "Master" quality badges, premium tier features, and secondary interactive highlights.
- **Glass Stroke:** A constant 10% opacity white (#FFFFFF) is used for the thin borders essential to the glassmorphic aesthetic.

## Typography

Typography in this design system creates a rhythmic contrast between editorial elegance and technical precision.

- **The Serif (Playfair Display):** Reserved for artist names, album titles, and high-level section headers. It conveys the "Boutique" nature of the platform.
- **The Sans-Serif (Manrope):** A clean, modern grotesque used for all functional data, track listings, and technical specifications (bitrate, sample rate). 

Special attention is given to **Technical Data** styling: it uses Manrope with increased letter-spacing and uppercase styling to mimic the precision of high-end audio equipment displays.

## Layout & Spacing

This design system employs a **Fluid Grid** with generous margins to maintain a cinematic feel. 

- **Desktop:** A 12-column grid with 24px gutters. Side margins are expansive (64px) to allow the full-bleed background imagery to breathe.
- **Tablet:** 8-column grid with 24px gutters and 40px margins.
- **Mobile:** 4-column grid with 16px gutters and 20px margins.

The spacing rhythm follows an 8px base unit. Component internal padding should be generous (typically 24px or 32px) to reinforce the "luxury" feel of the interface, avoiding cluttered information density.

## Elevation & Depth

Depth is not communicated through shadows, but through **material translucency and blur intensity**.

- **Level 0 (Background):** Full-bleed cinematic artist/album imagery with a 40% black overlay.
- **Level 1 (Main UI):** Surfaces with `backdrop-filter: blur(20px)` and 60% opacity of #121212. Borders are 1px, 10% white.
- **Level 2 (Modals/Overlays):** Surfaces with `backdrop-filter: blur(40px)` and 80% opacity of #121212. These elements feature a subtle inner glow using a 0.5px Rose Gold top-border to suggest light hitting the edge of glass.

## Shapes

The shape language is "Softly Architectural." While the overall layout feels structured and linear, individual containers and interactive elements use a 0.5rem (8px) base radius. This prevents the dark, high-contrast aesthetic from feeling overly aggressive or sharp. 

Album art should always maintain a standard `rounded-lg` (16px) radius to differentiate "Content" from "Interface" containers.

## Components

### Premium Interactive Sliders
Volume and playback sliders are not mere lines. They consist of a 4px track in #121212 with a Rose Gold fill. The "thumb" or handle is a polished Rose Gold circle that glows slightly when active.

### High-Fidelity Meters
Frequency visualizers and level meters use thin, vertical bars. They transition from Rose Gold at the base to Champagne Gold at the peak, utilizing a 2px width with 1px gaps for a high-density, technical look.

### 'Master' Quality Badges
The 'Master' badge is a signature component. It features a solid #E0AC69 (Champagne Gold) background with #050505 text. It should use the `technical-data` typography spec and have a subtle outer glow of the same color to denote its premium status.

### Buttons
- **Primary:** Solid Rose Gold (#B76E79) with #050505 text.
- **Secondary (Glass):** Frosted glass background with 1px white (10% opacity) border and Rose Gold text.

### Cards
Cards for albums and playlists utilize a "floating" effect. No solid backgrounds; instead, they use the Level 1 Glassmorphic spec. On hover, the border opacity increases from 10% to 30%, and the background blur intensifies.