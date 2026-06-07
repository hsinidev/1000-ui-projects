---
name: Hearth & Acre
colors:
  surface: '#fff8f4'
  surface-dim: '#e2d8d1'
  surface-bright: '#fff8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fcf2ea'
  surface-container: '#f6ece5'
  surface-container-high: '#f1e6df'
  surface-container-highest: '#ebe1da'
  on-surface: '#1f1b17'
  on-surface-variant: '#54433e'
  inverse-surface: '#352f2b'
  inverse-on-surface: '#f9efe8'
  outline: '#87736d'
  outline-variant: '#dac1bb'
  surface-tint: '#944933'
  primary: '#914631'
  on-primary: '#ffffff'
  primary-container: '#af5e47'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb5a0'
  secondary: '#566249'
  on-secondary: '#ffffff'
  secondary-container: '#d7e4c5'
  on-secondary-container: '#5a674d'
  tertiary: '#775534'
  on-tertiary: '#ffffff'
  tertiary-container: '#926d4a'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd1'
  primary-fixed-dim: '#ffb5a0'
  on-primary-fixed: '#3b0900'
  on-primary-fixed-variant: '#76321e'
  secondary-fixed: '#dae7c7'
  secondary-fixed-dim: '#becbac'
  on-secondary-fixed: '#141e0b'
  on-secondary-fixed-variant: '#3f4a33'
  tertiary-fixed: '#ffdcbe'
  tertiary-fixed-dim: '#ebbe95'
  on-tertiary-fixed: '#2c1600'
  on-tertiary-fixed-variant: '#5f4021'
  background: '#fff8f4'
  on-background: '#1f1b17'
  surface-variant: '#ebe1da'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
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
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base-unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-gap: 80px
  stack-sm: 12px
  stack-md: 24px
---

## Brand & Style

This design system is built on the concept of "The Modern Heritage." It balances the reliability of a traditional brokerage with the warmth of a family home. The personality is grounded, empathetic, and organized, aiming to reduce the stress of home buying by creating a digital environment that feels like a comfortable living room.

The design style is **Corporate Modern with Tactile influences**. It utilizes generous whitespace and a "soft-UI" approach to ensure the interface feels approachable rather than clinical. By mixing traditional serif elements with modern functional layouts, the system establishes immediate trust and professional authority while maintaining a neighborly, suburban charm.

## Colors

The palette is derived from natural, earthy materials to evoke a sense of "home" and "land."

*   **Primary (Terracotta):** Used for primary actions, branding, and key highlights. It provides a warm, energetic focal point that feels artisanal.
*   **Secondary (Sage Green):** Represents growth, peace, and suburban landscapes. Used for secondary actions, "New Listing" tags, and success states.
*   **Background (Cream):** A soft, warm off-white that reduces eye strain and feels more premium and inviting than pure digital white.
*   **Neutral (Deep Umber):** Used for text and borders instead of pure black to maintain the organic, warm temperature of the design system.

## Typography

This design system employs a sophisticated dual-type strategy. **Noto Serif** is used for all headlines and display text to provide an editorial, "established" feel that mirrors traditional real estate signage and luxury home magazines.

**Manrope** is used for all functional text, including body copy, property details, and labels. Its geometric yet slightly softened terminals offer high readability and a modern, efficient contrast to the serif headings. Letter spacing is slightly tightened on large headings for impact and slightly opened on small labels for clarity.

## Layout & Spacing

The system uses a **fixed grid model** for large screens (centered 12-column grid with a 1280px max-width) and a fluid model for mobile devices. 

The rhythm is based on an 8px linear scale. Generous vertical spacing (Section Gaps) is prioritized to allow the high-quality photography of homes to breathe, creating a feeling of "space" and "acreage." Internal component spacing (Stacks) should be kept consistent to maintain an organized, professional appearance.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and subtle tonal layering. Shadows should be soft, highly diffused, and use a slight warm tint (#4A443F at low opacity) rather than grey.

*   **Level 0 (Flat):** Used for the Cream background.
*   **Level 1 (Subtle):** Used for cards and property listings. Features a 4px Y-offset and 12px blur with 5% opacity.
*   **Level 2 (Hover/Floating):** Used for interactive cards and navigation menus. Features an 8px Y-offset and 24px blur with 10% opacity.
*   **Level 3 (Modal):** High elevation with a warm-tinted backdrop blur (glassmorphism) to keep the context of the underlying property visible.

## Shapes

The shape language is defined by a "Friendly-Professional" radius. The **Rounded** (Level 2) setting ensures that there are no harsh, aggressive corners, reinforcing the welcoming nature of the brand.

*   **Standard Components:** 8px (0.5rem) for buttons and input fields.
*   **Large Containers:** 16px (1rem) for property cards and image galleries.
*   **Specific Elements:** 24px (1.5rem) for high-impact promotional sections and "Search" containers.

## Components

*   **Buttons:** Primary buttons use the Terracotta color with white text. Secondary buttons use a Sage Green outline or ghost style. All buttons feature a 0.5rem radius and a subtle hover state that increases shadow depth rather than changing color dramatically.
*   **Cards:** Property listing cards are the cornerstone. They feature a Level 1 shadow, 1rem corner radius, and use Noto Serif for the price and Manrope for the address/details.
*   **Input Fields:** Use a subtle Cream-tinted fill with a 1px Umber border (20% opacity). Focus states transition the border to Terracotta.
*   **Chips/Tags:** Used for "Open House" or "New" badges. These use the Sage Green background with white text and a pill-shaped radius.
*   **Checkboxes & Radios:** Softly rounded (not square) to match the shape language, using Terracotta for the active state.
*   **Neighborhood Maps:** Integrated map components should use a customized "warm" tile skin that removes high-contrast blue water in favor of muted tones that match the palette.
*   **Agent Profile Cards:** Small, intimate components featuring circular headshots and a secondary "Contact" button to facilitate personal trust.