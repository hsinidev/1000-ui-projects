---
name: Relo-Luxe
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#44474d'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#75777e'
  outline-variant: '#c5c6ce'
  surface-tint: '#4f5e7e'
  primary: '#041632'
  on-primary: '#ffffff'
  primary-container: '#1b2b48'
  on-primary-container: '#8393b5'
  inverse-primary: '#b7c7eb'
  secondary: '#a63a25'
  on-secondary: '#ffffff'
  secondary-container: '#ff7c62'
  on-secondary-container: '#721504'
  tertiary: '#151716'
  on-tertiary: '#ffffff'
  tertiary-container: '#2a2b2a'
  on-tertiary-container: '#929291'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#b7c7eb'
  on-primary-fixed: '#091b37'
  on-primary-fixed-variant: '#374765'
  secondary-fixed: '#ffdad3'
  secondary-fixed-dim: '#ffb4a5'
  on-secondary-fixed: '#3e0500'
  on-secondary-fixed-variant: '#852310'
  tertiary-fixed: '#e3e2e0'
  tertiary-fixed-dim: '#c7c6c5'
  on-tertiary-fixed: '#1a1c1b'
  on-tertiary-fixed-variant: '#464746'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-xl:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: EB Garamond
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
  label-sm:
    fontFamily: Manrope
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
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
  container-max: 1280px
  gutter: 24px
---

## Brand & Style
The brand personality centers on "Compassionate Authority." This design system balances the high-stakes logistical nature of international relocation with the emotional sensitivity required when moving executive families. The visual style is rooted in **Editorial Minimalism**, utilizing generous whitespace, intentional asymmetry, and high-end typography to create a sense of calm and curated care.

The interface should feel like a premium concierge service rather than a utility. To achieve this, the design system employs "soft-glow" CSS effects—subtle, colored outer glows that mimic a warm light source—to soften the corporate edges of the Navy and Terra-Cotta palette. The emotional response is one of settled confidence: the user should feel that every detail is being handled by a sophisticated, trustworthy partner.

## Colors
The palette uses **Silk White (#F9F8F6)** as the primary canvas color to avoid the clinical feel of pure white, providing a warm, paper-like foundation. **Navy (#1B2B48)** serves as the anchor, used for primary typography and structural elements to establish professional trust. 

**Terra-Cotta (#C04D36)** is used sparingly as a "humanizing" accent. It highlights interactive elements and key emotional touchpoints, representing the warmth of a new home. For state-based feedback, use desaturated versions of these tones to maintain the sophisticated atmosphere. Soft-glow effects should utilize the Terra-Cotta hex with high transparency to create "halo" depths around featured cards or active states.

## Typography
This design system employs a classic serif/sans-serif pairing to communicate the "Warm-Professional" aesthetic. **EB Garamond** is the voice of the brand, used for all headlines and display text to evoke editorial heritage and intellectual sophistication. It should be typeset with slightly tighter letter-spacing in display sizes.

**Manrope** provides a functional, highly legible counterpoint for body copy and UI labels. Its clean, geometric forms ensure that complex relocation data remains accessible and calm. Use "label-sm" for utility-heavy elements like form headers or breadcrumbs, always in uppercase with increased tracking to maintain a disciplined, high-end feel.

## Layout & Spacing
The layout follows a **Fixed-Grid Editorial** model. On desktop, content is contained within a 12-column grid with generous 80px top/bottom margins to allow the design to breathe. On mobile, the system transitions to a single-column flow with 24px side gutters to ensure ease of use during travel.

Spacing should be used to group related information into "chapters." Use the "xl" spacing unit to separate major content sections, reinforcing the editorial feel. Alignment should occasionally break the grid—such as offsetting an image from its caption—to mimic high-end print layouts.

## Elevation & Depth
Depth is achieved through **Tonal Layering and Soft Glows** rather than traditional high-contrast shadows. Surfaces should appear to sit just above the Silk White background.

1.  **Level 0 (Base):** Silk White background.
2.  **Level 1 (Cards):** Navy or White surfaces with a very subtle 2px blur shadow (Navy at 5% opacity).
3.  **The "Luxe Glow":** For active or featured elements, apply a `box-shadow` using the Terra-Cotta color at 10-15% opacity with a large 40px spread. This creates a soft "aura" effect that feels warm and inviting.
4.  **Overlays:** Use a subtle backdrop blur (8px) on modals to maintain context while focusing the executive's attention.

## Shapes
This design system utilizes a **Soft (Level 1)** shape language. The 0.25rem (4px) base radius provides a tailored, "expensive" feel—reminiscent of high-end stationery or leather goods. 

Avoid large, playful radii. The goal is precision and structure. Containers and inputs should use the base `rounded` (4px), while primary call-to-action buttons may use `rounded-lg` (8px) to subtly differentiate them from the more rigid informational components.

## Components
### Buttons
Primary buttons use the Navy background with Silk White text, featuring a subtle Terra-Cotta soft-glow on hover. Secondary buttons are outlined in Navy with a 1px weight.

### Input Fields
Inputs should feel like filling out a guest ledger. Use a 1px bottom border in Navy for a "minimalist form" look, with the label in "label-sm" style floating above. On focus, the bottom border thickens to 2px and a faint Terra-Cotta glow appears.

### Cards
Cards are the primary vehicle for relocation data (e.g., "School Search" or "Visa Status"). They should have a 1px Silk-Grey border or a soft shadow. Use EB Garamond for card titles to maintain the editorial tone.

### Progress Indicators
Given the long-term nature of relocation, use "Timeline" components. These should be thin Navy lines with Terra-Cotta dots, using the soft-glow effect to indicate the "Current" stage.

### Interactive "Concierge" Chips
Small, Navy-outlined chips used for filtering or quick-selection. They use the Manrope font at a small scale and transition to a solid Navy fill when selected.