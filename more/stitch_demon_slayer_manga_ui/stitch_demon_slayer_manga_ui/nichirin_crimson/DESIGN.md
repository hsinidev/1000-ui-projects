# Design System Specification: The Breath of Ink & Shadow

## 1. Overview & Creative North Star: "Atmospheric Editorial"
The North Star for this design system is **"The Digital Scroll."** Unlike traditional grid-heavy manga sites that feel like cluttered databases, this system treats every screen as a high-end editorial experience. We are moving away from the "app-like" feel and toward a "cinematic" atmosphere.

To achieve this, the design system utilizes **Intentional Asymmetry** and **Tonal Depth**. Elements should feel like they are floating in a dark, misty void, inspired by the atmospheric backgrounds of *Demon Slayer*. We break the "template" look by using oversized typography, overlapping image containers that break the grid, and a strict "No-Line" policy to ensure the interface feels organic and fluid.

## 2. Color & Atmospheric Surface Layering
This system uses a "Depth-First" approach to UI. We do not use borders to define space; we use light and shadow.

### The Palette
- **Background (`#131313`)**: Our deep, ink-wash base.
- **Primary Crimson (`#ffb3ac` / `#d32f2f`)**: Used for "Total Concentration" moments—actions of high importance and violent motion.
- **Secondary Teal (`#84d5c5` / `#00685b`)**: Represents the calm of the water surface. Used for secondary navigation and utility.
- **Tertiary Gold (`#ffba38`)**: Reserved for "Legendary" or premium highlights.

### The "No-Line" Rule
**Strict Mandate:** Designers are prohibited from using 1px solid borders for sectioning. 
- Define boundaries solely through background shifts. For example, a `surface-container-low` reader settings panel should sit atop the `surface` background without a stroke.
- Use **Vertical Rhythm** and white space to imply containment rather than physical boxes.

### Surface Hierarchy & Nesting
Treat the UI as physical layers of "Washi" paper stacked in the dark.
- **Level 1 (Base):** `surface` (#131313) for the main canvas.
- **Level 2 (Sectioning):** `surface-container-low` (#1c1b1b) for large content areas.
- **Level 3 (Interactive):** `surface-container-high` (#2a2a2a) for cards and floating menus.
- **Level 4 (Prominence):** `surface-bright` (#3a3939) for active states or elevated modals.

### The "Glass & Gradient" Rule
To mimic the "breath" effects of the source material, use **Glassmorphism**. Floating navigation bars should use `surface` at 70% opacity with a 20px `backdrop-blur`. Main CTAs should utilize a subtle linear gradient from `primary` to `primary_container` at a 135-degree angle to provide a sense of directional energy.

## 3. Typography: The Calligrapher’s Contrast
We pair the geometric precision of **Plus Jakarta Sans** with the high-impact, editorial weight of **Epilogue**.

- **Display (Epilogue):** Massive, high-contrast headings (`display-lg` at 3.5rem). These should often be placed with negative letter-spacing (-0.02em) to feel like title cards.
- **Headlines (Epilogue):** Used for manga titles and chapter names. It conveys authority and "The Blade."
- **Body (Plus Jakarta Sans):** The "Modernist" counterpoint. Its clean, open apertures ensure that even after hours of reading, eye strain is minimized.
- **Label (Plus Jakarta Sans):** Used for metadata (e.g., "Updated 2h ago"). These should always be in `label-md` or `label-sm` to maintain a clear hierarchy against the bold headlines.

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are too "software-like." We use **Ambient Gloom**.

- **The Layering Principle:** Depth is achieved by "stacking" the surface tokens. A `surface-container-lowest` card placed on a `surface-container-low` section creates a "sunken" effect, perfect for secondary feed items.
- **Ambient Shadows:** For floating elements (Modals/Popovers), use a shadow color tinted with the primary hue: `rgba(147, 0, 10, 0.08)` with a 40px blur. This makes the shadow feel like a "glow" or "aura" rather than a grey drop-shadow.
- **Ghost Border Fallback:** If accessibility requires a container edge, use the `outline_variant` token at **15% opacity**. Never use a 100% opaque border.

## 5. Components: The Martial Toolkit

### Buttons (The "Strike")
- **Primary:** Gradient fill (`primary` to `primary_container`). `0.25rem` (DEFAULT) roundedness. No border. Text is `on_primary_fixed`.
- **Secondary:** Ghost style. No fill, `outline` at 20% opacity. On hover, the background transitions to `surface_container_highest`.

### Cards & Manga Tiles
- **The Rule of No Dividers:** Use `surface_container_low` for the card background. Use 24px of padding (Spacing Scale) to separate the title from the metadata.
- **The "Overhang" Effect:** Allow the manga cover art to slightly overlap the card's top edge (negative margin) to break the "boxed" layout feel.

### Input Fields
- Underline style only. Use `outline_variant` for the default state. On focus, the underline transforms into a `primary` color glow. Avoid full-box inputs to keep the "Editorial" feel.

### Reader Controls (The "Breath" Overlay)
- Use `surface_container_highest` with 80% opacity and `backdrop-blur`. Components inside (sliders, toggles) should use `secondary` (Teal) to signify "utility" and differentiate from "action" (Red).

### Navigation (The "Path")
- Top navigation is transparent until scroll. Upon scroll, it transitions to `surface_container_lowest` with a 10% `outline_variant` bottom "Ghost Border."

## 6. Do's and Don'ts

### Do:
- **Do** use asymmetrical margins. If the left margin is 48px, try a 64px right margin for hero sections to create visual tension.
- **Do** use `tertiary` (Gold) sparingly—only for "New" badges or "Legendary" tier content.
- **Do** prioritize the artwork. The UI should feel like a frame, not the main event.

### Don't:
- **Don't** use pure white (#FFFFFF). Use `on_surface` (#e5e2e1) to protect the user's eyes in dark environments.
- **Don't** use standard "Material" shadows. If it looks like a standard Google app, it has failed the "Editorial" test.
- **Don't** use 1px dividers to separate list items. Use 16px of vertical space and a 2% background shift instead.