---
name: Vibrant Asian Fusion
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#5b403f'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#8f6f6e'
  outline-variant: '#e4bebc'
  surface-tint: '#bb152c'
  primary: '#b7102a'
  on-primary: '#ffffff'
  primary-container: '#db313f'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb3b1'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e5e2e1'
  on-secondary-container: '#656464'
  tertiary: '#5a5c5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#737575'
  on-tertiary-container: '#fcfcfc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3b1'
  on-primary-fixed: '#410007'
  on-primary-fixed-variant: '#92001c'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c9c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-display:
    fontFamily: Newsreader
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  utility-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1280px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
This design system centers on a "Modern Orientalist" aesthetic, blending the stark, disciplined beauty of traditional calligraphy with the aggressive energy of high-fashion editorial design. The brand personality is sensory-focused, intense, and precise. It targets a modern audience that values culinary artistry and bold flavors. 

The design style is **High-Contrast / Bold** with elements of **Minimalism**. It uses a restricted color palette to ensure that the rich, saturated food photography provides the primary visual texture. The emotional response should be one of "dramatic clarity"—where the UI acts as a structured gallery for the vibrant, tactile nature of the recipes.

## Colors
The palette is a high-tension triad designed for maximum impact and readability. 
- **Vibrant Crimson Red (#E63946):** Used as an aggressive accent for calls to action, active states, and essential highlights. It evokes spice and energy.
- **Deep Black (#0A0A0A):** The structural foundation. Used for heavy typography, thin borders, and solid backgrounds in immersive sections.
- **Crisp White (#FFFFFF):** The primary canvas for recipe steps and body text, ensuring a clean, high-readability experience.
- **Neutral Stone (#F4F4F4):** A subtle off-white used for secondary backgrounds or "slate" textures to prevent visual fatigue in long-form reading.

## Typography
The typography strategy plays on the tension between the classic and the contemporary. 
- **Headlines (Newsreader):** A sophisticated serif that mirrors the elegance of traditional print media and culinary heritage. Use heavy weights for display titles to create a vertical rhythm.
- **Body & UI (Be Vietnam Pro):** A modern, geometric sans-serif that provides a neutral, highly legible contrast to the serif headings. Its contemporary feel aligns with the "fusion" aspect of the brand. 
- **Letter Spacing:** Headlines should be tight to feel impactful, while labels and metadata (cook time, difficulty) should have increased tracking for a clean, technical appearance.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model for desktop (12 columns) and a fluid 2-column model for mobile. 
- **The "Editorial" Rhythm:** Spacing is generous between sections (`stack-lg`) to allow the high-contrast imagery to breathe. 
- **Structural Lines:** Use 1px black borders to define sections instead of large gaps, creating a layout that feels like a structured recipe card or newspaper.
- **Negative Space:** Whitespace is treated as a design element, used aggressively around photography to focus the user's eye on the food.

## Elevation & Depth
In alignment with the sharp, bold aesthetic, this design system avoids soft shadows and organic blurs.
- **Bold Borders:** Hierarchy is established through 1px or 2px solid strokes in Deep Black.
- **Tonal Layering:** Depth is created by "stacking" white cards directly onto a Neutral Stone (#F4F4F4) background without shadows.
- **Hard Shadows:** Where depth is absolutely necessary (e.g., a hover state on a recipe card), use a "hard shadow"—a solid black offset (e.g., 4px 4px 0px 0px) rather than a soft blur.
- **Subtle Textures:** Apply a very faint paper grain texture to the White (#FFFFFF) surfaces to evoke the tactile feel of a physical cookbook.

## Shapes
The shape language is strictly **Sharp (0)**. 
- All buttons, images, cards, and input fields must have 90-degree corners. 
- This geometric rigidity mimics the precision of knife work in Asian cuisine and reinforces the modern, architectural feel of the brand.
- Any "containers" should be defined by thin, crisp lines rather than rounded corners.

## Components
- **Buttons:** Solid Deep Black background with White text for primary; White background with 1px Black border for secondary. No rounded corners. On hover, the primary button fills with Crimson Red.
- **Recipe Cards:** Full-bleed imagery with a 1px black border. The recipe title should overlay the bottom on a solid white block, ensuring no text sits directly on busy photography.
- **Input Fields:** 1px Black bottom border only (minimalist style) or full rectangular border. Use Newsreader for the label and Be Vietnam Pro for the input text.
- **Chips/Tags:** Small, sharp-edged boxes with a Crimson Red background and White text for categories like "Spicy" or "Vegan."
- **Ingredient Lists:** Use custom checkboxes that are simple 1px squares; when checked, they fill solid Crimson Red with a white "X" or check.
- **The "Hero" Slider:** Use large-scale, high-saturation imagery that spans the width of the container, framed by a thick 4px Black border for a gallery-like effect.
- **Measurement Toggle:** A sharp, segmented control for switching between Metric and Imperial, using solid black for the active state.