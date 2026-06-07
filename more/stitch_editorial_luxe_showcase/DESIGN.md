---
name: Editorial Luxe
colors:
  surface: '#faf9f5'
  surface-dim: '#dadad6'
  surface-bright: '#faf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f0'
  surface-container: '#eeeeea'
  surface-container-high: '#e8e8e4'
  surface-container-highest: '#e3e3df'
  on-surface: '#1a1c1a'
  on-surface-variant: '#444846'
  inverse-surface: '#2f312e'
  inverse-on-surface: '#f1f1ed'
  outline: '#747876'
  outline-variant: '#c4c7c5'
  surface-tint: '#5d5f5d'
  primary: '#5d5f5d'
  on-primary: '#ffffff'
  primary-container: '#f9f9f7'
  on-primary-container: '#717271'
  inverse-primary: '#c6c7c5'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#6c5e06'
  on-tertiary: '#ffffff'
  tertiary-container: '#fff8e8'
  on-tertiary-container: '#81721d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e3e1'
  primary-fixed-dim: '#c6c7c5'
  on-primary-fixed: '#1a1c1b'
  on-primary-fixed-variant: '#454746'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#f7e382'
  tertiary-fixed-dim: '#dac769'
  on-tertiary-fixed: '#211b00'
  on-tertiary-fixed-variant: '#524700'
  background: '#faf9f5'
  on-background: '#1a1c1a'
  surface-variant: '#e3e3df'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 84px
    fontWeight: '400'
    lineHeight: 92px
    letterSpacing: 0.02em
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 56px
    fontWeight: '400'
    lineHeight: 64px
    letterSpacing: 0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Newsreader
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 32px
  body-md:
    fontFamily: Newsreader
    fontSize: 17px
    fontWeight: '400'
    lineHeight: 28px
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.15em
  label-md:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
spacing:
  unit: 4px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style
This design system embodies the "Editorial-Luxe" aesthetic, targeting a sophisticated audience that values slow consumption and high-fidelity storytelling. The brand personality is authoritative yet graceful, drawing heavily from high-end print journalism and fashion houses.

The design style is a fusion of **Minimalism** and **High-Contrast Editorial**. It prioritizes breathability through expansive whitespace, treating the digital screen like a physical canvas. The emotional response should be one of calm, intellectual stimulation, and exclusivity. Visual interest is generated not through clutter, but through the tension between bold typography and delicate structural elements.

## Colors
The palette is anchored by **Ivory (#F9F9F7)**, which serves as the primary canvas color. This off-white provides a warmer, more expensive feel than pure white, reducing eye strain for long-form reading. 

**Charcoal (#1A1A1A)** provides the structural weight, used for all primary communication and deep tonal contrasts. **Champagne Gold (#C5B358)** is reserved for high-value interactions: key call-to-actions, active states, and refined borders. A soft neutral shade is utilized for subtle dividers to maintain the grid without disrupting the visual flow.

## Typography
The typographic hierarchy is the core of this design system. We use **Noto Serif** for headlines to achieve a timeless, authoritative look, utilizing generous tracking to enhance the "premium" feel. 

**Newsreader** is selected for body copy to provide a literary, comfortable reading experience for long-form content. For functional elements, metadata, and navigational labels, **Work Sans** provides a clean, neutral contrast that ensures the interface remains legible without competing with the editorial content. All uppercase labels should be set with increased letter spacing to maintain the airy, luxe feel.

## Layout & Spacing
The layout follows a **Fixed Grid** model for desktop, shifting to a fluid model for smaller viewports. It employs a 12-column structure with wide 32px gutters and significant 64px outer margins to frame the content.

Layouts should lean into **asymmetry**—for instance, an article title might span columns 1-8 while the lead image is offset to columns 4-12. This creates a rhythmic, curated feeling rather than a templated one. Large "Section Gaps" of 128px or more are used to separate major content blocks, allowing the Ivory background to act as a visual palette cleanser.

## Elevation & Depth
In this design system, depth is communicated through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows. Shadows are strictly avoided to maintain the "ink on paper" aesthetic.

Hierarchy is created by layering elements with thin (1px) borders in Champagne Gold or muted Neutrals. When an element must "float" (such as a dropdown or modal), it should use a subtle Ivory fill that is slightly lighter or darker than the background, or a very soft, high-diffusion ambient blur that mimics the natural lift of paper.

## Shapes
The shape language is defined by **Sharp (0px)** edges. All buttons, containers, image frames, and input fields utilize hard 90-degree angles. This severity reinforces the high-fashion, architectural nature of the design system. 

Rounded corners are seen as too "friendly" or "app-like" for this specific editorial direction. The only exceptions are specific organic shapes found within photography; UI elements must remain strictly geometric.

## Components

### Buttons
Primary buttons are solid Charcoal with Ivory text. Secondary buttons are Ivory with a 1px Champagne Gold border. On hover, buttons should exhibit a subtle "fade-in" transition of 300ms, with the text color shifting to Gold.

### Typography Dividers
Use thin 1px horizontal lines in Gold (#C5B358) to separate sections. These lines should often be shorter than the full width of the container to emphasize the asymmetric layout.

### Input Fields
Inputs are minimal, consisting of a single 1px Charcoal bottom border. Labels use `label-caps` typography and sit above the line. Error states are indicated by a shift to a deep garnet (used sparingly) rather than a bright red.

### Article Cards
Cards do not use containers or shadows. They consist of a high-fidelity image with an editorial treatment (e.g., desaturated or high contrast), followed by a headline in `headline-md`. The "hover" state for a card is a slight 1.02x scale of the image only, maintaining the frame's position.

### Navigation
The navigation should be sparse. Use `label-caps` for top-level links. A "sticky" header is permitted but should be semi-transparent Ivory with a backdrop-blur to maintain a sense of layering.

### Interactive Accents
Interactive elements like "Read More" links or "Next Article" prompts should be accompanied by a thin Gold arrow or underline that animates (slides 4px to the right) on hover.