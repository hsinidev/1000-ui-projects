---
name: Port-Concierge
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdbf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff3ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dde9ff'
  surface-container-highest: '#d7e3fa'
  on-surface: '#101c2c'
  on-surface-variant: '#43474e'
  inverse-surface: '#253142'
  inverse-on-surface: '#ebf1ff'
  outline: '#74777f'
  outline-variant: '#c4c6d0'
  surface-tint: '#455f8a'
  primary: '#000e24'
  on-primary: '#ffffff'
  primary-container: '#00234b'
  on-primary-container: '#718bb9'
  inverse-primary: '#adc7f8'
  secondary: '#645e4f'
  on-secondary: '#ffffff'
  secondary-container: '#e8dfcc'
  on-secondary-container: '#696253'
  tertiary: '#0c0f0f'
  on-tertiary: '#ffffff'
  tertiary-container: '#222424'
  on-tertiary-container: '#8a8b8b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#adc7f8'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2c4771'
  secondary-fixed: '#ebe1cf'
  secondary-fixed-dim: '#cfc6b3'
  on-secondary-fixed: '#1f1b10'
  on-secondary-fixed-variant: '#4c4638'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9ff'
  on-background: '#101c2c'
  surface-variant: '#d7e3fa'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
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
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  headline-lg-mobile:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 40px
  gutter: 24px
  section-gap: 64px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style

This design system targets the elite maritime sector, specifically yacht captains and logistics officers who require high-efficiency tools that mirror the luxury of their environments. The brand personality is **composed, authoritative, and frictionless**. It avoids the cluttered, industrial look of traditional maritime software in favor of a **Minimalist-Refined** aesthetic.

The UI utilizes **Soft-UI Neumorphism**, characterized by subtle extrusions and indentations that mimic physical consoles without the heavy visual noise of early skuomorphism. The goal is to evoke a sense of "digital craftsmanship"—where every interaction feels tactile, premium, and calm. This system prioritizes wide margins and generous negative space to reduce cognitive load during high-stakes navigation and logistics management.

## Colors

The palette is rooted in maritime heritage but executed with a modern, luxury finish. 

- **Navy (#00234B):** Represents professional authority and the deep sea. Used for primary actions, critical navigation, and typography to ensure maximum legibility.
- **Soft Champagne (#F2E8D5):** The core of the "Soft-UI" effect. This warm neutral acts as the primary surface color, providing a more sophisticated and eye-straining-resistant alternative to pure grey.
- **Silk White (#FFFFFF):** Used for the "light" side of neumorphic extrusions and as a clean, airy background for content modules.
- **Functional Accents:** Success and warning states should be muted (Sage Green and Burnt Sienna) to maintain the refined atmosphere without breaking the minimalist harmony.

## Typography

The typographic strategy balances the heritage of the sea with modern clarity. **Noto Serif** is used for headlines to provide a sense of tradition, luxury, and "editorial" authority. **Manrope** is selected for body copy and data entry due to its exceptional readability, modern geometric balance, and professional tone.

All secondary labels should use Manrope in uppercase with increased letter spacing to emulate the precise labeling found on high-end nautical instruments. Line heights are purposefully generous to maintain an "airy" feel even in data-heavy logistics tables.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy on desktop to ensure that logistical data doesn't become over-extended and difficult to scan. A 12-column grid is used with wide 48px outer margins to frame the content like a high-end magazine.

Rhythm is maintained through an 8px base unit. Wide margins are a signature of this design system, ensuring that the interface never feels "cramped" even when displaying complex manifests or port schedules. On mobile devices, the system transitions to a single-column fluid layout with 16px safe-area margins.

## Elevation & Depth

This system uses a **Soft-UI Neumorphic** approach. Depth is not created by stacking layers (z-index), but by "molding" the surface. 

- **Extruded Elements (Buttons, Cards):** These use a dual-shadow technique on the Soft Champagne background. A top-left highlight of Silk White (#FFFFFF) and a bottom-right shadow of a slightly darker, warm neutral (#D1C7B7). 
- **Sunken Elements (Inputs, Search Bars):** These use inner shadows to appear recessed into the interface, suggesting a functional area for data entry.
- **Shadow Quality:** Shadows must be extremely diffused (blur radius of 20px-40px) with low opacity (15-20%) to ensure the effect remains "minimalist" rather than distracting.

## Shapes

The shape language is **smooth and organic**. Rounded corners (0.5rem base) are applied to all interactive components to soften the professional Navy tones and make the "tactile" extrusions feel more natural. Larger containers like port info cards use `rounded-xl` (1.5rem) to emphasize the premium, soft-touch feel of the platform.

## Components

- **Buttons:** Primary buttons are Navy with Silk White text, featuring a subtle "raised" neumorphic effect. On hover, the highlight intensifies. Secondary buttons are Soft Champagne, blending into the background with only the shadow/highlight defining their shape.
- **Cards:** Content is housed in large, soft-edged cards. There are no borders; the card is defined entirely by the soft light/dark shadow interplay. 
- **Input Fields:** These appear "punched into" the Champagne surface using inner shadows. Typography inside inputs is Navy for high contrast.
- **Logistics Lists:** Rows are separated by generous padding rather than lines. A selected row uses a "sunken" effect to indicate it is active.
- **Maritime Specifics:**
    - **Status Chips:** Small, pill-shaped indicators for "In Port," "At Sea," or "Maintenance." Use low-saturation colors to preserve the elegant aesthetic.
    - **Tactile Gauges:** Visual indicators for fuel or weather use the same extruded style, making the digital dashboard feel like a custom-molded physical bridge console.