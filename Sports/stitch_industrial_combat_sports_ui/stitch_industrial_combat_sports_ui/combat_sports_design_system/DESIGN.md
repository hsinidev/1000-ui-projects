---
name: Combat Sports Design System
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#e7bdb3'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#ae887f'
  outline-variant: '#5d3f38'
  surface-tint: '#ffb4a2'
  primary: '#ffb4a2'
  on-primary: '#611200'
  primary-container: '#ff562b'
  on-primary-container: '#550e00'
  inverse-primary: '#b42900'
  secondary: '#c1c8ca'
  on-secondary: '#2b3234'
  secondary-container: '#434a4c'
  on-secondary-container: '#b2babc'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a29'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad2'
  primary-fixed-dim: '#ffb4a2'
  on-primary-fixed: '#3c0700'
  on-primary-fixed-variant: '#891d00'
  secondary-fixed: '#dde4e6'
  secondary-fixed-dim: '#c1c8ca'
  on-secondary-fixed: '#161d1f'
  on-secondary-fixed-variant: '#41484a'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-xl:
    fontFamily: Epilogue
    fontSize: 72px
    fontWeight: '900'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 24px
  margin: 48px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system is engineered to capture the visceral intensity of professional combat sports. The brand personality is aggressive, unapologetic, and elite—evoking the atmosphere of a main-event walkout under heavy arena lights. It targets a demographic that values technical mastery and raw physical stakes.

The aesthetic follows a **High-Contrast / Brutalist** hybrid style. It prioritizes structural integrity over decorative softness, using heavy strokes and industrial layouts to communicate durability. The emotional response should be one of "controlled chaos"—a cinematic experience where every UI element feels like it was forged in an industrial environment, mirroring the grit of a training camp and the polished spectacle of a live broadcast.

## Colors

The palette is strictly high-performance. The "Blood-Orange" primary color acts as the sole driver of action, used exclusively for critical calls-to-action, live status indicators, and victory states. It must vibrate against the deep charcoal backgrounds to ensure immediate visual hierarchy.

The neutral scale is composed of "Soot" (#0F0F0F) for primary backgrounds and "Obsidian" (#1A1A1A) for surface layers. Slate grays provide the necessary mid-tones for borders and secondary text. White is reserved for maximum-impact typography and essential data points, ensuring a crisp, "broadcast-ready" readout that cuts through the dark UI.

## Typography

Typography in this design system is treated as a structural element. **Epilogue** is used for headlines in its heaviest weights (ExtraBold and Black) to create an intense, editorial feel. Letter spacing is tightened on larger displays to mimic the condensed look of traditional fight posters.

**Work Sans** provides a grounded, neutral balance for long-form content, ensuring legibility against dark backgrounds. **Lexend** is employed for labels and data visualizations; its "athletic" geometry reinforces the sports-centric nature of the interface. All uppercase styling should be applied to labels and callouts to maintain a formal, professional tone.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model on desktop to maintain a cinematic aspect ratio, transitioning to a fluid model on mobile. The layout is built on a strict 8px rhythm to ensure all elements feel robust and aligned. 

Large margins (48px+) are used to isolate primary content, creating a focused, "arena-like" center stage. Gutters are intentionally wide to prevent the UI from feeling cluttered, allowing the high-contrast typography and imagery to breathe. Vertical stacking follows a rhythmic progression (16/32/64), emphasizing clear separation between different "fight cards" or content sections.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Bold Borders** rather than traditional shadows. Surfaces do not "float" with soft blurs; instead, they are stacked like industrial plates. 

Backgrounds use the deepest charcoal, while interactive surfaces use a slightly lighter slate gray. To indicate focus or elevation, elements use a 2px solid border in a mid-gray or the primary Blood-Orange. Subtle, low-opacity noise textures or "brushed metal" overlays may be applied to cards to enhance the raw, industrial aesthetic. Background blurs are used sparingly only for overlays, maintaining a sharp, high-fidelity look throughout.

## Shapes

The shape language is defined by **Sharp (0)** corners. In this design system, there are no rounded corners; every element is rectangular and hard-edged to reflect the "unrefined" and "raw" brand pillars. This lack of curvature creates an architectural, aggressive aesthetic that differentiates the product from softer, consumer-grade applications. Buttons, input fields, and image containers must adhere to these 90-degree angles to maintain the industrial narrative.

## Components

### Buttons
Primary buttons are solid Blood-Orange with black text, utilizing the `label-caps` typography. They feature a "hard shadow" effect—a 2px offset solid black border—to feel tactile and pressed into the UI. Secondary buttons use a thick 2px white border with no fill.

### Cards
Cards are the primary container for fighter profiles and event data. They use the Obsidian (#1A1A1A) background with a subtle concrete texture overlay at 5% opacity. All images within cards should have a slight desaturation or "film grain" filter applied to maintain the cinematic tone.

### Inputs
Input fields are "boxed" with a 2px slate border. Upon focus, the border transitions to Blood-Orange. Labels are always positioned above the field in `label-caps` for maximum clarity.

### Chips & Status Indicators
Used for "LIVE" or "UPCOMING" status. These are small, rectangular blocks of solid color. Live indicators should use the primary Blood-Orange with a subtle pulse animation, while weight classes or rankings use a neutral slate.

### Additional Components
- **The Tale of the Tape:** A specialized comparison component using heavy vertical lines and centered `display-xl` typography to compare fighter stats.
- **Broadcast Ticker:** A high-contrast horizontal scroll for live results and news, positioned at the bottom of the viewport.