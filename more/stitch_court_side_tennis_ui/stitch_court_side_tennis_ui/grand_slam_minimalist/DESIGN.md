---
name: Grand Slam Minimalist
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#454652'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#767683'
  outline-variant: '#c6c5d4'
  surface-tint: '#4c56af'
  primary: '#000666'
  on-primary: '#ffffff'
  primary-container: '#1a237e'
  on-primary-container: '#8690ee'
  inverse-primary: '#bdc2ff'
  secondary: '#b52424'
  on-secondary: '#ffffff'
  secondary-container: '#ff5a52'
  on-secondary-container: '#600006'
  tertiary: '#321200'
  on-tertiary: '#ffffff'
  tertiary-container: '#522200'
  on-tertiary-container: '#e87a2f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bdc2ff'
  on-primary-fixed: '#000767'
  on-primary-fixed-variant: '#343d96'
  secondary-fixed: '#ffdad6'
  secondary-fixed-dim: '#ffb4ac'
  on-secondary-fixed: '#410003'
  on-secondary-fixed-variant: '#92030f'
  tertiary-fixed: '#ffdbc9'
  tertiary-fixed-dim: '#ffb68d'
  on-tertiary-fixed: '#321200'
  on-tertiary-fixed-variant: '#763400'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  score-display:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  body-regular:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  caption:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1280px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
The brand personality is prestigious, athletic, and disciplined. This design system evokes the quiet intensity of a championship point—focused, professional, and high-end. It targets a discerning audience of tennis enthusiasts and professionals who value precision over spectacle.

The design style is a blend of **Minimalism** and **Modern Corporate** aesthetics. It utilizes a structured grid, generous whitespace to allow data to breathe, and thin, deliberate lines that mimic court markings. The emotional response is one of clarity and exclusivity, moving away from "gamified" sports apps toward a refined, editorial experience.

## Colors
The palette is grounded in "Championship Navy" (#1A237E) for core structural elements and primary typography, providing a stable and authoritative foundation. "Clay Red" (#B22222) serves as a high-impact secondary color, reserved for live status indicators, active scores, and key CTAs. The lighter clay variant (#D2691E) is used for subtle accents and data visualization.

The background is a crisp, brilliant white to maintain a high-end feel. Neutral grays are utilized strictly for thin borders and secondary metadata, ensuring that the primary colors stand out with intent.

## Typography
This design system employs **Inter** for all functional UI and body text to ensure maximum legibility and a neutral, systematic feel. For sports data, scores, and specific labels, **Lexend** is introduced to provide a rhythmic, athletic character that remains highly readable at small sizes.

Headlines should be tight and impactful, while score displays require generous tracking (letter spacing) to maintain clarity during fast-paced updates. All labels should lean into uppercase styling to evoke a professional scoreboard aesthetic.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy for desktop (12 columns) and a fluid model for mobile. A strict 4px baseline shift ensures vertical rhythm. 

Whitespace is treated as a luxury element; margins should be expansive to prevent data density from feeling overwhelming. Elements are grouped using logical "stacks"—use `stack-lg` to separate distinct match sessions and `stack-sm` for related player statistics.

## Elevation & Depth
In alignment with the "Clean & Court-Side" aesthetic, this design system avoids heavy shadows. Depth is conveyed through **Low-Contrast Outlines** and **Tonal Layers**. 

- **Primary Surface:** White (#FFFFFF).
- **Secondary Surface:** Off-white/Light Gray (#F8F9FA) for grouping related content.
- **Borders:** 1px solid lines using #E0E0E0 are the primary method of separation.
- **Overlays:** For photography, use a 40% Navy Blue gradient overlay at the base to ensure white typography remains legible while maintaining a premium, "broadcast" feel.

## Shapes
The shape language is defined by **Sharp** (0px) corners. This mirrors the precision of a tennis court's lines and contributes to a professional, high-performance vibe. 

All buttons, cards, and input fields must use 90-degree angles. Any deviation (such as circular player avatars) should be framed within a sharp-edged square container to maintain consistency with the architectural nature of the design system.

## Components
- **Score Cards:** Use a white background with a thin 1px light gray border. Use Navy Blue for player names and Clay Red for live set scores. Ensure a vertical "court line" (a 2px Navy divider) separates the match status from the scoring data.
- **Buttons:** Primary buttons are solid Navy Blue with white text. Secondary buttons use a Navy Blue 1px stroke with no fill. All buttons are rectangular with zero corner radius.
- **Data Tables:** Remove all vertical grid lines; use only horizontal 1px dividers in light gray. Headers should be in `label-caps` typography.
- **Chips:** Used for tournament categories (e.g., "ATP 500"). Sharp-edged boxes with a light gray background and Navy text.
- **Refined Overlays:** Image containers for player portraits should feature a subtle Navy-to-transparent gradient to anchor text at the bottom.
- **Match Timeline:** A vertical 1px line with sharp square "pips" to indicate key match events (Aces, Break Points).