---
name: Cinematic Pitch Platform
colors:
  surface: '#081425'
  surface-dim: '#081425'
  surface-bright: '#2f3a4c'
  surface-container-lowest: '#040e1f'
  surface-container-low: '#111c2d'
  surface-container: '#152031'
  surface-container-high: '#1f2a3c'
  surface-container-highest: '#2a3548'
  on-surface: '#d8e3fb'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#d8e3fb'
  inverse-on-surface: '#263143'
  outline: '#909097'
  outline-variant: '#46464c'
  surface-tint: '#c0c6de'
  primary: '#c0c6de'
  on-primary: '#2a3043'
  primary-container: '#020617'
  on-primary-container: '#72778d'
  inverse-primary: '#585e73'
  secondary: '#ffb95f'
  on-secondary: '#472a00'
  secondary-container: '#ee9800'
  on-secondary-container: '#5b3800'
  tertiary: '#b9c8de'
  on-tertiary: '#233143'
  tertiary-container: '#000713'
  on-tertiary-container: '#6a798d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dce1fb'
  primary-fixed-dim: '#c0c6de'
  on-primary-fixed: '#151b2d'
  on-primary-fixed-variant: '#40465a'
  secondary-fixed: '#ffddb8'
  secondary-fixed-dim: '#ffb95f'
  on-secondary-fixed: '#2a1700'
  on-secondary-fixed-variant: '#653e00'
  tertiary-fixed: '#d4e4fa'
  tertiary-fixed-dim: '#b9c8de'
  on-tertiary-fixed: '#0d1c2d'
  on-tertiary-fixed-variant: '#39485a'
  background: '#081425'
  on-background: '#d8e3fb'
  surface-variant: '#2a3548'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  status:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 16px
  gutter: 12px
---

## Brand & Style

This design system is engineered to evoke the high-stakes, high-energy atmosphere of a live tech keynote. The brand personality is prestigious, urgent, and visionary, designed to make every startup pitch feel like a major cinematic event. The target audience includes venture capitalists, angel investors, and tech entrepreneurs who value professional polish and seamless digital experiences.

The visual style blends **Glassmorphism** with **High-Contrast** elements. By utilizing translucent layers and deep background blurs, we create a sense of physical space and depth within the mobile viewport. The "Atmospheric" quality is achieved through the interaction of light (Amber) and void (Midnight Blue), ensuring that the primary focus remains on the live video stream and the real-time data overlays.

## Colors

The palette is strictly dark-mode to maintain focus on video content and reduce eye strain during long pitch sessions.

- **Midnight Blue (#020617):** The foundation. Used for the base background to create an infinite, "void-like" depth.
- **Amber (#F59E0B):** The interactive spark. Used exclusively for primary calls to action, high-priority notifications, and highlighting "Winning" pitches.
- **Smoke (#94A3B8):** The utility layer. Used for secondary text, borders of glass containers, and subtle icons to ensure they don't compete with the primary content.
- **Surface (#1E293B):** Used for card backgrounds and container fills where glassmorphism is not performance-optimal.

Apply subtle radial gradients using Midnight Blue and a slightly lighter navy to prevent the background from feeling flat.

## Typography

This design system utilizes a dual-font strategy to balance technical edge with absolute readability.

- **Headlines & Labels:** **Space Grotesk** provides a geometric, futuristic feel that aligns with the startup and tech-science theme. Use "H1" for event titles and "Label-Caps" for metadata like "VALUATION" or "SECTOR."
- **Body & Data:** **Inter** is used for all descriptive text, founder bios, and real-time chat. Its neutral, utilitarian design ensures clarity at small sizes on mobile devices.

All headlines should be set with tight letter-spacing to reinforce the "Bold" aesthetic, while body text should maintain standard spacing for maximum legibility against dark backgrounds.

## Layout & Spacing

This design system employs a **Fluid Grid** model optimized for mobile-first constraints. 

- **The Rhythm:** A 4px base unit governs all dimensions.
- **Safe Zones:** Content must respect a 16px lateral margin to ensure UI elements don't bleed into curved screen edges.
- **Vertical Flow:** Use 24px (lg) spacing between distinct sections (e.g., Video Player to Pitch Deck) and 8px (sm) between related elements (e.g., Name to Title).
- **Interactions:** Tap targets must be a minimum of 44x44px. In the live-stream view, prioritize the bottom 40% of the screen for interactive controls (Voting, Chat) to enable one-handed thumb operation.

## Elevation & Depth

Depth in this design system is created through light transmission rather than traditional shadows.

1.  **The Base Layer:** The deep Midnight Blue background.
2.  **The Glass Layer:** Used for floating panels (Chat, Leaderboards). Apply a `backdrop-filter: blur(12px)` with a semi-transparent `Smoke` fill at 10% opacity.
3.  **The Accent Layer:** Primary buttons and "Live" indicators. These should have a subtle outer glow (drop-shadow) using a saturated Amber color at 30% opacity to simulate an emissive light source.
4.  **Borders:** Instead of heavy shadows, use 1px "Ghost Borders" with a top-to-bottom gradient (Smoke at 20% to 5% opacity) to define the edges of glass cards.

## Shapes

The shape language is "Refined Geometric."

- **Cards & Modals:** Use a 16px (rounded-lg) radius to soften the high-contrast edges and make the glass panels feel like premium hardware.
- **Buttons:** Use a 8px (rounded-md) radius for a professional, precise appearance. Avoid fully rounded pill shapes except for status tags.
- **Inputs:** Match the 8px radius of buttons to maintain consistency in form layouts.
- **Iconography:** Use line-based icons with a 1.5px stroke weight and slightly rounded terminals to match the typography.

## Components

- **Buttons:** 
    - *Primary:* Solid Amber fill with black text. No shadow, but a subtle inner glow on hover/press.
    - *Secondary:* Glassmorphic background with a 1px Smoke border and white text.
- **Live Indicator:** A pill-shaped chip with a pulsing red dot. The background should be a dark red tint (15% opacity) with a solid red border.
- **Pitch Cards:** Utilizing the glassmorphism style, these cards feature a high-resolution blur background. The company logo should be "floated" on a white circular base for visibility.
- **Input Fields:** Dark Midnight Blue fill with a 1px Smoke border. On focus, the border transitions to Amber with a subtle outer glow.
- **Progress Bars (Funding/Timer):** Thin 4px tracks. The background is a dark neutral, and the "fill" is a linear gradient from Amber to a brighter yellow-gold.
- **The "Pitch-Tray":** A unique component for this system. A persistent, bottom-docked glass panel that houses the "Invest" or "Vote" button, ensuring it is always within reach during a live presentation.