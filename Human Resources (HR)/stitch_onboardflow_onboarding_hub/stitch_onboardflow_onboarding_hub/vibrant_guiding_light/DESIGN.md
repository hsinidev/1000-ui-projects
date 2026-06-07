---
name: Vibrant Guiding Light
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
  on-surface-variant: '#584237'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#8c7265'
  outline-variant: '#dfc0b2'
  surface-tint: '#9f4200'
  primary: '#9f4200'
  on-primary: '#ffffff'
  primary-container: '#f27121'
  on-primary-container: '#541f00'
  inverse-primary: '#ffb692'
  secondary: '#4f5f78'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1ff'
  on-secondary-container: '#53637d'
  tertiary: '#605e58'
  on-tertiary: '#ffffff'
  tertiary-container: '#99978f'
  on-tertiary-container: '#30302a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcb'
  primary-fixed-dim: '#ffb692'
  on-primary-fixed: '#341100'
  on-primary-fixed-variant: '#793100'
  secondary-fixed: '#d4e3ff'
  secondary-fixed-dim: '#b7c7e5'
  on-secondary-fixed: '#0a1c32'
  on-secondary-fixed-variant: '#374860'
  tertiary-fixed: '#e6e2d9'
  tertiary-fixed-dim: '#c9c6be'
  on-tertiary-fixed: '#1c1c17'
  on-tertiary-fixed-variant: '#484741'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  display:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '700'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
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
  lg: 40px
  xl: 64px
  gutter: 16px
  margin-mobile: 20px
---

## Brand & Style
The brand personality of this design system is built on the concept of "Enthusiastic Guidance." It aims to transform the often-stressful process of onboarding into an immersive, welcoming journey. The UI balances the energy of high-growth tech with the grounded reliability of a professional service.

The design style utilizes a **Modern Minimalist** framework enriched with **Tactile** depth. By using a warm, creamy canvas instead of sterile white, the interface feels human and approachable. Interaction patterns are designed to feel fluid and supportive, ensuring the user feels empowered rather than overwhelmed. The aesthetic is optimized for high-impact mobile experiences, utilizing large touch targets and clear visual hierarchies.

## Colors
The palette is centered around three distinct pillars:
- **Warm Orange (Primary):** Used for calls-to-action, progress indicators, and active states. It signals energy and momentum.
- **Navy (Secondary):** Provides the professional anchor. Used for typography, navigation bars, and structural elements to instill trust.
- **Cream (Background):** Replaces pure white to create a soft, paper-like warmth that reduces eye strain and feels more inviting.

Neutral grays are used sparingly for borders and secondary labels, ensuring the focus remains on the vibrant brand colors.

## Typography
This design system utilizes **Plus Jakarta Sans** for its modern, friendly, and highly legible geometric forms. The typeface choice ensures that even complex onboarding instructions feel breezy and accessible.

Headlines use a heavier weight and tighter letter spacing to create a sense of confidence. Body text is set with generous line height to prioritize readability on mobile devices. Labels and captions utilize a slightly medium weight to maintain clarity at smaller scales, particularly for document management and form fields.

## Layout & Spacing
The layout follows a **Fluid Grid** model optimized for mobile-first consumption. On mobile devices, a 4-column grid is used with 20px side margins to give content room to breathe. 

Spacing follows a strict 8px rhythmic scale. We use "Internal Padding" (md) for card containers to ensure content doesn't feel cramped, and "Section Spacing" (lg) to clearly demarcate different steps in the onboarding flow. For document lists and chat interfaces, a tighter vertical rhythm (sm) is applied to maximize information density without sacrificing touch accuracy.

## Elevation & Depth
Depth in this design system is achieved through **Tonal Layers** and **Ambient Shadows**. Surfaces do not simply "sit" on top of the background; they emerge from it.

The Cream background acts as the lowest layer. Cards and interactive modules use a pure white surface with a very soft, diffused Navy-tinted shadow (0px 4px 20px, 4% opacity) to create a subtle lift. High-priority elements, like floating action buttons or active chat bubbles, use a slightly more pronounced shadow to signify "Immediacy." This creates a tactile experience where the user understands what can be moved, swiped, or tapped.

## Shapes
The shape language is consistently **Rounded**, reinforcing the friendly and modern brand personality. 

Standard components like input fields and buttons utilize a 0.5rem (8px) radius. Larger containers, such as onboarding cards and document previews, use the `rounded-lg` (1rem) setting to create a softer, more contained feel. Progress steppers and interactive "chips" in the chat interface use the `rounded-xl` (1.5rem) or full pill shapes to indicate their interactive and dynamic nature.

## Components

### Buttons & Controls
Primary buttons are vibrant Orange with Navy text or white text for high contrast. They feature a slight scale-down animation on press to provide tactile feedback on mobile. Secondary buttons use a Navy outline or a subtle Cream-tinted fill.

### Progress Steppers
The stepper is a signature component. It uses a horizontal track on mobile with "filled" Orange nodes for completed steps and a "glowing" Orange ring for the current active state. Transitioning between steps should feel like a horizontal slide.

### Chat Interface
Chat bubbles for the system/bot are Navy with white text to represent authority and help. User bubbles are Cream with a thin Navy border. The input area is pinned to the bottom of the mobile screen with a large, accessible Orange "Send" icon.

### Document Management
Documents are presented as cards with clear file-type icons. A "Status Chip" (e.g., Pending, Verified) is positioned in the top right. Actions like "Upload" or "Sign" are primary Orange text links to ensure they are the first things a user sees.

### Interactive Maps
Maps use a customized "Light Mode" style that matches the Cream and Navy palette. Markers are vibrant Orange dots with a subtle pulse animation to draw the user's attention to specific locations or required visits.

### Cards
All cards feature the standard `rounded-lg` corners and a soft ambient shadow. They are the primary container for all onboarding tasks, ensuring that even complex data entry feels modular and manageable.