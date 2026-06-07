---
name: Eco-Expedition
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#434842'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#737971'
  outline-variant: '#c3c8c0'
  surface-tint: '#4b644e'
  primary: '#18301d'
  on-primary: '#ffffff'
  primary-container: '#2e4632'
  on-primary-container: '#98b39a'
  inverse-primary: '#b2ceb3'
  secondary: '#805533'
  on-secondary: '#ffffff'
  secondary-container: '#fdc39a'
  on-secondary-container: '#794e2e'
  tertiary: '#2a2b28'
  on-tertiary: '#ffffff'
  tertiary-container: '#40413e'
  on-tertiary-container: '#aeada8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cdeace'
  primary-fixed-dim: '#b2ceb3'
  on-primary-fixed: '#08200f'
  on-primary-fixed-variant: '#344c38'
  secondary-fixed: '#ffdcc5'
  secondary-fixed-dim: '#f4bb92'
  on-secondary-fixed: '#301400'
  on-secondary-fixed-variant: '#653d1e'
  tertiary-fixed: '#e4e2dd'
  tertiary-fixed-dim: '#c8c6c2'
  on-tertiary-fixed: '#1b1c19'
  on-tertiary-fixed-variant: '#474744'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 64px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-lg:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '400'
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
  label-md:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  caption:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
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
  margin-mobile: 16px
  margin-desktop: 64px
  section-padding: 120px
---

## Brand & Style

This design system is anchored in the concept of "Lush & Grounded" luxury. It rejects the cold sterility of modern tech in favor of a tactile, heritage-inspired aesthetic that feels as enduring as the landscapes it promotes. The brand personality is that of an expert guide: sophisticated, calm, and deeply knowledgeable about the natural world.

The visual style utilizes a **Tactile Minimalism** approach. We leverage generous whitespace to signify luxury and breathing room, punctuated by rich, organic textures like recycled paper grain and subtle wood finishes. High-resolution photography is the centerpiece, treated as windows into the wild rather than mere decoration. The emotional response should be one of profound trust, quiet awe, and an immediate physical connection to the earth.

## Colors

The palette is derived directly from the safari environment. **Deep Moss Green** serves as our primary anchor, used for key actions and brand moments to represent the canopy and conservation. **Raw Wood Brown** is used for secondary accents, providing a sturdy, earth-bound warmth. 

The interface lives on a foundation of **Warm Off-White**, which provides a softer, more premium reading experience than pure white, mimicking sun-bleached linen or high-quality archival paper. Typography primarily utilizes a deep charcoal (Neutral) rather than true black to maintain the organic, low-strain visual harmony of the system.

## Typography

This design system employs a sophisticated typographic pairing to balance heritage with utility. **EB Garamond** is the voice of the brand—elegant, literary, and timeless. It is used for all major headings and display moments to evoke the feeling of a classic naturalist’s journal.

**Work Sans** provides the functional counterpoint. Chosen for its exceptional legibility in various lighting conditions (crucial for field use), it handles all body copy, navigation, and data points. Labels and small caps are given slight tracking (letter spacing) to enhance the "archival" feel of the interface while maintaining modern clarity.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model with expansive safe areas. We use a 12-column grid for desktop with a wide 64px outer margin to ensure the content feels centered and curated. 

A "Generous Breathing Room" rule applies: section vertical padding is intentionally high (120px+) to prevent the UI from feeling cluttered or rushed. Elements should be grouped using a strict 8px base unit, but global sections should prioritize asymmetrical compositions that mirror the unpredictability of nature.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering** and physical metaphors rather than synthetic shadows. 

1.  **Surface Tiers:** We use subtle variations of the off-white base to separate content. A slightly darker "sand" tint defines background containers.
2.  **Subtle Textures:** Backgrounds are never flat hex codes; they incorporate a microscopic noise texture to simulate recycled paper stock.
3.  **Low-Contrast Outlines:** Instead of heavy shadows, cards and inputs are defined by 1px borders in a muted version of the Raw Wood Brown (at 15-20% opacity).
4.  **Photography Depth:** Depth of field in images is used to pull the user’s eye into the screen, creating a layered effect without relying on UI shadows.

## Shapes

The shape language is **Organic and Soft**. We avoid clinical 90-degree angles in favor of a standard 0.5rem (8px) radius for most components. For larger feature cards or image containers, we use a more pronounced "Rounded-LG" (1rem) or even "Rounded-XL" (1.5rem) to mimic the smoothed edges of river stones or weathered wood. 

Interactive elements like "Book Now" buttons may use a pill-shape to contrast against the more structured content blocks, providing a clear, friendly call to action.

## Components

### Buttons
Primary buttons use the **Deep Moss Green** with white text. They should have a subtle grain overlay to feel like dyed canvas. Secondary buttons are outlined in **Raw Wood Brown** with a transparent background, emphasizing a lighter touch.

### Cards
Cards are the primary container for tour packages. They feature a full-bleed photograph at the top, a 1px "Wood" border, and the **Warm Off-White** background for the content area. Typography inside cards must follow a strict hierarchy to ensure legibility over the textured background.

### Input Fields
Inputs are minimalist, using only a bottom border in **Raw Wood Brown** to simulate a ledger or field notes book. Focus states are indicated by the border thickening slightly and changing to **Deep Moss Green**.

### Chips & Tags
Used for "Sustainable," "Limited Spots," or "Wildlife Type." These should have a very soft, organic feel—perhaps using slightly irregular border radii—and use desaturated earth tones to avoid distracting from the primary imagery.

### Additional Components
*   **The Progress Ledger:** A custom vertical stepper for itinerary views that looks like a hand-drawn timeline.
*   **Weather/Environment HUD:** A small, transparent widget providing real-time data from safari locations, using the clean Sans-Serif font for high utility.