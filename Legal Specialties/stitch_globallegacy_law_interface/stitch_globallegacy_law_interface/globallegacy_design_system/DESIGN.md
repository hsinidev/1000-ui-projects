---
name: GlobalLegacy Design System
colors:
  surface: '#faf9f7'
  surface-dim: '#dadad8'
  surface-bright: '#faf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeec'
  surface-container-high: '#e9e8e6'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1b'
  on-surface-variant: '#434842'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f1ef'
  outline: '#747872'
  outline-variant: '#c4c8c0'
  surface-tint: '#546254'
  primary: '#516051'
  on-primary: '#ffffff'
  primary-container: '#6a7869'
  on-primary-container: '#f7fff3'
  inverse-primary: '#bbcbb9'
  secondary: '#655d51'
  on-secondary: '#ffffff'
  secondary-container: '#eadece'
  on-secondary-container: '#6a6255'
  tertiary: '#755717'
  on-tertiary: '#ffffff'
  tertiary-container: '#90702e'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e7d4'
  primary-fixed-dim: '#bbcbb9'
  on-primary-fixed: '#121e13'
  on-primary-fixed-variant: '#3c4a3d'
  secondary-fixed: '#ede1d1'
  secondary-fixed-dim: '#d0c5b5'
  on-secondary-fixed: '#201b11'
  on-secondary-fixed-variant: '#4d463a'
  tertiary-fixed: '#ffdea5'
  tertiary-fixed-dim: '#e9c176'
  on-tertiary-fixed: '#261900'
  on-tertiary-fixed-variant: '#5d4201'
  background: '#faf9f7'
  on-background: '#1a1c1b'
  surface-variant: '#e3e2e0'
typography:
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-sm:
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
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-lg:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-md:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.03em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 32px
  margin: 64px
  section-padding: 120px
---

## Brand & Style
The brand personality is rooted in empathy, discretion, and enduring value. It seeks to provide a sanctuary for clients navigating complex international estate matters, evoking an emotional response of profound relief and quiet confidence. 

The design style is **Minimalism** infused with **Modern Corporate** reliability. It prioritizes "Calm-Centric" layouts, utilizing expansive negative space to prevent cognitive overload. The interface avoids aggressive call-to-actions, opting instead for a guided, editorial flow that feels both prestigious and accessible.

## Colors
The palette is designed to ground the user through organic, earthy tones.
- **Primary (Soft Sage):** Used for primary actions and stabilizing UI elements to promote a sense of calm and growth.
- **Secondary (Taupe):** Applied to secondary navigation and structural accents to provide professional grounding.
- **Tertiary (Gold):** Reserved for high-value highlights, success states, and legacy markers to signify quality and heritage.
- **Neutral (Warm White/Stone):** The background canvas is a warm, off-white to reduce eye strain and provide a softer contrast than pure white.

## Typography
This design system employs a classic serif/sans-serif pairing to balance heritage with modern utility. 
- **Headlines:** Noto Serif provides a literary, authoritative voice, suggesting deep-rooted expertise. Use generous top margins for headlines to let themes breathe.
- **Body & Labels:** Manrope offers a clean, geometric balance that ensures high legibility for complex legal text. 
- **Hierarchy:** Maintain a clear distinction by keeping headlines strictly serif and functional UI elements (buttons, inputs, navigation) strictly sans-serif.

## Layout & Spacing
The layout follows a **Fixed Grid** model centered on the screen to create a focused, high-end experience. 
- **Rhythm:** An 8px base unit drives all spacing. 
- **Generosity:** Vertical spacing between sections is intentionally large (120px+) to ensure the "Calm-Centric" narrative. 
- **Grid:** A 12-column structure is used, but content should ideally be constrained to the inner 8 columns for long-form reading to enhance focus and reduce scanning fatigue.

## Elevation & Depth
To minimize visual stress, the design system avoids harsh dropshadows. Instead, it uses:
- **Ambient Shadows:** Very soft, diffused shadows (Blur: 20px-40px) with low opacity (5-8%) tinted with the Taupe secondary color.
- **Tonal Layers:** Depth is primarily communicated through subtle shifts in background color (e.g., a Sage-tinted light grey surface sitting on a Stone background).
- **Glassmorphism (Subtle):** Use background blurs on fixed navigation bars to maintain a sense of context without breaking the visual flow.

## Shapes
The shape language is **Rounded**, moving away from "sharp" legal stereotypes toward an "approachable" aesthetic. 
- **Standard Elements:** Buttons and input fields use 0.5rem (8px) corners.
- **Containers:** Large cards and content sections use 1rem (16px) for a soft, protective feel.
- **Iconography:** Use "Linear" icons with rounded terminals to match the typography's softness.

## Components
- **Buttons:** Primary buttons use a solid Soft Sage fill with white Manrope text. Secondary buttons use a Taupe outline with a subtle Sage tint on hover.
- **Input Fields:** Use a light Taupe border (1px) that transitions to Gold on focus. Labels should always be visible (no floating placeholders) to ensure clarity.
- **Cards:** Use "Paper" style cards with a 1px soft Taupe border and no shadow, or a deep ambient shadow with no border for featured content.
- **Chips:** Small, rounded-pill tags used for categorizing legal jurisdictions or document types, using muted Sage or Taupe backgrounds.
- **Progress Indicators:** For long estate-planning workflows, use soft, horizontal steppers with Gold accents to signify progression toward a "Legacy."
- **Accordions:** Essential for legal FAQs; ensure smooth transitions and generous padding within expanded states to maintain the calm aesthetic.