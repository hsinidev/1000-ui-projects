---
name: Kinetic Precision
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c4c5da'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#8e8fa3'
  outline-variant: '#434657'
  surface-tint: '#b9c3ff'
  primary: '#b9c3ff'
  on-primary: '#00228a'
  primary-container: '#0046ff'
  on-primary-container: '#d3d9ff'
  inverse-primary: '#0045fc'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#ffb4a3'
  on-tertiary: '#621000'
  tertiary-container: '#b72700'
  on-tertiary-container: '#ffd0c5'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b9c3ff'
  on-primary-fixed: '#001257'
  on-primary-fixed-variant: '#0033c1'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdad2'
  tertiary-fixed-dim: '#ffb4a3'
  on-tertiary-fixed: '#3d0700'
  on-tertiary-fixed-variant: '#8a1b00'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Spline Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Spline Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Spline Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Spline Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: Spline Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-point:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 12px
  bento-gap: 16px
---

## Brand & Style

The brand personality is high-octane and hyper-connected, designed for social media professionals who operate in real-time. This design system utilizes a **High-Contrast / Bold** aesthetic paired with **Minimalist** precision to ensure that massive amounts of data remain legible and actionable. 

The emotional response is one of "controlled energy"—the UI feels fast and reactive, mirroring the pace of social feeds. By utilizing stark blacks and whites against a singular, vibrating primary color, the system achieves a professional yet aggressive modern edge that differentiates it from traditional corporate SaaS.

## Colors

The palette is restricted to a high-contrast triad to maintain focus and energy.
- **Electric Blue (#0046FF):** Used exclusively for primary actions, active states, and connectivity indicators. It is the "pulse" of the system.
- **Pure Black (#000000) & Deep Grey (#111111):** The foundation. A dark mode default reduces eye strain for power users monitoring feeds for long durations.
- **White (#FFFFFF):** Reserved for high-priority typography and icons to ensure maximum "pop" against the dark canvas.
- **System States:** Success and Error states should use highly saturated greens and reds, but only in small doses (dots/lines) to avoid clashing with the Electric Blue.

## Typography

This design system uses **Spline Sans** for its youthful, geometric energy and exceptional readability in SaaS environments. It is paired with **Space Grotesk** for technical data points and labels to lean into the "technology and science" feel of social analytics.

- **Headlines:** Should be tight, bold, and impactful. 
- **Labels:** Use Space Grotesk in all-caps for metadata, categories, and timestamps to create a distinct visual "type-set" look.
- **Data Visualization:** Numbers within Bento boxes should be prominent, using Space Grotesk to emphasize the technical nature of the metrics.

## Layout & Spacing

The layout follows a **Fluid Bento-Box** philosophy. Content is organized into modular containers that rearrange based on screen size, prioritizing mobile-first consumption.

- **Bento Grid:** Use a consistent 16px gap between all cards. 
- **Mobile-First:** On mobile devices, the bento boxes stack into a single column with horizontal swiping permitted for secondary data clusters. 
- **Safe Areas:** Maintain a 20px outer margin on mobile to ensure thumb-friendly navigation.
- **Quick Actions:** A "Command Bar" or floating action button (FAB) should be anchored to the bottom-center of the mobile viewport for instant post-creation or alert clearing.

## Elevation & Depth

This design system eschews soft shadows in favor of **Tonal Layers** and **Low-Contrast Outlines**. 

- **Depth:** Created by stacking `#111111` (surface) on top of `#000000` (canvas). 
- **Borders:** Cards and Bento boxes use a subtle `1px` solid border of `#222222` to define boundaries without adding visual weight.
- **Active State:** When an element is focused or active, the border shifts to the Electric Blue primary color. 
- **No Shadows:** Shadows are not used; visual hierarchy is strictly managed through color value and scale.

## Shapes

The shape language is **Rounded**, balancing the aggressive high-contrast colors with a sense of modern approachability. 

- **Standard Containers:** Use a `16px` (1rem) radius for all Bento boxes.
- **Buttons & Chips:** Use a `24px` radius for a "Pill-like" feel on interactive elements, making them distinct from the data containers.
- **Alerts:** Real-time alert notifications should use the same `16px` radius but may feature a vertical accent bar on the left edge.

## Components

- **Buttons:** Primary buttons are Electric Blue with White text. Secondary buttons are Ghost-style with White borders and text. Mobile buttons must have a minimum 48px touch target.
- **Bento Cards:** Every card must have a `label-caps` header and a clear metric or visualization. Backgrounds are consistently `#111111`.
- **Quick-Action Chips:** Horizontal scrolling list of pills for filtering "All", "Instagram", "Twitter", etc. Active chips are filled with Electric Blue.
- **Real-Time Alerts:** High-priority notifications that slide in from the top or bottom with a vibrant glow effect (backdrop-filter) to catch the eye.
- **Data Visuals:** Charts should use Electric Blue for the primary data line, with a subtle gradient fill below the line at 10% opacity.
- **Inputs:** Dark fields with a `1px` grey border that "glows" Electric Blue on focus.