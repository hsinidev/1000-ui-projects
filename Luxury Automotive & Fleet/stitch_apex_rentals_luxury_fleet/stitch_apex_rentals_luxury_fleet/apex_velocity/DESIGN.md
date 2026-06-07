---
name: Apex Velocity
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#e9bcb5'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#b08781'
  outline-variant: '#5f3f3a'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690000'
  primary-container: '#e60000'
  on-primary-container: '#fff7f5'
  inverse-primary: '#c00000'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#717272'
  on-tertiary-container: '#f8f8f8'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: lexend
    fontSize: 72px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: lexend
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 20px
  margin: 40px
---

## Brand & Style

The design system is engineered to evoke the raw adrenaline of a supercar cockpit and the precision of high-end automotive engineering. It targets an elite clientele who value speed, status, and mechanical perfection. The brand personality is aggressive yet refined, focusing on "performance luxury."

The visual language utilizes a **High-Contrast / Bold** style fused with **Tactile** elements. It prioritizes high-impact visuals through large-scale imagery and a dark, immersive interface. The emotional response is one of immediate power and exclusivity, ensuring the user feels they are not just renting a vehicle, but gaining access to a high-performance lifestyle.

## Colors

The palette is rooted in the high-stakes world of competitive racing. **Racing Red (#E60000)** serves as the primary action color, used sparingly for critical CTAs and performance indicators to simulate brake lights and ignition buttons. 

**Carbon Black (#1A1A1A)** is the foundational surface color, providing a deep, non-reflective background that allows the vehicles to stand out. **Pure White (#FFFFFF)** is reserved for high-priority typography and icons to ensure maximum readability against the dark surfaces. A secondary neutral, a slightly lighter charcoal, is used for subtle UI borders and structural depth.

## Typography

This design system employs a dual-font strategy to balance aggressive motion with premium legibility. **Lexend** is utilized for all headlines and display text; its athletic, wide proportions are emphasized by a heavy weight and a consistent 8-to-12 degree slant (italicization) to imply forward momentum and aerodynamic speed.

**Manrope** provides a technical, clean counter-balance for body copy and long-form information. It offers the refined, stable feel of a luxury brand brochure. All labels and secondary metadata should be rendered in uppercase Lexend with increased letter spacing to mimic the typography found on automotive gauges and telemetry displays.

## Layout & Spacing

The layout utilizes a **Fixed Grid** model to maintain a sense of structural integrity and precision. A 12-column grid system is the standard for desktop, with generous outer margins to frame the content like a gallery piece.

The spacing rhythm is tight and disciplined, based on a 4px baseline grid. This "mechanical" density reflects the compact, efficient packaging of a supercar engine. Use larger `xl` spacing only to separate major content sections, while keeping functional UI elements (like input groups and controls) tightly grouped to maintain a high-energy, cockpit-like density.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Bold Borders** rather than soft ambient shadows. Deep charcoal surfaces are layered on top of the black background to create a sense of physical components.

Depth is enhanced using:
1.  **Carbon Fiber Textures:** Subtle, low-opacity repeating diagonal patterns applied to primary container backgrounds.
2.  **Sleek Gradients:** Linear gradients (45-degree angle) from Racing Red to a darker crimson are used to give buttons a metallic, "anodized" finish.
3.  **Hard Outlines:** 1px solid borders in neutral-gray or white at low opacity (10-20%) define element boundaries without softening the "sharp" aesthetic.

## Shapes

The design system strictly adheres to a **Sharp (0px)** corner radius. There are no rounded corners in this system. This decision reflects the aggressive styling of modern supercar splitters, diffusers, and geometric chassis designs. 

Every button, input field, card, and image container must feature hard 90-degree angles. To add dynamism without rounding, use diagonal "clipped" corners (chamfers) at 45-degree angles for specialized components like status tags or "Next" buttons to further the aerodynamic narrative.

## Components

### Buttons
Primary buttons use a "Turbo Gradient" (Racing Red to Dark Red) with white uppercase text. Hover states should trigger a high-contrast white flash or a slight increase in the red's saturation. Use a slanted "parallelogram" shape for secondary action buttons to emphasize the speed motif.

### Cards & Containers
Cards feature a subtle carbon fiber background texture and a 1px "ghost" border. On hover, the border color should transition to Racing Red. Content inside cards should be strictly aligned to a micro-grid.

### Input Fields
Fields are solid Carbon Black with a bottom-only border in Racing Red to mimic a digital dashboard. Focus states should see the border glow slightly with a sharp, outer neon-red stroke.

### Chips & Badges
Small, rectangular badges with high-contrast backgrounds (e.g., White background with Black text). These should resemble the "Option" or "Drive Mode" toggles on a steering wheel.

### Selection Controls
Checkboxes and radio buttons are strictly square. When active, they fill with a solid Racing Red and a white checkmark/dot, ensuring high visibility at a glance.

### Specialized Components
- **Speedometer Progress Bars:** Use for showing availability or rental duration.
- **Telemetry Data Tables:** High-density tables with monospace-leaning typography for vehicle specs (0-60, Horsepower).