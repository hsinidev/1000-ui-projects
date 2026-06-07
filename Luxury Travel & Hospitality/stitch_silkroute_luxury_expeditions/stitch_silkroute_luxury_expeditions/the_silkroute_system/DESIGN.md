---
name: The SilkRoute System
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
  on-surface-variant: '#55423e'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#88726d'
  outline-variant: '#dcc1ba'
  surface-tint: '#9b442e'
  primary: '#98412c'
  on-primary: '#ffffff'
  primary-container: '#b75942'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb4a2'
  secondary: '#516169'
  on-secondary: '#ffffff'
  secondary-container: '#d2e2ec'
  on-secondary-container: '#55656d'
  tertiary: '#735c00'
  on-tertiary: '#ffffff'
  tertiary-container: '#cba72f'
  on-tertiary-container: '#4e3d00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad2'
  primary-fixed-dim: '#ffb4a2'
  on-primary-fixed: '#3c0700'
  on-primary-fixed-variant: '#7c2d19'
  secondary-fixed: '#d5e5ef'
  secondary-fixed-dim: '#b9c9d3'
  on-secondary-fixed: '#0e1d25'
  on-secondary-fixed-variant: '#3a4951'
  tertiary-fixed: '#ffe088'
  tertiary-fixed-dim: '#e9c349'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#574500'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
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
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
---

## Brand & Style

This design system is built to evoke the sensation of a bespoke, high-end travel journal. It targets a discerning audience that seeks both rugged adventure and uncompromising refinement. The brand personality is "The Sophisticated Explorer"—authoritative yet inviting, weathered yet polished.

The visual style is a fusion of **Tactile Minimalism** and **Organic Modernism**. Unlike rigid corporate interfaces, this design system prioritizes a physical feel through the use of subtle grain, paper-like textures, and fluid, non-geometric containers. It avoids harsh digital perfections in favor of soft, natural edges that suggest hand-drawn maps and curated scrapbooks. The emotional response should be one of quiet confidence, heritage, and the tactile thrill of planning a once-in-a-lifetime expedition.

## Colors

The palette is rooted in the natural world, drawing from the raw pigments of the Silk Road. 

*   **Creamy Paper (#F9F7F2):** Serves as the primary canvas, providing a warm, non-glare background that feels more premium than pure white.
*   **Earthy Terracotta (#C06048):** Used for primary actions and key highlights, evoking sun-baked clay and vitality.
*   **Slate (#2F3E46):** Provides grounding and contrast, used for secondary elements and deep readability.
*   **Gold (#D4AF37):** Reserved for moments of luxury, status indicators, and delicate embellishments.

Apply a 2% monochromatic noise overlay to the Creamy Paper backgrounds to simulate physical paper stock.

## Typography

This design system utilizes a classic serif for narrative and a contemporary sans-serif for utility. **Noto Serif** provides an editorial, authoritative voice for headlines, suggesting the weight of a published journal. **Plus Jakarta Sans** is used for body copy and UI labels to ensure high legibility and a modern, approachable feel against the more traditional serif.

Use "label-caps" for small metadata or navigational cues to provide a structured, "catalogued" look. Maintain generous line heights to preserve a sense of airiness and luxury.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid Hybrid**. While content is constrained to a 1280px maximum width to maintain readability, background textures and organic decorative elements should bleed to the edge of the viewport.

The spacing rhythm is intentional and spacious. Use large vertical margins between sections (80px–120px) to allow the "paper" to breathe. Avoid dense clusters of information; the goal is a curated experience where every element has a dedicated place, much like a high-end coffee table book.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layers** and **Tactile Textures** rather than traditional drop shadows.

1.  **The Base:** The Creamy Paper (#F9F7F2) with subtle grain.
2.  **Raised Elements:** Use a slightly darker "parchment" tint (#F2EFE9) for cards or inset sections to create depth through color shifts.
3.  **The "Ink" Shadow:** When a shadow is strictly necessary for interactivity (like a floating button), use an ultra-diffused, low-opacity Slate (#2F3E46) shadow with a 15% opacity, simulating an object resting on a soft surface rather than hovering in digital space.
4.  **Separator Lines:** Use thin, 1px lines in 10% Slate to mimic hand-ruled journal lines.

## Shapes

The shape language is **Organic and Fluid**. Avoid perfect circles or rigid, sharp rectangles.

*   **Containers:** Use "squircle" or slightly irregular radii to mimic hand-cut paper or natural stones.
*   **Buttons:** Apply a high roundedness (rounded-xl) but with a subtle "wobble" in the border-radius (e.g., 24px 28px 22px 30px) if the technical environment allows, to enhance the organic feel.
*   **Images:** Use asymmetrical masks for hero images to create a dynamic, adventurous composition that breaks the grid.

## Components

**Buttons:** Primary buttons should be Terracotta with Creamy Paper text. Use a subtle inner-glow to suggest a "pressed" or "embossed" feel. Secondary buttons use a Slate outline with no fill.

**Cards:** Cards should not have borders. Use the tonal shift (#F2EFE9) and a 1px subtle grain overlay. The top corner should have a larger radius than the bottom to create a "tabbed" journal look.

**Input Fields:** Bottom-border only, mimicking a line in a notebook. When focused, the line transforms from Slate to Terracotta.

**Chips/Tags:** Small, pill-shaped elements in Gold (#D4AF37) with Slate text, used for "Curated," "Luxury," or "Limited" status badges.

**Navigation:** A minimalist top bar with a centered logo. Use a "Stamp" or "Wax Seal" component for call-to-action buttons in the header to reinforce the expedition theme.

**Additional Component - The "Travel Log" List:** A specialized list style for itineraries where items are connected by a vertical dashed line, mimicking a path on a map.