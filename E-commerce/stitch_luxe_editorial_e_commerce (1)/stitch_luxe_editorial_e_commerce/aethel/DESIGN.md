---
name: Aethel
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#4c4546'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#5e5e5d'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfde'
  on-secondary-container: '#626361'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c1c17'
  on-tertiary-container: '#85847d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c5'
  on-secondary-fixed: '#1a1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e5e2da'
  tertiary-fixed-dim: '#c8c6bf'
  on-tertiary-fixed: '#1c1c17'
  on-tertiary-fixed-variant: '#474741'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-xl:
    fontFamily: Newsreader
    fontSize: 120px
    fontWeight: '600'
    lineHeight: 110px
    letterSpacing: -0.04em
  display-lg:
    fontFamily: Newsreader
    fontSize: 80px
    fontWeight: '500'
    lineHeight: 84px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '500'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 32px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 28px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.15em
spacing:
  margin-page: 4rem
  gutter-grid: 1.5rem
  stack-xl: 10rem
  stack-lg: 6rem
  stack-md: 3rem
  stack-sm: 1.5rem
---

## Brand & Style

This design system is built upon the principles of **High-Fashion Editorial Minimalism**. It targets a discerning, luxury-oriented audience that values curation over clutter and substance over flash. The emotional response is one of exclusivity, architectural stillness, and timeless authority.

The aesthetic draws from mid-century Swiss modernism and contemporary avant-garde magazine layouts. It prioritizes the "void"—using generous whitespace not as empty space, but as a luxury asset that frames and elevates high-resolution photography. The interface acts as a quiet gallery, ensuring that the garments and brand imagery remain the focal point.

## Colors

The palette is anchored in a sophisticated, monochromatic spectrum to maintain a high-fashion editorial feel.

- **Primary (Ink Black):** Used for oversized typography and structural elements to provide a heavy, grounded contrast against the light background.
- **Secondary (Bone/Off-White):** The canvas color. A soft, warm-toned white that feels more expensive and "tactile" than a sterile digital white.
- **Tertiary (Warm Grey):** A subtle neutral for dividers, borders, and secondary UI elements that need to recede.
- **Neutral (Slate):** Used for body text and descriptive labels to ensure high legibility without the harshness of pure black.

Functional colors (success, error) should be used sparingly and desaturated to avoid breaking the minimalist harmony.

## Typography

The typographic strategy utilizes **Newsreader** for headings to evoke the heritage and authority of traditional print media. It is scaled aggressively to create "High-Impact" focal points. Large display sizes should use tighter tracking and heavier weights to feel structural.

**Inter** provides a clean, utilitarian counterpoint for body copy and navigational elements. By using a highly legible sans-serif for functional text, the design system maintains modern usability standards within a classic editorial framework. All labels should be set in uppercase with increased letter spacing to denote a premium, curated feel.

## Layout & Spacing

This design system employs a **Fixed 12-Column Grid** with extreme internal margins. The layout philosophy is "asymmetric balance." Content should not always fill the horizontal span; instead, use offset columns to create visual interest similar to a magazine spread.

- **Margins:** Oversized page margins (64px+) ensure the content feels "contained" and precious.
- **Vertical Rhythm:** Large "Stack" units (10rem+) are used between sections to allow the eye to rest and to signal a change in narrative.
- **Photography:** Images should frequently break the grid or bleed to the edge of the viewport to create impact.

## Elevation & Depth

To maintain a flat, editorial aesthetic, this design system avoids traditional drop shadows and blurs. Depth is communicated through **Tonal Layering** and **Compositional Overlap**.

- **Flat Planes:** Elements exist on a single flat plane. Use subtle variations in background color (Bone vs. White) to define separate zones.
- **Overlays:** Text may overlap photography using high-contrast color shifts (White text on dark areas of an image) to create a sense of physical layering without using shadows.
- **Hairline Borders:** Use 1px solid lines in the Tertiary color to define boundaries where necessary. These should feel like "pencil lines" on a draft.

## Shapes

The shape language is strictly **Sharp (0px)**. Rounded corners are avoided to maintain an architectural, precise, and high-fashion feel. Square edges convey a sense of discipline and formality consistent with luxury branding. 

Buttons, image containers, and input fields must all adhere to a 90-degree corner radius. This rigidity acts as a frame for the more organic shapes found within the photography (e.g., fabric drapes, human forms).

## Components

Components in this design system are intentionally understated, acting as functional footnotes to the visual content.

- **Buttons:** Primary buttons are solid black rectangles with centered white uppercase labels. Secondary buttons are "Ghost" style with a 1px black border. Transitions should be an instantaneous or very fast opacity shift.
- **Inputs:** Minimalist underlines or 1px boxed frames. No background fills. Placeholder text should be in the Neutral Slate color.
- **Cards:** For product listings, cards should have no borders or shadows. The image is the card. Text (Title/Price) is placed below in a simple, left-aligned stack with ample breathing room.
- **Navigation:** A persistent but thin top bar. Use the `label-caps` style for menu items. Hide complex navigation behind a "Menu" label to keep the viewport clean.
- **Chips/Tags:** Small, rectangular boxes with 1px borders. Use sparingly for "New Arrival" or "Limited Edition" status.
- **Image Carousels:** Use simple "Previous / Next" text links or thin arrows instead of bulky dots or heavy navigation bars.