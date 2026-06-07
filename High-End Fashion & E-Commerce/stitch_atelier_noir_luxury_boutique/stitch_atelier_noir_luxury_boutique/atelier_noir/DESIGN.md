---
name: Atelier-Noir
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#121212'
  on-primary-container: '#7e7d7d'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#b8c8da'
  on-tertiary: '#223240'
  tertiary-container: '#031320'
  on-tertiary-container: '#6f7f8f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#d4e4f6'
  tertiary-fixed-dim: '#b8c8da'
  on-tertiary-fixed: '#0d1d2a'
  on-tertiary-fixed-variant: '#394857'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  margin-mobile: 24px
  margin-desktop: 80px
  gutter: 16px
  stack-xl: 120px
  stack-lg: 64px
  stack-md: 32px
---

## Brand & Style

This design system embodies the "Avant-Garde Luxury" aesthetic, drawing heavily from high-fashion editorial layouts and minimalist movements. The personality is cold, sophisticated, and unapologetically exclusive. It targets a discerning audience that values form as much as function, where the UI acts as a silent gallery frame for the products.

The emotional response is one of curated prestige—quiet, confident, and high-contrast. The style utilizes **Minimalism** with a **Stark/High-Contrast** edge. It features oversized, museum-quality imagery, extreme whitespace, and a rigid adherence to a grid that feels both structural and expansive. Visual noise is eliminated to ensure every element on the screen feels intentional and architectural.

## Colors

The palette is strictly limited to maintain a high-fashion editorial feel. The default mode is **Dark**, utilizing Matte Black (#121212) as the primary canvas to allow product photography and Stark White (#FFFFFF) typography to pierce through the void. 

Slate (#708090) is used sparingly for secondary information, meta-data, and subtle dividers to prevent the UI from feeling flat. Backgrounds should primarily remain Matte Black, with Stark White reserved for high-impact call-to-action sections or "inverted" editorial spreads. All imagery should ideally follow a desaturated or high-key lighting style to harmonize with this monochromatic scheme.

## Typography

Typography is the primary driver of the design system's luxury feel. We use **Noto Serif** for all headlines to provide a traditional, authoritative, and literary tone reminiscent of VOGUE or Harper’s Bazaar. Headlines should be oversized and command the layout.

For functional text, **Inter** provides a utilitarian contrast that ensures readability and a modern, systematic feel. 

**Instructional Notes:**
- Use `label-caps` for all navigation items, small buttons, and category tags to create a rhythmic, architectural feel.
- Maintain wide tracking (letter spacing) on uppercase labels but tight tracking on large serif headlines.
- Paragraphs should be kept short with generous line heights to ensure a "breathable" reading experience.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with a mobile-first priority. On mobile, we use a 4-column system with generous 24px side margins. On desktop, this expands to a 12-column system with ultra-wide 80px margins to create a "boutique" feel.

Spacing is aggressive. We prioritize "white space" (or "black space" in this context) to separate content sections. Instead of tight clusters, use `stack-xl` (120px) to separate major editorial blocks. All elements should align to a 4px baseline grid to maintain mathematical rigor despite the airy layout. Imagery should often break the margin or span the full width of the viewport to create an immersive, avant-garde experience.

## Elevation & Depth

This design system rejects traditional shadows and depth metaphors in favor of **Bold Borders** and **Tonal Layers**. 

Hierarchy is achieved through:
- **Flat Overlays:** Elements do not "float" with shadows; they sit directly on top of one another with 1px Stark White or Slate borders.
- **High-Contrast Z-Indexing:** Overlapping images or text blocks create depth through layering rather than lighting.
- **Thin Outlines:** 1px borders are the primary method of containment for cards, buttons, and inputs. 
- **The "Glass" Exception:** Only in mobile navigation menus may a subtle backdrop blur be used to maintain context, but it must remain desaturated and dark.

## Shapes

The shape language is strictly **Sharp (0)**. There are no rounded corners in this design system. 

Every image, button, input field, and container must have 90-degree angles. This geometric rigidity reinforces the architectural, avant-garde nature of the brand. Borders should be a consistent 1px width. Avoid using heavy containers; let the edges of images and the alignment of text define the boundaries of the UI.

## Components

### Buttons
Primary buttons are solid Stark White with Matte Black text, strictly rectangular. Secondary buttons are transparent with a 1px Stark White border. Hover states should simply invert the colors.

### Input Fields
Inputs consist of a single 1px Slate bottom border that turns Stark White on focus. Labels use the `label-caps` style and sit above the line. No background fills.

### Cards
Product cards are "borderless." The image occupies the full width of the container, with the product name (Serif) and price (Sans-Serif) positioned underneath with ample padding.

### Chips & Tags
Small, rectangular boxes with 1px Slate borders. Text is always `label-caps`.

### Imagery
Images are the most important "component." Use "Full-Bleed" treatments where possible. Every image should have a subtle 1px border or be separated by enough whitespace that it feels like a framed piece of art.

### Navigation
The mobile menu is a full-screen overlay with oversized serif links. Transition animations should be slow and deliberate (e.g., a "curtain" reveal) to emphasize the luxury pace.