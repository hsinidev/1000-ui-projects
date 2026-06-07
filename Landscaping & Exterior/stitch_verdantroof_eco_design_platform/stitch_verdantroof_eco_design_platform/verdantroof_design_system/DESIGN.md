---
name: VerdantRoof Design System
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
  on-surface-variant: '#3f4a3b'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6f7a6a'
  outline-variant: '#becab7'
  surface-tint: '#006e0c'
  primary: '#006c0c'
  on-primary: '#ffffff'
  primary-container: '#1c871e'
  on-primary-container: '#f8fff0'
  inverse-primary: '#77dd6a'
  secondary: '#725a39'
  on-secondary: '#ffffff'
  secondary-container: '#fbdbb0'
  on-secondary-container: '#765f3d'
  tertiary: '#276929'
  on-tertiary: '#ffffff'
  tertiary-container: '#418340'
  on-tertiary-container: '#f7fff1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#92fa83'
  primary-fixed-dim: '#77dd6a'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#005307'
  secondary-fixed: '#feddb3'
  secondary-fixed-dim: '#e1c299'
  on-secondary-fixed: '#281801'
  on-secondary-fixed-variant: '#584324'
  tertiary-fixed: '#acf4a4'
  tertiary-fixed-dim: '#91d78a'
  on-tertiary-fixed: '#002203'
  on-tertiary-fixed-variant: '#0c5216'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
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
  container-max: 1280px
---

## Brand & Style

The brand personality of this design system is rooted in the concept of "Urban Sanctuary." It balances the raw, organic vitality of nature with the precision of modern architectural design. The target audience includes eco-conscious city dwellers and commercial developers looking to integrate sustainable life into concrete environments. 

The UI evokes an emotional response of serenity, reliability, and renewal. To achieve this, the design system employs a **Minimalist Organic** style. This approach uses vast expanses of white space to allow content to "breathe," paired with tactile, nature-inspired elements that prevent the interface from feeling cold or industrial. High-quality imagery of lush greenery should be treated as a core structural element rather than mere decoration.

## Colors

The palette is derived from the lifecycle of a garden. **Deep Forest Green** serves as the primary driver of brand recognition, representing growth and density. **Bamboo** acts as the secondary accent, providing a warm, structural contrast that grounds the vibrant greens. 

**Pure White** is the foundational canvas, ensuring the "breathing" layout feels airy and clean. For typography and deep interface accents, a darker forest shade is used to maintain high legibility while staying within the monochromatic green family. Functional colors for success or warnings should be muted to avoid clashing with the natural aesthetic.

## Typography

This design system utilizes a sophisticated typographic pairing to reflect its "Modern Organic" roots. **Noto Serif** is reserved for headings; its elegant serifs and classic proportions communicate authority and the timelessness of nature. 

For body text and functional labels, **Plus Jakarta Sans** provides a soft, approachable, and highly legible experience. The rounded terminals of the sans-serif font echo the organic shapes found in the UI elements. Line heights are intentionally generous to support the "breathing" layout philosophy and ensure a relaxed reading rhythm.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model with expansive safe areas. Content is centered within a 1280px container to ensure focus and prevent visual fatigue on wide displays. 

A 12-column system is used, but with a preference for asymmetric compositions—such as 5-column text blocks paired with 7-column imagery—to mimic the non-linear beauty of natural growth. Spacing follows a 8px geometric scale, with a heavy emphasis on the 'LG' and 'XL' tokens to create the signature "breathing" effect. Sections should be clearly separated by significant vertical padding rather than harsh lines.

## Elevation & Depth

To maintain an organic feel, this design system avoids harsh, artificial dropshadows. Instead, it utilizes **Ambient Shadows**—soft, extra-diffused blurs with a very low opacity (3-5%). These shadows are subtly tinted with the Primary Green color to make elements feel as though they are floating naturally above a surface, like leaves on a path.

Depth is also created through **Tonal Layering**. Primary content sits on Pure White, while secondary modules or asides may sit on very pale washes of Bamboo or off-white. This subtle contrast guides the eye without the need for heavy borders or structural dividers.

## Shapes

The shape language is strictly **Rounded**, avoiding sharp 90-degree angles which feel industrial and aggressive. Standard components use a 0.5rem base radius, while larger containers like cards and imagery utilize a 1rem to 1.5rem radius to soften the visual perimeter.

A signature element of this design system is the use of **Organic Bezier Curves**. Buttons and certain containers should feature slightly asymmetrical "pebble" rounding where possible. Dividers are never simple lines; they are custom leaf-patterned paths or soft, undulating waves that suggest a horizon or a garden edge.

## Components

### Buttons
Primary buttons are styled with a solid Deep Forest Green background and white text, featuring highly rounded corners (Pill-style). Secondary buttons use a Bamboo border with a transparent center. Hover states should involve a subtle "growth" animation—a slight scale increase or a darkening of the green.

### Cards
Cards are the primary vehicle for content. They feature a white background, a soft green-tinted ambient shadow, and a 1rem corner radius. Padding within cards should be generous (MD or LG spacing tokens) to maintain the airy aesthetic.

### Inputs & Form Fields
Input fields utilize a subtle off-white fill with a 1px Bamboo border that thickens slightly on focus. Labels use the "label-caps" typographic style for clear hierarchy.

### Leaf-Patterned Dividers
Standard horizontal rules are replaced by a custom SVG divider featuring a minimalist, repeating leaf motif. These should be rendered in a 20% opacity of the Primary Green.

### Icons
Icons must be "Nature-Inspired"—monolinear with rounded ends, avoiding jagged edges. Where possible, icons should incorporate leaf or petal details into standard UI symbols (e.g., a "Home" icon with a small leaf sprouting from the roof).

### Progress Indicators
For sustainability metrics or loading states, use an organic "growing" bar that fills with a gradient of green, rather than a standard mechanical bar.