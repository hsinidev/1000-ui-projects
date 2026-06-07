---
name: Clinical & Airy
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#434654'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#737685'
  outline-variant: '#c3c6d6'
  surface-tint: '#0c56d0'
  primary: '#003d9b'
  on-primary: '#ffffff'
  primary-container: '#0052cc'
  on-primary-container: '#c4d2ff'
  inverse-primary: '#b2c5ff'
  secondary: '#006876'
  on-secondary: '#ffffff'
  secondary-container: '#69e8fe'
  on-secondary-container: '#006774'
  tertiary: '#324749'
  on-tertiary: '#ffffff'
  tertiary-container: '#495e61'
  on-tertiary-container: '#c0d7da'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001848'
  on-primary-fixed-variant: '#0040a2'
  secondary-fixed: '#9eefff'
  secondary-fixed-dim: '#55d7ed'
  on-secondary-fixed: '#001f24'
  on-secondary-fixed-variant: '#004e59'
  tertiary-fixed: '#d0e7ea'
  tertiary-fixed-dim: '#b4cbce'
  on-tertiary-fixed: '#091f21'
  on-tertiary-fixed-variant: '#364a4d'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Public Sans
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: Public Sans
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
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

The design system is engineered to evoke professional trust and atmospheric clarity. It targets health-conscious individuals and medical professionals who require precise air quality data delivered through a calming, non-intrusive interface.

The aesthetic follows a **Clinical & Airy** philosophy, merging high-performance medical standards with a breathable, modern digital experience. Key visual pillars include:
- **Glassmorphism:** Using translucent layers to mimic the transparency of clean air.
- **Organic Softness:** Avoiding harsh angles to create a welcoming, "breathable" environment.
- **Sterile Precision:** Utilizing high-contrast accents against vast white space to emphasize cleanliness and technological sophistication.

## Colors

The palette is rooted in medical authority and environmental purity.

- **Pure White (#FFFFFF):** The primary canvas color, representing sterility and a "blank slate" of clean air.
- **Medical Blue (#0052CC):** Used for primary actions and critical data points. It establishes authority and scientific rigor.
- **Glass-Cyan (#E0F7FA / #00ACC1):** Used for atmospheric accents, data visualizations related to airflow, and glassmorphic background blurs.
- **Semantic Accents:** Success states should utilize a cool-toned emerald, while warnings use a soft amber to maintain the calm vibe without inducing panic.

The color mode is strictly **Light**, ensuring the "Airy" quality is maintained through high-key lighting.

## Typography

Typography focuses on immediate legibility and institutional reliability. 

**Public Sans** is utilized for headlines to provide a structural, authoritative feel that mimics government health signage. **Inter** is used for body copy and data labels for its exceptional clarity on high-density screens and its neutral, modern tone.

Hierarchy is established through weight and purposeful whitespace rather than excessive color. Large display sizes for Air Quality Index (AQI) numbers should use a semi-bold weight to ensure they are the first thing a user sees.

## Layout & Spacing

The layout philosophy centers on **expansion and breathability**. 

A **12-column fluid grid** is used for desktop, transitioning to a **4-column grid** for mobile. Large margins (24px on mobile, up to 80px on desktop) are essential to prevent the UI from feeling "clogged"—mimicking the feeling of a wide-open, filtered space.

Spacing follows an 8px linear scale. Generous vertical padding between sections (using the `xl` unit) is encouraged to allow content to sit in isolation, reinforcing the airy aesthetic.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and soft, environmental shadows rather than heavy layering.

1.  **Backdrop Blurs:** High-level containers (like navigation bars or foreground cards) use a 20px - 30px blur with a 60% opaque white background.
2.  **Soft Shadows:** Shadows are extremely diffused (Blur: 40px, Spread: 0, Opacity: 4%) and tinted with Medical Blue (#0052CC) to give the appearance of floating above the surface.
3.  **Inner Glows:** To simulate a sterile, backlit look, buttons and active cards may use a subtle 1px white inner stroke to catch light.

## Shapes

The design system uses a **Pill-shaped (3)** geometry for primary elements and **highly rounded** corners for containers.

- **Buttons & Chips:** Full-capsule (pill) radius to communicate friendliness and organic movement.
- **Cards:** Large radius (rounded-xl) to avoid sharp, "dangerous" corners, reinforcing the welcoming nature of the product.
- **Icons:** Custom icons should have rounded terminals and consistent 2px stroke weights to match the typography.

## Components

- **Buttons:** Primary buttons use a Medical Blue fill with white text. Secondary buttons utilize a glassmorphic Cyan tint with blue text. All buttons are pill-shaped.
- **Glass-Cards:** Main content containers should have a subtle 1px white border at 50% opacity and a backdrop filter to create a frosted glass effect over background gradients.
- **Data Visualizers:** Use soft, pulsing circular gradients to represent air purification cycles. Avoid harsh line graphs; prefer "flowing" area charts with smooth cubic-bezier transitions.
- **Inputs:** Fields should be pill-shaped with a soft Cyan background (#E0F7FA). Focus states use a 2px Medical Blue stroke.
- **Progress Bars:** Representing filtration life, these should use a dual-tone gradient from Glass-Cyan to Medical Blue, housed in a pill-shaped track.
- **Air Status Indicator:** A prominent, glassmorphic "orb" component that shifts color (Cyan to Green) to reflect real-time air quality.