---
name: Sky-Sleek
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
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c5c7c8'
  on-tertiary: '#2e3132'
  tertiary-container: '#1c1f20'
  on-tertiary-container: '#848688'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 16px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for high-stakes IoT environments, where clarity and authority are paramount. It targets professional operators and high-end residential users who demand absolute reliability and sophisticated aesthetics.

The visual style is **Corporate Modern** with a **Glassmorphic** layer for contextual depth. It prioritizes precision and "high-tech elegance" through the use of sharp details, metallic textures, and a disciplined color application. The emotional response is one of controlled power—the interface should feel like a premium instrument panel rather than a consumer app. 

Key stylistic pillars include:
- **Precision-Oriented Layouts:** Mathematical alignment and consistent optical weights.
- **Glassmorphism:** Reserved for overlays, modals, and navigation sidebars to maintain environmental context.
- **Liquid Data Visualization:** Utilizing organic, fluid animations for progress bars and data streams to contrast against the rigid structural grid, symbolizing the "flow" of real-time data.

## Colors

The design system utilizes a "Deep Tech" dark-mode default to reduce eye strain in monitoring environments and to enhance the metallic qualities of the silver accents.

- **Primary (Deep Navy Blue):** Used for the primary canvas and deep structural backgrounds. It provides the "authoritative" foundation.
- **Secondary (Brushed Silver):** Applied to interactive borders, icons, and subtle gradients. This should mimic the sheen of high-end hardware.
- **Tertiary (Cloud White):** Reserved for high-priority typography and data readouts to ensure maximum contrast.
- **Surface & Overlays:** A semi-transparent variation of Deep Navy is used for glassmorphic elements, with a `blur` value of 20px and a 1px Brushed Silver stroke.
- **Data Visualization:** While the palette is monochromatic/navy, use a vibrant "Electric Cyan" or "Liquid Blue" for active data flows and success states.

## Typography

This design system employs **Inter** for its systematic, utilitarian clarity. For technical readouts, device IDs, and telemetry data, **JetBrains Mono** is introduced to provide a "developer-grade" precision feel.

- **Headlines:** Should be tight, bold, and authoritative. Use "Cloud White" for primary headings and "Brushed Silver" for secondary descriptions.
- **Body:** Optimized for legibility against dark backgrounds. Use a slightly increased line-height to prevent "shimmering" on high-resolution displays.
- **Labels:** Monospaced labels are used for all status indicators, timestamps, and metric units to emphasize the technical nature of the IoT platform.

## Layout & Spacing

The design system follows a **Fixed Grid** philosophy on desktop to maintain the "control console" feel, transitioning to a fluid model on mobile devices.

- **Grid:** A 12-column grid is used for desktop (1440px max-width).
- **Rhythm:** An 8px linear scale governs all padding and margins. 4px increments are used for fine-tuning technical components (e.g., small input fields).
- **Breakpoints:**
  - **Desktop (1200px+):** Full sidebar navigation, multi-pane dashboard views.
  - **Tablet (768px - 1199px):** Collapsed sidebar (icons only), stacked data widgets.
  - **Mobile (Under 767px):** Single column flow, bottom-sheet navigation for tool access.

## Elevation & Depth

In this design system, depth is communicated through **translucency and metallic strokes** rather than traditional drop shadows.

- **The Base Layer:** Deep Navy Blue (#001F3F).
- **The Surface Layer:** Standard containers use a slightly lighter navy with a 1px border of Brushed Silver at 20% opacity.
- **The Interactive Layer (Glassmorphism):** Overlays, dropdowns, and floating modals use a backdrop-blur (20px) with a semi-transparent Deep Navy fill.
- **Edge Highlighting:** Instead of shadows, use a "top-light" effect—a subtle 1px inner-shadow or border-top in Brushed Silver to simulate light hitting a metallic edge.

## Shapes

The shape language is **Soft (0.25rem)**, leaning toward a more technical, architectural feel. 

- **Components:** Standard buttons and input fields use a 4px (0.25rem) radius to maintain a sense of precision.
- **Containers:** Dashboard widgets and cards use a 8px (0.5rem) radius for a slightly softer internal containment.
- **Liquid Elements:** Specifically for data visualizations (progress bars, wave charts), corners should be fully rounded (Pill-shaped) to accentuate the "fluid" metaphor.

## Components

### Buttons
Primary buttons feature a subtle metallic gradient (Brushed Silver to Cloud White) with dark text. Secondary buttons are "Ghost" style with a Brushed Silver stroke. Interaction states should involve a subtle "glow" effect rather than a color shift.

### Input Fields
Inputs are dark-filled with a 1px bottom-border in Brushed Silver. Upon focus, the border transitions to the primary accent color with a faint outer-glow.

### Liquid Progress Bars
Unlike static bars, these utilize a CSS-driven "wave" or "bubble" animation within the fill. The fill color is a gradient of electric blues, suggesting movement and active energy consumption or data flow.

### Chips & Tags
Technical tags use JetBrains Mono in all-caps. They are rendered with a Deep Navy background and a high-contrast Silver border, appearing like "stamped" metal plates.

### Cards & Modals
Cards utilize the subtle glassmorphism effect. Modals are triggered with a "zoom-in" transition, utilizing heavy backdrop blurs to isolate the user's focus on the critical IoT control.

### IoT Status Indicators
Small, pulsating "Liquid" pips indicate device connectivity. A slow pulse signifies "Standby," while a rapid, fluid motion signifies "Active Transmission."