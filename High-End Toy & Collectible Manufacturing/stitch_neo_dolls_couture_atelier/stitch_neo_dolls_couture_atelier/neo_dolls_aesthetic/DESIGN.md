---
name: Neo-Dolls Aesthetic
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#544243'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#877273'
  outline-variant: '#dac1c2'
  surface-tint: '#97444e'
  primary: '#2d0008'
  on-primary: '#ffffff'
  primary-container: '#4e0b19'
  on-primary-container: '#d0717b'
  inverse-primary: '#ffb2b8'
  secondary: '#7a5646'
  on-secondary: '#ffffff'
  secondary-container: '#fecdb9'
  on-secondary-container: '#795545'
  tertiary: '#0f1112'
  on-tertiary: '#ffffff'
  tertiary-container: '#242626'
  on-tertiary-container: '#8c8d8d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdadb'
  primary-fixed-dim: '#ffb2b8'
  on-primary-fixed: '#3f010f'
  on-primary-fixed-variant: '#792d38'
  secondary-fixed: '#ffdbcd'
  secondary-fixed-dim: '#ecbca9'
  on-secondary-fixed: '#2e1509'
  on-secondary-fixed-variant: '#603f30'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 72px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

The design system is rooted in the world of haute couture and fine art collectables. It targets a discerning audience of collectors and fashion enthusiasts who value craftsmanship, exclusivity, and avant-garde aesthetics. The emotional response should be one of "aspirational quietude"—a sense of entering a high-end gallery where the interface recedes to let the artistry of the dolls command the spotlight.

The style is a synthesis of **High-Contrast Minimalism** and **Editorial Luxe**. It leverages vast expanses of whitespace to create "breathing room" for high-performance imagery. Unlike traditional retail, the interface prioritizes a cinematic feel, using thin structural lines and subtle metallic finishes to mirror the premium materials used in the dolls themselves.

## Colors

The palette is anchored by **Deep Burgundy**, used for primary actions and core typography to provide a sense of weight and heritage. **Crisp White** serves as the primary canvas, ensuring a high-fashion editorial clarity. 

**Rose Gold** is reserved strictly for high-value accents, highlights, and subtle gradients. It should be used sparingly—on hover states, small icons, or thin borders—to maintain its status as a luxury signifier. Neutral greys are largely avoided in favor of varying densities of Burgundy or soft off-whites to keep the temperature of the design warm and sophisticated.

## Typography

This design system utilizes **Noto Serif** for all editorial headings to evoke the timeless authority of a fashion magazine masthead. High-level displays should use the Light (300) weight to emphasize elegance and precision.

For functional text and long-form descriptions, **Inter** provides a clean, neutral counterpoint. Its utilitarian nature ensures that technical doll specifications remain legible. **Label-sm** styles must always be rendered in uppercase with increased letter-spacing to function as architectural markers within the layout.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop, centered within a generous margin-edge of 64px. A 12-column system is used, but content should frequently span 6 or 8 columns to create asymmetrical, editorial-style compositions.

Generous vertical spacing (section-gaps) is mandatory to prevent the "clutter" common in standard e-commerce. Use white space as a structural element to separate different "collections" or "chapters" of the doll's narrative.

## Elevation & Depth

This design system avoids traditional drop shadows in favor of **Tonal Layers** and **Low-Contrast Outlines**. 

- **Depth:** Conveyed through the layering of images over text or the use of 1px Deep Burgundy or Rose Gold borders. 
- **Glassmorphism:** Apply a subtle backdrop blur (12px to 20px) on navigation bars and floating modals to maintain a sense of the high-performance imagery sitting beneath the UI.
- **Interactions:** Depth is expressed through scale (e.g., an image subtly expanding on hover) rather than elevation (shadows).

## Shapes

The shape language is strictly **Sharp (0px)**. Rectilinear forms reinforce the sophisticated, architectural nature of the brand. Every button, input field, and card container must have 90-degree corners. This sharpness contrasts with the organic, soft curves of the doll photography, framing the art with professional precision.

## Components

**Buttons**
Primary buttons are solid Deep Burgundy with white text. Secondary buttons use a 1px Rose Gold border with a transparent background. All buttons are rectangular with no corner radius. On hover, the primary button should transition to a Rose Gold gradient.

**Input Fields**
Inputs are defined by a single 1px bottom border in Deep Burgundy. The label sits above in the `label-sm` style. Validation errors should be shown in a muted version of the primary color, never a bright "system red."

**Cards**
Doll cards should be borderless, utilizing the full width of their grid container. The image is the primary element, with typography (Name and Collection) placed below in a centered, minimal stack.

**Image/Video Integration**
Images should always use `object-fit: cover`. Video backgrounds in hero sections should be desaturated by 10% to ensure that the Burgundy text overlays remain legible and pass accessibility standards.

**Chips/Tags**
Used for "Limited Edition" or "Sold Out" status. These should be 1px Deep Burgundy boxes with `label-sm` text, positioned as an absolute overlay in the top-right corner of image containers.