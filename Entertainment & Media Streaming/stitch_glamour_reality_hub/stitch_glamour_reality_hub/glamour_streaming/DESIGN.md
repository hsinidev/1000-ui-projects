---
name: Glamour Streaming
colors:
  surface: '#fff8f7'
  surface-dim: '#e0d8d8'
  surface-bright: '#fff8f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf2f1'
  surface-container: '#f5eceb'
  surface-container-high: '#efe6e6'
  surface-container-highest: '#e9e1e0'
  on-surface: '#1e1b1b'
  on-surface-variant: '#524345'
  inverse-surface: '#342f2f'
  inverse-on-surface: '#f8efee'
  outline: '#857374'
  outline-variant: '#d7c1c3'
  surface-tint: '#8c4b55'
  primary: '#8a4853'
  on-primary: '#ffffff'
  primary-container: '#a6606b'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb2bc'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#735c00'
  on-tertiary: '#ffffff'
  tertiary-container: '#cba72f'
  on-tertiary-container: '#4e3d00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9dd'
  primary-fixed-dim: '#ffb2bc'
  on-primary-fixed: '#3a0915'
  on-primary-fixed-variant: '#70343e'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffe088'
  tertiary-fixed-dim: '#e9c349'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#574500'
  background: '#fff8f7'
  on-background: '#1e1b1b'
  surface-variant: '#e9e1e0'
typography:
  headline-xl:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: notoSerif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: beVietnamPro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: beVietnamPro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: beVietnamPro
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: beVietnamPro
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
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
  margin: 64px
---

## Brand & Style

This design system is built for the high-stakes, emotionally charged world of reality television. The aesthetic is "Luxurious High-Energy," blending the opulence of high-end fashion with the kinetic vibrancy of live entertainment. It is designed to evoke a sense of exclusivity, excitement, and intimacy, making the user feel like a VIP guest with front-row access to the drama.

The visual direction utilizes a refined **Glassmorphism** approach. Layers of semi-transparent surfaces, subtle backdrop blurs, and rose-gold tinted glows create a multi-dimensional interface that feels light yet substantial. The interface prioritizes motion and interactivity, ensuring that every user action—from casting a vote to selecting a show—feels like a grand gesture.

## Colors

The palette is anchored by **Rose Gold (#B76E79)**, used as the primary driver for brand recognition and interactive states. **White (#FFFFFF)** serves as the canvas, providing a crisp, clean background that allows the vibrant content of reality TV—neon lights, tropical locales, and studio sets—to pop.

To add depth and luxury, a tertiary **Champagne Gold (#D4AF37)** is used sparingly for "Winner" states and premium badges. The neutral palette consists of a warm charcoal (#2D2929) for text and deep shadows, ensuring legibility against the light, metallic primary tones. Use gradients of Rose Gold to White to simulate the shimmer of precious metal on buttons and active headers.

## Typography

The typographic strategy balances editorial sophistication with modern utility. **Noto Serif** is used for all headlines and show titles to convey a sense of high-end drama and "prestige" media. Large headlines should utilize tight letter spacing and bold weights to command attention.

**Be Vietnam Pro** is the workhorse for the UI. Its contemporary, friendly, and approachable character ensures that navigation, descriptions, and metadata remain highly legible. Use all-caps with generous letter spacing for labels and categories to create a rhythmic, organized hierarchy that mimics luxury magazine layouts.

## Layout & Spacing

The design system employs a **Fluid Grid** model with a 12-column structure for desktop and a 4-column structure for mobile. To maintain an "expensive" feel, the layout uses generous outer margins (64px+) and significant vertical whitespace (Section spacing of 80px+). 

The spacing rhythm is based on an 8px scale. Content cards and interactive modules should be separated by a 24px gutter to prevent the interface from feeling cluttered. Alignment should be intentional and airy; avoid packing elements too closely, as whitespace is a key indicator of the "Glamour" aesthetic.

## Elevation & Depth

Depth in this design system is achieved through **Rose Gold Glassmorphism**. Surfaces do not simply "sit" on the background; they float with varying degrees of transparency and backdrop blur (20px to 40px).

Elevation is communicated via:
- **Tonal Glows:** Instead of standard grey shadows, use soft, diffused dropshadows tinted with the primary Rose Gold color at low opacity (15-20%).
- **Inner Borders:** High-elevation components (like active cards) should feature a 1px semi-transparent white inner border to simulate the glint of light on a glass edge.
- **Ambient Lighting:** Use radial gradients in the background to create a "spotlight" effect behind featured content, drawing the eye toward primary actions.

## Shapes

The shape language is **Rounded**, striking a balance between the sharp edges of high-fashion and the approachability of social media. The standard radius of 0.5rem (8px) provides a modern, polished look for buttons and input fields. 

Large-scale components like product cards and decorative containers use a "rounded-xl" radius (1.5rem / 24px) to create a softer, more inviting container for imagery. Interactive voting chips should use pill-shaped radii to distinguish them as highly touchable, playful elements.

## Components

### Glowing Live Status Indicators
Live indicators must feel urgent and high-energy. Use a Rose Gold circular badge with a double-ring pulse animation. The outer ring should have a blurred "neon" glow effect that expands and fades, signaling immediate, live-action content.

### Interactive Voting Buttons
Voting buttons are the centerpiece of engagement. Use a high-contrast gradient (Rose Gold to Champagne Gold) with a tactile "pressed" state. On hover, the button should increase its glow intensity and slightly scale up (1.05x) to mimic the excitement of casting a game-changing vote.

### Elegant Product Cards
Cards for shows and contestants feature a "Glass-Fill" style. The bottom 30% of the card uses a backdrop-blur overlay where the title (Noto Serif) and metadata sit. The border should be a subtle 1px gradient that catches the light as the user scrolls.

### Luxury Input Fields
Text inputs and search bars use a semi-transparent white fill with a Rose Gold bottom-border. On focus, the border should expand into a full-stroke glowing outline to provide clear, high-energy feedback.

### Narrative Chips
Use small, pill-shaped chips for categories (e.g., "Trending," "Finale"). These should use a solid White background with Rose Gold text and a subtle 2px drop shadow to make them "pop" off the glass surfaces.