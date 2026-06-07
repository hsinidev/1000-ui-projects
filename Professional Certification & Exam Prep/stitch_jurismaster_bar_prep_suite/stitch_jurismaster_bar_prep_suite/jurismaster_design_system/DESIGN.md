---
name: JurisMaster Design System
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
  on-surface-variant: '#44474e'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#465f88'
  primary: '#000a1e'
  on-primary: '#ffffff'
  primary-container: '#002147'
  on-primary-container: '#708ab5'
  inverse-primary: '#aec7f6'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#0b0c02'
  on-tertiary: '#ffffff'
  tertiary-container: '#212313'
  on-tertiary-container: '#898b75'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f6'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e4e4cc'
  tertiary-fixed-dim: '#c8c8b0'
  on-tertiary-fixed: '#1b1d0e'
  on-tertiary-fixed-variant: '#474836'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  h1:
    fontFamily: newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: newsreader
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  study-body:
    fontFamily: newsreader
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  ui-body:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  button:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
spacing:
  base: 8px
  container-max: 1200px
  gutter: 24px
  margin-edge: 48px
  section-gap: 80px
---

## Brand & Style

The design system is rooted in the concepts of **Academic Institutionalism** and **Legal Authority**. It is designed to evoke the gravitas of a high court and the quiet focus of a prestigious law library. The target audience—law students and legal professionals—requires an environment that feels rigorous, dependable, and free from modern distractions.

The visual style leans heavily into **Minimalism** with a **Corporate Modern** structure. It prioritizes high-contrast readability and structural integrity over decorative trends. Use expansive whitespace to simulate the margins of a legal brief, and employ a strict alignment grid to project a sense of order and meticulousness. The emotional response should be one of "earned success" and "unshakeable trust."

## Colors

The palette utilizes a "Parchment" base rather than a pure white to reduce ocular fatigue during long study sessions and to reference historical legal documents. 

- **Primary (Deep Navy):** Used for headers, primary actions, and branding. It represents the "weight" of the law.
- **Secondary (Gold):** Used sparingly for achievement markers, high-level highlights, and calls to action that require a "premium" feel.
- **Background (Parchment):** The foundational canvas for all study materials.
- **Typography:** Deep Navy is the preferred "black" for body text to maintain a softer but still high-contrast relationship with the parchment background.

## Typography

This design system employs a dual-font strategy to distinguish between content and interface. 

**Newsreader** is the voice of the law. It is used for all long-form study materials, case studies, and primary headings. Its serif structure is designed for "reading to learn."

**Inter** is the functional engine. It is used for all UI components, navigation, metadata, and labels. It provides a clean, neutral contrast to the serif headings, ensuring the application feels like a modern tool despite its traditional aesthetic. 

- Use **Large Serif Headlines** for section titles.
- Use **All-Caps Sans-Serif Labels** for categorization and small metadata.
- Maintain a **1.6 line-height** for serif body text to ensure maximum legibility during intense reading.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model. Content should be centered with generous side margins to mimic the layout of a physical book or a legal transcript. 

- **8px Rhythm:** All spacing increments must be multiples of 8.
- **Margins:** Use wide horizontal margins (minimum 48px on desktop) to focus the eye on the central column of text.
- **Reading Column:** For study materials, the content width should be constrained to a maximum of 720px to prevent excessive line lengths.
- **Verticality:** Use significant vertical gaps (80px+) between major sections to allow the design to "breathe" and to signal transitions in topic.

## Elevation & Depth

To maintain a traditional feel, the design system avoids heavy drop shadows and modern "floating" effects. Depth is instead conveyed through:

- **Tonal Layering:** Using slightly darker or lighter shades of Parchment or Navy to define containers.
- **Low-Contrast Outlines:** Use thin (1px) borders in a muted Navy or Gold tint rather than shadows to define card boundaries.
- **Rule Lines:** Use horizontal rules (1px) to separate content, echoing the structure of legal ledgers.
- **Depth through Typography:** Use the "weight" of the serif font to pull attention forward, rather than physical elevation.

## Shapes

The shape language is strictly **Sharp (0px)**. This design system rejects the "friendliness" of rounded corners in favor of the precision and formality of a professional legal environment. 

- **Buttons & Inputs:** Must have 90-degree corners.
- **Cards & Modals:** Sharp edges emphasize the institutional nature of the platform.
- **Focus States:** Use a secondary Gold border or a solid Navy offset outline to indicate focus, maintaining sharp corners throughout.

## Components

- **Buttons:** Primary buttons are solid Deep Navy with Gold or White text. Secondary buttons are outlined (1px) Navy. No gradients.
- **Input Fields:** Classic "Box" style with a 1px Navy border. On focus, the border thickens or changes to Gold. Labels sit above the field in Inter (All-Caps).
- **Cards:** Simple parchment-colored containers with a thin, low-opacity Navy border. No shadows.
- **Progress Bars:** Use a thin, elegant Gold line to represent completion against a Navy track.
- **Tabs:** Underline-style tabs using the Gold accent for the active state, reinforcing the "ledger" aesthetic.
- **Legal Citations:** A specialized component using a monospaced variant or a small-caps Newsreader style to make case citations distinct from the body text.
- **Flashcards:** A high-contrast component with a flip animation that maintains the sharp-cornered, paper-like aesthetic.