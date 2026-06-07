---
name: Eco-District Living
colors:
  surface: '#f9faf2'
  surface-dim: '#d9dbd3'
  surface-bright: '#f9faf2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4ec'
  surface-container: '#edefe7'
  surface-container-high: '#e8e9e1'
  surface-container-highest: '#e2e3db'
  on-surface: '#1a1c18'
  on-surface-variant: '#414844'
  inverse-surface: '#2f312c'
  inverse-on-surface: '#f0f1e9'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#0e6c4a'
  on-secondary: '#ffffff'
  secondary-container: '#a0f4c8'
  on-secondary-container: '#19724f'
  tertiary: '#39200d'
  on-tertiary: '#ffffff'
  tertiary-container: '#523520'
  on-tertiary-container: '#c69e83'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#a0f4c8'
  secondary-fixed-dim: '#85d7ad'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdcc5'
  tertiary-fixed-dim: '#e9bea1'
  on-tertiary-fixed: '#2d1604'
  on-tertiary-fixed-variant: '#5e402a'
  background: '#f9faf2'
  on-background: '#1a1c18'
  surface-variant: '#e2e3db'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
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
  xl: 40px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style
The design system is rooted in "Biophilic Minimalism"—a style that bridges the gap between high-tech net-zero efficiency and organic, tactile comfort. The brand personality is restorative, transparent, and forward-thinking, targeting eco-conscious residents who value both modern convenience and a deep connection to nature.

The UI evokes a sense of "digital forest bathing" by utilizing ample whitespace (Off-White) and soft, fluid transitions. It leverages a **Tactile / Modern** approach where digital elements inherit properties of physical materials like wood and paper, ensuring the technology feels human-centric rather than cold or industrial.

## Colors
This design system uses a palette inspired by old-growth forests and sustainable architecture.

- **Primary (Deep Forest Green):** Used for high-level branding, primary actions, and grounding text to provide a sense of stability and depth.
- **Secondary (Sage Green):** Used for interactive states, success feedback, and soft accents to inject freshness.
- **Tertiary (Warm Wood):** Reserved for call-to-action highlights and decorative elements that require a tactile, grounded feel.
- **Neutral (Off-White):** The primary canvas color. It is warmer than pure white, reducing eye strain and mimicking natural light.
- **Surface Accents:** Use low-opacity versions of Sage Green (5-10%) for subtle backgrounds and containers.

## Typography
The typography strategy pairs approachable warmth with professional clarity. 

**Plus Jakarta Sans** is used for headlines. Its soft, rounded terminals echo the organic shapes of the UI, making large text feel welcoming. **Work Sans** is utilized for body and UI labels; its optimized legibility and slightly wider stance provide a grounded, reliable reading experience for technical data regarding net-zero metrics.

Use "Sentence case" for all headlines to maintain an approachable, conversational tone.

## Layout & Spacing
The design system employs a **Fluid Grid** model with generous margins to symbolize the openness of the development's architecture. 

A 12-column grid is standard for desktop, but spacing is driven by a 4px baseline unit. Layouts should prioritize "breathability"—avoiding dense clusters of information. Use wide gutters (24px) to separate content modules, ensuring that the background Off-White flows between elements like natural air. Components should use `xl` (40px) vertical spacing between distinct sections to reinforce a sense of calm.

## Elevation & Depth
In this design system, hierarchy is created through **Tonal Layers** and texture rather than heavy shadows.

- **Level 0 (Base):** Off-White surface.
- **Level 1 (Cards):** Low-contrast outlines (1px solid #E2E4D8) with a very soft, tinted ambient shadow (Deep Forest Green at 4% opacity).
- **Level 2 (Active Elements):** For high-priority cards, apply a subtle wood grain SVG mask at 5% opacity to the background.
- **Depth Metaphor:** Elements do not "float" high above the surface; they rest upon it like natural materials. Use backdrop blurs (10px) on navigation bars to suggest a frosted glass effect that lets the environment peak through.

## Shapes
The shape language is strictly **Organic**. 

Avoid sharp 90-degree angles. Primary containers use `rounded-lg` (1rem), while buttons and interactive chips use `rounded-xl` (1.5rem) or full pill shapes to feel pebble-like and tactile. 

**Leaf-patterned Dividers:** Instead of horizontal lines, use custom SVG dividers featuring a stylized, repeating leaf motif in Sage Green at 30% opacity. Containers should occasionally use asymmetrical rounding (e.g., top-left and bottom-right at 2rem, others at 1rem) to mimic the irregularity of natural forms.

## Components
- **Buttons:** Primary buttons are Deep Forest Green with Off-White text, featuring a pill-shaped radius. Secondary buttons use a Sage Green border with an "Inward Glow" on hover.
- **Cards:** Cards feature a 1px border in a darker shade of the neutral color. For "Eco-Highlights," apply a subtle, warm Wood texture (#967259) as a background with white text.
- **Input Fields:** Softly rounded (1rem) with a thick (2px) focus ring in Sage Green. The background is a slightly darker shade of Off-White to indicate interactivity.
- **Chips/Tags:** Used for sustainability certifications (e.g., "LEED Gold"). These are pill-shaped with Sage Green backgrounds and Deep Forest Green text.
- **Dividers:** Horizontal rules are replaced by "Vine Dividers"—a thin, organic line that tapers at the ends.
- **Progress Bars:** Used for energy-saving metrics. These use a thick, rounded track in light Sage and a fill in Deep Forest Green, mimicking growth.
- **Icons:** Linear, 2px stroke icons with rounded ends, occasionally featuring a "leaf" sprout detail on one corner.