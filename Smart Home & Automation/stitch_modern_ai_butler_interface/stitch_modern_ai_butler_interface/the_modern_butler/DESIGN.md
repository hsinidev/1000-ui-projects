---
name: The Modern Butler
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#444650'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#775a19'
  on-secondary: '#ffffff'
  secondary-container: '#fed488'
  on-secondary-container: '#785a1a'
  tertiary: '#121515'
  on-tertiary: '#ffffff'
  tertiary-container: '#272929'
  on-tertiary-container: '#8f9090'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  button:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 24px
  margin-desktop: 64px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  stack-xl: 64px
---

## Brand & Style

The design system is anchored in the concept of "Invisible Excellence." It targets a discerning audience that values time, precision, and understated luxury. The UI must feel like a white-glove service—proactive yet unobtrusive, sophisticated yet remarkably simple to navigate.

The aesthetic follows a **Minimalist Luxury** movement. It eschews the clutter of traditional dashboards in favor of an editorial layout. By prioritizing "negative space" as a functional element rather than a void, the design system ensures that every user interaction feels deliberate and calm. The visual language utilizes thin architectural lines and a restricted color palette to evoke the feeling of a high-end concierge desk or a private members' club.

## Colors

The color palette is a study in classic prestige and cleanliness.

- **Primary (Royal Blue):** Used for core navigation, primary actions, and brand presence. It represents authority, stability, and intelligence.
- **Secondary (Gold):** Used sparingly as an accent for focus states, thin decorative borders, and premium indicators. It adds a layer of warmth and exclusivity.
- **Background (White):** The canvas is pure and expansive, ensuring that the AI’s suggestions remain the focal point.
- **Tertiary (Silk Grey):** A very light, cool-toned grey used for subtle section dividers and surface layering without breaking the minimalist aesthetic.

## Typography

This design system employs a pairing that balances heritage with modernity. 

**Noto Serif** is reserved for headlines and editorial moments. Its classic proportions convey the wisdom and reliability of a seasoned butler. **Manrope** is used for all functional text, body copy, and UI labels. Its geometric yet refined structure ensures high legibility on screens while maintaining a premium, tech-forward feel. 

Strict attention should be paid to the `label-caps` style, which should be used for category headers and small metadata to provide a structured, organized hierarchy.

## Layout & Spacing

The layout philosophy relies on a **fixed grid** with exaggerated margins to create a sense of focus. 

The system uses an 8px base grid. For desktop views, a 12-column grid is utilized with a maximum container width of 1200px. High-end design is often defined by what is *not* there; therefore, vertical rhythm should favor `stack-xl` (64px) between major sections to allow the interface to "breathe." Content should be centered to create a balanced, symmetrical composition that feels stable and reliable.

## Elevation & Depth

Hierarchy is established through **tonal layers** and **ambient shadows** rather than heavy fills.

- **Surface Layering:** The primary background is white. Secondary surfaces (like cards or sidebars) use a subtle Silk Grey (#F9F9F9) to denote a different functional area.
- **Shadows:** Use extremely diffused, low-opacity shadows. The shadow color should be tinted with a hint of Royal Blue (e.g., `rgba(0, 35, 102, 0.04)`) to maintain color harmony and avoid a "muddy" appearance.
- **Gold Accents:** Use 1px Gold (#C5A059) strokes to define the edges of active elements or premium cards. These lines should feel like delicate threads, providing definition without adding visual weight.

## Shapes

The shape language is **Soft (Level 1)**. 

While the system is modern, "pill-shaped" or overly rounded elements are avoided as they can appear too casual. Small radius corners (4px for standard components, 8px for cards) provide a professional, tailored look reminiscent of high-end stationery or architectural detailing. Sharp corners are avoided to ensure the assistant feels approachable and "human," but the curves remain disciplined and subtle.

## Components

### Buttons
Primary buttons use a solid Royal Blue fill with white Manrope text. Secondary buttons are "ghost" style with a 1px Gold border and Gold text. Interactions should be subtle—a slight deepening of color rather than a dramatic shift.

### Cards
Cards should be used to present AI suggestions or "concierge briefs." They feature a white background, a very soft ambient shadow, and a 1px Silk Grey border. A thin Gold line at the very top of a card can denote a "VIP" or "Urgent" status.

### Input Fields
Inputs are minimalist, utilizing only a bottom border that transitions from Silk Grey to Royal Blue upon focus. The placeholder text should be Manrope in a light grey, suggesting a quiet invitation to converse.

### Chips & Tags
Used for categories like "Schedule," "Travel," or "Lifestyle." These are small, rectangular with a 2px radius, using a Silk Grey background and dark navy text to remain unobtrusive.

### Concierge Feed
A specialized component for the AI assistant's communication. AI messages are distinguished by a subtle Silk Grey background, while user messages remain in plain text against the white background, emphasizing the assistant's supportive role.