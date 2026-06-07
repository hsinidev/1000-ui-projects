---
name: WildResponse
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#58423c'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#8b716a'
  outline-variant: '#dfc0b7'
  surface-tint: '#a73918'
  primary: '#a43716'
  on-primary: '#ffffff'
  primary-container: '#c54f2c'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb5a0'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#595c5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#727577'
  on-tertiary-container: '#fbfdff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd1'
  primary-fixed-dim: '#ffb5a0'
  on-primary-fixed: '#3b0900'
  on-primary-fixed-variant: '#862201'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  display-hero:
    fontFamily: Newsreader
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 3rem
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 2rem
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
  label-emergency:
    fontFamily: Work Sans
    fontSize: 0.875rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Work Sans
    fontSize: 0.75rem
    fontWeight: '500'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
---

## Brand & Style

The design system is built to balance the high-stakes urgency of wildlife rescue with the profound hope of conservation success. It positions the organization as both a rapid-response emergency service and a deeply empathetic storyteller. 

The visual style is **Modern Corporate with Editorial influence**. It avoids the clinical feel of traditional NGOs by leaning into high-impact, full-bleed wildlife photography that places the viewer face-to-face with the subjects. By utilizing a sophisticated color palette and balanced typography, the interface communicates professionalism to donors while remaining highly functional for field agents and volunteers. The UI should feel grounded and stable, yet capable of immediate action.

## Colors

The palette is anchored by **Burnt Orange**, a color of vitality and immediate action. It is used strategically for primary call-to-actions, emergency alerts, and highlights within the narrative. **Slate** provides the necessary counterweight, offering a sense of institutional stability and calm during crises.

- **Primary (Burnt Orange):** Represents the heat of the rescue and the warmth of care. Use for "Donate," "Report an Injury," and active status indicators.
- **Secondary (Slate):** The professional foundation. Used for navigation bars, footer backgrounds, and secondary UI elements to provide a sense of authority.
- **Backgrounds:** Utilize off-white and light slate washes to maintain high legibility without the harshness of pure white, softening the overall experience.
- **Functional Colors:** Success states utilize a forest green, while critical alerts leverage a deeper crimson to distinguish from the brand orange.

## Typography

This design system employs a dual-typeface strategy to separate emotional narrative from technical utility.

- **Newsreader (Serif):** Used for headlines and long-form storytelling. Its literary qualities evoke empathy and emphasize the "voice" of the wildlife. It should be typeset with generous leading to allow the stories to breathe.
- **Work Sans (Sans-serif):** Used for all functional components, emergency guides, maps, and UI labels. Its neutral, optimized-for-screen geometry ensures that critical information—like medical instructions or GPS coordinates—is processed without friction.

Hierarchy is strictly enforced: Serif for the "Why," Sans-serif for the "How."

## Layout & Spacing

The layout utilizes a **12-column fixed grid** on desktop and a fluid single-column grid on mobile. The spacing rhythm is based on an 8px base unit to ensure consistent alignment across all components.

Large-scale wildlife photography should often break the grid or be used as full-width backgrounds to create an immersive, cinematic feel. Negative space is used intentionally to prevent the "urgency" of the brand from feeling cluttered or chaotic. In emergency guides, the layout switches to a tighter, more utilitarian spacing model to prioritize information density and speed of reading.

## Elevation & Depth

Visual hierarchy in this design system is achieved through **Tonal Layers and Ambient Shadows**. Rather than heavy skeuomorphism, we use depth to signify interactability and importance.

- **Surface Layers:** The base layer is typically light. Elevated "Cards" for animal profiles or rescue cases use a slightly higher brightness or a subtle 1px border in Slate-200.
- **Shadows:** Use extra-diffused, low-opacity shadows (e.g., 8% opacity) with a slight hint of Burnt Orange or Slate to ground the elements. Shadows should feel soft and natural, mimicking an overcast outdoor environment.
- **Interaction:** Upon hover, cards should lift slightly using a more pronounced but still soft shadow to invite the user into the story.

## Shapes

The shape language is defined by **Soft Roundedness**. This approach balances the rugged nature of wildlife work with the accessibility of a modern humanitarian organization.

All standard containers, buttons, and input fields utilize a 0.5rem (8px) radius. Larger cards and image containers can scale up to 1rem (16px) to emphasize the "soft" and protective nature of the rescue mission. Circles are reserved exclusively for avatars (staff/vets) or status indicators to provide a distinct visual language for people vs. data.

## Components

- **Buttons:** Primary buttons are Burnt Orange with white text, using bold Work Sans. They feature a subtle bottom-heavy shadow to feel "pressable." Secondary buttons use a Slate outline.
- **Emergency Chips:** High-visibility tags used on maps and lists. They use the `label-emergency` type style with high-contrast backgrounds to indicate species, status (e.g., "CRITICAL"), or location.
- **Story Cards:** Feature a vertical layout with a high-resolution image at the top, transitioning into a Newsreader headline. The bottom section uses a Work Sans "Read More" link.
- **Input Fields:** Designed for field use with thick borders in Slate-300, turning Burnt Orange on focus. Labels are always visible above the field for maximum clarity.
- **Map Markers:** Custom Slate-colored teardrops with Burnt Orange centers, designed to be legible over complex satellite imagery.
- **Impact Progress Bars:** Thick, soft-rounded bars showing funding goals. The "filled" portion uses a gradient of Burnt Orange to symbolize energy being poured into a cause.