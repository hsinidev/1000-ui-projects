---
name: Civic Engagement Framework
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fa'
  on-surface: '#111c2c'
  on-surface-variant: '#44474e'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#465f88'
  primary: '#000a1e'
  on-primary: '#ffffff'
  primary-container: '#002147'
  on-primary-container: '#708ab5'
  inverse-primary: '#aec7f6'
  secondary: '#bb0024'
  on-secondary: '#ffffff'
  secondary-container: '#e32137'
  on-secondary-container: '#fffbff'
  tertiary: '#090b0c'
  on-tertiary: '#ffffff'
  tertiary-container: '#1f2223'
  on-tertiary-container: '#87898a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f6'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#ffdad8'
  secondary-fixed-dim: '#ffb3b0'
  on-secondary-fixed: '#410006'
  on-secondary-fixed-variant: '#93001a'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-bold:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  caption:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

The brand personality for this design system is **Authoritative yet Accessible**. It aims to evoke a sense of civic duty and institutional stability without the coldness of traditional bureaucracy. The target audience is a broad, non-partisan demographic, requiring the interface to feel inclusive, inviting, and inherently trustworthy.

The visual style is a **Modernized Corporate** aesthetic. It prioritizes clarity and functionalism through heavy whitespace and a refined patriotic palette. By stripping away unnecessary ornamentation and focusing on high-quality typography, the design system establishes a "neutral ground" that encourages democratic participation. The result is a UI that feels like a reliable digital infrastructure for the modern citizen.

## Colors

The color palette uses a "modernized patriotic" scheme to establish immediate credibility.
- **Deep Navy (#002147)**: Used for primary actions, navigation, and headers to convey authority and stability.
- **Vibrant Scarlet (#E01E35)**: Reserved for high-priority call-to-actions, alerts, and interactive highlights. It is used sparingly to maintain professional balance.
- **Soft Grays**: A range of cool-toned grays provides depth and separates content sections without the harshness of black lines.
- **Crisp White**: The primary canvas, ensuring a high-contrast environment that meets WCAG AAA standards for text legibility.

Color is applied systematically to guide the user's eye toward engagement opportunities while maintaining a neutral, non-partisan tone throughout the experience.

## Typography

This design system utilizes **Public Sans**, an institutional-grade typeface designed for legibility and neutrality. The type scale is optimized for high-contrast reading, ensuring accessibility for all users regardless of visual acuity.

Key typographic principles include:
- **Generous Line-Height**: Body text uses a 1.6x multiplier to reduce cognitive load during long-form reading.
- **Bold Hierarchy**: Headlines are set in heavy weights to provide clear "signposts" for users scanning the page.
- **Uppercase Labels**: Small labels and utility text use increased letter spacing and semi-bold weights to distinguish them from body content while maintaining a clean, official look.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop to ensure content remains centered and readable, transitioning to a fluid model for tablet and mobile devices. 

The spacing rhythm is based on an **8px base unit**. Margins and padding are intentionally generous to create a "breathable" interface that feels organized and calm. 
- **Information Density**: Low to Medium. Elements are given significant room to avoid overwhelming the user.
- **Touch Targets**: All interactive elements (buttons, inputs, links) maintain a minimum height of 48px to ensure accessibility on mobile devices and ease of use for those with motor impairments.

## Elevation & Depth

To maintain an "official" and "trustworthy" feel, this design system avoids excessive shadows or trendy gradients. Depth is conveyed through **Tonal Layering** and **Ambient Shadows**:

- **Surface Levels**: The background is pure white. Secondary content containers use the softest gray tint (#F8F9FA) to create subtle separation without adding visual weight.
- **Shadow Character**: Shadows are extremely diffused (large blur, low opacity) and slightly tinted with the primary Navy hue to maintain color harmony. They are used only on "floating" elements like cards, dropdowns, and modals to indicate interactivity or hierarchy.
- **Borders**: Soft, low-contrast outlines are used for form inputs and static containers to define boundaries without cluttering the layout.

## Shapes

The shape language of this design system is **Rounded (Level 2)**. 

Components utilize a base corner radius of **0.5rem (8px)**. This specific level of roundedness is chosen to strike a balance between the "sharp" professionalism of government institutions and the "soft" approachability of modern consumer apps. 

- **Standard Elements**: Buttons and Input fields use the 8px radius.
- **Large Containers**: Cards and Modals use a 1rem (16px) radius to emphasize their role as distinct content areas.
- **Status Pills**: Tags and chips use a fully rounded "pill" shape to distinguish them from actionable buttons.

## Components

This design system defines several core components designed for maximum accessibility and clarity:

- **Buttons**: Primary buttons are solid Navy with White text. Secondary buttons use a Navy outline. All buttons have a minimum height of 48px and clear focus states for keyboard navigation.
- **Input Fields**: Feature a light gray border that thickens and changes to Navy upon focus. Labels are always visible (never placeholder-only) to meet AAA standards.
- **Cards**: Utilize a white background with a subtle 1px gray border or a very soft ambient shadow to distinguish themselves from the main page background.
- **Action Chips**: Used for selecting categories or voting topics. They utilize a pill shape and high-contrast color shifts when toggled.
- **Progress Indicators**: Steppers and progress bars use the Scarlet accent color to show completion, providing a clear visual sense of momentum through civic tasks.
- **Voter Checklists**: A specialized list component with large checkboxes and strike-through text for completed items, designed to make complex civic processes feel manageable.