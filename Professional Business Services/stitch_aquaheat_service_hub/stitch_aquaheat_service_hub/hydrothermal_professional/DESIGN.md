---
name: HydroThermal Professional
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#444650'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#b52619'
  on-secondary: '#ffffff'
  secondary-container: '#ff5c47'
  on-secondary-container: '#610000'
  tertiary: '#071427'
  on-tertiary: '#ffffff'
  tertiary-container: '#1d293c'
  on-tertiary-container: '#8490a8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#ffdad4'
  secondary-fixed-dim: '#ffb4a8'
  on-secondary-fixed: '#410000'
  on-secondary-fixed-variant: '#920703'
  tertiary-fixed: '#d7e3fd'
  tertiary-fixed-dim: '#bbc7e0'
  on-tertiary-fixed: '#0f1c2e'
  on-tertiary-fixed-variant: '#3b475c'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
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
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The visual identity of this design system is built upon the pillars of reliability, technical expertise, and immediate trust. It caters to homeowners and commercial property managers who require precision and dependability in high-stakes utility maintenance. 

The aesthetic follows a **Corporate / Modern** direction. It avoids unnecessary flourishes in favor of a structured, functional interface that communicates stability. By balancing the coolness of "Water" (Royal Blue) with the urgency and power of "Heat" (Deep Red), the UI creates a psychological bridge between problem-solving and safety. The overall feel is clinical yet accessible, ensuring users feel they are in the hands of seasoned specialists.

## Colors

The palette utilizes a high-contrast "Water-and-Heat" theme. 

- **Royal Blue (#002366):** The primary anchor. Used for navigation, primary buttons, and headings to establish authority and represent water systems.
- **Deep Red (#8B0000):** The secondary brand color. Reserved for urgent calls-to-action, heating-related indicators, and critical status alerts.
- **Soft Grey (#F4F4F4):** The foundational background color. It reduces eye strain and provides a clean canvas that makes primary colors pop without feeling aggressive.
- **Surface Neutrals:** Use pure white (#FFFFFF) for cards and input fields to create a clear "layer" above the soft grey background.

## Typography

This design system utilizes **Inter** for all applications. Inter’s tall x-height and neutral geometric forms provide the clarity required for technical specifications and service quotes.

- **Headlines:** Use Bold (700) or SemiBold (600) weights in Royal Blue to establish a clear information hierarchy.
- **Body Text:** Maintained at a highly readable 16px for standard content. Use a slightly darker grey (#1A1A1A) rather than pure black to keep the professional tone soft yet legible.
- **Data Display:** Numerical values in tables and invoices should use tabular lining (available in Inter) to ensure columns of figures align perfectly.

## Layout & Spacing

The design system employs a **Fixed Grid** model for desktop and a fluid model for mobile. 

- **Grid:** A 12-column grid with a maximum container width of 1280px. 
- **Rhythm:** An 8px linear scale governs all padding and margins. 
- **Application:** Use generous `lg` (48px) vertical spacing between major sections (e.g., Service Overviews vs. Contact Forms) to maintain the "clean" aesthetic and prevent the UI from feeling cluttered with technical data.

## Elevation & Depth

To maintain a sense of modern professionalism, depth is handled through **Low-contrast outlines** supplemented by subtle ambient shadows.

- **Surface Levels:** The background is #F4F4F4. Cards and interactive containers are #FFFFFF with a 1px border (#E5E5E5).
- **Shadows:** Use a single, soft "Elevation-1" shadow for floating elements like dropdowns or active cards: `0px 4px 12px rgba(0, 0, 0, 0.05)`.
- **Interactivity:** Elements should not feel "flat" nor "heavy." Depth is used sparingly to indicate focus, such as a subtle lift when hovering over a service card.

## Shapes

The shape language is defined by **Soft** (Level 1) roundedness. 

- **Primary Radius:** A 4px (0.25rem) radius is applied to buttons, input fields, and small components. This provides a modern touch without sacrificing the "sturdy" feel associated with industrial services.
- **Large Components:** Cards and modals use an 8px (0.5rem) radius to soften the larger surface areas.
- **Strictness:** Avoid pill-shaped or circular buttons (except for icons); rectangular forms with subtle rounding reinforce the engineering and structural nature of the brand.

## Components

### Buttons
- **Primary:** Royal Blue background with White text. Bold and high-contrast.
- **Secondary/Urgent:** Deep Red background with White text. Used exclusively for "Emergency Service" or "Book Now" actions.
- **Ghost:** Transparent background with Royal Blue 1px border. Used for secondary actions like "View Details."

### Status Indicators
Small, pill-shaped badges used for service tracking (e.g., "In Progress," "Scheduled," "Completed"). These use low-saturation background tints with high-saturation text to ensure clarity without competing with primary CTAs.

### Data Tables
Tables are the backbone of this design system for displaying quotes and service history.
- **Header:** Light grey (#E5E5E5) background with `label-sm` typography.
- **Rows:** 1px bottom stroke, no vertical borders. 
- **Zebra Striping:** Use #F9F9F9 on alternate rows for complex data sets.

### Input Fields
Strict, rectangular fields with a 1px #D1D1D1 border. Upon focus, the border shifts to Royal Blue with a 2px thickness to provide clear visual feedback for users filling out service request forms.

### Service Cards
White background, 1px border, and 8px corner radius. These cards feature a bold Royal Blue icon at the top left to categorize the service (e.g., a boiler icon for heating, a wrench for plumbing).