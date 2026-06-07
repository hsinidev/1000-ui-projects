---
name: Aero-Cycle Visual Language
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
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
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#f8f5f5'
  on-tertiary: '#303030'
  tertiary-container: '#dbd9d8'
  on-tertiary-container: '#5f5e5e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

This design system is engineered for the elite cycling sector, where performance is measured in watts and drag coefficients. The brand personality is clinical, elite, and focused, catering to professional athletes and aerodynamic engineers who require absolute clarity under physical duress.

The visual style is a hybrid of **Minimalism** and **Technical High-Contrast**. It leverages the "Matte" aesthetic—non-reflective, deep, and sophisticated—to serve as a silent backdrop for "Electric" telemetry data. Drawing inspiration from wind-tunnel visualizations, the system utilizes thin vector-line graphics and hairline strokes to imply airflow, motion, and structural integrity. The emotional response is one of trust in data and the sensation of cutting through the air.

## Colors

This design system utilizes a restricted, high-contrast palette to ensure legibility in high-velocity environments.

- **Matte Grey (#121212):** The foundation. Used for deep backgrounds to minimize eye strain and maximize the "pop" of data.
- **Electric Cyan (#00F0FF):** The primary kinetic color. Reserved for active states, critical telemetry, and path-of-travel indicators.
- **White (#FFFFFF):** High-level text and essential highlights. Used sparingly to maintain the dark-mode sophistication.
- **Surface Grey (#2A2A2A):** Used for container layering and subtle structural separation.

Data visualization should use gradients of Electric Cyan to transparent to represent "airflow" or "intensity" without introducing new hues that would break the technical focus.

## Typography

The typography strategy prioritizes precision and technical urgency. 

**Space Grotesk** is used for headlines, data points, and labels. Its geometric construction mirrors the engineering of a carbon-fiber frame. For telemetry and numerical values, use `data-mono` to ensure tabular alignment and a "lab-spec" appearance.

**Inter** is utilized for all long-form body text and UI controls. Its neutrality balances the aggressive nature of the headlines, ensuring that instructions and descriptions remain highly legible and professional. Large headlines should use tight letter spacing to imply speed, while labels use expanded tracking for a refined, technical feel.

## Layout & Spacing

The layout is built on a **12-column fixed grid** that anchors content within a 1440px max-width container, ensuring the "cockpit" of data feels centered and controlled. 

The spacing rhythm follows a strict 4px baseline, emphasizing density and information richness over airy whitespace. Gutters are kept tight (16px) to maintain a sense of structural rigidity. Layouts should favor horizontal modules that mimic the elongated profile of an aerodynamic bicycle frame. Components should be grouped into logical "clusters" or "instrument panels" using the margin units to create clear separation between different data streams (e.g., Biometrics vs. Atmospheric Data).

## Elevation & Depth

This design system avoids traditional shadows to maintain its matte, high-tech aesthetic. Instead, depth is achieved through **Tonal Layers** and **Low-Contrast Outlines**.

1.  **Level 0 (Background):** Matte Grey (#121212).
2.  **Level 1 (Panels):** Surface Grey (#1E1E1E) with a subtle 1px border (#2A2A2A).
3.  **Level 2 (Active Elements):** Electric Cyan (#00F0FF) accents or glows.

To imply movement and wind-tunnel dynamics, use semi-transparent "vector lines" (0.5px to 1px thickness) that bleed off the edges of containers. These lines act as structural guides and visual metaphors for airflow, creating a sense of 3D space without the use of skeuomorphic lighting.

## Shapes

The shape language is driven by the concept of "functional aerodynamics." While 0px sharp corners are too brutal, large rounded corners are too soft for a performance lab. 

This design system utilizes **Level 1 (Soft)** rounding. A consistent 4px (0.25rem) radius is applied to buttons, cards, and input fields. This subtle rounding suggests a "machined" finish—precise and intentional. Data visualizations and charts should use sharp terminals for lines to maintain a surgical, technical aesthetic.

## Components

- **Buttons:** Primary buttons use a solid Electric Cyan fill with black text. Secondary buttons use a transparent background with a 1px White border. All buttons have a high-contrast hover state where the glow increases slightly via a 1px Cyan outer stroke.
- **Telemetry Chips:** Small, high-density indicators with a label (Space Grotesk) and a value. These should look like individual sensors.
- **Cards:** Defined by a 1px border (#2A2A2A) rather than a shadow. The header of the card should often include a "vector line" element to tie it into the airflow aesthetic.
- **Input Fields:** Matte Grey background (#1A1A1A) with a bottom-only border in White. On focus, the border transitions to Electric Cyan.
- **Data Visualization:** Line charts should be Electric Cyan with a subtle gradient fill below the line, tapering to transparent. Use hairline grids in #2A2A2A for reference.
- **Status Indicators:** Use Electric Cyan for "Optimal," White for "Neutral," and a high-visibility Red (introduced only for warnings) for "Critical."

Additional recommended components include **Performance Gauges** (circular progress for cadence/power) and **Wind Direction Vectors** (stylized arrows using hairline strokes).