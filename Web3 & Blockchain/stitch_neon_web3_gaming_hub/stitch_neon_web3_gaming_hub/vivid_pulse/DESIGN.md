---
name: Vivid Pulse
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#fface8'
  on-secondary: '#5e0053'
  secondary-container: '#ff24e4'
  on-secondary-container: '#520049'
  tertiary: '#f9f5f5'
  on-tertiary: '#313030'
  tertiary-container: '#dcd9d8'
  on-tertiary-container: '#605f5e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#ffd7f0'
  secondary-fixed-dim: '#fface8'
  on-secondary-fixed: '#3a0033'
  on-secondary-fixed-variant: '#840076'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 20px
  lg: 32px
  xl: 48px
  touch-target-min: 48px
  safe-margin: 20px
---

## Brand & Style

This design system targets high-performance Web3 gamers and asset collectors. The brand personality is aggressive, high-energy, and futuristic, evoking the sensation of a high-end gaming console's dashboard. It focuses on the "thrill of the win" and the "prestige of ownership."

The style is a fusion of **Glassmorphism** and **High-Contrast / Bold** aesthetics. It utilizes deep matte foundations to allow neon accents and translucent surfaces to pop. Overlapping elements and "broken" layouts create a sense of depth and motion, moving away from traditional static grids toward a dynamic, layered interface.

## Colors

The palette is anchored by a deep **Matte Black** (#080808) to provide maximum contrast for the high-intensity neon colors. **Electric Blue** (#00F0FF) serves as the primary action and utility color, representing technology and "the grid." **Hot Pink** (#FF00E5) is the secondary accent, reserved for high-value rewards, rare assets, and "earn" moments.

A "Surface Black" (#121212) is used for container backgrounds to distinguish them from the base canvas. All primary and secondary colors should be implemented with a corresponding glow (bloom) effect to simulate a hardware-emitted light source.

## Typography

This design system uses a triple-font approach to balance futurism, readability, and athletic performance. 

- **Space Grotesk** is the voice of the system, used for large headlines and "hero" stats. Its geometric quirks reinforce the tech-heavy theme.
- **Be Vietnam Pro** provides a contemporary, friendly warmth for body text and long-form asset descriptions, ensuring the Web3 complexity remains approachable.
- **Lexend** is utilized for labels, buttons, and data-heavy tables. Its athletic, wide-set nature improves legibility in high-stakes gaming environments.

## Layout & Spacing

The layout philosophy follows a **Mobile-First Game Launcher** model. It ignores standard document grids in favor of a **Layered Dynamic Layout**. Elements should frequently overlap—for example, a character card might "break out" of its container, or a floating action menu might sit atop a blurred background.

Spacing is generous to accommodate large touch-targets. Use a safe-area margin of 20px on the horizontal axis for mobile devices. Vertical rhythm should be driven by the 8px base unit, but significant sections should be separated by "XL" spacing to give elements room to "breathe" amidst the high-contrast colors.

## Elevation & Depth

Depth in this design system is created through **Glassmorphism** and **Neon Bloom**. 

1.  **The Canvas:** Deepest layer, solid Matte Black.
2.  **Backdrop Layers:** Semi-transparent dark surfaces with a 20px - 40px background blur. These surfaces should have a 1px inner border (stroke) using a low-opacity Electric Blue to define the edges.
3.  **Active Elements:** Elements "glow" onto the layers beneath them. Higher elevation is signaled by more intense "neon bloom" (outer glows) rather than traditional drop shadows.
4.  **Parallax:** As the user scrolls, overlapping cards should move at slightly different speeds to emphasize the physical depth of the "launcher" style interface.

## Shapes

The shape language is **Rounded but Aggressive**. A standard 0.5rem (8px) radius is used for small UI components, but large cards and "hero" containers should use a 1.5rem (24px) radius. 

To reinforce the gaming aesthetic, use 45-degree angled "beveled" clips on the top-right or bottom-left corners of primary buttons and status badges. This "tech-cut" shape differentiates the system from standard corporate interfaces.

## Components

- **Buttons:** Large, high-profile targets. Primary buttons use a solid Electric Blue fill with black text and a matching outer glow. Secondary buttons use a transparent background with a 2px Hot Pink border. Use the "beveled" corner style for all high-level actions.
- **Asset Cards:** Use high-blur glassmorphism backgrounds. The NFT or game asset should overlap the top edge of the card. A "Glow-Grip" indicator (a neon line) should appear on the side of the card when it is interactable.
- **Chips/Badges:** Small, pill-shaped elements with Lexend Bold typography. Use a Hot Pink background for "Earn" or "Live" status, and Electric Blue for "Level" or "Category."
- **Input Fields:** Bottom-border only or fully enclosed with a faint 1px Electric Blue outline. When focused, the outline should glow and the label should shift to the Hot Pink secondary color.
- **Navigation:** A floating bottom bar using a heavy glassmorphism effect. Icons should be neon-line art; the active icon receives a circular glow behind it.
- **Progress Bars:** Segmented bars (resembling a battery or energy meter) rather than a smooth continuous line. Filled segments should pulse slightly when active.