---
name: Studio Vibe
colors:
  surface: '#121416'
  surface-dim: '#121416'
  surface-bright: '#37393b'
  surface-container-lowest: '#0c0e10'
  surface-container-low: '#1a1c1e'
  surface-container: '#1e2022'
  surface-container-high: '#282a2c'
  surface-container-highest: '#333537'
  on-surface: '#e2e2e5'
  on-surface-variant: '#e2bfb3'
  inverse-surface: '#e2e2e5'
  inverse-on-surface: '#2f3133'
  outline: '#a98a7f'
  outline-variant: '#594139'
  surface-tint: '#ffb59a'
  primary: '#ffb59a'
  on-primary: '#5b1b00'
  primary-container: '#ff6b2c'
  on-primary-container: '#5c1c00'
  inverse-primary: '#a83900'
  secondary: '#e3c19f'
  on-secondary: '#412c14'
  secondary-container: '#5c442b'
  on-secondary-container: '#d4b392'
  tertiary: '#bcc7dd'
  on-tertiary: '#263142'
  tertiary-container: '#8f9aaf'
  on-tertiary-container: '#273244'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcf'
  primary-fixed-dim: '#ffb59a'
  on-primary-fixed: '#380d00'
  on-primary-fixed-variant: '#802900'
  secondary-fixed: '#ffddbb'
  secondary-fixed-dim: '#e3c19f'
  on-secondary-fixed: '#291803'
  on-secondary-fixed-variant: '#5a4229'
  tertiary-fixed: '#d8e3fa'
  tertiary-fixed-dim: '#bcc7dd'
  on-tertiary-fixed: '#111c2c'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#121416'
  on-background: '#e2e2e5'
  surface-variant: '#333537'
typography:
  headline-xl:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  label-mono:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-page: 40px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is built for a premium video-podcast audience that values high-fidelity production and professional discourse. The brand personality is **authoritative yet warm**, mimicking the physical sensation of sitting in a sound-proofed, wood-paneled recording suite. 

The aesthetic is **Tactile Minimalism**. It leverages the richness of natural textures (wood) and professional hardware (slate) while maintaining a modern digital interface. It rejects flat, sterile design in favor of subtle depth, simulating the "touchable" quality of high-end audio gear. The UI evokes a sense of focus, intimacy, and sophisticated craftsmanship, ensuring the content feels like a curated experience rather than a generic stream.

## Colors

The palette is anchored in a professional **Dark Mode** to simulate a dimly lit studio environment. 

- **Primary (Vibrant Orange):** Inspired by "On Air" signs and tally lights. It is used exclusively for high-priority calls to action, active recording indicators, and critical highlights.
- **Secondary (Warm Wood):** A range of rich tans and deep browns used for surfaces and containers. This provides the "analog" warmth that balances the technical slate.
- **Tertiary (Slate):** Dark, professional grays with a slight blue undertone, used for navigation sidebars and secondary UI elements to represent the "hardware" of the platform.
- **Neutral (Ink Black):** The deepest foundation for background layers, ensuring maximum contrast for video content and crisp typography.

## Typography

This design system uses a trio of typefaces to establish a clear hierarchy between editorial style and technical utility.

- **Epilogue** serves as the headline face. Its geometric yet expressive nature provides an editorial feel, reminiscent of high-end lifestyle or tech magazines.
- **Manrope** is the workhorse for body copy. Its refined and balanced proportions ensure high readability during long-form episode descriptions or comments.
- **Space Grotesk** is used for "meta" information—timestamps, bitrates, and labels. Its technical, slightly futuristic appearance reinforces the "Studio" metaphor and provides a clear contrast to the warmer editorial fonts.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for desktop to maintain a cinematic, controlled composition, while transitioning to a fluid model for mobile devices.

- **The 8px Rhythm:** All spacing is derived from an 8px base unit. 
- **Generous Whitespace:** To offset the "heavy" colors (Wood and Slate), the design system utilizes wide margins and large internal padding. This creates a gallery-like feel where content is given room to breathe.
- **Structural Columns:** A 12-column grid is standard. Content modules (Video player, Transcript, Sidebar) should align to these columns with 24px gutters to ensure a structured, professional alignment.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Ambient Shadows**, moving away from flat design. 

1.  **The Floor (Neutral):** The base background is the darkest neutral.
2.  **The Deck (Slate/Wood):** Cards and main containers sit on the floor. They use subtle inner glows (top edge) to simulate the thickness of a physical material like wood or metal.
3.  **The Controls (Primary):** Interactive elements use soft, diffused shadows with a slight color tint (Orange or Brown) to appear "pressed in" or "raised up" from the surface.
4.  **Backdrop Blurs:** For overlays and dropdowns, use high-intensity blurs (32px+) with a Slate-tinted overlay to maintain focus on the immediate task without losing the immersive background context.

## Shapes

The shape language is **Rounded**, striking a balance between the precision of professional equipment and the organic warmth of wood surfaces. 

- UI containers and cards utilize a `1rem` (16px) radius to soften the technical Slate aesthetic. 
- High-level interactive elements (buttons) use more pronounced rounding, while technical elements like volume sliders and input fields use more conservative radii to imply precision. 
- Avoid sharp corners (0px) entirely, as they feel too clinical for the intended "Studio-Vibe."

## Components

- **Buttons:** Primary buttons are vibrant Orange with white text. They should have a subtle "pressed" state and an outer glow on hover to mimic a backlit physical switch.
- **Cards:** Episode cards should use a vertical layout with a Wood-textured header or footer. Use a 1px Slate border with 10% opacity to define edges against dark backgrounds.
- **Chips:** Tags for categories or guests should use the Space Grotesk font. Use an outlined style for "unselected" and a Slate-fill for "selected."
- **Input Fields:** Search and comment fields should appear "recessed" into the layout using a subtle inner shadow, reinforcing the tactile nature of the UI.
- **Audio/Video Player:** The core component. It should feature custom-styled sliders for progress and volume that resemble high-end mixing board faders.
- **Live Indicator:** A pulsing "Live" chip in the primary Orange color, using a slight blur effect to simulate the glow of an incandescent bulb.
- **Transcript View:** A dedicated vertical component using Manrope, highlighting the "active" spoken text with a Wood-tinted background highlight.