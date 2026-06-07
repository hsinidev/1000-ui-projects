---
name: Obsidian Flux
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cbc3d7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#958ea0'
  outline-variant: '#494454'
  surface-tint: '#d0bcff'
  primary: '#d0bcff'
  on-primary: '#3c0091'
  primary-container: '#a078ff'
  on-primary-container: '#340080'
  inverse-primary: '#6d3bd7'
  secondary: '#4cd7f6'
  on-secondary: '#003640'
  secondary-container: '#03b5d3'
  on-secondary-container: '#00424e'
  tertiary: '#ffb2b7'
  on-tertiary: '#67001b'
  tertiary-container: '#ff516a'
  on-tertiary-container: '#5b0017'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#5516be'
  secondary-fixed: '#acedff'
  secondary-fixed-dim: '#4cd7f6'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5c'
  tertiary-fixed: '#ffdadb'
  tertiary-fixed-dim: '#ffb2b7'
  on-tertiary-fixed: '#40000d'
  on-tertiary-fixed-variant: '#92002a'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
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
    lineHeight: '1.6'
  label-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for a high-octane, WebGL-driven gaming environment. It prioritizes immersion, speed, and technical precision. The brand personality is aggressive yet sophisticated, evoking the feeling of a premium cockpit or a futuristic terminal. 

The aesthetic is a fusion of **Glassmorphism** and **High-Contrast Neon**. It relies on deep blacks to provide an infinite sense of space, while vibrant accents create a "light-in-the-dark" effect. Users should feel they are interacting with a living, breathing digital organism. Motion and depth are central to the experience, using transparency and blurs to maintain a sense of the underlying WebGL canvas at all times.

## Colors

The palette centers on a "Deep Obsidian" base that acts as a void, allowing the "Electric Violet" and "Vivid Cyan" to cut through with maximum luminosity. 

- **Primary (Electric Violet):** Used for primary actions, branding, and high-energy focal points.
- **Secondary (Vivid Cyan):** Used for data visualization, technical readouts, and secondary interactive states.
- **Tertiary (Cyber Rose):** Reserved for critical alerts and destructive actions.
- **Surface:** A series of semi-transparent blacks (#0A0A0A at various opacities) are used to create the glass effect.
- **Glows:** Every accent color must have a corresponding "Glow" value (the color at 20-30% opacity with a large blur radius) to simulate neon emission.

## Typography

This design system utilizes **Space Grotesk** for its technical, geometric aesthetic in headlines and UI labels, providing a futuristic "tech-stack" feel. **Inter** is used for body copy to ensure maximum legibility against dark, vibrating backgrounds.

Headline elements should occasionally utilize a `text-shadow` effect matching their color token to simulate a neon glow. Labels are frequently set in uppercase with increased letter spacing to mimic serial numbers or military-grade hardware markings.

## Layout & Spacing

The layout utilizes a **Fixed Grid** model for the HUD (Heads-Up Display) elements and a **Fluid Grid** for content galleries. A 12-column system is standard, but margins are intentionally wide (40px) to prevent UI elements from feeling cramped against the edge of the screen.

Spacing follows a strict 4px base unit. Larger gaps between sections (64px+) are encouraged to allow the background WebGL effects to breathe and remain visible, reinforcing the "hub" as a gateway to other worlds rather than a static document.

## Elevation & Depth

Depth is achieved through **Glassmorphism** rather than traditional drop shadows. 

1.  **Backdrop Blur:** All floating panels (sidebars, modals, cards) must use a `backdrop-filter: blur(20px)` combined with a semi-transparent background fill (`rgba(10, 10, 10, 0.6)`).
2.  **Inner Glow Borders:** Instead of shadows, use a 1px solid border with low opacity (10-20%) of the primary or secondary color.
3.  **Z-Axis Stacking:** Elements closer to the user are brighter and have more saturated "neon" borders. Elements further away are darker and more transparent.
4.  **Parallax:** When possible, UI layers should react to mouse movement with subtle parallax to reinforce the sense of 3D space.

## Shapes

The design system employs a **Sharp** shape language. 90-degree angles communicate precision and technical rigidity. 

To prevent the UI from feeling dated, use "clipped corners" (45-degree chamfers) on large panels and buttons rather than rounded corners. This geometric aggression aligns with the Cyber-Neon aesthetic. Decorative elements like scanlines, crosshair corners, and micro-rectangles should be used to detail the edges of containers.

## Components

### Buttons
Primary buttons feature a solid #8B5CF6 fill with black text. Hovering triggers a "Pulse" effect where a large, soft violet glow expands behind the button. Secondary buttons are transparent with a 1px Cyan border and glowing text.

### Side Panels
Side panels must use the full Glassmorphism stack: blur, semi-transparency, and a top-to-bottom subtle gradient border. They should feel like "HUD overlays" pinned to the screen.

### Cards (Game Tiles)
Cards are borderless with a "Vignette" overlay. On hover, the 1px neon border (Violet or Cyan) activates, and the background image scales slightly (1.05x) to create a "zoom" into the game world.

### Inputs
Input fields are underlined only, using a 2px Cyan line. When focused, the line glows and a subtle scanline texture ripples across the input background.

### Status Chips
Small, rectangular tags with monochromatic backgrounds and high-contrast text. For "Live" or "Active" states, a 2px blinking dot (Primary Color) is mandatory.

### HUD Elements
Include specialized components like "Performance Monitors" (small sparklines) and "Coordinate Readouts" (changing numbers) in the corners of the hub to enhance the gaming atmosphere.