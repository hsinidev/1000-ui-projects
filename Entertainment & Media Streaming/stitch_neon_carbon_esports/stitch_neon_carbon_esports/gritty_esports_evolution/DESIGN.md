---
name: Gritty eSports Evolution
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#bccbb4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#869580'
  outline-variant: '#3d4a39'
  surface-tint: '#4ce346'
  primary: '#55ea4d'
  on-primary: '#003a03'
  primary-container: '#32cd32'
  on-primary-container: '#005105'
  inverse-primary: '#006e0a'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#00ee3c'
  on-tertiary: '#003907'
  tertiary-container: '#00ce32'
  on-tertiary-container: '#00500d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#75ff68'
  primary-fixed-dim: '#4ce346'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#005306'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#72ff70'
  tertiary-fixed-dim: '#00e639'
  on-tertiary-fixed: '#002203'
  on-tertiary-fixed-variant: '#00530e'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
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
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
---

## Brand & Style

The brand personality is aggressive, competitive, and uncompromising. This design system is built for an elite eSports audience that demands high-performance visuals and data-rich interfaces. It evokes a sense of "digital combat" and professional-grade machinery.

The visual style is a fusion of **Tactile / Skeuomorphism** and **High-Contrast / Bold** design movements. It utilizes physical metaphors like carbon-fiber textures and metallic finishes, punctuated by neon accents that simulate high-energy electronic components. The mood is dark, focused, and relentless, prioritizing immediate recognition of critical game stats and live broadcast events.

## Colors

The palette is anchored by "Kill-Zone Black" (#121212), providing a deep, high-contrast foundation that eliminates distractions. The primary accent is "Overclock Lime" (#32CD32), used exclusively for critical calls-to-action, active statuses, and high-priority data points.

Secondary grays provide structural depth, while a tertiary "Matrix Green" (#00FF41) is reserved for subtle glows and secondary success states. The color logic follows a high-signal-to-noise ratio: if it isn't vital information, it remains desaturated; if it’s live or interactive, it pulses with vibrant green.

## Typography

This design system uses **Space Grotesk** for headlines to deliver a technical, futuristic edge that mirrors the precision of pro-gaming hardware. **Lexend** is utilized for body text, chosen for its athletic clarity and exceptional readability during fast-paced streaming sessions. **Inter** handles the heavy lifting for data-dense labels and UI metadata, ensuring utility is never sacrificed for style. All headers should be treated with tight tracking and uppercase styling where maximum aggression is required.

## Layout & Spacing

The layout utilizes a **Fixed Grid** model on desktop (12 columns) to maintain the structural integrity required for complex data overlays and multi-stream views. On smaller viewports, it shifts to a fluid system with aggressive 16px gutters.

A strict 4px base-unit ensures a tight, "engineered" aesthetic. Padding is intentionally lean to allow as much content as possible on screen, catering to power users who monitor multiple stats, chats, and feeds simultaneously. Large margins are avoided; the UI should feel packed and powerful, filling the screen with information.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and **Bold Borders** rather than traditional shadows. Surfaces are stacked using varying shades of dark gray, with the highest "elevation" having the lightest gray tint.

To enhance the gritty aesthetic, a subtle **Carbon Fiber Texture** overlay is applied to the base background layer. Interactive elements do not use soft shadows; instead, they utilize **Primary Color Glows** (0px blur, 4-8px spread neon green) when active or hovered. 1px solid borders in a slightly lighter gray (#2A2A2A) define the edges of cards and containers, creating a "machined" look.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. Every button, input, card, and modal must feature hard 90-degree angles to reinforce the aggressive, military-grade tech theme. Angled "clipped corners" (45-degree cuts) may be used on primary container corners via CSS clip-paths to further the futuristic, high-performance aesthetic.

## Components

### Buttons
Primary buttons are solid "Overclock Lime" with black text, featuring sharp edges and a subtle inner-bevel effect to simulate a physical toggle. Secondary buttons use a 1px lime border with transparent backgrounds.

### Cards
Cards utilize a dark gray background with a subtle carbon-fiber texture overlay. A 1px border is mandatory. Header areas of cards should have a slightly lighter background to differentiate the "title bar" from the content.

### Inputs & Forms
Input fields are "hollow" (transparent background with a bottom border or full 1px border). On focus, the border turns lime green and emits a subtle outer glow.

### Status Indicators
Live indicators must pulse. A "LIVE" tag should be a sharp rectangle with a lime-green background and a high-frequency opacity animation to draw immediate attention.

### Progress Bars & Data Viz
Data visualizations should use thick, blocky strokes. Progress bars should be segmented into small blocks rather than a smooth continuous line, mimicking digital hardware readouts.