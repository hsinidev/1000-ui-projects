---
name: UrologyPro Biomorphic Medical System
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#43474f'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#747780'
  outline-variant: '#c3c6d0'
  surface-tint: '#3e5f91'
  primary: '#001937'
  on-primary: '#ffffff'
  primary-container: '#002d5c'
  on-primary-container: '#7696cb'
  inverse-primary: '#a8c8ff'
  secondary: '#006b5d'
  on-secondary: '#ffffff'
  secondary-container: '#90f1dd'
  on-secondary-container: '#006f61'
  tertiary: '#121a1a'
  on-tertiary: '#ffffff'
  tertiary-container: '#262f2f'
  on-tertiary-container: '#8d9796'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3ff'
  primary-fixed-dim: '#a8c8ff'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#254777'
  secondary-fixed: '#93f4e0'
  secondary-fixed-dim: '#76d7c4'
  on-secondary-fixed: '#00201b'
  on-secondary-fixed-variant: '#005046'
  tertiary-fixed: '#dbe4e3'
  tertiary-fixed-dim: '#bfc8c7'
  on-tertiary-fixed: '#151d1d'
  on-tertiary-fixed-variant: '#404848'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
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
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  xxl: 80px
  gutter: 24px
  margin-safe: 32px
---

## Brand & Style

The brand personality of this design system is rooted in "Technical Precision with Human Empathy." It targets patients seeking expert urological care and healthcare professionals who require efficient clinical workflows. The aesthetic is a fusion of **Corporate Modernism** and **Biomorphic Design**, moving away from clinical rigidity toward organic, soft-edged shapes that mimic biological structures.

The visual narrative conveys security and sterile cleanliness through a high-contrast palette, while the "biomorphic" influence—seen in asymmetric curves and fluid container shapes—softens the technical nature of surgery to reduce patient anxiety. The interface feels high-tech, yet inherently natural and approachable.

## Colors

The color strategy uses **Navy Blue** (#002D5C) as the foundation of authority and surgical precision. It is used for primary headings, navigation, and core interaction points to establish trust.

**Seafoam Green** (#76D7C4) serves as the secondary "healing" color, used for success states, active biological indicators, and call-to-action buttons. To maintain the medical aesthetic, **White** and **Tertiary Seafoam Tint** (#F0F9F8) provide a spacious, sterile background that allows technical information to breathe. Neutral grays are replaced with cool-toned Navy tints to maintain a cohesive, high-end medical feel.

## Typography

This design system utilizes a dual-font approach to balance technicality with readability. **Space Grotesk** is used for headlines; its geometric and slightly technical letterforms mirror the precision of surgical instruments. For body copy and patient data, **Manrope** provides a balanced, modern, and highly legible experience that feels calm and professional.

To emphasize the biomorphic theme, large headlines should use tighter letter-spacing, while functional labels should be tracked out for clarity in clinical settings.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid Grid**. Content is housed within a 12-column system (max-width 1280px) for desktop, but spacing is generous to reflect a "premium" medical experience. 

Rhythm is based on a **4px base unit**. Elements use "Biological Breathing Room"—increased padding within cards and around text blocks to prevent the UI from feeling claustrophobic. Use `xl` (48px) and `xxl` (80px) spacing between major sections to emphasize the clean, sterile aesthetic.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Soft Ambient Shadows**. Instead of harsh shadows, the system uses a "Seafoam Glow" technique: shadows are tinted with the secondary color (Navy or Seafoam) at very low opacities (3-5%) to create a soft, lifelike lift.

1.  **Base Surface:** White (#FFFFFF).
2.  **Raised Biomorphic Containers:** Tertiary Seafoam Tint (#F0F9F8) with a 1px border in a slightly darker Navy-tinted gray.
3.  **Active Elements:** Low-opacity background blurs (10px) are used for surgical overlays and modal windows to maintain the clean, "glass-like" medical vibe without losing context.

## Shapes

The "Biomorphic" nature of this design system is most evident in its shapes. While standard elements use a **Rounded** (0.5rem) base, container corners should be asymmetrical where possible—for example, a card might have a 32px top-left radius and a 12px bottom-right radius to mimic organic cellular structures.

Buttons and active categories use "Super-ellipses" (Squircles) rather than perfect circles or rectangles, providing a softer, more natural touchpoint that feels comfortable and safe.

## Components

### Buttons & Interaction
Primary buttons utilize the **Navy Blue** background with white text, featuring a high-radius (pill-like) shape. Hover states introduce a subtle biomorphic expansion (1.02x scale) and a soft **Seafoam** glow.

### Clean Cards
Service cards should be borderless, using the tertiary background color. To achieve the biomorphic look, the top edge should have a slight "wave" or organic curve. Information is clustered with high internal padding (32px).

### Secure Form Fields
Input fields are designed to feel "Fortified." Use a light Navy stroke (1px) that thickens to 2px on focus. Backgrounds should be pure white to stand out against the tertiary page background, signaling a secure area for sensitive patient data entry.

### Service Categories
Use biological icons (abstracted urological forms) housed in soft, organic Seafoam shapes. Each category acts as a "Cell"—a self-contained unit with a distinct, soft-edged silhouette.

### Progress & Health Indicators
Use "Pulse" animations on active state icons. Loading states should utilize a fluid, mercury-like motion rather than a standard circular spinner to reinforce the biological narrative.