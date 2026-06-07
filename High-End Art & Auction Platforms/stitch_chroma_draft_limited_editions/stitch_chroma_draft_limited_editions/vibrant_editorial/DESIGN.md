---
name: Vibrant Editorial
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#4d4732'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#7e775f'
  outline-variant: '#d0c6ab'
  surface-tint: '#705d00'
  primary: '#705d00'
  on-primary: '#ffffff'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#e9c400'
  secondary: '#b7102a'
  on-secondary: '#ffffff'
  secondary-container: '#db313f'
  on-secondary-container: '#fffbff'
  tertiary: '#485f84'
  on-tertiary: '#ffffff'
  tertiary-container: '#c8dbff'
  on-tertiary-container: '#496084'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#ffdad8'
  secondary-fixed-dim: '#ffb3b1'
  on-secondary-fixed: '#410007'
  on-secondary-fixed-variant: '#92001c'
  tertiary-fixed: '#d5e3ff'
  tertiary-fixed-dim: '#b0c7f1'
  on-tertiary-fixed: '#001b3c'
  on-tertiary-fixed-variant: '#30476a'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 80px
    fontWeight: '900'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Montserrat
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Montserrat
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  caption:
    fontFamily: Montserrat
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
spacing:
  base: 8px
  xs: 4px
  sm: 16px
  md: 32px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 40px
---

## Brand & Style

This design system is built for an elite, high-energy environment that bridges the gap between traditional fine art and contemporary editorial design. It targets discerning collectors who appreciate both the tactile history of lithography and the bold, unapologetic aesthetics of modern culture.

The style is defined as **Vibrant-Editorial**. It leverages high-contrast visuals, heavy structural lines, and a rigid "Bento-box" layout system to organize content into punchy, digestible modules. The emotional response is one of authority and excitement—treating each artist's work with the importance of a front-page headline. A subtle paper-texture overlay is applied globally to ground the digital experience in the physical medium of print.

## Colors

The palette is rooted in a primary-color foundation that mimics the base inks of a print shop. **Vibrant Yellow (#FFD700)** serves as the high-energy highlight, used for primary calls to action and critical focus areas. **Bold Red (#E63946)** provides urgency and artistic flair, while **Deep Blue (#1D3557)** offers a sophisticated, grounding anchor for secondary information and navigation elements.

The background remains a **Crisp White (#FFFFFF)** to ensure maximum legibility and to allow the primary colors to pop without competition. All structural elements are defined by absolute black borders to maintain the "editorial" grid feel.

## Typography

This design system utilizes a high-contrast typographic pairing to reinforce its editorial roots. 

**Playfair Display** is the primary headline face. It should be used at large scales with heavy weights (700-900) to create a dramatic, sophisticated presence. Its sharp serifs and high stroke contrast echo the elegance of traditional lithography.

**Montserrat** is the workhorse sans-serif for body copy, labels, and UI elements. Its geometric clarity provides a modern counterpoint to the serif headlines. For labels and buttons, use the Bold weight with increased letter-spacing and uppercase transformations to maintain the high-energy, "poster" aesthetic.

## Layout & Spacing

The layout philosophy follows a strict **Bento-box grid**—a modular, fixed-grid approach where every element is housed within a defined rectangular cell. The system uses a 12-column structure with generous 24px gutters.

Spacing is aggressive. Large blocks of whitespace (48px to 80px) are used to separate major content sections, while tight, 16px internal padding is used within "boxes" to keep information dense and impactful. Alignment is always pixel-perfect to the grid, reinforcing the feeling of a well-composed magazine layout.

## Elevation & Depth

In this design system, depth is achieved through **color blocking and bold strokes** rather than shadows or blurs. It is a strictly flat aesthetic that relies on the "Z-index" of color.

1. **Surface 0:** The crisp white background with a subtle paper texture overlay.
2. **Surface 1:** Primary color blocks (Yellow, Red, Blue) that sit directly on the background.
3. **Borders:** Every container, button, and input field must have a **3px solid black border**. This creates a "cut-out" effect that replaces the need for elevation shadows.
4. **Overlays:** For modals or pop-outs, use a solid black 4px offset "hard shadow" (no blur) to simulate physical stacking.

## Shapes

The shape language is defined by **absolute precision**. There are no rounded corners in this design system. Every container, button, image, and input field must have **0px (Sharp) corners**. 

This geometric rigidity communicates a sense of elite craftsmanship and architectural stability. The sharp corners allow the bento-box cells to sit flush against one another, creating a seamless, interlocking grid.

## Components

### Buttons
Primary buttons use the Vibrant Yellow background with a 3px black border and black Montserrat Bold text. On hover, the button shifts to the Deep Blue background with White text. All buttons are rectangular with sharp corners.

### Cards (Bento Boxes)
Cards are the core of the design system. They must have a 3px black border and can either be white or filled with one of the primary colors. Use color-blocked headers within cards to separate metadata from the primary image.

### Input Fields
Inputs are white with a 2px black border. When focused, the border thickness increases to 4px. Labels sit above the field in Montserrat Bold, uppercase.

### Chips & Tags
Artist signatures or edition numbers are displayed in small, rectangular chips with a Bold Red background and White text, or a white background with a 2px black border.

### Texture Overlay
A global `paper-texture.png` (low opacity, multiply mode) is applied to all primary color blocks and the main background to ensure the digital interface feels like a physical print.

### Editorial Dividers
Vertical and horizontal lines must be 3px solid black. These are used to separate grid cells and content sections within the Bento layout.