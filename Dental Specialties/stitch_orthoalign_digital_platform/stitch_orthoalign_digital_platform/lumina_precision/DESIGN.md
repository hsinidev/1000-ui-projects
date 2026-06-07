---
name: Lumina Precision
colors:
  surface: '#f7fafc'
  surface-dim: '#d7dadc'
  surface-bright: '#f7fafc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f6'
  surface-container: '#ebeef0'
  surface-container-high: '#e5e9eb'
  surface-container-highest: '#e0e3e5'
  on-surface: '#181c1e'
  on-surface-variant: '#444748'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eef1f3'
  outline: '#747878'
  outline-variant: '#c4c7c8'
  surface-tint: '#5d5f5f'
  primary: '#5d5f5f'
  on-primary: '#ffffff'
  primary-container: '#ffffff'
  on-primary-container: '#747676'
  inverse-primary: '#c6c6c7'
  secondary: '#006970'
  on-secondary: '#ffffff'
  secondary-container: '#00eefc'
  on-secondary-container: '#00686f'
  tertiary: '#515f78'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffffff'
  on-tertiary-container: '#687691'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c7'
  on-primary-fixed: '#1a1c1c'
  on-primary-fixed-variant: '#454747'
  secondary-fixed: '#7df4ff'
  secondary-fixed-dim: '#00dbe9'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#d6e3ff'
  tertiary-fixed-dim: '#b9c7e4'
  on-tertiary-fixed: '#0d1c32'
  on-tertiary-fixed-variant: '#39475f'
  background: '#f7fafc'
  on-background: '#181c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  stack-xs: 8px
  stack-md: 24px
  stack-xl: 64px
---

## Brand & Style
The design system is engineered to evoke the precision of high-end orthodontics and the futuristic clarity of digital smile design. It targets an affluent, tech-savvy demographic that values both clinical excellence and aesthetic refinement. 

The visual style is a fusion of **Minimalism** and **Glassmorphism**, creating a "Digital-First" environment that feels like an advanced medical interface. High-gloss surfaces and translucent layers suggest a sterilized, high-tech laboratory setting. Every interaction should feel intentional and crisp, reinforcing the brand's position as a leader in invisible alignment technology.

## Colors
This design system utilizes a high-contrast, high-key palette to maintain a clinical atmosphere.
- **Primary (Glossy White):** Dominates the interface to provide a sense of cleanliness and space.
- **Secondary (Electric Cyan):** Used sparingly for high-action focal points and to represent digital energy.
- **Tertiary (Deep Tech-Blue):** Provides necessary grounding and contrast for typography and deep navigation elements.
- **Surface Neutrals:** Cool-toned grays prevent the white from feeling stark, adding depth to the clinical aesthetic.

## Typography
The typography strategy prioritizes technical precision. **Space Grotesk** is used for headlines to provide a futuristic, geometric edge that mirrors architectural orthodontic structures. **Inter** is utilized for body text and labels to ensure maximum readability and a systematic, clinical feel. Headlines should use tight tracking to emphasize the "engineered" nature of the brand, while labels should be set in all-caps with increased letter-spacing for a "spec-sheet" aesthetic.

## Layout & Spacing
The design system employs a **Fixed Grid** on desktop (12 columns, 1200px max-width) and a fluid layout on mobile. The spacing rhythm is based on a 4px scale, favoring generous whitespace to maintain a premium, uncluttered feel. Structural elements are separated by "Stack" variables to create clear visual hierarchies, ensuring the interface feels as organized and precise as a clinical workstation.

## Elevation & Depth
Depth is achieved through **Glassmorphism** rather than traditional shadows. 
- **Backdrop Blurs:** Use 20px–30px blurs on semi-transparent white surfaces (#FFFFFF80) to create a frosted-glass effect.
- **Inner Glows:** Instead of drop shadows, use 1px inner borders (strokes) in white or 10% Cyan to simulate light catching the edge of a polished lens.
- **Subtle Ambient Shadows:** When depth is required for overlays, use extremely diffused, low-opacity Deep Tech-Blue shadows (#0A192F with 5% opacity) to avoid "dirtying" the clean white environment.

## Shapes
The shape language is "Soft-Tech." While the brand is futuristic, the medical context requires a sense of safety and comfort. Subtle rounding (Soft) is applied to all components to mimic the ergonomics of orthodontic appliances. 
- Large containers and cards: 0.75rem.
- Buttons and inputs: 0.25rem.
- High-gloss icons: Enclosed in circular or squircle containers with light-refracting gradients.

## Components
- **Buttons:** Primary buttons feature an Electric Cyan fill with a subtle "high-gloss" top gradient. Text is bold and concise. Hover states should introduce a "pulse" glow effect.
- **Cards:** Utilize the glassmorphism style—frosted backgrounds with a 1px solid white border. Background content should blur significantly behind them.
- **Input Fields:** Minimalist under-lines or very light-gray ghost borders. On focus, the border transitions to Electric Cyan with a sharp, digital glow.
- **Chips/Status Tags:** Small, pill-shaped elements with low-opacity Cyan backgrounds and high-contrast Cyan text, used to indicate treatment phases.
- **Interactive 3D Visualizers:** This design system should include specific containers for dental scans and 3D smile previews, framed in "Viewfinder" corners to emphasize the diagnostic technology.
- **Progress Steppers:** Thin, horizontal lines using Electric Cyan to track patient treatment journeys, appearing like a digital timeline.