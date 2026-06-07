---
name: Sonic Digital Luxury
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2a'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#e5bcc5'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#ac878f'
  outline-variant: '#5c3f46'
  surface-tint: '#ffb1c4'
  primary: '#ffb1c4'
  on-primary: '#65002e'
  primary-container: '#ff4a8d'
  on-primary-container: '#590028'
  inverse-primary: '#ba005b'
  secondary: '#a2e7ff'
  on-secondary: '#003642'
  secondary-container: '#00d2fd'
  on-secondary-container: '#005669'
  tertiary: '#e5b5ff'
  on-tertiary: '#4e0078'
  tertiary-container: '#c365ff'
  on-tertiary-container: '#450069'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffd9e1'
  primary-fixed-dim: '#ffb1c4'
  on-primary-fixed: '#3f001a'
  on-primary-fixed-variant: '#8f0044'
  secondary-fixed: '#b4ebff'
  secondary-fixed-dim: '#3cd7ff'
  on-secondary-fixed: '#001f27'
  on-secondary-fixed-variant: '#004e5f'
  tertiary-fixed: '#f4d9ff'
  tertiary-fixed-dim: '#e5b5ff'
  on-tertiary-fixed: '#30004b'
  on-tertiary-fixed-variant: '#7000a8'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-xl:
    fontFamily: Epilogue
    fontSize: 72px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Epilogue
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Epilogue
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Epilogue
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Epilogue
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-mono:
    fontFamily: Epilogue
    fontSize: 11px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
  density-high: 8px
  density-medium: 16px
---

## Brand & Style

This design system targets elite music producers and sound designers who demand a professional workstation environment that feels both high-end and technologically advanced. The brand personality is aggressive, precise, and high-fidelity, evoking the "digital adrenaline" of a late-night studio session. 

The aesthetic is a sophisticated fusion of **Glassmorphism** and **High-Contrast Digital** styles. It utilizes deep matte surfaces to provide a grounding foundation for vibrant, luminous accents. The UI is designed to feel like a premium hardware controller translated into a digital interface—dense with information but organized with surgical clarity. The emotional response is one of creative empowerment, where every interaction feels tactile, responsive, and visually stimulating.

## Colors

The color palette is built on a foundation of **Matte Black (#121414)** to minimize eye strain during long production sessions. The primary functional color is **Hot Pink (#FF007F)**, used for critical actions and high-energy focal points. **Electric Blue (#00D4FF)** serves as the secondary color, typically representing active states, selection paths, and secondary functional groups.

A "Digital Purple" tertiary accent is introduced for complex data visualizations or rare UI states. Neutral tones are strictly cool-shifted to maintain the digital atmosphere. Contrast is maintained through luminosity rather than hue alone, ensuring that the neon accents "pop" against the deep, non-reflective surfaces of the background.

## Typography

This design system utilizes **Epilogue** exclusively to leverage its geometric, high-contrast personality. The typographic scale is optimized for a high-density workstation layout. Display and Headline weights are set to Extra Bold or Bold to create an "editorial boutique" feel, contrasting sharply with the technical data surrounding them.

Body text maintains a generous line height for readability against dark backgrounds. A specialized "Label" tier is used for metadata, file types, and technical parameters (BPM, Key, Bit-rate), often utilizing uppercase styling and increased letter spacing to mimic the industrial labeling found on professional MIDI controllers and rack-mount gear.

## Layout & Spacing

This design system employs a **Fixed Grid** model for the desktop-first experience, ensuring that complex audio tools remain in predictable locations. The layout is structured on a 12-column grid with a 1440px max-width, though the matte background extends infinitely to the edges of the viewport.

Spacing follows a strict 4px baseline rhythm. Given the professional "workstation" requirement, high-density spacing (8px) is used within functional panels to maximize the visibility of sample libraries and parameter controls. Layouts often feature "Panel-in-Panel" logic, where internal modules have their own padding and gutter systems, creating a tiered, modular hierarchy reminiscent of a DAW (Digital Audio Workstation).

## Elevation & Depth

Visual hierarchy is established through a combination of **Glassmorphism** and **Neon Light Attribution**. Layers are not just stacked; they are filtered.

1.  **Base Layer:** The Matte Black background (#121414).
2.  **Mid Layer (Glass):** Semi-transparent surfaces (10% - 15% opacity white or primary color) with a 20px backdrop blur. These "floating" panels host the main content.
3.  **Accent Layer:** Glowing accent lines (1px) are applied to the top or left borders of glass panels to simulate a directional light source from above.
4.  **Neon Shadows:** Interactive elements (like active sample cards) use diffused, low-opacity drop shadows tinted with the primary Hot Pink or secondary Electric Blue. This creates a "glow" effect rather than a traditional shadow, making the elements appear as if they are light-emitting hardware components.

## Shapes

The shape language is "Soft" (Level 1) to maintain a technical, engineered feel. Sharp corners are avoided to prevent the UI from feeling dated or overly "Brutalist," while large radii are avoided to preserve the high-density workstation aesthetic. 

Standard components use a 0.25rem (4px) corner radius. Elements that require more visual distinction, such as primary call-to-action buttons or featured sample pack covers, utilize `rounded-lg` (0.5rem) to slightly soften their appearance and draw the eye. The consistency of these tight radii ensures that modular panels look interlocking and efficient.

## Components

### Buttons
Primary buttons use a solid **Hot Pink** background with black text for maximum contrast. Secondary buttons utilize the **Glassmorphic** style: a translucent background with an **Electric Blue** 1px border and a subtle neon outer glow. Hover states trigger a "flicker" transition where the glow intensity increases.

### Cards (Sample Packs)
Cards are treated as "Modules." They feature a matte surface, a 1px top-accent glow line, and high-contrast Epilogue typography. Upon interaction, the card's border should transition to a gradient of Pink to Blue, with a neon shadow matching the dominant color of the pack artwork.

### Input Fields & Controls
Inputs are recessed (inset shadow) and dark. The focus state is signaled by an **Electric Blue** glow around the perimeter. Checkboxes and radio buttons are custom-styled to look like LED indicators on a mixer.

### Audio Specific Components
*   **Waveform Display:** Rendered in Electric Blue with a Hot Pink "playhead" line. The background of the waveform should be 50% darker than the panel surface.
*   **Knobs & Faders:** Use a minimalist vertical fader style with a Hot Pink indicator. Use 1px "ticks" for scale, utilizing the label-mono typographic style for values.
*   **Genre Chips:** Small, uppercase labels with a subtle background tint and a high-saturation border of the same color.