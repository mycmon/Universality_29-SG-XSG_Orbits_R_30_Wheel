**Reformulation de Goldbach modulo 30**  
**Une approche structurelle via la Loi p-e de Monfette et la Conjecture Cube-Orbit**

**Version complète et autonome – 16 avril 2026**  
**Auteur** : Michel Monfette

---

### 1. Contexte et définition de la Loi p-e

La **Loi p-e** (ou Loi p-k) est une relation combinatoire exacte qui décrit comment évolue le nombre de résidus admissibles lorsqu’on étend le primorial \(P_n = 2 \cdot 3 \cdots p_n\).

Pour un k-uplet admissible (ici k=2 pour les **premiers sûrs** ou SG : \(p\) et \(2p+1\)), la loi s’écrit :

\[
\text{Res}(P_{n+1}) = \text{Res}(P_n) \times (p_{n+1} - k)
\]

Cette relation est **exacte** et **déterministe**. Elle justifie le facteur local \((1 - k/p)\) de la conjecture de Hardy-Littlewood et donne la constante :

\[
C_2 = \prod_{p \ge 3} \frac{p(p-2)}{(p-1)^2} \approx 0.6601683
\]

dans l’asymptotique :

\[
\pi_{\text{SG}}(x) \sim C_2 \cdot \mathrm{li}_2(x)
\]

---

### 2. Conjecture Cube-Orbit (représentation géométrique)

Pour rendre la Loi p-e visuelle, l’auteur a introduit la **grille 3×3 de carrés** (Cube-Orbit) sur les positions candidates modulo 8 (C1, C3, C5, C7). Chaque nombre est projeté sur un label cube A1–C9.

**Figure 1 : Exemple de grille 3×3 Cube-Orbit pour N = 94**  
*(image à insérer : la grille 3×3 avec les cubes A1–C9 et les liaisons bleu/rose/orange pour N=94)*

Cette grille montre les 45 orbites admissibles de période minimale 30 et de densité uniforme \(\alpha = 1/30\).

---

### 3. Reformulation de Goldbach modulo 30

**Proposition 3.1 (Goldbach modulo 30 – version structurelle)**

Pour tout entier pair \(N \ge 4\), il existe une paire de résidus admissibles \((a,b) \in \mathcal{R}_{30}^2\) telle que :

\[
a + b \equiv N \pmod{30},
\]

et il existe des nombres premiers \(p, q\) vérifiant :

\[
N = p + q, \quad p \equiv a \pmod{30}, \quad q \equiv b \pmod{30}.
\]

---

### 4. Partie combinatoire (prouvée)

**Lemme 4.1**  
Pour tout entier pair \(N\), il existe au moins une paire \((a,b) \in \mathcal{R}_{30}^2\) telle que \(a + b \equiv N \pmod{30}\).

**Preuve** : vérification exhaustive que l’ensemble des sommes \(a + b \pmod{30}\) couvre tous les résidus pairs. ∎

---

### 5. Exemples concrets

#### Exemple 5.1 — \(N = 94\)

\[
94 \equiv 4 \pmod{30}
\]

Paires admissibles modulo 30 :

- \((11, 23)\)
- \((17, 17)\)

Réalisation observée :

\[
94 = 11 + 83
\]

- \(11 \equiv 11 \pmod{30}\)
- \(83 \equiv 23 \pmod{30}\)

→ La paire admissible \((11, 23)\) est réalisée par deux premiers.

#### Exemple 5.2 — \(N = 2024\)

\[
2024 \equiv 14 \pmod{30}
\]

Paires admissibles :

- \((1, 13)\)
- \((7, 7)\)

Réalisation observée :

\[
2024 = 13 + 2011
\]

- \(13 \equiv 13 \pmod{30}\)
- \(2011 \equiv 1 \pmod{30}\)

→ La paire admissible \((1, 13)\) est réalisée par deux premiers.

#### Exemple 5.3 — \(N = 1\,000\,000\) (grand nombre)

Pour MOD = 30030, on a 992 classes admissibles.  
Parmi elles, 5 402 réalisations réelles ont été trouvées.  
Le ratio = 5.4456 montre que chaque classe admissible contient en moyenne plus de 5 vraies partitions.

**Figure 2 : Évolution du ratio réalisations/admissibles pour MOD = 30030**  
*(image à insérer : le graphique linéaire et log que tu as déjà généré – courbe bleue observée vs courbe rouge théorique)*

On voit clairement la croissance rapide du ratio, conforme à la prédiction asymptotique de Hardy-Littlewood.

---

### 6. Lien avec la Loi p-e et la constante \(C_2\)

La Loi p-e donne la relation exacte pour les candidats.  
La reformulation modulo 30 montre que Goldbach est équivalente à l’existence d’une réalisation première dans l’une des 45 orbites admissibles de la grille Cube-Orbit.

Le \(C_2\) empirique pondéré converge lentement vers la valeur théorique 0.660168.

---

### 7. Conclusion

La reformulation de Goldbach modulo 30 :

- Sépare nettement la partie **combinatoire prouvée** (existence de paires admissibles) de la partie **arithmétique ouverte** (existence de deux premiers).
- Fournit un cadre géométrique clair via la grille Cube-Orbit et la Loi p-e.
- Montre que le crible primorial élimine toutes les obstructions locales.

Cette approche ne prouve pas Goldbach, mais elle en donne une présentation structurelle, visuelle et cohérente avec la Loi p-e, qui peut servir de base à de nouvelles approches analytiques.

---

