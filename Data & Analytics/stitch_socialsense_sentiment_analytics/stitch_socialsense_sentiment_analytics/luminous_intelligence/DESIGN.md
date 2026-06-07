---
name: Luminous Intelligence
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#121212'
  on-primary-container: '#7e7d7d'
  inverse-primary: '#5f5e5e'
  secondary: '#d0bcff'
  on-secondary: '#3c0091'
  secondary-container: '#571bc1'
  on-secondary-container: '#c4abff'
  tertiary: '#4cd7f6'
  on-tertiary: '#003640'
  tertiary-container: '#00151a'
  on-tertiary-container: '#008aa1'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#acedff'
  tertiary-fixed-dim: '#4cd7f6'
  on-tertiary-fixed: '#001f26'
  on-tertiary-fixed-variant: '#004e5c'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  display-sm:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-xs:
    fontFamily: Inter
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.08em
  data-point:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 12px
  margin-mobile: 16px
---

## Brand & Style

The brand personality of this design system is focused on **Precision Intelligence** and **Vibrant Connectivity**. It targets data analysts and brand managers who require immediate, actionable insights in a high-pressure environment. The UI evokes a sense of "The Command Center"—authoritative, futuristic, and highly organized.

The design style merges **Minimalism** with **Glassmorphism** and **High-Contrast** accents. By utilizing a deep matte foundation, we allow data visualizations to "pop" with neon-inspired vibrance, creating a clear hierarchy where the data is the hero. The aesthetic is sophisticated yet energetic, ensuring that real-time monitoring feels active rather than static.

## Colors

The palette is built upon a **Matte Black (#121212)** base to minimize eye strain during long monitoring sessions. Data is categorized through high-vibrancy gradients:
- **Vibrant Purple:** Represents brand influence and reach.
- **Electric Blue:** Signifies real-time connectivity and stream health.
- **Neon Pink:** Highlights critical alerts and high-sentiment peaks.

The neutral palette utilizes off-whites and cool greys for secondary text, maintaining high legibility without the harshness of pure white. Sentiment monitoring follows a specialized spectrum: deep emerald for positive, muted slate for neutral, and a luminous crimson for negative.

## Typography

This design system utilizes **Inter** for its exceptional clarity in high-density data environments. To handle the "mobile-first" requirement, typography emphasizes vertical hierarchy. Headings use tight letter-spacing and bold weights to command attention, while data points utilize a slightly larger, high-contrast weight to ensure critical metrics are readable at a glance. Label styles use uppercase tracking to distinguish metadata from primary content streams.

## Layout & Spacing

The layout philosophy follows a **High-Density Fluid Grid**. Given the mobile-first priority, we utilize a 4-column grid for mobile devices, expanding to 12-columns for tablet/desktop. 

The rhythm is built on a **4px base unit**. Dashboards use tight 12px gutters to maximize information density ("data-heavy"), while external margins remain at 16px to prevent content from feeling cramped against the screen edges. Data modules should be stacked vertically on mobile, utilizing card-based encapsulation to separate distinct sentiment streams.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and **Luminous Layering** rather than traditional shadows. 
1.  **Base Layer:** The Matte Black (#121212) background.
2.  **Surface Layer:** Semi-transparent containers (Background: `rgba(255, 255, 255, 0.05)`) with a `20px` backdrop blur.
3.  **Accent Layer:** Components at this level feature a `1px` inner stroke in a low-opacity version of the primary gradient to simulate a "glowing edge."

Shadows, when used, are colored (tinted with the accent purple or blue) and highly diffused (e.g., `0 8px 32px rgba(139, 92, 246, 0.15)`) to create the effect of light emitting from the screen.

## Shapes

The shape language is **Rounded (Level 2)**. This balance softens the technical, data-heavy nature of the UI, making it feel more like a modern consumer app while retaining professional structure. 
- **Cards/Modules:** 1rem (16px) corner radius.
- **Buttons/Inputs:** 0.5rem (8px) corner radius.
- **Sentiment Tags:** Full pill (100px) to distinguish them from structural elements.

## Components

- **Buttons:** Primary buttons use a linear gradient (Purple to Blue). Ghost buttons use a `1px` gradient border with no fill.
- **Sentiment Chips:** Small pill-shaped indicators. They use a low-opacity background of their status color (e.g., 10% Green) with a high-contrast text and a left-aligned dot icon for color-blind accessibility.
- **Data Cards:** Utilize the glassmorphic style with a subtle `1px` border. Headers within cards should be separated by a faint `rgba(255,255,255,0.1)` divider.
- **Real-time Feeds:** List items use a "glowing connector" line on the left side to indicate live updates.
- **Input Fields:** Matte finish with a slightly lighter grey (`#1E1E1E`). On focus, the border transitions into an Electric Blue glow.
- **Brand Health Gauges:** Circular progress indicators using the multi-color gradient, featuring a centered "Pulse" animation for real-time data ingestion.