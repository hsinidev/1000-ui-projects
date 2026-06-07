---
name: Clean & Industrial Hub
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
  on-surface-variant: '#43474c'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#74777c'
  outline-variant: '#c4c7cc'
  surface-tint: '#50606f'
  primary: '#4e5e6d'
  on-primary: '#ffffff'
  primary-container: '#667686'
  on-primary-container: '#fdfcff'
  inverse-primary: '#b8c8da'
  secondary: '#ab3600'
  on-secondary: '#ffffff'
  secondary-container: '#fe5e1e'
  on-secondary-container: '#551600'
  tertiary: '#416261'
  on-tertiary: '#ffffff'
  tertiary-container: '#5a7a7a'
  on-tertiary-container: '#f3fffe'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e4f6'
  primary-fixed-dim: '#b8c8da'
  on-primary-fixed: '#0d1d2a'
  on-primary-fixed-variant: '#394857'
  secondary-fixed: '#ffdbcf'
  secondary-fixed-dim: '#ffb59c'
  on-secondary-fixed: '#390c00'
  on-secondary-fixed-variant: '#832700'
  tertiary-fixed: '#c6e9e9'
  tertiary-fixed-dim: '#abcdcd'
  on-tertiary-fixed: '#002020'
  on-tertiary-fixed-variant: '#2c4c4c'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
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
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
spacing:
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  stack-xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is built for the home repair professional and the serious DIYer. The brand personality is **rugged, dependable, and high-utility**. It avoids unnecessary ornamentation in favor of structural clarity and functional aesthetics. The target audience expects a tool-like experience that feels as sturdy as the hardware they use.

The visual style is a hybrid of **Minimalism and Brutalism**. It utilizes a "Utility-First" approach: heavy-weight borders represent structural integrity, while generous whitespace ensures clarity under stressful repair conditions. The interface should feel "built" rather than "drawn," evoking the emotional response of a well-organized workshop or a blueprint. Subtle background patterns, such as a faint 10px dot grid or diamond-plate micro-textures, reinforce the industrial theme without distracting from data.

## Colors

The color palette is anchored by **Slate Grey (#708090)**, providing a neutral, metallic foundation that suggests steel and stone. **Safety Orange (#FF5F1F)** is the high-visibility accent color, reserved strictly for primary actions, warnings, and critical highlights—mimicking industrial safety equipment.

For the **Project Difficulty** scale, the system uses a high-contrast semantic palette:
- **Beginner:** Forest Green, signifying "Go" and safety.
- **Intermediate:** Amber, signifying "Caution" or required skill.
- **Advanced:** Deep Red, signifying "High Risk" or specialized tools needed.
- **Pro:** Solid Black/Carbon, signifying "Expertise" and mastery.

Surface backgrounds use a light "Cool Grey" (#F5F5F5) to maintain a clean environment, while text and borders utilize deep charcoals to ensure maximum legibility and "rugged" definition.

## Typography

This design system utilizes **Inter** exclusively for its neutral, systematic, and highly legible characteristics. The typographic hierarchy is intentionally "top-heavy," with extra-bold weights for headlines to mimic architectural lettering and industrial signage.

**Labels** are frequently set in uppercase with increased letter spacing to serve as clear identifiers for technical data points and status badges. **Body text** maintains a generous line height to ensure instructions are easy to read in low-light or "on-the-job" environments.

## Layout & Spacing

The layout philosophy follows a **fixed grid system** on desktop and a **fluid grid** on mobile. It uses a strict 8px spacing rhythm to maintain "mathematical" alignment, echoing the precision of engineering. 

Margins and gutters are wider than standard consumer apps to prevent the UI from feeling "cramped" and to allow the heavy borders space to breathe. Elements should span specific column counts (e.g., sidebars at 3 columns, main feeds at 9) to maintain a rigid, structural feel.

## Elevation & Depth

In this design system, depth is achieved through **Bold Borders and Tonal Layers** rather than soft shadows. Shadows are largely avoided to maintain a "flat/rugged" aesthetic.

- **Level 0 (Floor):** Neutral background (#F5F5F5) with a subtle micro-dot texture.
- **Level 1 (Card/Container):** White background with a 2px solid Slate Grey (#708090) border.
- **Level 2 (Interactive/Active):** White background with a 4px solid Safety Orange (#FF5F1F) border or a "stamped" inset shadow to simulate physical depression.
- **Layering:** Elements are stacked using hard edges. When one element is "above" another, it is indicated by a thicker border or a high-contrast outline rather than a blur.

## Shapes

The design system employs **Sharp (0px)** corners for all structural components, including cards, buttons, and input fields. This reinforces the "Industrial" narrative, mimicking the raw edges of cut metal, blueprints, and heavy machinery. 

The only exception to the 0px rule is for small status indicators or circular icons where a geometric "pill" may be used to signify a toggle or indicator light.

## Components

### Buttons
Primary buttons use a solid Safety Orange (#FF5F1F) fill with black text and a 2px black bottom-border to give a "tactile" click feel. Secondary buttons use a thick 2px Slate Grey border with no fill. All buttons use uppercase bold labels.

### Project Difficulty Badges
These are "Tag" style components with a solid background matching the status color tokens. They should feature a small icon (e.g., a wrench or a hard hat) next to the text.
- **Beginner:** Single wrench icon.
- **Pro:** Three wrench icons or a "Certified" seal icon.

### Input Fields
Inputs are rectangular with a 2px Slate Grey border. On focus, the border thickens and changes to Safety Orange. Labels are always positioned above the field in uppercase `label-sm` style.

### Progress Bars
Heavy, thick bars (16px height). The "filled" portion uses a diagonal "hazard stripe" pattern (Orange/Black) to indicate work in progress.

### Cards
Cards are the primary container. They must have a 2px solid border. Headers within cards should be separated by a 1px horizontal rule to mimic a technical form.

### Additional Components
- **The "Blueprint" Toggle:** A specialized switch that toggles the UI into a high-contrast wireframe mode.
- **Tool Checklists:** Checkboxes are larger than standard (24px) with heavy borders, designed for "fat-finger" ease on mobile devices.