import os
os.system('cls')

element = {
   'H': ' Hydrogen \n Chemical Symbol: H \n Element No.: 1 \n Electronegativity: 2.20 \n Atomic Weight: 1.0080 \n Specific Heat: 14.304 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 1s¹ \n Type: Nonmetal' ,
'HYDROGEN': ' Hydrogen \n Chemical Symbol: H \n Element No.: 1 \n Electronegativity: 2.20 \n Atomic Weight: 1.0080 \n Specific Heat: 14.304 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 1s¹ \n Type: Nonmetal',

'HE': ' Helium \n Chemical Symbol: He \n Element No.: 2 \n Electronegativity: — \n Atomic Weight: 4.0026 \n Specific Heat: 5.193 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 1s² \n Type: Noble Gas' ,
'HELIUM': ' Helium \n Chemical Symbol: He \n Element No.: 2 \n Electronegativity: — \n Atomic Weight: 4.0026 \n Specific Heat: 5.193 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 1s² \n Type: Noble Gas',

'LI': ' Lithium \n Chemical Symbol: Li \n Element No.: 3 \n Electronegativity: 0.98 \n Atomic Weight: 6.94 \n Specific Heat: 3.582 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 2s¹ \n Type: Alkali Metal',
'LITHIUM': ' Lithium \n Chemical Symbol: Li \n Element No.: 3 \n Electronegativity: 0.98 \n Atomic Weight: 6.94 \n Specific Heat: 3.582 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 2s¹ \n Type: Alkali Metal',

'BE': ' Beryllium \n Chemical Symbol: Be \n Element No.: 4 \n Electronegativity: 1.57 \n Atomic Weight: 9.0122 \n Specific Heat: 1.825 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 2s² \n Type: Alkaline Earth Metal',
'BERYLLIUM': ' Beryllium \n Chemical Symbol: Be \n Element No.: 4 \n Electronegativity: 1.57 \n Atomic Weight: 9.0122 \n Specific Heat: 1.825 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 2s² \n Type: Alkaline Earth Metal',

'B': ' Boron \n Chemical Symbol: B \n Element No.: 5 \n Electronegativity: 2.04 \n Atomic Weight: 10.81 \n Specific Heat: 1.026 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 2s² 2p¹  \n Type: Metalloid',
'BORON': ' Boron \n Chemical Symbol: B \n Element No.: 5 \n Electronegativity: 2.04 \n Atomic Weight: 10.81 \n Specific Heat: 1.026 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 2s² 2p¹ \n Type: Metalloid',

'C': ' Carbon \n Chemical Symbol: C \n Element No.: 6 \n Electronegativity: 2.55 \n Atomic Weight: 12.011 \n Specific Heat: 0.709 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 2s² 2p² \n Type: Nonmetal',
'CARBON': ' Carbon \n Chemical Symbol: C \n Element No.: 6 \n Electronegativity: 2.55 \n Atomic Weight: 12.011 \n Specific Heat: 0.709 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 2s² 2p²  \n Type: Nonmetal',

'N': ' Nitrogen \n Chemical Symbol: N \n Element No.: 7 \n Electronegativity: 3.04 \n Atomic Weight: 14.007 \n Specific Heat: 1.040 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 2s² 2p³ \n Type: Nonmetal',
'NITROGEN': ' Nitrogen \n Chemical Symbol: N \n Element No.: 7 \n Electronegativity: 3.04 \n Atomic Weight: 14.007 \n Specific Heat: 1.040 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 2s² 2p³ \n Type: Nonmetal',

'O': ' Oxygen \n Chemical Symbol: O \n Element No.: 8 \n Electronegativity: 3.44 \n Atomic Weight: 15.999 \n Specific Heat: 0.918 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 2s² 2p⁴ \n Type: Nonmetal',
'OXYGEN': ' Oxygen \n Chemical Symbol: O \n Element No.: 8 \n Electronegativity: 3.44 \n Atomic Weight: 15.999 \n Specific Heat: 0.918 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 2s² 2p⁴ \n Type: Nonmetal',

'F': ' Fluorine \n Chemical Symbol: F \n Element No.: 9 \n Electronegativity: 3.98 \n Atomic Weight: 18.998 \n Specific Heat: 0.824 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 2s² 2p⁵ \n Type: Halogen',
'FLUORINE': ' Fluorine \n Chemical Symbol: F \n Element No.: 9 \n Electronegativity: 3.98 \n Atomic Weight: 18.998 \n Specific Heat: 0.824 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 2s² 2p⁵ \n Type: Halogen',

'NE': ' Neon \n Chemical Symbol: Ne \n Element No.: 10 \n Electronegativity: — \n Atomic Weight: 20.180 \n Specific Heat: 1.030 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 2s² 2p⁶ \n Type: Noble Gas',
'NEON': ' Neon \n Chemical Symbol: Ne \n Element No.: 10 \n Electronegativity: — \n Atomic Weight: 20.180 \n Specific Heat: 1.030 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 2s² 2p⁶ \n Type: Noble Gas',

'NA': ' Sodium \n Chemical Symbol: Na \n Element No.: 11 \n Electronegativity: 0.93 \n Atomic Weight: 22.990 \n Specific Heat: 1.228 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s¹ \n Type: Alkali  Metal',
'SODIUM': ' Sodium \n Chemical Symbol: Na \n Element No.: 11 \n Electronegativity: 0.93 \n Atomic Weight: 22.990 \n Specific Heat: 1.228 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s¹ \n Type: Alkali Metal',

'MG': ' Magnesium \n Chemical Symbol: Mg \n Element No.: 12 \n Electronegativity: 1.31 \n Atomic Weight: 24.305 \n Specific Heat: 1.023 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² \n Type: Alkaline Earth Metal',
'MAGNESIUM': ' Magnesium \n Chemical Symbol: Mg \n Element No.: 12 \n Electronegativity: 1.31 \n Atomic Weight: 24.305 \n Specific Heat: 1.023 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² \n Type: Alkaline Earth Metal',

'AL': ' Aluminum \n Chemical Symbol: Al \n Element No.: 13 \n Electronegativity: 1.61 \n Atomic Weight: 26.982 \n Specific Heat: 0.897 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² 3p¹ \n Type: Post-Transition Metal',
'ALUMINUM': ' Aluminum \n Chemical Symbol: Al \n Element No.: 13 \n Electronegativity: 1.61 \n Atomic Weight: 26.982 \n Specific Heat: 0.897 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² 3p¹ \n Type: Post-Transition Metal',

'SI': ' Silicon \n Chemical Symbol: Si \n Element No.: 14 \n Electronegativity: 1.90 \n Atomic Weight: 28.085 \n Specific Heat: 0.705 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² 3p² \n Type: Metalloid',
'SILICON': ' Silicon \n Chemical Symbol: Si \n Element No.: 14 \n Electronegativity: 1.90 \n Atomic Weight: 28.085 \n Specific Heat: 0.705 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² 3p² \n Type: Metalloid',

'P': ' Phosphorus \n Chemical Symbol: P \n Element No.: 15 \n Electronegativity: 2.19 \n Atomic Weight: 30.974 \n Specific Heat: 0.769 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² 3p³ \n Type: Nonmetal',
'PHOSPHORUS': ' Phosphorus \n Chemical Symbol: P \n Element No.: 15 \n Electronegativity: 2.19 \n Atomic Weight: 30.974 \n Specific Heat: 0.769 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² 3p³ \n Type: Nonmetal',

'S': ' Sulfur \n Chemical Symbol: S \n Element No.: 16 \n Electronegativity: 2.58 \n Atomic Weight: 32.06 \n Specific Heat: 0.710 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² 3p⁴ \n Type: Nonmetal',
'SULFUR': ' Sulfur \n Chemical Symbol: S \n Element No.: 16 \n Electronegativity: 2.58 \n Atomic Weight: 32.06 \n Specific Heat: 0.710 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3s² 3p⁴ \n Type: Nonmetal',

'CL': ' Chlorine \n Chemical Symbol: Cl \n Element No.: 17 \n Electronegativity: 3.16 \n Atomic Weight: 35.45 \n Specific Heat: 0.479 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 3s² 3p⁵ \n Type: Halogen',
'CHLORINE': ' Chlorine \n Chemical Symbol: Cl \n Element No.: 17 \n Electronegativity: 3.16 \n Atomic Weight: 35.45 \n Specific Heat: 0.479 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 3s² 3p⁵ \n Type: Halogen',

'AR': ' Argon \n Chemical Symbol: Ar \n Element No.: 18 \n Electronegativity: — \n Atomic Weight: 39.948 \n Specific Heat: 0.520 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 3s² 3p⁶ \n Type: Noble Gas',
'ARGON': ' Argon \n Chemical Symbol: Ar \n Element No.: 18 \n Electronegativity: — \n Atomic Weight: 39.948 \n Specific Heat: 0.520 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 3s² 3p⁶ \n Type: Noble Gas',

'K': ' Potassium \n Chemical Symbol: K \n Element No.: 19 \n Electronegativity: 0.82 \n Atomic Weight: 39.098 \n Specific Heat: 0.757 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s¹ \n Type: Alkali Metal',
'POTASSIUM': ' Potassium \n Chemical Symbol: K \n Element No.: 19 \n Electronegativity: 0.82 \n Atomic Weight: 39.098 \n Specific Heat: 0.757 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s¹ \n Type: Alkali Metal',

'CA': ' Calcium \n Chemical Symbol: Ca \n Element No.: 20 \n Electronegativity: 1.00 \n Atomic Weight: 40.078 \n Specific Heat: 0.647 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² \n Type: Alkaline Earth Metal',
'CALCIUM': ' Calcium \n Chemical Symbol: Ca \n Element No.: 20 \n Electronegativity: 1.00 \n Atomic Weight: 40.078 \n Specific Heat: 0.647 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² \n Type: Alkaline Earth Metal',

'SC': ' Scandium \n Chemical Symbol: Sc \n Element No.: 21 \n Electronegativity: 1.36 \n Atomic Weight: 44.956 \n Specific Heat: 0.568 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d¹ 4s² \n Type: Transition Metal',
'SCANDIUM': ' Scandium \n Chemical Symbol: Sc \n Element No.: 21 \n Electronegativity: 1.36 \n Atomic Weight: 44.956 \n Specific Heat: 0.568 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d¹ 4s² \n Type: Transition Metal',

'TI': ' Titanium \n Chemical Symbol: Ti \n Element No.: 22 \n Electronegativity: 1.54 \n Atomic Weight: 47.867 \n Specific Heat: 0.523 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d² 4s² \n Type: Transition Metal',
'TITANIUM': ' Titanium \n Chemical Symbol: Ti \n Element No.: 22 \n Electronegativity: 1.54 \n Atomic Weight: 47.867 \n Specific Heat: 0.523 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d² 4s² \n Type: Transition Metal',

'V': ' Vanadium \n Chemical Symbol: V \n Element No.: 23 \n Electronegativity: 1.63 \n Atomic Weight: 50.942 \n Specific Heat: 0.489 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d³ 4s² \n Type: Transition Metal',
'VANADIUM': ' Vanadium \n Chemical Symbol: V \n Element No.: 23 \n Electronegativity: 1.63 \n Atomic Weight: 50.942 \n Specific Heat: 0.489 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d³ 4s² \n Type: Transition Metal',

'CR': ' Chromium \n Chemical Symbol: Cr \n Element No.: 24 \n Electronegativity: 1.66 \n Atomic Weight: 51.996 \n Specific Heat: 0.449 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁵ 4s¹ \n Type: Transition Metal',
'CHROMIUM': ' Chromium \n Chemical Symbol: Cr \n Element No.: 24 \n Electronegativity: 1.66 \n Atomic Weight: 51.996 \n Specific Heat: 0.449 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁵ 4s¹ \n Type: Transition Metal',

'MN': ' Manganese \n Chemical Symbol: Mn \n Element No.: 25 \n Electronegativity: 1.55 \n Atomic Weight: 54.938 \n Specific Heat: 0.479 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁵ 4s² \n Type: Transition Metal',
'MANGANESE': ' Manganese \n Chemical Symbol: Mn \n Element No.: 25 \n Electronegativity: 1.55 \n Atomic Weight: 54.938 \n Specific Heat: 0.479 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁵ 4s² \n Type: Transition Metal',

'FE': ' Iron \n Chemical Symbol: Fe \n Element No.: 26 \n Electronegativity: 1.83 \n Atomic Weight: 55.845 \n Specific Heat: 0.449 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁶ 4s² \n Type: Transition Metal',
'IRON': ' Iron \n Chemical Symbol: Fe \n Element No.: 26 \n Electronegativity: 1.83 \n Atomic Weight: 55.845 \n Specific Heat: 0.449 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁶ 4s² \n Type: Transition Metal',

'CO': ' Cobalt \n Chemical Symbol: Co \n Element No.: 27 \n Electronegativity: 1.88 \n Atomic Weight: 58.933 \n Specific Heat: 0.421 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁷ 4s² \n Type: Transition Metal',
'COBALT': ' Cobalt \n Chemical Symbol: Co \n Element No.: 27 \n Electronegativity: 1.88 \n Atomic Weight: 58.933 \n Specific Heat: 0.421 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁷ 4s² \n Type: Transition Metal',

'NI': ' Nickel \n Chemical Symbol: Ni \n Element No.: 28 \n Electronegativity: 1.91 \n Atomic Weight: 58.693 \n Specific Heat: 0.444 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁸ 4s² \n Type: Transition Metal',
'NICKEL': ' Nickel \n Chemical Symbol: Ni \n Element No.: 28 \n Electronegativity: 1.91 \n Atomic Weight: 58.693 \n Specific Heat: 0.444 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d⁸ 4s² \n Type: Transition Metal',

'CU': ' Copper \n Chemical Symbol: Cu \n Element No.: 29 \n Electronegativity: 1.90 \n Atomic Weight: 63.546 \n Specific Heat: 0.385 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d¹⁰ 4s¹ \n Type: Transition Metal',
'COPPER': ' Copper \n Chemical Symbol: Cu \n Element No.: 29 \n Electronegativity: 1.90 \n Atomic Weight: 63.546 \n Specific Heat: 0.385 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d¹⁰ 4s¹ \n Type: Transition Metal',

'ZN': ' Zinc \n Chemical Symbol: Zn \n Element No.: 30 \n Electronegativity: 1.65 \n Atomic Weight: 65.38 \n Specific Heat: 0.388 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d¹⁰ 4s² \n Type: Transition Metal',
'ZINC': ' Zinc \n Chemical Symbol: Zn \n Element No.: 30 \n Electronegativity: 1.65 \n Atomic Weight: 65.38 \n Specific Heat: 0.388 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 3d¹⁰ 4s² \n Type: Transition Metal',

'GA': ' Gallium \n Chemical Symbol: Ga \n Element No.: 31 \n Electronegativity: 1.81 \n Atomic Weight: 69.723 \n Specific Heat: 0.371 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² 4p¹ \n Type: Post-Transition Metal',
'GALLIUM': ' Gallium \n Chemical Symbol: Ga \n Element No.: 31 \n Electronegativity: 1.81 \n Atomic Weight: 69.723 \n Specific Heat: 0.371 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² 4p¹ \n Type: Post-Transition Metal',

'GE': ' Germanium \n Chemical Symbol: Ge \n Element No.: 32 \n Electronegativity: 2.01 \n Atomic Weight: 72.630 \n Specific Heat: 0.320 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² 4p² \n Type: Metalloid',
'GERMANIUM': ' Germanium \n Chemical Symbol: Ge \n Element No.: 32 \n Electronegativity: 2.01 \n Atomic Weight: 72.630 \n Specific Heat: 0.320 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² 4p² \n Type: Metalloid',

'AS': ' Arsenic \n Chemical Symbol: As \n Element No.: 33 \n Electronegativity: 2.18 \n Atomic Weight: 74.922 \n Specific Heat: 0.329 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² 4p³ \n Type: Metalloid',
'ARSENIC': ' Arsenic \n Chemical Symbol: As \n Element No.: 33 \n Electronegativity: 2.18 \n Atomic Weight: 74.922 \n Specific Heat: 0.329 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² 4p³ \n Type: Metalloid',

'SE': ' Selenium \n Chemical Symbol: Se \n Element No.: 34 \n Electronegativity: 2.55 \n Atomic Weight: 78.971 \n Specific Heat: 0.321 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² 4p⁴ \n Type: Nonmetal',
'SELENIUM': ' Selenium \n Chemical Symbol: Se \n Element No.: 34 \n Electronegativity: 2.55 \n Atomic Weight: 78.971 \n Specific Heat: 0.321 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4s² 4p⁴ \n Type: Nonmetal',

'BR': ' Bromine \n Chemical Symbol: Br \n Element No.: 35 \n Electronegativity: 2.96 \n Atomic Weight: 79.904 \n Specific Heat: 0.474 (J/g * K) \n Phase: Liquid \n Valence Electron Configuration: 4s² 4p⁵ \n Type: Halogen',
'BROMINE': ' Bromine \n Chemical Symbol: Br \n Element No.: 35 \n Electronegativity: 2.96 \n Atomic Weight: 79.904 \n Specific Heat: 0.474 (J/g * K) \n Phase: Liquid \n Valence Electron Configuration: 4s² 4p⁵ \n Type: Halogen',

'KR': ' Krypton \n Chemical Symbol: Kr \n Element No.: 36 \n Electronegativity: 3.00 \n Atomic Weight: 83.798 \n Specific Heat: 0.248 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 4s² 4p⁶ \n Type: Noble Gas',
'KRYPTON': ' Krypton \n Chemical Symbol: Kr \n Element No.: 36 \n Electronegativity: 3.00 \n Atomic Weight: 83.798 \n Specific Heat: 0.248 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 4s² 4p⁶ \n Type: Noble Gas',

'RB': ' Rubidium \n Chemical Symbol: Rb \n Element No.: 37 \n Electronegativity: 0.82 \n Atomic Weight: 85.468 \n Specific Heat: 0.363 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s¹ \n Type: Alkali Metal',
'RUBIDIUM': ' Rubidium \n Chemical Symbol: Rb \n Element No.: 37 \n Electronegativity: 0.82 \n Atomic Weight: 85.468 \n Specific Heat: 0.363 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s¹ \n Type: Alkali Metal',

'SR': ' Strontium \n Chemical Symbol: Sr \n Element No.: 38 \n Electronegativity: 0.95 \n Atomic Weight: 87.62 \n Specific Heat: 0.301 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² \n Type: Alkaline Earth Metal',
'STRONTIUM': ' Strontium \n Chemical Symbol: Sr \n Element No.: 38 \n Electronegativity: 0.95 \n Atomic Weight: 87.62 \n Specific Heat: 0.301 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² \n Type: Alkaline Earth Metal',

'Y': ' Yttrium \n Chemical Symbol: Y \n Element No.: 39 \n Electronegativity: 1.22 \n Atomic Weight: 88.906 \n Specific Heat: 0.298 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d¹ 5s² \n Type: Transition Metal',
'YTTRIUM': ' Yttrium \n Chemical Symbol: Y \n Element No.: 39 \n Electronegativity: 1.22 \n Atomic Weight: 88.906 \n Specific Heat: 0.298 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d¹ 5s² \n Type: Transition Metal',

'ZR': ' Zirconium \n Chemical Symbol: Zr \n Element No.: 40 \n Electronegativity: 1.33 \n Atomic Weight: 91.224 \n Specific Heat: 0.278 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d² 5s² \n Type: Transition Metal',
'ZIRCONIUM': ' Zirconium \n Chemical Symbol: Zr \n Element No.: 40 \n Electronegativity: 1.33 \n Atomic Weight: 91.224 \n Specific Heat: 0.278 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d² 5s² \n Type: Transition Metal',

'NB': ' Niobium \n Chemical Symbol: Nb \n Element No.: 41 \n Electronegativity: 1.6 \n Atomic Weight: 92.906 \n Specific Heat: 0.265 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d⁴ 5s¹ \n Type: Transition Metal',
'NIOBIUM': ' Niobium \n Chemical Symbol: Nb \n Element No.: 41 \n Electronegativity: 1.6 \n Atomic Weight: 92.906 \n Specific Heat: 0.265 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d⁴ 5s¹ \n Type: Transition Metal',

'MO': ' Molybdenum \n Chemical Symbol: Mo \n Element No.: 42 \n Electronegativity: 2.16 \n Atomic Weight: 95.95 \n Specific Heat: 0.251 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d⁵ 5s¹ \n Type: Transition Metal',
'MOLYBDENUM': ' Molybdenum \n Chemical Symbol: Mo \n Element No.: 42 \n Electronegativity: 2.16 \n Atomic Weight: 95.95 \n Specific Heat: 0.251 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d⁵ 5s¹ \n Type: Transition Metal',

'TC': ' Technetium \n Chemical Symbol: Tc \n Element No.: 43 \n Electronegativity: 1.9 \n Atomic Weight: [98] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 4d⁵ 5s² \n Type: Transition Metal',
'TECHNETIUM': ' Technetium \n Chemical Symbol: Tc \n Element No.: 43 \n Electronegativity: 1.9 \n Atomic Weight: [98] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 4d⁵ 5s² \n Type: Transition Metal',

'RU': ' Ruthenium \n Chemical Symbol: Ru \n Element No.: 44 \n Electronegativity: 2.2 \n Atomic Weight: 101.07 \n Specific Heat: 0.238 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d⁷ 5s¹ \n Type: Transition Metal',
'RUTHENIUM': ' Ruthenium \n Chemical Symbol: Ru \n Element No.: 44 \n Electronegativity: 2.2 \n Atomic Weight: 101.07 \n Specific Heat: 0.238 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d⁷ 5s¹ \n Type: Transition Metal',

'RH': ' Rhodium \n Chemical Symbol: Rh \n Element No.: 45 \n Electronegativity: 2.28 \n Atomic Weight: 102.906 \n Specific Heat: 0.243 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d⁸ 5s¹ \n Type: Transition Metal',
'RHODIUM': ' Rhodium \n Chemical Symbol: Rh \n Element No.: 45 \n Electronegativity: 2.28 \n Atomic Weight: 102.906 \n Specific Heat: 0.243 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d⁸ 5s¹ \n Type: Transition Metal',

'PD': ' Palladium \n Chemical Symbol: Pd \n Element No.: 46 \n Electronegativity: 2.20 \n Atomic Weight: 106.42 \n Specific Heat: 0.244 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d¹⁰ \n Type: Transition Metal',
'PALLADIUM': ' Palladium \n Chemical Symbol: Pd \n Element No.: 46 \n Electronegativity: 2.20 \n Atomic Weight: 106.42 \n Specific Heat: 0.244 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d¹⁰ \n Type: Transition Metal',

'AG': ' Silver \n Chemical Symbol: Ag \n Element No.: 47 \n Electronegativity: 1.93 \n Atomic Weight: 107.868 \n Specific Heat: 0.235 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d¹⁰ 5s¹ \n Type: Transition Metal',
'SILVER': ' Silver \n Chemical Symbol: Ag \n Element No.: 47 \n Electronegativity: 1.93 \n Atomic Weight: 107.868 \n Specific Heat: 0.235 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d¹⁰ 5s¹ \n Type: Transition Metal',

'CD': ' Cadmium \n Chemical Symbol: Cd \n Element No.: 48 \n Electronegativity: 1.69 \n Atomic Weight: 112.414 \n Specific Heat: 0.232 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d¹⁰ 5s² \n Type: Transition Metal',
'CADMIUM': ' Cadmium \n Chemical Symbol: Cd \n Element No.: 48 \n Electronegativity: 1.69 \n Atomic Weight: 112.414 \n Specific Heat: 0.232 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4d¹⁰ 5s² \n Type: Transition Metal',

'IN': ' Indium \n Chemical Symbol: In \n Element No.: 49 \n Electronegativity: 1.78 \n Atomic Weight: 114.818 \n Specific Heat: 0.233 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p¹ \n Type: Post-Transition Metal',
'INDIUM': ' Indium \n Chemical Symbol: In \n Element No.: 49 \n Electronegativity: 1.78 \n Atomic Weight: 114.818 \n Specific Heat: 0.233 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p¹ \n Type: Post-Transition Metal',

'SN': ' Tin \n Chemical Symbol: Sn \n Element No.: 50 \n Electronegativity: 1.96 \n Atomic Weight: 118.710 \n Specific Heat: 0.228 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p² \n Type: Post-Transition Metal',
'TIN': ' Tin \n Chemical Symbol: Sn \n Element No.: 50 \n Electronegativity: 1.96 \n Atomic Weight: 118.710 \n Specific Heat: 0.228 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p² \n Type: Post-Transition Metal',

'SB': ' Antimony \n Chemical Symbol: Sb \n Element No.: 51 \n Electronegativity: 2.05 \n Atomic Weight: 121.760 \n Specific Heat: 0.207 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p³ \n Type: Metalloid',
'ANTIMONY': ' Antimony \n Chemical Symbol: Sb \n Element No.: 51 \n Electronegativity: 2.05 \n Atomic Weight: 121.760 \n Specific Heat: 0.207 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p³ \n Type: Metalloid',

'TE': ' Tellurium \n Chemical Symbol: Te \n Element No.: 52 \n Electronegativity: 2.10 \n Atomic Weight: 127.60 \n Specific Heat: 0.202 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p⁴ \n Type: Metalloid',
'TELLURIUM': ' Tellurium \n Chemical Symbol: Te \n Element No.: 52 \n Electronegativity: 2.10 \n Atomic Weight: 127.60 \n Specific Heat: 0.202 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p⁴ \n Type: Metalloid',

'I': ' Iodine \n Chemical Symbol: I \n Element No.: 53 \n Electronegativity: 2.66 \n Atomic Weight: 126.904 \n Specific Heat: 0.214 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p⁵ \n Type: Halogen',
'IODINE': ' Iodine \n Chemical Symbol: I \n Element No.: 53 \n Electronegativity: 2.66 \n Atomic Weight: 126.904 \n Specific Heat: 0.214 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5s² 5p⁵ \n Type: Halogen',

'XE': ' Xenon \n Chemical Symbol: Xe \n Element No.: 54 \n Electronegativity: 2.60 \n Atomic Weight: 131.293 \n Specific Heat: 0.158 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 5s² 5p⁶ \n Type: Noble Gas',
'XENON': ' Xenon \n Chemical Symbol: Xe \n Element No.: 54 \n Electronegativity: 2.60 \n Atomic Weight: 131.293 \n Specific Heat: 0.158 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 5s² 5p⁶ \n Type: Noble Gas',

'CS': ' Cesium \n Chemical Symbol: Cs \n Element No.: 55 \n Electronegativity: 0.79 \n Atomic Weight: 132.905 \n Specific Heat: 0.242 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s¹ \n Type: Alkali Metal',
'CESIUM': ' Cesium \n Chemical Symbol: Cs \n Element No.: 55 \n Electronegativity: 0.79 \n Atomic Weight: 132.905 \n Specific Heat: 0.242 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s¹ \n Type: Alkali Metal',

'BA': ' Barium \n Chemical Symbol: Ba \n Element No.: 56 \n Electronegativity: 0.89 \n Atomic Weight: 137.327 \n Specific Heat: 0.204 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² \n Type: Alkaline Earth Metal',
'BARIUM': ' Barium \n Chemical Symbol: Ba \n Element No.: 56 \n Electronegativity: 0.89 \n Atomic Weight: 137.327 \n Specific Heat: 0.204 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² \n Type: Alkaline Earth Metal',

'LA': ' Lanthanum \n Chemical Symbol: La \n Element No.: 57 \n Electronegativity: 1.10 \n Atomic Weight: 138.905 \n Specific Heat: 0.195 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d¹ 6s² \n Type: Lanthanide',
'LANTHANUM': ' Lanthanum \n Chemical Symbol: La \n Element No.: 57 \n Electronegativity: 1.10 \n Atomic Weight: 138.905 \n Specific Heat: 0.195 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d¹ 6s² \n Type: Lanthanide',

'CE': ' Cerium \n Chemical Symbol: Ce \n Element No.: 58 \n Electronegativity: 1.12 \n Atomic Weight: 140.116 \n Specific Heat: 0.192 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹ 5d¹ 6s² \n Type: Lanthanide',
'CERIUM': ' Cerium \n Chemical Symbol: Ce \n Element No.: 58 \n Electronegativity: 1.12 \n Atomic Weight: 140.116 \n Specific Heat: 0.192 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹ 5d¹ 6s² \n Type: Lanthanide',

'PR': ' Praseodymium \n Chemical Symbol: Pr \n Element No.: 59 \n Electronegativity: 1.13 \n Atomic Weight: 140.908 \n Specific Heat: 0.193 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f³ 6s² \n Type: Lanthanide',
'PRASEODYMIUM': ' Praseodymium \n Chemical Symbol: Pr \n Element No.: 59 \n Electronegativity: 1.13 \n Atomic Weight: 140.908 \n Specific Heat: 0.193 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f³ 6s² \n Type: Lanthanide',

'ND': ' Neodymium \n Chemical Symbol: Nd \n Element No.: 60 \n Electronegativity: 1.14 \n Atomic Weight: 144.242 \n Specific Heat: 0.190 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁴ 6s² \n Type: Lanthanide',
'NEODYMIUM': ' Neodymium \n Chemical Symbol: Nd \n Element No.: 60 \n Electronegativity: 1.14 \n Atomic Weight: 144.242 \n Specific Heat: 0.190 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁴ 6s² \n Type: Lanthanide',

'PM': ' Promethium \n Chemical Symbol: Pm \n Element No.: 61 \n Electronegativity: — \n Atomic Weight: [145] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 4f⁵ 6s² \n Type: Lanthanide',
'PROMETHIUM': ' Promethium \n Chemical Symbol: Pm \n Element No.: 61 \n Electronegativity: — \n Atomic Weight: [145] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 4f⁵ 6s² \n Type: Lanthanide',

'SM': ' Samarium \n Chemical Symbol: Sm \n Element No.: 62 \n Electronegativity: 1.17 \n Atomic Weight: 150.36 \n Specific Heat: 0.197 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁶ 6s² \n Type: Lanthanide',
'SAMARIUM': ' Samarium \n Chemical Symbol: Sm \n Element No.: 62 \n Electronegativity: 1.17 \n Atomic Weight: 150.36 \n Specific Heat: 0.197 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁶ 6s² \n Type: Lanthanide',

'EU': ' Europium \n Chemical Symbol: Eu \n Element No.: 63 \n Electronegativity: 1.20 \n Atomic Weight: 151.964 \n Specific Heat: 0.182 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁷ 6s² \n Type: Lanthanide',
'EUROPIUM': ' Europium \n Chemical Symbol: Eu \n Element No.: 63 \n Electronegativity: 1.20 \n Atomic Weight: 151.964 \n Specific Heat: 0.182 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁷ 6s² \n Type: Lanthanide',

'GD': ' Gadolinium \n Chemical Symbol: Gd \n Element No.: 64 \n Electronegativity: 1.20 \n Atomic Weight: 157.25 \n Specific Heat: 0.236 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁷ 5d¹ 6s² \n Type: Lanthanide',
'GADOLINIUM': ' Gadolinium \n Chemical Symbol: Gd \n Element No.: 64 \n Electronegativity: 1.20 \n Atomic Weight: 157.25 \n Specific Heat: 0.236 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁷ 5d¹ 6s² \n Type: Lanthanide',

'TB': ' Terbium \n Chemical Symbol: Tb \n Element No.: 65 \n Electronegativity: 1.2 \n Atomic Weight: 158.925 \n Specific Heat: 0.182 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁹ 6s² \n Type: Lanthanide',
'TERBIUM': ' Terbium \n Chemical Symbol: Tb \n Element No.: 65 \n Electronegativity: 1.2 \n Atomic Weight: 158.925 \n Specific Heat: 0.182 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f⁹ 6s² \n Type: Lanthanide',

'DY': ' Dysprosium \n Chemical Symbol: Dy \n Element No.: 66 \n Electronegativity: 1.22 \n Atomic Weight: 162.500 \n Specific Heat: 0.168 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹⁰ 6s² \n Type: Lanthanide',
'DYSPROSIUM': ' Dysprosium \n Chemical Symbol: Dy \n Element No.: 66 \n Electronegativity: 1.22 \n Atomic Weight: 162.500 \n Specific Heat: 0.168 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹⁰ 6s² \n Type: Lanthanide',

'HO': ' Holmium \n Chemical Symbol: Ho \n Element No.: 67 \n Electronegativity: 1.23 \n Atomic Weight: 164.930 \n Specific Heat: 0.165 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹¹ 6s² \n Type: Lanthanide',
'HOLMIUM': ' Holmium \n Chemical Symbol: Ho \n Element No.: 67 \n Electronegativity: 1.23 \n Atomic Weight: 164.930 \n Specific Heat: 0.165 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹¹ 6s² \n Type: Lanthanide',

'ER': ' Erbium \n Chemical Symbol: Er \n Element No.: 68 \n Electronegativity: 1.24 \n Atomic Weight: 167.259 \n Specific Heat: 0.192 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹² 6s² \n Type: Lanthanide',
'ERBIUM': ' Erbium \n Chemical Symbol: Er \n Element No.: 68 \n Electronegativity: 1.24 \n Atomic Weight: 167.259 \n Specific Heat: 0.192 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹² 6s² \n Type: Lanthanide',

'TM': ' Thulium \n Chemical Symbol: Tm \n Element No.: 69 \n Electronegativity: 1.25 \n Atomic Weight: 168.934 \n Specific Heat: 0.160 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹³ 6s² \n Type: Lanthanide',
'THULIUM': ' Thulium \n Chemical Symbol: Tm \n Element No.: 69 \n Electronegativity: 1.25 \n Atomic Weight: 168.934 \n Specific Heat: 0.160 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹³ 6s² \n Type: Lanthanide',

'YB': ' Ytterbium \n Chemical Symbol: Yb \n Element No.: 70 \n Electronegativity: 1.10 \n Atomic Weight: 173.045 \n Specific Heat: 0.155 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹⁴ 6s² \n Type: Lanthanide',
'YTTERBIUM': ' Ytterbium \n Chemical Symbol: Yb \n Element No.: 70 \n Electronegativity: 1.10 \n Atomic Weight: 173.045 \n Specific Heat: 0.155 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹⁴ 6s² \n Type: Lanthanide',

'LU': ' Lutetium \n Chemical Symbol: Lu \n Element No.: 71 \n Electronegativity: 1.27 \n Atomic Weight: 174.966 \n Specific Heat: 0.154 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹⁴ 5d¹ 6s² \n Type: Lanthanide',
'LUTETIUM': ' Lutetium \n Chemical Symbol: Lu \n Element No.: 71 \n Electronegativity: 1.27 \n Atomic Weight: 174.966 \n Specific Heat: 0.154 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 4f¹⁴ 5d¹ 6s² \n Type: Lanthanide',

'HF': ' Hafnium \n Chemical Symbol: Hf \n Element No.: 72 \n Electronegativity: 1.3 \n Atomic Weight: 178.49 \n Specific Heat: 0.144 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d² 6s² \n Type: Transition Metal',
'HAFNIUM': ' Hafnium \n Chemical Symbol: Hf \n Element No.: 72 \n Electronegativity: 1.3 \n Atomic Weight: 178.49 \n Specific Heat: 0.144 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d² 6s² \n Type: Transition Metal',

'TA': ' Tantalum \n Chemical Symbol: Ta \n Element No.: 73 \n Electronegativity: 1.5 \n Atomic Weight: 180.948 \n Specific Heat: 0.140 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d³ 6s² \n Type: Transition Metal',
'TANTALUM': ' Tantalum \n Chemical Symbol: Ta \n Element No.: 73 \n Electronegativity: 1.5 \n Atomic Weight: 180.948 \n Specific Heat: 0.140 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d³ 6s² \n Type: Transition Metal',

'W': ' Tungsten \n Chemical Symbol: W \n Element No.: 74 \n Electronegativity: 2.36 \n Atomic Weight: 183.84 \n Specific Heat: 0.134 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁴ 6s² \n Type: Transition Metal',
'TUNGSTEN': ' Tungsten \n Chemical Symbol: W \n Element No.: 74 \n Electronegativity: 2.36 \n Atomic Weight: 183.84 \n Specific Heat: 0.134 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁴ 6s² \n Type: Transition Metal',

'RE': ' Rhenium \n Chemical Symbol: Re \n Element No.: 75 \n Electronegativity: 1.9 \n Atomic Weight: 186.207 \n Specific Heat: 0.137 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁵ 6s² \n Type: Transition Metal',
'RHENIUM': ' Rhenium \n Chemical Symbol: Re \n Element No.: 75 \n Electronegativity: 1.9 \n Atomic Weight: 186.207 \n Specific Heat: 0.137 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁵ 6s² \n Type: Transition Metal',

'OS': ' Osmium \n Chemical Symbol: Os \n Element No.: 76 \n Electronegativity: 2.2 \n Atomic Weight: 190.23 \n Specific Heat: 0.130 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁶ 6s² \n Type: Transition Metal',
'OSMIUM': ' Osmium \n Chemical Symbol: Os \n Element No.: 76 \n Electronegativity: 2.2 \n Atomic Weight: 190.23 \n Specific Heat: 0.130 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁶ 6s² \n Type: Transition Metal',

'IR': ' Iridium \n Chemical Symbol: Ir \n Element No.: 77 \n Electronegativity: 2.20 \n Atomic Weight: 192.217 \n Specific Heat: 0.131 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁷ 6s² \n Type: Transition Metal',
'IRIDIUM': ' Iridium \n Chemical Symbol: Ir \n Element No.: 77 \n Electronegativity: 2.20 \n Atomic Weight: 192.217 \n Specific Heat: 0.131 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁷ 6s² \n Type: Transition Metal',

'PT': ' Platinum \n Chemical Symbol: Pt \n Element No.: 78 \n Electronegativity: 2.28 \n Atomic Weight: 195.084 \n Specific Heat: 0.133 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁹ 6s¹ \n Type: Transition Metal',
'PLATINUM': ' Platinum \n Chemical Symbol: Pt \n Element No.: 78 \n Electronegativity: 2.28 \n Atomic Weight: 195.084 \n Specific Heat: 0.133 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d⁹ 6s¹ \n Type: Transition Metal',

'AU': ' Gold \n Chemical Symbol: Au \n Element No.: 79 \n Electronegativity: 2.54 \n Atomic Weight: 196.967 \n Specific Heat: 0.129 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d¹⁰ 6s¹ \n Type: Transition Metal',
'GOLD': ' Gold \n Chemical Symbol: Au \n Element No.: 79 \n Electronegativity: 2.54 \n Atomic Weight: 196.967 \n Specific Heat: 0.129 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5d¹⁰ 6s¹ \n Type: Transition Metal',

'HG': ' Mercury \n Chemical Symbol: Hg \n Element No.: 80 \n Electronegativity: 2.00 \n Atomic Weight: 200.592 \n Specific Heat: 0.140 (J/g * K) \n Phase: Liquid \n Valence Electron Configuration: 5d¹⁰ 6s² \n Type: Transition Metal',
'MERCURY': ' Mercury \n Chemical Symbol: Hg \n Element No.: 80 \n Electronegativity: 2.00 \n Atomic Weight: 200.592 \n Specific Heat: 0.140 (J/g * K) \n Phase: Liquid \n Valence Electron Configuration: 5d¹⁰ 6s² \n Type: Transition Metal',

'Tl': ' Thallium \n Chemical Symbol: Tl \n Element No.: 81 \n Electronegativity: 1.62 \n Atomic Weight: 204.38 \n Specific Heat: 0.129 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² 6p¹ \n Type: Post-Transition Metal',
'THALLIUM': ' Thallium \n Chemical Symbol: Tl \n Element No.: 81 \n Electronegativity: 1.62 \n Atomic Weight: 204.38 \n Specific Heat: 0.129 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² 6p¹ \n Type: Post-Transition Metal',

'PB': ' Lead \n Chemical Symbol: Pb \n Element No.: 82 \n Electronegativity: 2.33 \n Atomic Weight: 207.2 \n Specific Heat: 0.128 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² 6p² \n Type: Post-Transition Metal',
'LEAD': ' Lead \n Chemical Symbol: Pb \n Element No.: 82 \n Electronegativity: 2.33 \n Atomic Weight: 207.2 \n Specific Heat: 0.128 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² 6p² \n Type: Post-Transition Metal',

'BI': ' Bismuth \n Chemical Symbol: Bi \n Element No.: 83 \n Electronegativity: 2.02 \n Atomic Weight: 208.980 \n Specific Heat: 0.122 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² 6p³ \n Type: Post-Transition Metal',
'BISMUTH': ' Bismuth \n Chemical Symbol: Bi \n Element No.: 83 \n Electronegativity: 2.02 \n Atomic Weight: 208.980 \n Specific Heat: 0.122 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² 6p³ \n Type: Post-Transition Metal',

'PO': ' Polonium \n Chemical Symbol: Po \n Element No.: 84 \n Electronegativity: 2.0 \n Atomic Weight: [209] \n Specific Heat: 0.123 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² 6p⁴ \n Type: Metalloid',
'POLONIUM': ' Polonium \n Chemical Symbol: Po \n Element No.: 84 \n Electronegativity: 2.0 \n Atomic Weight: [209] \n Specific Heat: 0.123 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6s² 6p⁴ \n Type: Metalloid',

'AT': ' Astatine \n Chemical Symbol: At \n Element No.: 85 \n Electronegativity: 2.2 \n Atomic Weight: [210] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6s² 6p⁵ \n Type: Halogen',
'ASTATINE': ' Astatine \n Chemical Symbol: At \n Element No.: 85 \n Electronegativity: 2.2 \n Atomic Weight: [210] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6s² 6p⁵ \n Type: Halogen',

'RN': ' Radon \n Chemical Symbol: Rn \n Element No.: 86 \n Electronegativity: — \n Atomic Weight: [222] \n Specific Heat: 0.094 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 6s² 6p⁶ \n Type: Noble Gas',
'RADON': ' Radon \n Chemical Symbol: Rn \n Element No.: 86 \n Electronegativity: — \n Atomic Weight: [222] \n Specific Heat: 0.094 (J/g * K) \n Phase: Gas \n Valence Electron Configuration: 6s² 6p⁶ \n Type: Noble Gas',

'FR': ' Francium \n Chemical Symbol: Fr \n Element No.: 87 \n Electronegativity: 0.7 \n Atomic Weight: [223] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 7s¹ \n Type: Alkali Metal',
'FRANCIUM': ' Francium \n Chemical Symbol: Fr \n Element No.: 87 \n Electronegativity: 0.7 \n Atomic Weight: [223] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 7s¹ \n Type: Alkali Metal',

'RA': ' Radium \n Chemical Symbol: Ra \n Element No.: 88 \n Electronegativity: 0.9 \n Atomic Weight: 226 \n Specific Heat: 0.180 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 7s² \n Type: Alkaline Earth Metal',
'RADIUM': ' Radium \n Chemical Symbol: Ra \n Element No.: 88 \n Electronegativity: 0.9 \n Atomic Weight: 226 \n Specific Heat: 0.180 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 7s² \n Type: Alkaline Earth Metal',

'AC': ' Actinium \n Chemical Symbol: Ac \n Element No.: 89 \n Electronegativity: 1.1 \n Atomic Weight: 227 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6d¹ 7s² \n Type: Actinide',
'ACTINIUM': ' Actinium \n Chemical Symbol: Ac \n Element No.: 89 \n Electronegativity: 1.1 \n Atomic Weight: 227 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6d¹ 7s² \n Type: Actinide',

'TH': ' Thorium \n Chemical Symbol: Th \n Element No.: 90 \n Electronegativity: 1.3 \n Atomic Weight: 232.038 \n Specific Heat: 0.113 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6d² 7s² \n Type: Actinide',
'THORIUM': ' Thorium \n Chemical Symbol: Th \n Element No.: 90 \n Electronegativity: 1.3 \n Atomic Weight: 232.038 \n Specific Heat: 0.113 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 6d² 7s² \n Type: Actinide',

'PA': ' Protactinium \n Chemical Symbol: Pa \n Element No.: 91 \n Electronegativity: 1.5 \n Atomic Weight: 231.036 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f² 6d¹ 7s² \n Type: Actinide',
'PROTACTINIUM': ' Protactinium \n Chemical Symbol: Pa \n Element No.: 91 \n Electronegativity: 1.5 \n Atomic Weight: 231.036 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f² 6d¹ 7s² \n Type: Actinide',

'U': ' Uranium \n Chemical Symbol: U \n Element No.: 92 \n Electronegativity: 1.38 \n Atomic Weight: 238.029 \n Specific Heat: 0.116 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f³ 6d¹ 7s² \n Type: Actinide',
'URANIUM': ' Uranium \n Chemical Symbol: U \n Element No.: 92 \n Electronegativity: 1.38 \n Atomic Weight: 238.029 \n Specific Heat: 0.116 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f³ 6d¹ 7s² \n Type: Actinide',

'NP': ' Neptunium \n Chemical Symbol: Np \n Element No.: 93 \n Electronegativity: 1.36 \n Atomic Weight: 237 \n Specific Heat: 0.113 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f⁴ 6d¹ 7s² \n Type: Actinide',
'NEPTUNIUM': ' Neptunium \n Chemical Symbol: Np \n Element No.: 93 \n Electronegativity: 1.36 \n Atomic Weight: 237 \n Specific Heat: 0.113 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f⁴ 6d¹ 7s² \n Type: Actinide',

'PU': ' Plutonium \n Chemical Symbol: Pu \n Element No.: 94 \n Electronegativity: 1.28 \n Atomic Weight: 244 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f⁶ 7s² \n Type: Actinide',
'PLUTONIUM': ' Plutonium \n Chemical Symbol: Pu \n Element No.: 94 \n Electronegativity: 1.28 \n Atomic Weight: 244 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f⁶ 7s² \n Type: Actinide',

'AM': ' Americium \n Chemical Symbol: Am \n Element No.: 95 \n Electronegativity: 1.3 \n Atomic Weight: 243 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f⁷ 7s² \n Type: Actinide',
'AMERICIUM': ' Americium \n Chemical Symbol: Am \n Element No.: 95 \n Electronegativity: 1.3 \n Atomic Weight: 243 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f⁷ 7s² \n Type: Actinide',

'CM': ' Curium \n Chemical Symbol: Cm \n Element No.: 96 \n Electronegativity: 1.3 \n Atomic Weight: 247 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f⁷ 6d¹ 7s² \n Type: Actinide',
'CURIUM': ' Curium \n Chemical Symbol: Cm \n Element No.: 96 \n Electronegativity: 1.3 \n Atomic Weight: 247 \n Specific Heat: 0.12 (J/g * K) \n Phase: Solid \n Valence Electron Configuration: 5f⁷ 6d¹ 7s² \n Type: Actinide',

'BK': ' Berkelium \n Chemical Symbol: Bk \n Element No.: 97 \n Electronegativity: 1.3 \n Atomic Weight: 247 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f⁹ 7s² \n Type: Actinide',
'BERKELIUM': ' Berkelium \n Chemical Symbol: Bk \n Element No.: 97 \n Electronegativity: 1.3 \n Atomic Weight: 247 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f⁹ 7s² \n Type: Actinide',

'CF': ' Californium \n Chemical Symbol: Cf \n Element No.: 98 \n Electronegativity: 1.3 \n Atomic Weight: 251 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁰ 7s² \n Type: Actinide',
'CALIFORNIUM': ' Californium \n Chemical Symbol: Cf \n Element No.: 98 \n Electronegativity: 1.3 \n Atomic Weight: 251 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁰ 7s² \n Type: Actinide',

'ES': ' Einsteinium \n Chemical Symbol: Es \n Element No.: 99 \n Electronegativity: 1.3 \n Atomic Weight: 252 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹¹ 7s² \n Type: Actinide',
'EINSTEINIUM': ' Einsteinium \n Chemical Symbol: Es \n Element No.: 99 \n Electronegativity: 1.3 \n Atomic Weight: 252 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹¹ 7s² \n Type: Actinide',

'FM': ' Fermium \n Chemical Symbol: Fm \n Element No.: 100 \n Electronegativity: 1.3 \n Atomic Weight: 257 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹² 7s² \n Type: Actinide',
'FERMIUM': ' Fermium \n Chemical Symbol: Fm \n Element No.: 100 \n Electronegativity: 1.3 \n Atomic Weight: 257 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹² 7s² \n Type: Actinide',

'MD': ' Mendelevium \n Chemical Symbol: Md \n Element No.: 101 \n Electronegativity: 1.3 \n Atomic Weight: 258 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹³ 7s² \n Type: Actinide',
'MENDELEVIUM': ' Mendelevium \n Chemical Symbol: Md \n Element No.: 101 \n Electronegativity: 1.3 \n Atomic Weight: 258 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹³ 7s² \n Type: Actinide',

'NO': ' Nobelium \n Chemical Symbol: No \n Element No.: 102 \n Electronegativity: 1.3 \n Atomic Weight: 259 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 7s² \n Type: Actinide',
'NOBELIUM': ' Nobelium \n Chemical Symbol: No \n Element No.: 102 \n Electronegativity: 1.3 \n Atomic Weight: 259 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 7s² \n Type: Actinide',

'Lr': ' Lawrencium \n Chemical Symbol: Lr \n Element No.: 103 \n Electronegativity: 1.3 \n Atomic Weight: 262 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 7s² 7p¹ \n Type: Actinide',
'LAWRENCIUM': ' Lawrencium \n Chemical Symbol: Lr \n Element No.: 103 \n Electronegativity: 1.3 \n Atomic Weight: 262 \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 7s² 7p¹ \n Type: Actinide',

'RF': ' Rutherfordium \n Chemical Symbol: Rf \n Element No.: 104 \n Electronegativity: — \n Atomic Weight: [267] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d² 7s² \n Type: Transition Metal',
'RUTHERFORDIUM': ' Rutherfordium \n Chemical Symbol: Rf \n Element No.: 104 \n Electronegativity: — \n Atomic Weight: [267] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d² 7s² \n Type: Transition Metal',

'DB': ' Dubnium \n Chemical Symbol: Db \n Element No.: 105 \n Electronegativity: — \n Atomic Weight: [270] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d³ 7s² \n Type: Transition Metal',
'DUBNIUM': ' Dubnium \n Chemical Symbol: Db \n Element No.: 105 \n Electronegativity: — \n Atomic Weight: [270] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d³ 7s² \n Type: Transition Metal',

'Sg': ' Seaborgium \n Chemical Symbol: Sg \n Element No.: 106 \n Electronegativity: — \n Atomic Weight: [271] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁴ 7s² \n Type: Transition Metal',
'SEABORGIUM': ' Seaborgium \n Chemical Symbol: Sg \n Element No.: 106 \n Electronegativity: — \n Atomic Weight: [271] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁴ 7s² \n Type: Transition Metal',

'BH': ' Bohrium \n Chemical Symbol: Bh \n Element No.: 107 \n Electronegativity: — \n Atomic Weight: [270] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁵ 7s² \n Type: Transition Metal',
'BOHRIUM': ' Bohrium \n Chemical Symbol: Bh \n Element No.: 107 \n Electronegativity: — \n Atomic Weight: [270] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁵ 7s² \n Type: Transition Metal',

'HS': ' Hassium \n Chemical Symbol: Hs \n Element No.: 108 \n Electronegativity: — \n Atomic Weight: [277] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁶ 7s² \n Type: Transition Metal',
'HASSIUM': ' Hassium \n Chemical Symbol: Hs \n Element No.: 108 \n Electronegativity: — \n Atomic Weight: [277] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁶ 7s² \n Type: Transition Metal',

'MT': ' Meitnerium \n Chemical Symbol: Mt \n Element No.: 109 \n Electronegativity: — \n Atomic Weight: [278] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁷ 7s² \n Type: Transition Metal',
'MEITNERIUM': ' Meitnerium \n Chemical Symbol: Mt \n Element No.: 109 \n Electronegativity: — \n Atomic Weight: [278] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁷ 7s² \n Type: Transition Metal',

'DS': ' Darmstadtium \n Chemical Symbol: Ds \n Element No.: 110 \n Electronegativity: — \n Atomic Weight: [281] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁸ 7s² \n Type: Transition Metal',
'DARMSTADTIUM': ' Darmstadtium \n Chemical Symbol: Ds \n Element No.: 110 \n Electronegativity: — \n Atomic Weight: [281] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁸ 7s² \n Type: Transition Metal',

'RG': ' Roentgenium \n Chemical Symbol: Rg \n Element No.: 111 \n Electronegativity: — \n Atomic Weight: [282] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁹ 7s² \n Type: Transition Metal',
'ROENTGENIUM': ' Roentgenium \n Chemical Symbol: Rg \n Element No.: 111 \n Electronegativity: — \n Atomic Weight: [282] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 6d⁹ 7s² \n Type: Transition Metal',

'CN': ' Copernicium \n Chemical Symbol: Cn \n Element No.: 112 \n Electronegativity: — \n Atomic Weight: [285] \n Specific Heat: — \n Phase: Liquid \n Valence Electron Configuration: 6d¹⁰ 7s² \n Type: Transition Metal',
'COPERNICIUM': ' Copernicium \n Chemical Symbol: Cn \n Element No.: 112 \n Electronegativity: — \n Atomic Weight: [285] \n Specific Heat: — \n Phase: Liquid \n Valence Electron Configuration: 6d¹⁰ 7s² \n Type: Transition Metal',

'NH': ' Nihonium \n Chemical Symbol: Nh \n Element No.: 113 \n Electronegativity: — \n Atomic Weight: [286] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p¹ \n Type: Post-Transition Metal',
'NIHONIUM': ' Nihonium \n Chemical Symbol: Nh \n Element No.: 113 \n Electronegativity: — \n Atomic Weight: [286] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p¹ \n Type: Post-Transition Metal',

'FL': ' Flerovium \n Chemical Symbol: Fl \n Element No.: 114 \n Electronegativity: — \n Atomic Weight: [289] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p² \n Type: Post-Transition Metal',
'FLEROVIUM': ' Flerovium \n Chemical Symbol: Fl \n Element No.: 114 \n Electronegativity: — \n Atomic Weight: [289] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p² \n Type: Post-Transition Metal',

'MC': ' Moscovium \n Chemical Symbol: Mc \n Element No.: 115 \n Electronegativity: — \n Atomic Weight: [288] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p³ \n Type: Post-Transition Metal',
'MOSCOVIUM': ' Moscovium \n Chemical Symbol: Mc \n Element No.: 115 \n Electronegativity: — \n Atomic Weight: [288] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p³ \n Type: Post-Transition Metal',

'LV': ' Livermorium \n Chemical Symbol: Lv \n Element No.: 116 \n Electronegativity: — \n Atomic Weight: [293] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p⁴ \n Type: Post-Transition Metal',
'LIVERMORIUM': ' Livermorium \n Chemical Symbol: Lv \n Element No.: 116 \n Electronegativity: — \n Atomic Weight: [293] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p⁴ \n Type: Post-Transition Metal',

'TS': ' Tennessine \n Chemical Symbol: Ts \n Element No.: 117 \n Electronegativity: — \n Atomic Weight: [294] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p⁵ \n Type: Halogen',
'TENNESSINE': ' Tennessine \n Chemical Symbol: Ts \n Element No.: 117 \n Electronegativity: — \n Atomic Weight: [294] \n Specific Heat: — \n Phase: Solid \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p⁵ \n Type: Halogen',

'OG': ' Oganesson \n Chemical Symbol: Og \n Element No.: 118 \n Electronegativity: — \n Atomic Weight: [294] \n Specific Heat: — \n Phase: Gas \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p⁶ \n Type: Noble Gas',
'OGANESSON': ' Oganesson \n Chemical Symbol: Og \n Element No.: 118 \n Electronegativity: — \n Atomic Weight: [294] \n Specific Heat: — \n Phase: Gas \n Valence Electron Configuration: 5f¹⁴ 6d¹⁰ 7s² 7p⁶ \n Type: Noble Gas',

}


while (True):
    elem=input("\nWhat element would you like information about? (or type 'exit' to quit) ").upper()
    if elem.lower()=='exit':
        print('Thank you for using this program!')
        break

    elif elem in element.keys():
        print(element [elem])
    else:
        print('Please enter a valid element ')
