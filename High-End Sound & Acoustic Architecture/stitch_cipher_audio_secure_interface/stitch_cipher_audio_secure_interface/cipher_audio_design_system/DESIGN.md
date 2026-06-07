---
name: Cipher-Audio Design System
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
  on-surface-variant: '#c8c5cd'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#929097'
  outline-variant: '#47464c'
  surface-tint: '#c6c4df'
  primary: '#c6c4df'
  on-primary: '#2f2e43'
  primary-container: '#1a1a2e'
  on-primary-container: '#83829b'
  inverse-primary: '#5d5c74'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#c3c0ff'
  on-tertiary: '#1d00a5'
  tertiary-container: '#0f006b'
  on-tertiary-container: '#7772ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e0fc'
  primary-fixed-dim: '#c6c4df'
  on-primary-fixed: '#1a1a2e'
  on-primary-fixed-variant: '#45455b'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e2dfff'
  tertiary-fixed-dim: '#c3c0ff'
  on-tertiary-fixed: '#0f0069'
  on-tertiary-fixed-variant: '#3323cc'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-lg:
    fontFamily: metropolis
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: hankenGrotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: hankenGrotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: jetbrainsMono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: jetbrainsMono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  max-width: 1440px
---

## Brand & Style

This design system embodies "Executive-Grade Security." The brand personality is stoic, impenetrable, and high-precision, targeting high-net-worth individuals, defense contractors, and corporate executives. The UI must evoke the feeling of entering a physical vault—heavy, silent, and absolute.

The visual style is a fusion of **Glassmorphism** and **Brutalism**. It utilizes the translucency and depth of glass to imply futuristic technology, but anchors it with the heavy, unyielding borders of platinum silver to signal structural integrity. 

Key emotive drivers:
*   **Absolute Privacy:** Every interaction should feel shielded and contained.
*   **Technological Superiority:** Use of "Scanning" animations and "Tamper-Proof" visual cues to signify active protection.
*   **Tactile Digitalism:** Despite being a digital interface, elements should feel like they have the weight of cold metal and reinforced glass.

## Colors

The palette is strictly limited to reinforce a sense of discipline and security.

*   **Deep Black (#0A0A0A):** The "Infinite Void" base. Used for the primary background to minimize light bleed and maximize the impact of glowing elements.
*   **Deep Indigo (#1A1A2E):** The "Subsurface" color. Used for container backgrounds and glass effects. It provides a subtle tonal shift from the pure black base.
*   **Platinum Silver (#E5E4E2):** The "Structural" color. Used for high-contrast borders, icons, and primary headings. It should feel like machined metal.
*   **Glow Indigo (#4F46E5):** The "Active" accent. A more vibrant indigo used for data-scans, active states, and holographic badges. It represents the energy within the machine.

## Typography

The typography system relies on a strict hierarchy between geometric structural text and technical data output.

*   **Primary Type (Metropolis):** Used for headlines. Its geometric perfection suggests architectural stability.
*   **Secondary Type (Hanken Grotesk):** Used for body copy. It is clean, contemporary, and highly legible for long-form encrypted transcripts.
*   **Technical Accents (JetBrains Mono):** Used for all metadata, encryption keys, timestamps, and "Tamper-Proof" badges. The monospace nature reinforces the "Cipher" aspect of the brand, suggesting the UI is a direct window into the secure data stream.

## Layout & Spacing

This design system utilizes a **Fixed Grid** approach to evoke a sense of controlled, military-spec precision. 

*   **Desktop:** 12-column grid with wide 64px margins to create a "centered vault" feel.
*   **Mobile:** 4-column grid with 16px margins, focusing on vertical density.
*   **Spacing Rhythm:** All spacing must be a multiple of 8px. Use generous internal padding within glass containers (minimum 32px) to allow the "Scanning" animations and borders room to breathe without crowding the content. 
*   **Alignment:** Harsh left-alignment for data; center-alignment is reserved only for high-level authentication moments or the "Vault Closed" splash screen.

## Elevation & Depth

Depth is not created with traditional drop shadows, but through **Tonal Stacking** and **Refractive Layers**.

1.  **Level 0 (Base):** Deep Black (#0A0A0A).
2.  **Level 1 (Containers):** Deep Indigo (#1A1A2E) with 60% opacity and a 20px background blur (Backdrop Filter). 
3.  **Level 2 (Active Elements):** Elements "hovering" above the glass have a subtle inner-glow of Glow Indigo (#4F46E5) rather than an outer shadow.
4.  **Borders:** Every glass container must be encased in a 1.5px to 2px solid Platinum Silver border. This acts as the physical "frame" of the secure element.

## Shapes

The shape language is **Sharp (0px)**. 

To maintain the "Vault-Secure" and "Executive" aesthetic, rounded corners are avoided. Sharp 90-degree angles suggest rigidity and uncompromising protection. 

The only exception to the sharp-edge rule is for "Tamper-Proof" holographic badges, which may use a 45-degree chamfered (clipped) corner to mimic industrial military hardware labels.

## Components

### Buttons
*   **Primary:** Solid Platinum Silver background with Deep Black text. No hover transition—instead, use a "Scanline" animation that passes over the button every 3 seconds.
*   **Secondary:** Ghost style. Deep Black background with 2px Platinum Silver border and Silver text.

### Input Fields
*   Underline style only or fully enclosed glass containers. 
*   Focus state: The border-bottom transforms into a 2px Glow Indigo line with a subtle neon flicker animation.

### Tamper-Proof Badges
*   Small, rectangular labels using **JetBrains Mono**.
*   Background: A subtle silver-to-indigo holographic gradient.
*   Content: "ENCRYPTED," "SECURE-LINK," or "VERIFIED."

### Scanning UI Elements
*   Horizontal lines (1px) in Glow Indigo that move vertically across glass cards at 10% opacity, simulating a continuous security sweep.

### Cards
*   Heavy glassmorphism (Indigo blur) with a 2px Platinum Silver border. 
*   Header areas of cards should be separated by a 1px silver divider.

### Audio Visualizers
*   Replace standard waveforms with technical, vertical frequency bars (FFT style) in Glow Indigo. Every peak should trigger a subtle glow intensity change in the nearest silver border.