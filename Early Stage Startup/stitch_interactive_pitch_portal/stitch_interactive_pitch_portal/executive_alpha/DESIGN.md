---
name: Executive Alpha
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1a1a1a'
  on-primary-container: '#848282'
  inverse-primary: '#5f5e5e'
  secondary: '#ffb4a8'
  on-secondary: '#690100'
  secondary-container: '#ff5540'
  on-secondary-container: '#5c0000'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#181a1a'
  on-tertiary-container: '#818383'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#ffdad4'
  secondary-fixed-dim: '#ffb4a8'
  on-secondary-fixed: '#410000'
  on-secondary-fixed-variant: '#930100'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Inter
    fontSize: 80px
    fontWeight: '800'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  h2:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  data-label:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  section-gap: 128px
---

## Brand & Style
The design system establishes a high-stakes environment for venture capital and private equity. It balances institutional authority with the raw energy of high-growth startups. The personality is "Aggressive Professionalism"—it is direct, urgent, and precise.

Drawing from **High-Contrast Minimalism** and **Brutalism**, the UI avoids soft gradients and decorative flourishes. Instead, it utilizes massive typography, razor-sharp edges, and a restricted palette to command attention. The emotional response is one of confidence and exclusivity; this is a portal where significant capital meets high-potential opportunities.

## Colors
The palette is dominated by **Deep Charcoal (#1A1A1A)** to provide a sophisticated, low-fatigue backdrop that feels premium and focused. 

**Signal Red (#FF0000)** is used surgically. It is reserved exclusively for primary calls to action, critical data points, and indicators of high momentum. It must never be used for background decorative elements. **Crisp White (#FFFFFF)** provides maximum legibility for data and body copy. A secondary neutral, a slightly lighter charcoal (#262626), is used for subtle surface layering and structural containment.

## Typography
This design system utilizes **Inter** for its systematic, utilitarian clarity. Headings are set with heavy weights and tight letter-spacing to create a "wall of text" impact that feels authoritative. 

For technical data points and small labels, **Space Grotesk** is introduced. Its geometric, slightly futuristic character emphasizes the "Live" and "Digital" nature of the portal. Use all-caps for labels to distinguish them from narrative body copy.

## Layout & Spacing
The layout follows a **Fluid Grid** model with high-impact margins. For desktop viewing, 12 columns provide the structure for complex data visualizations, while full-screen horizontal sections house narrative "pitch" content.

Spacing is aggressive. Large gaps between sections (128px+) create a sense of scale and focus. Components use a strict 8px base grid. On mobile, charts must expand to the full width of the viewport minus the 20px margins to ensure technical legibility.

## Elevation & Depth
This design system rejects traditional shadows. Depth is achieved through **Tonal Layers** and **Bold Borders**. 

1. **Surface 0 (Background):** #1A1A1A.
2. **Surface 1 (Cards/Containers):** #262626.
3. **Borders:** Use 1px solid white at 10% opacity for standard containers, or 2px solid white at 100% opacity for active/focused states.

No blur or frosted glass is permitted. Overlays and modals should be opaque or utilize a solid Signal Red accent line at the top to indicate hierarchy.

## Shapes
The shape language is strictly **Sharp (0px)**. Every element—from buttons and cards to input fields and image containers—must have 90-degree corners. This reinforces the "Aggressive" and "Minimalist" brand style, suggesting precision and institutional rigidity. 

Geometry should be used as a graphic device: diagonal lines at 45 degrees can be used for section dividers or decorative "arrow" elements to suggest upward growth.

## Components
- **Primary Action (CTA):** Signal Red background, White bold text, all-caps. No border. On hover, the color shifts to a slightly darker red or black with a white border.
- **Data Cards:** #262626 background with a 1px #FFFFFF (10% opacity) border. Use Signal Red for the most important metric on the card.
- **Charts:** Use thin (1px) lines. Trend lines should be White or Signal Red. Grid lines should be very faint (5% white opacity).
- **Inputs:** Dark background (#1A1A1A) with a bottom-only border in White. Transitions to Signal Red on focus.
- **Scroll Indicators:** Minimalist vertical lines that animate downward, signaling to the user that more data is available below the fold.
- **Investment Progress Bar:** Solid Signal Red fill against a #262626 track. No rounded ends.