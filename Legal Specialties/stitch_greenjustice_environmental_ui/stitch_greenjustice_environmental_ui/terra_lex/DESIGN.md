---
name: Terra Lex
colors:
  surface: '#faf9f5'
  surface-dim: '#dbdad6'
  surface-bright: '#faf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f0'
  surface-container: '#efeeea'
  surface-container-high: '#e9e8e4'
  surface-container-highest: '#e3e2df'
  on-surface: '#1b1c1a'
  on-surface-variant: '#414844'
  inverse-surface: '#2f312e'
  inverse-on-surface: '#f2f1ed'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#77574d'
  on-secondary: '#ffffff'
  secondary-container: '#fed3c7'
  on-secondary-container: '#795950'
  tertiary: '#20291a'
  on-tertiary: '#ffffff'
  tertiary-container: '#353f2f'
  on-tertiary-container: '#9faa95'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#e7bdb1'
  on-secondary-fixed: '#2c160e'
  on-secondary-fixed-variant: '#5d4037'
  tertiary-fixed: '#dbe6cf'
  tertiary-fixed-dim: '#bfcab4'
  on-tertiary-fixed: '#151e10'
  on-tertiary-fixed-variant: '#404a39'
  background: '#faf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e3e2df'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Work Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.4'
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
  container-max: 1200px
  gutter: 24px
  margin: 32px
  section-gap: 80px
---

## Brand & Style

The brand personality is rooted in the intersection of legal stoicism and ecological stewardship. This design system communicates a "protector" archetype—someone who is as comfortable in a high-stakes courtroom as they are in an old-growth forest. The UI should evoke a sense of permanence, reliability, and organic growth.

The chosen style is **Tactile Minimalism**. It strips away unnecessary digital clutter to focus on authoritative content, but softens the edges with physical metaphors. By incorporating subtle grain textures and paper-like surfaces, the design system avoids the sterile coldness of typical corporate law, replacing it with a grounded, human-centric warmth that aligns with environmental advocacy.

## Colors

The palette is derived directly from the forest floor and deep canopy. 

- **Primary (Forest Green):** A deep, saturated evergreen used for primary actions and headers to establish authority and represent the core mission of conservation.
- **Secondary (Earthy Brown):** A loamy, rich brown used for secondary elements and borders, grounding the UI in a physical reality.
- **Neutral (Paper White):** Not a pure digital white, but a warm, unbleached paper tone that reduces eye strain and reinforces the tactile, organic theme.
- **Tertiary (Moss/Sage):** A muted green for backgrounds and subtle accents.
- **Accent (Sunlight/Energy):** A vibrant lime-tinted green used sparingly to highlight renewable energy initiatives and interactive "success" states.

## Typography

This design system utilizes a sophisticated typographic pairing to balance tradition with modernity.

- **Headings (Newsreader):** This sturdy, editorial serif brings a sense of literary authority and legal precedent. It should be used for all storytelling and high-level navigation to command respect.
- **Body & Interface (Work Sans):** A clean, grounded sans-serif that ensures maximum legibility for complex legal documents. Its slightly wider apertures and stable stance make it feel more approachable and modern than a traditional grotesque.

Hierarchy should be strictly maintained to guide the user through dense information, using generous line heights to allow the text to "breathe" like a forest clearing.

## Layout & Spacing

The layout follows a **Fixed Grid** model to mirror the structured nature of law. Content is centered within a 1200px container to ensure readability and a focused user experience.

- **Rhythm:** An 8px base unit governs all spatial relationships.
- **Breathing Room:** Large "section-gaps" are encouraged to prevent the interface from feeling claustrophobic, symbolizing the open spaces the firm seeks to protect.
- **Alignment:** Use asymmetrical layouts for imagery to maintain an "organic" feel, while keeping text blocks strictly aligned to the grid for professional clarity.

## Elevation & Depth

In this design system, depth is communicated through **Tonal Layers** and texture rather than aggressive shadows. 

- **Surface Levels:** Use slight color shifts (from Paper White to Sage) to distinguish between background and foreground elements.
- **Grain Texture:** Apply a very fine, low-opacity noise overlay (2-4% opacity) to the entire UI. This breaks the "flatness" of the screen and gives the interface a tangible, recycled-paper quality.
- **Soft Insets:** Use subtle inner shadows on input fields and containers to make them feel "pressed" into the paper surface, creating a debossed effect.
- **Subtle Shadows:** When elevation is required (e.g., for modals), use long, low-opacity shadows tinted with the Primary Forest Green color to keep the lighting feel natural and ambient.

## Shapes

The shape language is strictly **Organic**. Sharp 90-degree corners are avoided to move away from the "harshness" of industrial design.

- **Standard Radius:** Elements like buttons and cards use a 0.5rem radius, giving them a soft, river-stone feel.
- **Large Components:** Hero sections and large image containers should utilize the `rounded-xl` (1.5rem) setting to emphasize the commitment to organic forms.
- **Custom Paths:** Where possible, use slightly imperfect, "hand-drawn" svg dividers for section transitions to reinforce the earthy aesthetic.

## Components

### Buttons
Primary buttons are styled in **Forest Green** with white text. They should feel solid and substantial. Secondary buttons use an **Earthy Brown** outline with a "pressed" tactile state. All buttons feature high-radius corners (level 2) to maintain the organic theme.

### Cards
Cards are the primary container for case studies and practice areas. They should have a subtle 1px border in a faded Earthy Brown and a background slightly darker than the page neutral. Apply a light grain texture exclusively to the card interior to distinguish it.

### Input Fields
Inputs should feel grounded. Use a thick bottom border or a soft, fully-rounded container. The focus state should transition the border color to Forest Green with a very soft, moss-colored outer glow.

### Chips & Tags
Used for categorizing legal topics (e.g., "Solar," "Litigation," "Water Rights"). These should be pill-shaped and use the Tertiary Moss Green with dark Forest Green text for high legibility and a natural look.

### Textural Elements
Incorporate "paper edge" dividers or subtle leaf-vein patterns in low-contrast background areas to further the connection to conservation without distracting from the professional legal content.