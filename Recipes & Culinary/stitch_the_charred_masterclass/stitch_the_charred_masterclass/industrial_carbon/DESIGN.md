---
name: Industrial Carbon
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
  on-surface-variant: '#e0c0b2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a78b7e'
  outline-variant: '#584238'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#562000'
  primary-container: '#ea6b1e'
  on-primary-container: '#4b1b00'
  inverse-primary: '#a04100'
  secondary: '#b8c8da'
  on-secondary: '#223240'
  secondary-container: '#394857'
  on-secondary-container: '#a7b7c8'
  tertiary: '#ffb4ac'
  on-tertiary: '#690007'
  tertiary-container: '#fb584f'
  on-tertiary-container: '#5c0005'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#ffdad6'
  tertiary-fixed-dim: '#ffb4ac'
  on-tertiary-fixed: '#410003'
  on-tertiary-fixed-variant: '#92030f'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Epilogue
    fontSize: 64px
    fontWeight: '900'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  technical-data:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  label:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style
The design system is engineered to evoke the raw intensity of open-fire cooking and the rugged durability of cast iron. It targets a serious grilling audience, moving away from "backyard hobbyist" tropes toward a professional, "industrial rustic" aesthetic.

The visual style leans heavily into **Brutalism** and **Tactile** design. It utilizes high-contrast interfaces, raw textures, and heavy-duty structural elements to create an atmosphere of heat, smoke, and steel. The emotional response is one of power, expertise, and technical precision. Every element should feel forged rather than rendered, using soot-like overlays and metallic finishes to ground the digital experience in the physical world of BBQ.

## Colors
The color palette is dominated by the **Deep Charcoal (#1A1A1A)** background, which must be implemented with a subtle 5-10% opacity noise or carbon texture overlay to prevent flat "digital" blacks. 

**Burnt Orange (#CC5500)** is the high-visibility signal color, reserved exclusively for primary calls to action, active states, and critical heat-related data points. **Ember Red (#B22222)** acts as a tertiary accent for alerts, warning zones on temperature gauges, or secondary highlights. **Smoke Grey (#708090)** provides the industrial framework, used for borders, inactive states, and secondary UI chrome. Typography and fine details utilize **Ash White (#E5E4E2)** to maintain high legibility against the dark, textured background.

## Typography
This design system utilizes a high-contrast typographic pairing. **Epilogue** serves as the heading typeface; its heavy weights provide the "weathered impact" feel required for a grit-focused brand. All major headlines should be set in Bold or Black weights with tight kerning to mimic industrial stenciling.

For body copy and technical specifications, **Work Sans** provides a grounded, neutral balance. Technical data (cook times, temperatures, weights) must utilize the `technical-data` style, featuring generous tracking (letter spacing) to ensure readability in high-heat or high-glare environments. All labels and metadata should be uppercase to reinforce the utilitarian, manual-style aesthetic.

## Layout & Spacing
The layout follows a **fixed grid** model to suggest the rigid structure of a technical manual or a machinist's blueprint. A standard 12-column grid is used for desktop, with a focus on asymmetrical compositions that favor large-scale video or imagery on one side and technical data on the other.

Spacing is generous to allow the high-impact typography room to breathe. Margins and gutters are heavy, creating a "framed" effect for content. Components should be spaced using an 8px rhythmic scale, prioritizing vertical stacks that emphasize the height and power of the imagery.

## Elevation & Depth
Elevation in this design system is conveyed through **Tonal Layers** and **Tactile Textures** rather than traditional soft shadows. 

1.  **Base Layer:** Deep Charcoal (#1A1A1A) with carbon texture.
2.  **Surface Layer:** Matte Black (#121212) used for cards and containers, appearing "etched" into the base layer using a 1px Smoke Grey top border.
3.  **Active Layer:** Burnt Orange surfaces for buttons, which utilize a slight inner-glow (Ember Red) to simulate heat radiating from within the component.

Depth is also created through "burnt" border effects—using a dark, blurred inner shadow (multiply mode) on cards to make them appear as though their edges have been scorched by fire.

## Shapes
The shape language is strictly **Sharp (0)**. Industrial tools and heavy machinery rarely feature decorative rounding; therefore, all buttons, input fields, cards, and image containers must have 0px border radii. 

This lack of rounding reinforces the "rugged" and "unrefined" nature of the design system. Where visual separation is needed between sharp elements, use a 1px solid stroke in Smoke Grey or a 2px "offset" border to create a layered, mechanical look.

## Components
### Buttons
Primary buttons are solid Burnt Orange with Black text. Secondary buttons are Ash White outlines with 0px corners. Hover states should trigger a "glow" effect using Ember Red, simulating a heating element.

### Heavy-Duty Sliders
Used for temperature and time controls. The track is a recessed Smoke Grey bar. The thumb (handle) is a large, metallic Ash White rectangle with "knurled" texture (3-4 vertical 1px lines) to suggest a physical dial that requires a firm grip.

### Burnt Cards
Containers for recipes or articles. These feature the Matte Black surface and a "burnt" edge effect—a subtle, irregular dark gradient on the inner perimeter. They must support high-contrast Ash White typography and full-bleed video headers.

### Iconography
Icons must be thick-stroked and high-contrast. Use geometric shapes and avoid thin lines. Icons should appear as if they were stamped or branded into the interface.

### Video-First Layouts
Video components are the primary source of engagement. They should be presented with "Letterbox" black bars on top and bottom, regardless of aspect ratio, to enhance the cinematic, high-production feel of the grilling content. Use Burnt Orange for playhead progress bars.

### Input Fields
Strictly rectangular with Smoke Grey borders. Focus states change the border to Burnt Orange with a 1px outer glow.