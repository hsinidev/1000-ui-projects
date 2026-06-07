---
name: High-Fashion Editorial
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
  on-surface-variant: '#524345'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#857374'
  outline-variant: '#d7c1c3'
  surface-tint: '#8c4b55'
  primary: '#8a4853'
  on-primary: '#ffffff'
  primary-container: '#a6606b'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb2bc'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#5a5c5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#737575'
  on-tertiary-container: '#fcfcfc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9dd'
  primary-fixed-dim: '#ffb2bc'
  on-primary-fixed: '#3a0915'
  on-primary-fixed-variant: '#70343e'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 84px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Montserrat
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.8'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Montserrat
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  label-md:
    fontFamily: Montserrat
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style
The design system is anchored in the visual language of high-fashion editorial. It evokes the feeling of a premium digital magazine, where content is curated rather than simply displayed. The target audience is discerning professionals and enthusiasts in the luxury sector who expect an interface that reflects the prestige of the subject matter.

The aesthetic leans heavily into **Minimalism** with a focus on editorial authority. It utilizes expansive whitespace to create a sense of "breathing room," suggesting exclusivity and calm. The visual narrative is driven by high-quality imagery and immersive video content, framed by architectural precision. Transitions are deliberate and fluid, mimicking the graceful movement of a physical luxury publication.

## Colors
The palette is a sophisticated trio designed to prioritize legibility and prestige. 
- **Rose Gold (#B76E79)**: Used as the primary accent for calls to action, active states, and subtle highlights. It provides a warm, metallic warmth against the cooler neutrals.
- **Deep Grey (#2F2F2F)**: The core color for typography and structural elements. It offers softer contrast than pure black, maintaining an expensive, cinematic feel.
- **Pure White (#FFFFFF)**: The primary canvas. It is used generously to establish the editorial whitespace essential for this design system.
- **Neutral Grey (#F9F9F9)**: A secondary background shade used for subtle section differentiation or bento-box container fills.

## Typography
Typography is the cornerstone of this design system. We pair the high-contrast, elegant serif **Playfair Display** for headlines with the clean, geometric **Montserrat** for functional text.

Headlines should be treated as graphic elements. Use significant scale shifts between display text and body copy to create a clear hierarchy. For labels and small utility text, utilize Montserrat with increased letter spacing and uppercase styling to evoke the branding found in luxury labels. Body text requires generous line heights (1.6 to 1.8) to ensure a comfortable, premium reading experience.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model for desktop, centered within a 1440px container, transitioning to a fluid model for mobile devices. The grid follows a 12-column structure with 24px gutters.

The spacing philosophy is "breath over density." Sections are separated by large vertical gaps (128px+) to signify shifts in topic. Galleries and portfolios use a **Bento-Box** layout—a modular grid where different-sized rectangles fit perfectly together. These grids should maintain consistent 1px or 2px internal borders to create a sharp, structured appearance. Immersive video sections should always break the container to go full-width, providing a cinematic pause in the editorial flow.

## Elevation & Depth
Depth in this design system is achieved through **low-contrast outlines** and **tonal layering** rather than traditional shadows. 

Avoid heavy dropshadows. To create a sense of layering, use thin 1px borders in Deep Grey at 10-15% opacity. For elements that require "lift" (like modals or dropdowns), use a very large, soft ambient shadow with a 0% to 5% opacity, making it almost imperceptible. Most components should appear to sit on the same plane, using whitespace and hairline borders to define boundaries. Backdrop blurs (Glassmorphism) can be used sparingly on navigation bars to maintain context while scrolling over high-fashion imagery.

## Shapes
The shape language is strictly **Sharp (0)**. 

To maintain the high-fashion editorial look, avoid rounded corners on buttons, inputs, and containers. Sharp 90-degree angles communicate precision, discipline, and architectural modernism. This applies to images in the bento-box grids as well as all interactive components. Borders should be thin (1px) and used to frame content like a gallery piece.

## Components
- **Buttons**: Rectangular with no radius. Primary buttons feature a Deep Grey background with White text; secondary buttons use a thin 1px Rose Gold border with Rose Gold text.
- **Input Fields**: Minimalist underlines or 1px borders on all sides. Labels should be small, uppercase Montserrat above the field.
- **Bento-Box Cards**: Non-interactive containers for imagery or video. They should use a "zoom-on-hover" effect where the image scales slightly within the sharp frame.
- **Video Players**: Custom controls using thin icons and Montserrat labels. Videos should ideally auto-play on mute when in view to provide dynamic energy.
- **Navigation**: A clean, centered top-tier navigation using uppercase labels. A thin 1px horizontal line separates the navigation from the hero content.
- **Chips/Tags**: Small, sharp-edged boxes with 1px borders. Avoid solid fills for tags to keep the layout feeling light and airy.