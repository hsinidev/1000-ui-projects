---
name: Kindhearted Play
colors:
  surface: '#f6f9ff'
  surface-dim: '#d4dbe3'
  surface-bright: '#f6f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef4fd'
  surface-container: '#e8eef7'
  surface-container-high: '#e2e9f1'
  surface-container-highest: '#dce3ec'
  on-surface: '#151c22'
  on-surface-variant: '#414940'
  inverse-surface: '#2a3138'
  inverse-on-surface: '#ebf1fa'
  outline: '#717970'
  outline-variant: '#c0c9be'
  surface-tint: '#2f6a3f'
  primary: '#2f6a3f'
  on-primary: '#ffffff'
  primary-container: '#b2f2bb'
  on-primary-container: '#367044'
  inverse-primary: '#96d5a0'
  secondary: '#665f36'
  on-secondary: '#ffffff'
  secondary-container: '#efe3b0'
  on-secondary-container: '#6d653c'
  tertiary: '#75565f'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffd9e2'
  on-tertiary-container: '#7b5c65'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b2f2bb'
  primary-fixed-dim: '#96d5a0'
  on-primary-fixed: '#00210b'
  on-primary-fixed-variant: '#145129'
  secondary-fixed: '#efe3b0'
  secondary-fixed-dim: '#d2c796'
  on-secondary-fixed: '#211c00'
  on-secondary-fixed-variant: '#4e4721'
  tertiary-fixed: '#ffd9e2'
  tertiary-fixed-dim: '#e4bcc6'
  on-tertiary-fixed: '#2b151c'
  on-tertiary-fixed-variant: '#5b3f47'
  background: '#f6f9ff'
  on-background: '#151c22'
  surface-variant: '#dce3ec'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  touch-target-min: 44px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is built on the philosophy of "Professional Playfulness." It balances the clinical expertise required to gain parental trust with the whimsical, safe atmosphere necessary for a child’s comfort. The aesthetic draws from **Tactile Minimalism**, utilizing "squishy" UI elements that feel physical and approachable rather than cold and digital. 

The visual language incorporates soft, organic forms and friendly character mascots to guide the user through the interface. The emotional response should be one of "gentle encouragement"—reducing anxiety for both the child and the caregiver through a predictable, warm, and highly accessible environment.

## Colors

The palette is anchored by **Mint (#B2F2BB)** and **Sunny Yellow (#FFF3BF)** to evoke feelings of growth, safety, and optimism. These are supplemented by a soft coral-pink tertiary color for accents and call-to-actions that require warmth without being aggressive. 

The background utilizes off-whites and extremely light creams to reduce glare and provide a "paper-like" softness. Darker neutral tones are reserved strictly for typography to maintain AAA accessibility standards against the pastel backgrounds.

## Typography

Typography in this design system prioritizes legibility and approachability. **Plus Jakarta Sans** is used for headings; its modern, rounded terminals feel friendly and non-threatening. For all functional text, **Lexend** is employed. Designed specifically to reduce visual stress and improve reading proficiency, Lexend’s generous character spacing is ideal for both young readers and busy parents.

Headlines should always use sentence case to maintain a conversational and humble tone. Line heights are kept generous to prevent the UI from feeling "cramped" or overwhelming.

## Layout & Spacing

This design system utilizes a **fluid grid** with an emphasis on large safe areas to accommodate motor-skill variations in children. A strict 8px rhythm governs the vertical stack, while the layout itself uses wide gutters (24px) to ensure elements do not feel cluttered.

The "Touch-First" rule is mandatory: no interactive element should be smaller than 44x44px. Information is presented in "digestible chunks" using wide margins and significant vertical whitespace (stack-lg) to separate different activities or topics.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and tonal layering. Rather than sharp, high-contrast shadows, this system uses ultra-diffused drops shadows (Blur: 20px+, Opacity: 8-12%) tinted with a hint of the brand colors (e.g., a soft mint-tinted shadow).

Interactive elements like buttons use a dual-shadow approach to create a "squishy," tactile feel—giving the impression that the button can be physically pressed into the screen. Cards use a single low-elevation tier to separate them from the background without creating a "floating" or disconnected effect.

## Shapes

The shape language is defined by extreme **pill-shaped** roundedness. Sharp corners are entirely avoided to reinforce the "soft and safe" brand promise. 

Standard containers use a minimum radius of 24px, while buttons and chips are fully pill-shaped. Mascots and icons should follow this organic geometry, avoiding any harsh angles or aggressive points. This creates a cohesive visual rhythm that feels consistent with toys and children’s play equipment.

## Components

### Buttons
Buttons are large and chunky. They feature a 4px bottom border (slightly darker than the fill color) to provide a 3D tactile effect. Icons are always included within primary buttons to assist non-readers.

### Navigation
The navigation is icon-centric. For children's interfaces, use a simplified bottom bar with oversized, colorful icons and no more than three choices. For the parental portal, navigation expands to include clear text labels in Lexend.

### Cards
Cards are the primary container for content. They use a white fill with a subtle 2px Mint or Yellow stroke rather than a heavy shadow. This keeps the interface feeling light and airy.

### Input Fields
Inputs are oversized with a 16px internal padding. Focus states are indicated by a thick (3px) Sunny Yellow glow, making it unmistakably clear where the user is currently typing or clicking.

### Progress Indicators
Instead of standard bars, use "pathway" indicators where a mascot moves from left to right, turning an abstract progress metric into a visual journey.