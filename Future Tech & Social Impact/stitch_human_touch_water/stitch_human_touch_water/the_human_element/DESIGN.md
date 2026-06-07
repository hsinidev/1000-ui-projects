---
name: The Human Element
colors:
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#41484c'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#71787d'
  outline-variant: '#c1c7cd'
  surface-tint: '#35647c'
  primary: '#00364a'
  on-primary: '#ffffff'
  primary-container: '#1b4d64'
  on-primary-container: '#8fbdd8'
  inverse-primary: '#9fcde8'
  secondary: '#96472e'
  on-secondary: '#ffffff'
  secondary-container: '#fd997a'
  on-secondary-container: '#762f18'
  tertiary: '#393124'
  on-tertiary: '#ffffff'
  tertiary-container: '#504739'
  on-tertiary-container: '#c3b5a3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c2e8ff'
  primary-fixed-dim: '#9fcde8'
  on-primary-fixed: '#001e2c'
  on-primary-fixed-variant: '#194c63'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#ffb59f'
  on-secondary-fixed: '#3a0a00'
  on-secondary-fixed-variant: '#78311a'
  tertiary-fixed: '#efe0cd'
  tertiary-fixed-dim: '#d3c4b2'
  on-tertiary-fixed: '#221a0f'
  on-tertiary-fixed-variant: '#4f4537'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
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
  label-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin: 32px
  section-gap: 120px
---

## Brand & Style
The core of this design system is "Empathy through Authenticity." It rejects the sterile, clinical nature of traditional non-profit interfaces in favor of a **Tactile and Minimalist** aesthetic that feels like a shared journal or a personal letter. The goal is to evoke a sense of global community, warmth, and urgent yet hopeful action.

The style leverages high-quality, sun-drenched photography with film-grain textures to create a nostalgic, "lived-in" feeling. To balance the professional requirements of a global charity with the "Human-Touch" directive, the UI incorporates deliberate imperfections: hand-drawn SVG "scribble" underlines, irregular border-radii on image containers, and a layout that breathes with editorial-inspired whitespace.

## Colors
The palette is rooted in the earth and the water it provides. 
- **Deep Water Blue (#1B4D64):** Used for primary actions and grounding headlines, representing the depth and reliability of the mission.
- **Terracotta (#C96F53):** Reserved for emotional call-to-actions, highlights, and "human" elements like donation buttons or impact statistics.
- **Warm Beige (#EADBC8) & Parchment (#F9F7F2):** These form the foundation of the UI, replacing harsh whites with a softer, more organic surface that reduces eye strain and feels more like natural material.

Avoid pure blacks; use a tinted charcoal derived from the primary blue for all text to maintain a soft, cohesive look.

## Typography
This design system utilizes a sophisticated pairing of an authoritative serif and a warm sans-serif. 

**Newsreader** serves as the voice of the story. Its literary heritage makes it perfect for long-form impact stories and evocative headlines. It should be used with generous leading to allow the "ink" to breathe.

**Be Vietnam Pro** handles the functional UI. Its contemporary, open terminals and friendly proportions make it highly legible for navigation, form fields, and secondary metadata. It provides the "professional" anchor to the more "expressive" serif headlines.

## Layout & Spacing
The layout follows a **Fixed Grid** model (12 columns) but intentionally breaks the grid with "asymmetric accents." While content is centered and structured, hand-drawn scribbles, arrows, and photo captions are permitted to bleed into the margins to create a scrapbook effect.

Spacing is generous. Section gaps are intentionally large to facilitate a slow, deliberate scrolling experience that encourages reading rather than skimming. Use an 8px baseline rhythm to ensure vertical harmony between disparate elements like images and text blocks.

## Elevation & Depth
In keeping with the tactile aesthetic, this design system avoids heavy, synthetic drop shadows. Depth is achieved through **Tonal Layers** and **Low-Contrast Outlines**.

- **Surfaces:** Use subtle shifts between the neutral parchment and warm beige to define "lifted" areas.
- **Borders:** Instead of shadows, use 1px solid borders in a slightly darker shade of the background color (e.g., a beige border on a parchment surface).
- **Interactive Elements:** Use a very soft, tinted "ambient" shadow (5% opacity of the primary blue) only when an element is hovered, simulating a physical piece of paper being slightly lifted.

## Shapes
The shape language is **Soft (0.25rem)**. This slight rounding removes the "digital" sharpness of 90-degree corners without making the UI feel bubbly or "app-like."

For photography, apply irregular masks or subtle "hand-cut" edge effects to reinforce the human-touch aesthetic. Icons and decorative "scribbles" should always use a variable stroke weight to mimic a physical pen or brush.

## Components
- **Buttons:** Primary buttons use the Terracotta fill with white Be Vietnam Pro text. They should have a slightly irregular "hand-drawn" border-radius (e.g., `4px 6px 4px 8px`) to feel organic.
- **Cards:** Use the warm beige background with a 1px "sand" border. Content should be padded generously.
- **Scribble Accents:** A set of SVG primitives (circles, underlines, arrows) used to highlight key phrases within serif headlines. These should animate "drawing in" as they enter the viewport.
- **Input Fields:** Minimalist design with only a bottom border in Deep Water Blue. Labels should use the `label-sm` style for a professional, organized look.
- **Progress Indicators:** For donation goals, use a "hand-filled" texture for the progress bar rather than a solid color block, emphasizing the individual effort behind the numbers.
- **Impact Cards:** Large-format cards featuring a full-bleed nostalgic photo, a Newsreader headline, and a short caption, used to bridge the gap between data and human storytelling.