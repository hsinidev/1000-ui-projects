---
name: Platinum Archive
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
  on-surface-variant: '#c4c7c4'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e918e'
  outline-variant: '#444845'
  surface-tint: '#c7c6c4'
  primary: '#ffffff'
  on-primary: '#303130'
  primary-container: '#e3e2e0'
  on-primary-container: '#646463'
  inverse-primary: '#5e5e5d'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#ffffff'
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3e2e0'
  primary-fixed-dim: '#c7c6c4'
  on-primary-fixed: '#1b1c1b'
  on-primary-fixed-variant: '#464746'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display:
    fontFamily: metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-sm:
    fontFamily: geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-edge: 40px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

The visual identity of this design system is rooted in the concepts of "Fortress" and "Gallery." It balances the heavy, immovable security required for high-value logistics with the airy, curated sophistication of a world-class museum. The aesthetic is Minimalist-Refined, stripping away unnecessary ornamentation to focus on the objects of value themselves.

The user experience must feel exclusive and impenetrable. We achieve this through a glassmorphic interface strategy where "layers of protection" are literal: frosted surfaces, razor-thin borders, and deep optical blurs. This creates a sense of depth and physical presence, suggesting that the data—like the assets—is encased in a state-of-the-art containment system.

## Colors

This design system utilizes a restricted, high-contrast palette to evoke prestige. 

- **Matte Black (#1A1A1A):** Used as the foundational surface color. It represents the "vault"—a deep, secure environment.
- **Stark White (#FFFFFF):** Reserved for primary typography and essential iconography to ensure maximum legibility and "clinical" cleanliness.
- **Platinum (#E5E4E2):** Used as the primary accent and for structural elements. It provides a metallic, cool-toned contrast to the black surfaces, signifying the high-value nature of the cargo.

Functional colors (Success, Warning, Error) should be used sparingly and desaturated to maintain the elite aesthetic, ensuring they do not disrupt the museum-grade neutrality of the interface.

## Typography

The typographic system relies on architectural precision. **Metropolis** is utilized for headlines; its geometric construction mirrors the structural integrity of high-end vaults. It should be typeset with tight tracking in larger sizes to feel impactful and modern.

**Geist** is used for all body copy and technical labels. Its monospaced-influenced clarity provides a "manifest" or "documentary" feel, essential for logistics and security tracking. Use uppercase labels with generous letter spacing for metadata and status indicators to maintain an organized, cataloged appearance.

## Layout & Spacing

This design system employs a **fixed grid** layout within a centered container to mimic the framed presentation of fine art. The 12-column grid is reinforced by generous exterior margins (40px+) to create a "gallery wall" effect, where content is given significant room to breathe.

Spacing follows a strict 8px rhythmic scale. Vertical rhythm should favor larger gaps (64px+) between major sections to prevent the interface from feeling cluttered or "cheap." Alignment should be predominantly left-aligned to reflect professional manifests, with occasional centered displays for hero moments or authentication screens.

## Elevation & Depth

Hierarchy is established through transparency and optical thickness rather than traditional drop shadows.

- **Surface Level:** Matte Black (#1A1A1A).
- **Glass Level (Floating):** Background blur (24px to 40px) with a 10% opacity Stark White fill. This layer represents a "protective casing."
- **Borders:** Every glass element must have a 1px solid border in Platinum (#E5E4E2) at 20% opacity. This "whisper-thin" line defines the boundaries of security.
- **Interaction Depth:** When an item is focused, the backdrop blur increases and the border opacity rises to 50%, "illuminating" the object of interest.

## Shapes

The shape language is "Soft-Precision." We avoid sharp 0px corners to prevent a purely industrial/brutalist look, instead using a subtle 0.25rem (4px) radius. This small radius conveys that the interface is engineered and machined rather than organic.

Containers and cards should maintain this consistent, subtle rounding. Interactive elements like buttons and input fields should strictly adhere to the same corner radius to maintain a unified "kit-of-parts" feel.

## Components

### Buttons
Primary buttons use a solid Platinum (#E5E4E2) background with Matte Black text. Secondary buttons are "Ghost" style: transparent background, 1px Platinum border, and White text. All buttons feature a 1.5s transition on hover where the border brightness subtly increases.

### Input Fields
Inputs are represented as simple Platinum underlines or very faint glassmorphic wells. Labels always sit above the input in the `label-sm` style (uppercase, tracked out). Focus states are indicated by the underline expanding or the glass border increasing in opacity.

### Cards & Containers
Cards are the primary expression of glassmorphism. They should never have a solid background. They rely on the `backdrop-filter: blur()` property to separate themselves from the Matte Black base. Use these for asset manifests, shipping details, and insurance certificates.

### Status Indicators
Security status (e.g., "In Transit," "Secured," "Vaulted") should be displayed in small, high-contrast badges. These use the `label-sm` typography and are encased in a thin Platinum border.

### Inventory Lists
Lists of high-value assets should resemble auction catalogs: high-quality image thumbnails, followed by structured Geist-font metadata. Use subtle Platinum dividers (0.5px thickness) to separate items.