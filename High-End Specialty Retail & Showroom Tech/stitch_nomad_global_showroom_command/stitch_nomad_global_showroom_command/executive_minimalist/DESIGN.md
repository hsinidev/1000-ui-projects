---
name: Executive Minimalist
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#444650'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#5d5e63'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfe4'
  on-secondary-container: '#626267'
  tertiary: '#131515'
  on-tertiary: '#ffffff'
  tertiary-container: '#272929'
  on-tertiary-container: '#8f9090'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
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
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: '0'
spacing:
  unit: 4px
  container-margin-mobile: 16px
  container-margin-desktop: 64px
  gutter: 16px
  section-gap: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style
This design system centers on **Engineering-grade Minimalism**, evoking the precision of high-end chronometers and aerospace instrumentation. The target audience comprises high-net-worth executives and luxury brand managers who require immediate clarity, authoritative aesthetics, and a frictionless experience. 

The visual narrative is "Industrial Luxury": a blend of corporate reliability and bespoke exclusivity. The interface utilizes a strict structural grid to communicate order and power, while subtle metallic gradients provide a tactile, premium finish. The emotional response is one of total confidence—a digital concierge that is as disciplined as it is sophisticated.

## Colors
The palette is rooted in **Royal Blue (#002366)**, used sparingly for primary actions and brand identifiers to maintain its authoritative impact. The primary canvas is **White (#FFFFFF)**, ensuring maximum legibility and a "gallery" feel.

**Brushed Steel** is implemented through two tones: a medium-dark slate (#8E8E93) for secondary text and icons, and a lighter silver (#C0C0C0) for borders and subtle metallic accents. Use the silver linear gradient for high-end interactive states or key dividers to simulate light hitting machined metal. Contrast ratios must never fall below 4.5:1 for body text and 3:1 for large display elements.

## Typography
This design system utilizes **Inter** for its systematic, utilitarian clarity. The typesetting mimics architectural blueprints: precise, rhythmic, and highly legible. 

**Hierarchy Rules:**
- **Display Text:** Reserved for impact moments. Use tight letter-spacing to create a "locked" look.
- **Label Caps:** Used for metadata, categories, and small headers to inject an authoritative, industrial feel.
- **Body Text:** Standardize on 16px for mobile-first accessibility.
- **Data Mono:** While Inter is the primary face, use a monospaced font for tracking numbers, coordinates, or financial figures to reinforce the "engineering-grade" narrative.

## Layout & Spacing
The layout follows a **Rigid 8pt Grid System**. Everything is aligned to a predictable rhythm to reflect executive order.

- **Mobile:** A 4-column fluid layout with 16px outer margins. Content should be stacked vertically with clear, generous negative space between functional groups.
- **Desktop:** A 12-column fixed-center grid (max-width 1280px). 
- **The "Technical Edge":** Use thin (1px) Brushed Steel dividers to separate layout sections instead of relying solely on whitespace. This mimics the partitions found in luxury luggage or high-end vehicle dashboards.

## Elevation & Depth
Depth in this design system is achieved through **Tonal Layering and Precision Outlines** rather than soft shadows.

1.  **Level 0 (Base):** White (#FFFFFF) background.
2.  **Level 1 (Surfaces):** Neutral Gray (#F8F9FA) for secondary content areas or card backgrounds.
3.  **The "Steel" Border:** Instead of drop shadows, use a 1px solid border (#C0C0C0) to define interactable elements.
4.  **Metallic Depth:** For active states or "Featured" cards, use a very subtle, high-diffusion ambient shadow (4% opacity, Royal Blue tint) combined with a Brushed Steel gradient border to simulate a raised metal plate.

## Shapes
The shape language is strictly **Sharp (0px)**. Rounded corners are avoided to maintain an aggressive, professional, and architectural aesthetic. 

Every button, input field, and card must have 90-degree angles. This conveys a "no-nonsense" engineering quality. The only exception is the use of circular "Status Indicators" (e.g., online/offline dots), which should remain small and functional.

## Components

**Buttons**
- **Primary:** Solid Royal Blue background, white text, sharp corners. No border.
- **Secondary:** Transparent background, 1px Brushed Steel (#8E8E93) border, Royal Blue text.
- **Hover/Active:** Apply the Brushed Steel linear gradient to the background to simulate a physical metal press.

**Input Fields**
- Bottom-border only (2px, #C0C0C0) or a full rectangular outline. 
- Use "Label Caps" for floating labels above the input.
- Focus state: Border color shifts to Royal Blue with a 1px inner inset.

**Cards**
- White background, 1px #C0C0C0 border.
- No shadows.
- Use a 4px Royal Blue vertical accent bar on the left edge for "High Priority" items.

**Lists & Navigation**
- Mobile-first bottom navigation with high-contrast icons (24px).
- List items separated by a 1px horizontal Brushed Steel line.
- Active nav items use a subtle Royal Blue underline.

**Additional Components**
- **The "Status Bar":** A specialized header component showing real-time logistics or brand health data in "Data Mono" typography.
- **Precision Toggle:** A square-based toggle switch (no rounds) that slides with mechanical rigidity.