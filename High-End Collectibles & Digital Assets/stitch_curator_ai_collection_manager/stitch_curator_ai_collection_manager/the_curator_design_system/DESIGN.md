---
name: The Curator Design System
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
  on-surface-variant: '#444842'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#747871'
  outline-variant: '#c4c8c0'
  surface-tint: '#546251'
  primary: '#536150'
  on-primary: '#ffffff'
  primary-container: '#6b7a68'
  on-primary-container: '#ffffff'
  inverse-primary: '#bbcbb6'
  secondary: '#6b5c4c'
  on-secondary: '#ffffff'
  secondary-container: '#f4dfcb'
  on-secondary-container: '#716252'
  tertiary: '#5e5d58'
  on-tertiary: '#ffffff'
  tertiary-container: '#777670'
  on-tertiary-container: '#ffffff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e7d2'
  primary-fixed-dim: '#bbcbb6'
  on-primary-fixed: '#121f11'
  on-primary-fixed-variant: '#3c4a3b'
  secondary-fixed: '#f4dfcb'
  secondary-fixed-dim: '#d7c3b0'
  on-secondary-fixed: '#241a0e'
  on-secondary-fixed-variant: '#524436'
  tertiary-fixed: '#e5e2db'
  tertiary-fixed-dim: '#c9c6c0'
  on-tertiary-fixed: '#1c1c18'
  on-tertiary-fixed-variant: '#474742'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Libre Caslon Text
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 28px
    fontWeight: '400'
    lineHeight: 36px
  title-md:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
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
  label-sm:
    fontFamily: Manrope
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
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
  margin-mobile: 20px
  margin-desktop: 64px
  max-width: 1440px
---

## Brand & Style

The design system is engineered for high-net-worth art and object collectors who value discretion, heritage, and the tactile nature of curation. The brand personality is that of a "Silent Connoisseur"—intelligent and sophisticated, yet warm and deeply human. 

The aesthetic leverages **Organic Minimalism** mixed with **Tactile Skeuomorphism**. It moves away from cold, industrial tech tropes toward a "digital gallery" feel. The UI should evoke a sense of calm and stewardship, using soft gradients to mimic natural light and subtle textures to reference the physical materials of the art world (wood, paper, and stone). Every interaction is designed to feel deliberate and compassionate, mirroring the careful handling of a physical masterpiece.

## Colors

The palette is rooted in a natural, muted spectrum that highlights the art without competing with it. 

*   **Sage Green (Primary):** A sophisticated, earthy green used for primary actions, active states, and branding. It represents growth and preservation.
*   **Pale Wood (Secondary/Accent):** A warm, desaturated tan used for secondary containers, dividers, and subtle background textures.
*   **Crisp White & Off-White:** The primary background is a pure White for high-clarity viewing areas, while the tertiary `F4F1EA` (Parchment) is used for utility panels to reduce eye strain.
*   **Text:** Primary text is a deep "Charcoal Green" rather than pure black, maintaining the organic softness of the system.

## Typography

This design system utilizes a high-contrast typographic pairing to balance heritage with modern utility.

*   **Headings:** **Libre Caslon Text** is used for all editorial and archival titles. Its classic proportions convey the authority of a museum and the intimacy of a private library.
*   **UI & Data:** **Manrope** provides a highly legible, modern sans-serif foundation for navigation, data visualization, and long-form collection data. Its geometric yet friendly character keeps the interface feeling current and accessible.
*   **Hierarchy:** Use generous leading (line height) for body text to ensure a relaxed reading pace, reflective of the slow-living philosophy of the target audience.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid with Generous Breathability**. The content is centered within a 1440px container on desktop to maintain focus.

*   **The "Air" Principle:** Spacing should be larger than typical SaaS applications. Utilize `64px` or `80px` of vertical rhythm between major sections to prevent the interface from feeling cluttered or stressful.
*   **Grid:** A 12-column grid is used for desktop, reflowing to a 4-column grid on mobile. 
*   **Margins:** Desktop margins are intentionally wide (64px) to create a "framed" effect, similar to a matted photograph in a gallery.

## Elevation & Depth

Visual hierarchy is established through **Ambient Depth** and **Material Layering** rather than harsh shadows.

*   **Soft Shadows:** Use very large blur radii (30px+) with low-opacity Sage-tinted shadows (e.g., `rgba(107, 122, 104, 0.08)`) to make cards appear to float gently above the surface.
*   **Tonal Layering:** Use the Pale Wood and Parchment tones to denote secondary depth. For example, a "Collection Details" panel should sit on a Parchment background to distinguish it from the main gallery.
*   **Soft Gradients:** Apply subtle linear gradients (top-to-bottom) on primary buttons and containers to mimic a soft overhead light source hitting a matte surface.

## Shapes

The shape language is defined by **Organic Curves**. Avoid harsh 90-degree angles.

*   **Primary Radius:** A base `0.5rem` is used for inputs and small components. 
*   **Organic Containers:** Large containers, such as image cards and modals, should use `rounded-xl` (1.5rem) to feel approachable and soft.
*   **Irregularity:** For decorative elements or high-level category chips, utilize slightly asymmetrical border-radii (e.g., `24px 32px 24px 32px`) to mimic the hand-crafted nature of organic objects.

## Components

*   **Buttons:** Primary buttons use a "Pill-plus" shape (high radius) with a subtle Sage-to-Dark-Sage gradient. Text is always centered and set in Manrope SemiBold.
*   **Cards:** Gallery cards feature a White background, a subtle 1px border in a lighter shade of Pale Wood, and a soft ambient shadow. Images within cards should have a slight inner glow to appear "set in" to the card.
*   **Secondary Containers:** Sidebars and footer areas should use a "Wood-grain" subtle texture—a very low-opacity SVG pattern overlaying the Pale Wood color.
*   **Input Fields:** Search and data entry fields are minimalist, using only a bottom border or a very soft Parchment fill, focusing on the elegance of the typeface.
*   **Curation Chips:** Used for tagging art periods or styles, these use a Pale Wood background with Sage Green text and high-roundedness (Pill).
*   **Status Indicators:** Use soft, pulsing rings for "Live Auction" or "Active Inquiry" states, maintaining the organic motion of the system.