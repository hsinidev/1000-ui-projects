---
name: Léxico Moderno
colors:
  surface: '#f5fbf5'
  surface-dim: '#d5dcd6'
  surface-bright: '#f5fbf5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff5ef'
  surface-container: '#e9efe9'
  surface-container-high: '#e4eae4'
  surface-container-highest: '#dee4de'
  on-surface: '#171d19'
  on-surface-variant: '#3d4a42'
  inverse-surface: '#2c322e'
  inverse-on-surface: '#ecf2ec'
  outline: '#6d7a72'
  outline-variant: '#bccac0'
  surface-tint: '#006c4a'
  primary: '#006948'
  on-primary: '#ffffff'
  primary-container: '#00855d'
  on-primary-container: '#f5fff7'
  inverse-primary: '#68dba9'
  secondary: '#904d00'
  on-secondary: '#ffffff'
  secondary-container: '#fe932c'
  on-secondary-container: '#663500'
  tertiary: '#4f5d71'
  on-tertiary: '#ffffff'
  tertiary-container: '#67758b'
  on-tertiary-container: '#fdfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#85f8c4'
  primary-fixed-dim: '#68dba9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#005137'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#ffb77d'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6e3900'
  tertiary-fixed: '#d5e3fc'
  tertiary-fixed-dim: '#b9c7df'
  on-tertiary-fixed: '#0d1c2e'
  on-tertiary-fixed-variant: '#3a485b'
  background: '#f5fbf5'
  on-background: '#171d19'
  surface-variant: '#dee4de'
typography:
  titulo-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  titulo-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  letra-grid:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '800'
    lineHeight: '1'
  cuerpo-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.5'
  teclado-label:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
  etiqueta-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  grid-gap: 8px
  container-padding: 24px
  keyboard-gap: 6px
  section-margin: 32px
---

## Brand & Style
The design system is rooted in a "Modern Corporate" aesthetic that leans into high-fidelity polish and intellectual play. It is designed for a sophisticated Spanish-speaking audience that values both linguistic challenge and aesthetic refinement. The brand personality is poised, vibrant, and premium, avoiding the flat "gamey" look of traditional puzzle apps in favor of a lifestyle-oriented interface. 

The visual direction uses a mix of deep tonal layers and subtle skeuomorphism—specifically soft, ambient shadows and tactile transitions—to make the game tiles feel like physical objects on a digital surface. The interface evokes a sense of calm focus through generous whitespace and a disciplined color application.

## Colors
The palette is built around three semantic pillars that define the Spanish Wordle experience: **Esmeralda (Correcto)**, **Ámbar (Presente)**, and **Pizarra (Ausente)**.

- **Primary (Esmeralda):** A rich emerald used for the "Correcto" state and primary actions. It signifies success and progression.
- **Secondary (Ámbar):** A warm amber used for the "Presente" state. It provides a clear, high-contrast warning that the letter is misplaced.
- **Tertiary (Pizarra):** A sophisticated slate gray used for the "Ausente" state and secondary UI elements. It recedes into the background to keep the user's focus on the remaining possibilities.
- **Neutral:** A clean off-white background (#F8FAFC) ensures that the vibrant state colors pop without causing eye strain during long play sessions.

## Typography
This design system utilizes **Plus Jakarta Sans** for headlines and game tiles to provide a modern, friendly, and geometric feel. Its high x-height ensures that individual letters in the grid remain highly legible and iconic.

**Manrope** is used for body copy, keyboard labels, and instructions. It offers a technical yet approachable balance that complements the geometric nature of the grid. All Spanish game text (e.g., "¡Excelente!", "Palabra no encontrada") should be rendered in Manrope with medium to bold weights to maintain a premium feel.

## Layout & Spacing
The layout follows a **Fixed Center** model. On mobile and desktop, the game board is restricted to a maximum width to maintain its iconic 5x6 square ratio. 

The vertical rhythm is divided into three distinct zones:
1. **Cabecera (Header):** Compact, containing the title and settings.
2. **Tablero (The Grid):** The focal point, using a consistent 8px gap between tiles.
3. **Teclado (Keyboard):** Anchored to the bottom, using a flexible fluid grid that adjusts for Spanish characters like the 'Ñ'.

Spacing is derived from an 8px base unit to ensure perfect alignment and a sense of mathematical order.

## Elevation & Depth
Depth is conveyed through **Ambient Shadows** and tonal layering. 
- **Level 0 (Background):** Flat, #F8FAFC.
- **Level 1 (Keyboard Keys):** Subtle 2px blur shadow with 5% opacity to make keys feel tappable.
- **Level 2 (Active Tiles):** When a user is typing, the active tile gains a soft glow/shadow to indicate focus.
- **Level 3 (Modals/Dialogs):** High-diffusion shadows (20px blur, 10% opacity) with a semi-transparent backdrop blur (12px) to focus the user on game results or settings.

## Shapes
The design system employs a **Rounded** shape language to soften the intensity of the game. 
- **Tiles:** Use `rounded-lg` (1rem) to create a friendly, modern appearance that differentiates it from the sharp corners of the original Wordle.
- **Keyboard Keys:** Use `rounded-md` (0.5rem) to maximize the hitting area while maintaining the design language.
- **Buttons:** Primary action buttons (e.g., "Jugar de Nuevo") use `rounded-xl` (1.5rem) for a more inviting, pill-like feel.

## Components

### Las Teselas (The Tiles)
The core component. Each tile has four states:
- **Empty:** Bordered with `vacio`, no background.
- **Correcto:** Emerald background, white text, subtle inner glow.
- **Presente:** Amber background, white text.
- **Ausente:** Slate background, white text.

### El Teclado (The Keyboard)
Keys should have a slightly tactile feel. The 'ENTER' and 'BORRAR' keys should be slightly wider than letter keys. The 'Ñ' key is integrated into the second row for the Spanish layout.

### Botones (Buttons)
Primary buttons should use the Emerald color with a "lifted" shadow effect that flattens upon press. Secondary buttons use a ghost style with a Slate border.

### Modales de Resultado (Stats Modals)
Stats are displayed using clean bar charts in Emerald. Use high-contrast typography for the "Countdown to next word" (Próxima palabra) to create a sense of anticipation.