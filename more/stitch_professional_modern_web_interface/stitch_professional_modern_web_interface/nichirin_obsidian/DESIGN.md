# Design System Strategy: The Eternal Echo

## 1. Overview & Creative North Star
This design system is not a template; it is a cinematic experience. Our Creative North Star is **"The Eternal Echo"**—a visual bridge between the traditional, ink-washed aesthetics of the Taisho era and the hyper-modern, high-fidelity world of contemporary digital interfaces. 

To achieve a "pro" feel, we must move away from the "boxy" nature of standard web design. We will break the grid through **intentional asymmetry**, where character art and typography bleed across containers, and **tonal depth**, where elements are felt rather than outlined. This system treats the screen like an editorial manuscript—scholarly, immersive, and premium.

## 2. Colors: Obsidian & Blood
The palette is rooted in a high-contrast, dark-mode-first philosophy. We use obsidian blacks to provide an infinite canvas for the vibrant crimson accents.

### The "No-Line" Rule
**Explicit Instruction:** You are prohibited from using 1px solid borders for sectioning. Structural boundaries must be defined solely through background color shifts. 
- Use `surface-container-low` (#1C1B1B) to define a section against the `surface` (#131313) background.
- Use `surface-container-lowest` (#0E0E0E) for deep, recessed areas like footer sections or navigation bars.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers, like stacked sheets of frosted obsidian glass.
- **Level 1 (Base):** `surface` (#131313).
- **Level 2 (Section):** `surface-container-low` (#1C1B1B).
- **Level 3 (Component):** `surface-container-high` (#2A2A2A).
Each inner container should use a slightly higher or lower tier to define its importance, creating a "natural" lift without visual noise.

### The "Glass & Gradient" Rule
To elevate the "cinematic" vibe, floating elements (modals, dropdowns, sticky navs) must use **Glassmorphism**.
- **Fill:** Semi-transparent `surface-container-highest` (e.g., 60% opacity).
- **Effect:** `backdrop-blur` (20px to 40px).
- **CTA Soul:** Apply a subtle linear gradient from `primary` (#FFB3AD) to `primary_container` (#FF544E) at a 45-degree angle to give call-to-actions a "glowing" ember effect.

## 3. Typography: The Scholarly Script
We utilize a high-tension pairing of **Noto Serif** and **Inter** to reflect the "Modern/Traditional" dichotomy of the source material.

*   **Headlines (Display & Headline Scale):** Use **Noto Serif**. This font represents the historical, "manga" soul of the experience. It should be used for large, impactful statements.
*   **Body & Utility (Title, Body, & Label Scale):** Use **Inter**. This provides the "pro" functional clarity needed for a site with high information density.

**The Hierarchy Concept:**
- **Display-LG (3.5rem):** Set with -0.02em letter spacing for a dense, authoritative look.
- **Body-MD (0.875rem):** High line-height (1.6) to ensure long-form manga analysis remains readable and premium.
- **Labels:** Always in Inter, often in Uppercase with +0.05em tracking for a "technical" metadata feel.

## 4. Elevation & Depth
In this system, depth is achieved through **Tonal Layering** rather than structural shadows.

### The Layering Principle
Place a `surface-container-lowest` card on a `surface-container-low` section. This creates a "recessed" look that mimics a library archive. The transition should be so subtle that the user "feels" the depth change before they see it.

### Ambient Shadows
If an element must "float" (e.g., a manga chapter preview):
- **Blur:** Minimum 30px.
- **Opacity:** 6% to 10%.
- **Tint:** The shadow should not be black; use a tinted version of `on_surface` to mimic light interacting with a dark room.

### The "Ghost Border" Fallback
If accessibility requires a border, use a **Ghost Border**:
- **Token:** `outline-variant`.
- **Opacity:** 10–15% max.
- **Purpose:** It should only appear as a faint glimmer on the edge of a container.

## 5. Components

### Buttons: The "Katana" Strike
- **Primary:** Background `primary_container` (#FF544E), text `on_primary_container` (#5C0006). No border. Roundedness: `sm` (0.125rem) for a sharp, aggressive feel.
- **Secondary:** Transparent background, Ghost Border (15% `outline`), text `primary`.
- **States:** On hover, the primary button should "ignite" with a 10px box-shadow glow using the `primary` color.

### Chapter Cards: Editorial Layout
- **Construction:** Use `surface-container-high`. Forbid divider lines between title and meta-data.
- **Imagery:** Cards should feature a "Bleed" layout where the manga art covers 50% of the card, fading into the background via a gradient mask.
- **Typography:** `title-md` for the chapter name, `label-sm` for the "New" or "Hot" tags.

### Character Profiles (Signature Component)
- Utilize overlapping layers. The character image should break the top container boundary, while the text description sits on a glassmorphic panel (`surface-variant` at 40% opacity) that partially overlays the image.

### Input Fields
- **Background:** `surface-container-lowest`.
- **Active State:** A bottom-only border (2px) using `secondary` (#FFB77F) to signify the "breathing" state of the form.

## 6. Do’s and Don’ts

### Do:
- **Use Breathing Room:** Use the `spacing-xl` scale to separate major content blocks. High-end design thrives on "empty" space.
- **Respect the Mask:** Use subtle linear-gradient masks (100% to 0% opacity) on images to blend them into the obsidian background.
- **Micro-interactions:** Use "Ease-in-out" transitions (300ms) for all hover states to mimic the fluid movement of a swordsman.

### Don’t:
- **No 100% Opaque Borders:** Never use a solid, high-contrast line to separate content. It breaks the immersive, cinematic flow.
- **No Pure White Text for Body:** Use `on_surface` (#E5E2E1) for body text. Pure white (#FFFFFF) is reserved for "Display" headings to create a sharp, moonlight-like contrast.
- **No Standard Grids:** Avoid perfectly symmetrical 3-column layouts. Try a 2/3 and 1/3 split to create visual tension and an editorial feel.