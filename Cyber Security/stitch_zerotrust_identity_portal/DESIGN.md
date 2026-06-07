---
name: ClearShield Zero Trust
colors:
  surface: '#fcf8ff'
  surface-dim: '#dcd8e5'
  surface-bright: '#fcf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f2ff'
  surface-container: '#f0ecf9'
  surface-container-high: '#eae6f4'
  surface-container-highest: '#e4e1ee'
  on-surface: '#1b1b24'
  on-surface-variant: '#464555'
  inverse-surface: '#302f39'
  inverse-on-surface: '#f3effc'
  outline: '#777587'
  outline-variant: '#c7c4d8'
  surface-tint: '#4d44e3'
  primary: '#3525cd'
  on-primary: '#ffffff'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#c3c0ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#46494b'
  on-tertiary: '#ffffff'
  tertiary-container: '#5e6163'
  on-tertiary-container: '#dadcde'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#fcf8ff'
  on-background: '#1b1b24'
  surface-variant: '#e4e1ee'
typography:
  display-xl:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-bold:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  code:
    fontFamily: Inter
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
  unit: 4px
  container-max-width: 1440px
  gutter: 24px
  margin-page: 48px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
  stack-xl: 48px
---

## Brand & Style

This design system is engineered for high-stakes security environments where clarity is synonymous with safety. The brand personality is **authoritative yet approachable**, moving away from the "black-box" opacity of traditional security software toward a "Glass Box" philosophy. 

The aesthetic leverages **Modern Minimalism** infused with **Glassmorphism**. By using translucent layers and blurred backgrounds, the UI communicates the "Zero Trust" concept: nothing is hidden, every layer is verified, and the infrastructure is transparent. The emotional response is one of calm control and professional precision, ensuring that critical security data is never obscured by visual clutter.

## Colors

The palette is centered on the concept of "Frost and Electricity." 

- **Frost White (#F8FAFC):** Used for large surface areas and background tints to maintain a light, airy feel that reduces cognitive load.
- **Electric Indigo (#4F46E5):** The primary action color. It signifies energy and intelligence, used for primary buttons, active states, and critical paths.
- **Slate (#64748B):** Provides the structural grounding. It is used for typography and iconography to ensure high contrast against the lighter backgrounds.
- **Transparency:** A core "color" in this system. Backgrounds often use a 70-80% opacity white with a 20px-40px backdrop blur to create the frosted glass effect.

## Typography

This design system employs a dual-font strategy to balance character with utility. 

**Manrope** is used for headlines to provide a modern, refined, and slightly technical feel. Its geometric nature complements the clean lines of the security platform. 

**Inter** is used for all body copy, labels, and data visualizations. It is chosen for its exceptional legibility at small sizes and its neutral, systematic appearance, which is essential for reading complex security logs and policy configurations. Text should primarily use Slate for high readability, with Electric Indigo reserved for links and interactive highlights.

## Layout & Spacing

The layout follows a **Fixed Grid** model for dashboard views to ensure consistency, while marketing or content-heavy pages may transition to a fluid model. 

- **Grid:** A 12-column grid system with a 24px gutter.
- **Rhythm:** A 4px baseline grid governs all spacing. Vertical margins between sections should be generous (48px+) to reinforce the "Clean" aesthetic and prevent the UI from feeling cramped.
- **Density:** The system defaults to a "Comfortable" density to ensure the "Transparent" feel isn't compromised by data saturation.

## Elevation & Depth

Hierarchy is established through **Backdrop Blurs** rather than heavy shadows. 

1. **Base Layer:** Solid White or Frost White.
2. **Mid Layer (Cards/Containers):** `rgba(255, 255, 255, 0.6)` with a 20px blur and a 1px solid white border at 40% opacity. This creates the "frosted glass" signature.
3. **Top Layer (Modals/Popovers):** `rgba(255, 255, 255, 0.9)` with a 40px blur and a very soft, diffused Slate-tinted shadow (`box-shadow: 0 20px 25px -5px rgba(100, 116, 139, 0.1)`).

Avoid dark shadows. Use subtle 1px inner strokes to define edges on light backgrounds.

## Shapes

The shape language is **Rounded (Level 2)**. 

- **Standard Elements:** Buttons, input fields, and small cards use a 0.5rem (8px) radius.
- **Large Containers:** Main dashboard widgets and modal containers use a 1rem (16px) radius.
- **Checkboxes:** Use a 4px radius to maintain a professional, slightly sharper appearance than the more friendly pill shapes found in consumer apps.

The use of consistent rounding across all "glass" panels softens the technical nature of the platform, making the security data feel more accessible.

## Components

- **Buttons:** Primary buttons use a solid Electric Indigo fill with white text. Secondary buttons use a transparent background with a 1px Slate border. "Glass" buttons (tertiary) use a subtle white tint with a blur effect.
- **Input Fields:** Use a light Slate stroke (20% opacity) that transitions to Electric Indigo on focus. Backgrounds should be slightly translucent.
- **Chips/Badges:** For status indicators (e.g., "Secure", "Threat Detected"), use high-saturation background tints with 10% opacity and bold text of the same color. 
- **Cards:** These are the primary vessel for the frosted glass effect. They must feature a subtle 1px white border to separate them from the background.
- **Security Health Meter:** A custom component using a gradient from Electric Indigo to a soft Cyan to visualize system integrity without using "alarmist" red/yellow unless a critical breach is present.
- **Data Tables:** Highly legible, using Slate for headers and Inter (body-sm) for row data. Zebra striping should use a very faint Frost White (#F1F5F9).