---
name: Pearly White Design System
colors:
  surface: '#fbf9f9'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e3e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#424848'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#727878'
  outline-variant: '#c2c8c7'
  surface-tint: '#516161'
  primary: '#516161'
  on-primary: '#ffffff'
  primary-container: '#e0f2f1'
  on-primary-container: '#5e6f6e'
  inverse-primary: '#b8cac9'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#006874'
  on-tertiary: '#ffffff'
  tertiary-container: '#c8f7ff'
  on-tertiary-container: '#007784'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e6e5'
  primary-fixed-dim: '#b8cac9'
  on-primary-fixed: '#0e1e1e'
  on-primary-fixed-variant: '#3a4a49'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#97f0ff'
  tertiary-fixed-dim: '#66d6e7'
  on-tertiary-fixed: '#001f24'
  on-tertiary-fixed-variant: '#004f58'
  background: '#fbf9f9'
  on-background: '#1b1c1c'
  surface-variant: '#e3e2e2'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
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
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
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
  margin: 64px
  container-max: 1280px
---

## Brand & Style
This design system is built to evoke a sense of professional serenity and absolute cleanliness. The brand personality is clinical yet approachable, stripping away the traditional anxiety associated with dental visits and replacing it with a spa-like, "Pearly White" atmosphere. The target audience is health-conscious individuals seeking high-end restorative and aesthetic care.

The design style is **Minimalism** blended with **Modern Corporate** sensibilities. It prioritizes extreme legibility, vast whitespace, and a high-fidelity aesthetic. Visuals should rely on high-quality photography of bright, airy clinical spaces and authentic, healthy smiles to build immediate trust and a "breath of fresh air" emotional response.

## Colors
The palette is dominated by **Crisp White** and **Soft Mint**, creating a luminous, high-key environment. 
- **Soft Mint (#E0F2F1):** Used as a primary background wash or for large structural sections to differentiate from the pure white surfaces.
- **Crisp White (#FFFFFF):** The foundation for all interactive cards and containers, ensuring the "Pearly" aesthetic remains central.
- **Dental Blue (#0097A7):** The high-contrast accent for primary calls-to-action, active states, and brand-critical iconography.
- **Gentle Grey (#757575):** Utilized for secondary text and subtle borders to maintain a soft visual hierarchy without the harshness of pure black.

## Typography
**Manrope** is selected for its refined, modern geometry and exceptional legibility in health-tech contexts. It strikes a balance between technical precision and human warmth. 

Headlines should be set with tighter letter-spacing and generous line-height to maintain an editorial feel. Body text stays strictly at 16px or above to ensure accessibility for all age groups. Use "Gentle Grey" for body copy to soften the contrast against "Crisp White" backgrounds, while reserved "Dental Blue" or a darker variant of grey for headlines to provide structural anchoring.

## Layout & Spacing
The layout follows a **Fixed Grid** model to ensure a disciplined, clinical alignment. Content is centered within a 1280px container using a 12-column system. 

The spacing rhythm is intentionally generous, utilizing an 8px base unit. Wide margins (64px+) and large gutters (24px) are essential to prevent the UI from feeling "crowded," which can induce stress. Every major section should have significant vertical padding (80px to 120px) to allow the "Pearly White" surfaces to breathe.

## Elevation & Depth
This design system avoids heavy, dark shadows in favor of **Ambient Shadows** and **Tonal Layers**. 
- **Depth:** Elevation is achieved by placing "Crisp White" cards on top of "Soft Mint" backgrounds. 
- **Shadows:** Use extremely diffused, low-opacity shadows (e.g., `box-shadow: 0 10px 30px rgba(0, 151, 167, 0.05)`). By tinting the shadow with a tiny hint of "Dental Blue," the UI feels cohesive and luminous rather than muddy. 
- **Borders:** Subtle, 1px "Soft Mint" or very light grey outlines are used for input fields and secondary buttons to define shape without adding visual weight.

## Shapes
The shape language is defined by **Large Border Radii**, specifically moving between 12px (rounded) and 24px (rounded-xl). This softness is critical to counteracting the "sharpness" often associated with dental tools, creating a psychological sense of safety and comfort. 

Buttons and small interactive elements use a 12px radius, while primary content cards and imagery containers use a 24px radius to create a distinct, friendly container style.

## Components
- **Buttons:** Primary buttons are "Dental Blue" with white text and a 12px radius. Secondary buttons use a "Soft Mint" fill with "Dental Blue" text.
- **Input Fields:** Large 16px padding with a 1px border in "Soft Mint." On focus, the border transitions to "Dental Blue" with a soft outer glow.
- **Cards:** "Crisp White" background, 24px border radius, and a subtle ambient shadow. Ensure 32px of internal padding to maintain the whitespace narrative.
- **Chips/Badges:** Pill-shaped (fully rounded) with a "Soft Mint" background and "Dental Blue" text for indicating services or tags.
- **Icons:** Use a medium-weight stroke (2px) in "Dental Blue" or "Gentle Grey." Avoid filled icons to keep the interface light.
- **Featured Appointment Card:** A specialized component using a "Soft Mint" border and high-quality smile imagery, acting as the primary conversion point.