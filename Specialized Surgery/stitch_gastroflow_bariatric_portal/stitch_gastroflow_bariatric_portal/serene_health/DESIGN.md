---
name: Serene Health
colors:
  surface: '#f8fafb'
  surface-dim: '#d8dadb'
  surface-bright: '#f8fafb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f5'
  surface-container: '#eceeef'
  surface-container-high: '#e6e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#3d4949'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#eff1f2'
  outline: '#6d7979'
  outline-variant: '#bdc9c8'
  surface-tint: '#006a6a'
  primary: '#006767'
  on-primary: '#ffffff'
  primary-container: '#008282'
  on-primary-container: '#f3fffe'
  inverse-primary: '#72d6d6'
  secondary: '#8c4e31'
  on-secondary: '#ffffff'
  secondary-container: '#ffae8a'
  on-secondary-container: '#793f23'
  tertiary: '#525f5d'
  on-tertiary: '#ffffff'
  tertiary-container: '#6a7775'
  on-tertiary-container: '#f3fffc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#8ff3f2'
  primary-fixed-dim: '#72d6d6'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f50'
  secondary-fixed: '#ffdbcd'
  secondary-fixed-dim: '#ffb596'
  on-secondary-fixed: '#360f00'
  on-secondary-fixed-variant: '#70371c'
  tertiary-fixed: '#d7e5e2'
  tertiary-fixed-dim: '#bcc9c7'
  on-tertiary-fixed: '#121e1c'
  on-tertiary-fixed-variant: '#3d4947'
  background: '#f8fafb'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.25'
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
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

This design system is built for a healthcare environment that prioritizes emotional safety and proactive care. The brand personality is **Clean & Encouraging**, striking a balance between clinical expertise and human warmth. It moves away from the cold, sterile nature of traditional medical interfaces toward a "Corporate Modern" aesthetic softened by organic elements.

The UI aims to evoke a sense of **relief and clarity**. By utilizing heavy whitespace and a calming palette, the system reduces cognitive load for users who may be in stressful health-related situations. The visual style leans into soft, tactile surfaces that feel approachable, ensuring the experience feels more like a supportive partner than a rigid institution.

## Colors

The color strategy uses **Teal** as the primary anchor to communicate stability and professional health standards. This is contrasted by **Peach**, an accent color used strategically for high-conversion actions and moments of encouragement. Peach provides a human "pulse" to the interface, preventing the teal from feeling too cold.

**Neutral tones** are rooted in a soft grey with slight blue undertones to maintain freshness. Backgrounds should primarily use the tertiary teal tint or pure white to maximize the "clean" aesthetic. Semantic colors (Success, Warning, Error) should be desaturated to fit the calming palette while maintaining clear communication.

## Typography

This design system utilizes a dual-font approach. **Manrope** is used for headlines; its modern, balanced geometry provides a refined and trustworthy appearance. **Inter** is employed for body text and functional labels to ensure maximum legibility and a systematic, utilitarian feel for complex medical data.

Hierarchy is established through scale rather than extreme weight. Avoid using "Black" or "Heavy" weights to keep the interface light and airy. Use sentence case for headlines to maintain a friendly, conversational tone.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop (12 columns, 1140px max-width) and a fluid model for mobile. A generous spacing rhythm based on an 8px scale is used to create "breathing room," which is essential for an encouraging healthcare experience.

Content should be grouped into clear logical sections with ample padding (typically `lg` or `xl` spacing) between them. This prevents the "wall of information" effect common in medical software. Gutters are kept wide to ensure a relaxed visual pace.

## Elevation & Depth

Depth in this design system is created through **Ambient Shadows**. These are extra-diffused, low-opacity shadows with a subtle Teal tint (`rgba(13, 139, 139, 0.08)`). This avoids the "dirty" look of pure black shadows and makes elements feel as though they are floating softly above a clean surface.

We use **Tonal Layers** to distinguish between global navigation and content areas. Surfaces that require user interaction (like cards and buttons) should have a slightly higher elevation or a subtle 1px border in a light grey-teal to define their boundaries without adding visual noise.

## Shapes

The shape language is consistently **Rounded**. The 0.5rem (8px) base radius removes harsh edges, signaling safety and empathy. Containers like cards and large modals should utilize `rounded-xl` (1.5rem/24px) to emphasize the soft, welcoming nature of the brand.

Avoid sharp 90-degree angles entirely. Even small elements like checkboxes and progress bars must have at least a `soft` radius to maintain the encouraging aesthetic.

## Components

**Buttons:** 
Primary buttons use the Teal base with white text. To increase "encouragement," the CTA (Call to Action) buttons for booking or signing up use the Peach accent. Hover states should involve a gentle upward shift and a slightly more diffused shadow.

**Cards:** 
Cards are the primary container for information. They feature a white background, `rounded-xl` corners, and a soft ambient shadow. For healthcare providers or patient summaries, cards may include a thin 1px Teal-tinted border to highlight their importance.

**Input Fields:** 
Inputs use a neutral grey background that turns white on focus, with a Teal 2px border. Focus states are crucial for accessibility; they should be clearly visible but soft.

**Chips & Labels:** 
Used for status indicators (e.g., "Confirmed", "Pending"). These use high-contrast text on very desaturated versions of the status color (e.g., Teal text on a Teal-tinted light background).

**Additional Components:**
- **Progress Steppers:** Use soft, rounded lines and Peach accents for completed steps to give a sense of achievement.
- **Empty States:** Use friendly, illustrated icons and warm, conversational copy to guide the user back to the main flow.