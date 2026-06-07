---
name: BioLiving Vitality
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
  on-surface-variant: '#3f4a3d'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#6f7a6c'
  outline-variant: '#becab9'
  surface-tint: '#006e20'
  primary: '#006e20'
  on-primary: '#ffffff'
  primary-container: '#98ff98'
  on-primary-container: '#007924'
  inverse-primary: '#77dc7a'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e2e2e2'
  on-secondary-container: '#636465'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#e8e8e8'
  on-tertiary-container: '#666868'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#93f993'
  primary-fixed-dim: '#77dc7a'
  on-primary-fixed: '#002105'
  on-primary-fixed-variant: '#005316'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
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
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  margin-page: 24px
  gutter: 16px
  cell-padding: 20px
  section-gap: 40px
---

## Brand & Style

The design system is centered on the intersection of biological harmony and modern technology. It targets health-conscious urban dwellers seeking to transform their living space into a sanctuary of wellness. The personality is "Living Technology"—sophisticated and high-performance, yet breathing and organic.

The UI utilizes a **Minimalist-Biomorphic** style. It moves away from rigid geometric grids in favor of asymmetrical, organic shapes that mimic cells, leaves, and water droplets. The atmosphere is light and airy, emphasizing purity and stasis. "Breathing" animations are integral to the experience, with elements subtly scaling or pulsing in opacity to signal background activity, creating a sense that the home itself is a living organism.

## Colors

The palette is intentionally restrained to maximize the impact of the primary Mint Green, which serves as a visual metaphor for oxygen, growth, and vitality. 

- **Primary (Mint Green):** Used for active states, health metrics, and primary calls to action. It should feel luminous against the white background.
- **Secondary (Soft Grey):** Used for structural elements, non-interactive icons, and secondary information to maintain a low-friction visual hierarchy.
- **Base (Crisp White):** The foundation of the design system, providing a high-purity "laboratory" aesthetic that feels clinical yet inviting.
- **Accents:** Use subtle variations of the primary mint (deeper forest tones for text legibility) to ensure accessibility standards are met while maintaining the monochromatic nature-focus.

## Typography

This design system utilizes a dual-sans-serif approach to balance character with utility. 

**Manrope** is used for headings and display text. Its rounded terminals and geometric balance complement the biomorphic shapes of the UI, feeling modern and friendly. 

**Inter** is utilized for all body copy, data readouts, and UI labels. It provides the "high-tech" precision required for a smart-home interface, ensuring that complex health data remains legible at small sizes. Type is predominantly dark grey (#4A4A4A) to reduce eye strain against the crisp white background.

## Layout & Spacing

The layout follows a **Fluid Bio-Grid**. While structural elements align to a standard 8px rhythmic unit, the content containers themselves use asymmetrical margins to evoke an organic, less "engineered" feel. 

Whitespace is treated as "breathable air." Content is never cramped; instead, large generous margins (24px+) are used to isolate different health modules. Components should have significant internal padding to allow the organic shapes of the containers to be fully appreciated.

## Elevation & Depth

Depth in the design system is achieved through **Tonal Softness and Blurs** rather than traditional shadows. 

- **Subtle Ambient Shadows:** Use very large blur radii (30px-60px) with extremely low opacity (2-5%) mint-tinted shadows to make cards appear as if they are floating on a cushion of air.
- **Glassmorphism:** Secondary overlays (like pop-ups or control drawers) use a high-saturation background blur (30px) with 80% white opacity, creating a "frosted leaf" effect.
- **Layering:** Active states are indicated by an increase in the intensity of the "breathing" pulse animation rather than an increase in physical height or shadow depth.

## Shapes

The shape language is the core differentiator of this design system. It avoids perfect circles and rectangles.

- **Squiggles & Blobs:** Containers use "squircle" geometry or custom SVG paths that mimic cellular structures. 
- **Variable Corner Radii:** Buttons and cards often have non-uniform corner radii (e.g., top-left 32px, top-right 12px) to create a more natural, hand-drawn appearance.
- **Interactive Morphing:** Upon interaction, shapes should "morph" or wobble slightly, reinforcing the biological metaphor.

## Components

### Buttons & Inputs
- **Primary Buttons:** Pill-shaped with a subtle Mint Green gradient. They should exhibit a soft pulse ("breathing") when the app is in an idle state.
- **Input Fields:** Minimalist underlines or soft-grey organic pods with floating labels. Focus states highlight the border in Mint Green.

### Cards & Modules
- **Vitality Cards:** Used for health metrics (Heart Rate, Air Quality). These use the biomorphic "blob" shapes with integrated micro-charts.
- **Glass Sliders:** For adjusting temperature or light. The thumb of the slider is a soft, semi-transparent circle that grows slightly when touched.

### Feedback & Selection
- **Chips:** Highly rounded, using the Soft Grey for inactive and Mint Green for active states.
- **Checkboxes:** Replaced with "Cell Toggles"—circular elements that expand and fill with color like a cell dividing when activated.

### Specialized Components
- **Breathing Indicator:** A central, large organic shape on the dashboard that expands and contracts in sync with the user's recommended respiratory rate or the home's current air filtration status.