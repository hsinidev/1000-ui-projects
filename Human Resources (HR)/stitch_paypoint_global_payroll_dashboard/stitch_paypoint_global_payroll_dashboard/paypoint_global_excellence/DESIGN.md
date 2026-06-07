---
name: PayPoint Global Excellence
colors:
  surface: '#faf8ff'
  surface-dim: '#dad9e0'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f9'
  surface-container: '#efedf3'
  surface-container-high: '#e9e7ee'
  surface-container-highest: '#e3e2e8'
  on-surface: '#1a1b20'
  on-surface-variant: '#444650'
  inverse-surface: '#2f3035'
  inverse-on-surface: '#f1f0f6'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#2d0700'
  on-tertiary: '#ffffff'
  tertiary-container: '#501300'
  on-tertiary-container: '#d37758'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#ffdbd0'
  tertiary-fixed-dim: '#ffb59e'
  on-tertiary-fixed: '#390b00'
  on-tertiary-fixed-variant: '#783018'
  background: '#faf8ff'
  on-background: '#1a1b20'
  surface-variant: '#e3e2e8'
typography:
  display-lg:
    fontFamily: Work Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Work Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  title-sm:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
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
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  numeric-data:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  touch-target: 44px
  container-margin: 20px
---

## Brand & Style

This design system is engineered for the global payroll sector, where precision, security, and reliability are paramount. The brand personality is institutional yet accessible, evoking the feeling of a high-tier private bank. The target audience includes international employees and HR administrators who require a "zero-error" environment.

The visual style is **Corporate Modern** with a focus on "Trust-heavy" architecture. This is achieved through a structural layout that emphasizes data integrity and systemic clarity. The UI avoids unnecessary ornamentation, instead using subtle depth and precise alignment to guide the user through sensitive financial workflows. Every interaction is designed to reassure the user that their data is protected and their compensation is accurate.

## Colors

The palette is anchored by **Royal Blue (#002366)**, a color synonymous with stability and global finance. This primary shade is reserved for brand touchpoints, primary actions, and navigational anchors. **Slate Grey (#708090)** serves as the secondary workhorse, providing a sophisticated tone for iconography, labels, and secondary text, ensuring high contrast without the harshness of pure black.

Functional colors are critical for this design system. Success indicators (green) and Error alerts (red) use deep, saturated tones to maintain the professional aesthetic while providing unmistakable feedback. The background is a crisp, clean White to maximize legibility and provide a clinical, organized feel to the portal.

## Typography

This design system utilizes a dual-font strategy to balance authority with utility. **Work Sans** is used for headings and titles to provide a grounded, professional structure. **Inter** is utilized for body copy and data entry due to its exceptional legibility at small sizes and its neutral, systematic character.

For financial values, the "numeric-data" style should always be applied, utilizing tabular figures (monospaced numbers) to ensure that currency columns align perfectly for easy visual scanning. Labels use a slightly increased letter spacing and semi-bold weights to remain legible even when secondary Slate Grey colors are applied.

## Layout & Spacing

A **Mobile-first fluid grid** approach is mandatory. On mobile devices, the system uses a single-column layout with 20px side margins. As the viewport expands, the system transitions to a 12-column fixed grid with a maximum content width of 1200px.

A strict 4px baseline rhythm ensures vertical consistency. Large touch targets (minimum 44px height) are required for all critical actions, such as "Download Payslip" or "Confirm Contribution," ensuring accessibility for users on the move. Padding within cards is generous (24px) to prevent information density from feeling overwhelming, providing "room to breathe" around sensitive financial figures.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Ambient Shadows**. The background remains at 0dp (White). Cards and interactive containers sit at +1dp, using a very soft, diffused shadow (Blur: 12px, Opacity: 4%, Color: Royal Blue) to create a sense of lift without appearing "floaty."

To emphasize security, "Active" or "Focused" states for input fields do not just change color; they utilize a subtle inner shadow to suggest the field is "recessed" and ready for secure data entry. Subtle 1px borders in a lightened Slate Grey (#E2E8F0) provide structural definition between different sections of the page without creating visual noise.

## Shapes

The shape language is **Soft**, utilizing a 0.25rem (4px) base radius. This provides a modern appearance while maintaining the serious, rectilinear "strength" associated with financial institutions. High-radius or "bubbly" shapes are avoided to ensure the portal is perceived as a professional tool.

Buttons and data entry fields follow the base 4px rounding. Larger containers, like the primary payslip card, may use an 8px (rounded-lg) radius to create a distinct visual hierarchy for the most important information on the screen.

## Components

### Buttons & Actions
Primary buttons use the Royal Blue background with White text. The "Download Payslip" action is treated as a "High-Priority" component, often spanning the full width of the mobile viewport with a leading icon for immediate recognition.

### Secure Input Fields
Input fields must include a state for "Data Masking." Sensitive values (like bank account numbers or salary amounts) should be obfuscated with asterisks by default, with a "Reveal" icon (eye) positioned at the trailing edge of the field.

### Interactive Charts
Pie charts for pay breakdowns should use a primary palette of Royal Blue and its tints, contrasted with Slate Grey for non-monetary segments. Legend items must be interactive, allowing users to toggle data visibility.

### Status Indicators
Use "Pill" chips with a light background tint and dark text of the same hue (e.g., a light green background with dark green text for "Processed"). These should always be placed in the top-right corner of cards for immediate status confirmation.

### Professional Cards
Cards are the primary container for information. They feature a 1px Slate Grey border and a subtle shadow. The header of the card is often separated by a thin horizontal rule to distinguish the title from the metadata.