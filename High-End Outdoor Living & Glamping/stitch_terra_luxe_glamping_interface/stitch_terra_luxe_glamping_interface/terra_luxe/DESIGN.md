---
name: Terra-Luxe
colors:
  surface: '#f7fafb'
  surface-dim: '#d7dadb'
  surface-bright: '#f7fafb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f5'
  surface-container: '#ebeeef'
  surface-container-high: '#e6e9ea'
  surface-container-highest: '#e0e3e4'
  on-surface: '#181c1d'
  on-surface-variant: '#56423d'
  inverse-surface: '#2d3132'
  inverse-on-surface: '#eef1f2'
  outline: '#89726c'
  outline-variant: '#ddc0b9'
  surface-tint: '#9e4127'
  primary: '#9b3f25'
  on-primary: '#ffffff'
  primary-container: '#bb563b'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb5a1'
  secondary: '#615e57'
  on-secondary: '#ffffff'
  secondary-container: '#e7e2d9'
  on-secondary-container: '#67645d'
  tertiary: '#655a4c'
  on-tertiary: '#ffffff'
  tertiary-container: '#7f7364'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd1'
  primary-fixed-dim: '#ffb5a1'
  on-primary-fixed: '#3b0800'
  on-primary-fixed-variant: '#7f2a12'
  secondary-fixed: '#e7e2d9'
  secondary-fixed-dim: '#cac6be'
  on-secondary-fixed: '#1d1c16'
  on-secondary-fixed-variant: '#494740'
  tertiary-fixed: '#f0e0ce'
  tertiary-fixed-dim: '#d3c4b3'
  on-tertiary-fixed: '#221a0f'
  on-tertiary-fixed-variant: '#4f4538'
  background: '#f7fafb'
  on-background: '#181c1d'
  surface-variant: '#e0e3e4'
typography:
  display-lg:
    fontFamily: ebGaramond
    fontSize: 64px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: ebGaramond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: ebGaramond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: plusJakartaSans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: plusJakartaSans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: plusJakartaSans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-edge: 40px
  section-gap: 120px
---

## Brand & Style

This design system is built upon the concept of **Grounded Luxury**. It avoids the sterile coldness of traditional luxury in favor of a warm, tactile, and immersive experience that mirrors the physical sensation of a high-end glamping retreat. The aesthetic balances an **Earthy & Refined** spirit, utilizing high-performance minimalism to ensure the UI never feels cluttered or slow.

The visual direction is a hybrid of **Minimalism** and **Tactile** design. It leverages generous whitespace (represented by soft sand tones) and high-quality editorial typography. To evoke a sense of the physical world, subtle 'Paper' textures are applied to surfaces, creating a multi-sensory digital environment that feels permanent, reliable, and deeply connected to nature.

## Colors

The palette is derived directly from the landscape. **Terracotta** serves as the primary accent, used sparingly for calls to action and key brand moments to represent the warmth of clay and evening sun. **Sand** provides a soft, non-reflective background that reduces eye strain and reinforces the tactile paper aesthetic.

**Deep Slate** is utilized for typography and structural boundaries, providing a sophisticated contrast that ensures high legibility and a sense of architectural permanence. A muted taupe is introduced as a tertiary color for secondary UI elements, ensuring the transition between sand and slate feels organic rather than jarring.

## Typography

This design system employs a sophisticated typographic contrast to signal luxury. **ebGaramond** is the primary display face; its classical proportions and graceful serifs convey an intellectual and premium tone. It should be used for headlines and storytelling elements.

**plusJakartaSans** provides a contemporary, friendly, and highly legible counterpoint for all functional UI text, body copy, and labels. The soft, rounded terminals of this font complement the organic shape language of the interface. All caps should be reserved for small labels and navigation items to maintain an editorial feel without sacrificing high-performance clarity.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model with an emphasis on "The Breathable Page." By using a 12-column grid with generous outer margins, the design ensures that content feels curated rather than crowded. 

Spacing follows a strict 8px rhythmic scale, but vertical gaps between major sections are intentionally oversized (120px+) to create a sense of calm and deliberate pacing. Elements should often overlap slightly or use asymmetrical alignments to mimic the fluid, non-linear lines found in nature.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and texture rather than aggressive shadows. Surfaces are stacked to create hierarchy:
1.  **Base Layer:** The 'Sand' background, featuring a subtle, full-screen noise grain to simulate high-end cotton paper.
2.  **Surface Layer:** Slightly lighter or tinted containers that use "Low-contrast outlines" (1px Deep Slate at 10% opacity) instead of drop shadows.
3.  **Active Layer:** Elements requiring immediate attention may use a very soft, "Ambient Shadow"—a diffused, terracotta-tinted glow that suggests the element is catching warm light.

Glassmorphism is used exclusively for navigation overlays, using a heavy backdrop blur to maintain the "immersive" quality while keeping the user grounded in their current context.

## Shapes

The shape language is defined by **Organic UI shapes**. Sharp corners are avoided to maintain the "Earthy & Refined" personality. Standard containers use a 0.5rem (8px) radius, while larger cards and featured imagery utilize a 1.5rem (24px) radius. 

To reinforce the "fluid lines" mentioned in the aesthetic brief, specific decorative elements or buttons may feature a "squircle" or slightly non-uniform roundedness to feel hand-crafted rather than machine-made.

## Components

### Buttons
Primary buttons use a solid Terracotta fill with Deep Slate text for high contrast. They feature a soft, pill-like radius. Secondary buttons use a Deep Slate outline with no fill, emphasizing the minimalist nature of the design system.

### Input Fields
Inputs are rendered as simple bottom-border lines or very soft Sand-toned wells. Focus states are indicated by a thickening of the Deep Slate underline and a subtle warm glow. Labels always use the `label-md` style in Plus Jakarta Sans.

### Cards
Cards are the primary vessel for retreat listings. They should feature full-bleed imagery with a subtle 'Paper' texture overlay on the text container portion. They do not use heavy shadows; instead, they are separated by 1px borders in a muted taupe.

### Progress Indicators & Sliders
In line with "High-Performance," these elements should be ultra-thin and sophisticated. Use Terracotta for the "active" portion of the track and Deep Slate for the "inactive" track at low opacity.

### Navigation
The navigation bar is persistent but minimal. It uses a frosted glass effect with the 'Sand' color to ensure it feels like a physical layer floating over the content. Links are set in Plus Jakarta Sans with generous tracking.