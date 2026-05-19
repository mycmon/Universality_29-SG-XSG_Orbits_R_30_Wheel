## **README.md **

------

## **README — Reformulation de Goldbach modulo 30 et Loi p–e**

**Auteur : Michel Monfette**  
 **Dernière mise à jour : 16 avril 2026**

------

## **Objectif du projet**

Ce dépôt présente une **reformulation structurelle de la conjecture de Goldbach** dans le cadre :

- du **crible primorial** $$(mod 30, 210, 2310, 30030)$$,
- de la **Loi p–e de Monfette** (structure exacte des résidus admissibles),
- de la **Conjecture Cube-Orbit** (lecture géométrique en grille 3×3),
- et d’une **analyse empirique complète** de $$(G(N))$$ et du ratio $$réalisations/admissibles$$.

Le projet inclut :

- un **programme Python/Tkinter** permettant de calculer :
  - Goldbach **mod primorial** (admissibles vs réalisations),
  - Goldbach **complet** (calcul exact de $$(G(N)))$$,
- des **rapports Markdown** et **CSV** générés automatiquement,
- des **graphes** comparant données observées et prédictions Hardy–Littlewood.

------

## 📌 **Contenu du dépôt**

```
goldbach/
│
├── src/
│   ├── goldbach_v4.py          # Application Tkinter complète
│
├── docs/
│   ├── Reformulation_Goldbach_mod30.md
│   ├── Résumé ci-dessous
│
├── goldbach_results/
│   ├── *.csv
│   ├── *.md
│   └── *.png
│
└── README.md
```

------

## **Résumé **

### 1. **Loi p–e de Monfette**

Relation exacte pour les résidus admissibles d’un k-uplet :

​				$$ \text{Res}(P_{n+1}) = \text{Res}(P_n),(p_{n+1}-k)$$

Pour $$(k=2)$$, elle donne  Loi p–e la constante de Hardy–Littlewood :

​				$$ C_2 = \prod_{p\ge 3} \frac{p(p-2)}{(p-1)^2} \approx 0.6601683 $$

------

### 2. **Reformulation de Goldbach modulo 30**

Pour tout pair $$(N\ge 4)$$, il existe :

- une paire admissible $$((a,b)\in \mathcal{R}_{30}^2)$$,

  - une paire de premiers $$((p,q))$$ telle que :  

    ​		  $$N = p+q,\quad p\equiv a\pmod{30},\quad q\equiv b\pmod{30}. $$$$


La partie **combinatoire** est prouvée.
 La partie **arithmétique** est équivalente à Goldbach.

------

### 3. **Conjecture Cube-Orbit**

- 45 orbites admissibles,
- période minimale **30**,
- densité uniforme **1/30**,
- erreur **O(1)** pour les candidats.

Cette structure géométrique clarifie le rôle du crible primorial.

---

### **4. Analyse empirique**

Le programme calcule :

- $$(G(N))$$ complet,
- le ratio réalisations/admissibles mod $$(P_k)$$,
- le $$(C_2(N))$$ empirique :      $$C_2(N) = \frac{G(N),\log^2 N}{2N} $$

Les résultats montrent :

- convergence lente mais stable vers $$(C_2)$$,
- croissance régulière du ratio mod primorial,
- cohérence avec Hardy–Littlewood.

------

### **Utilisation**

Lancer l’application :

```bash
python3 goldbach_v4.py
```

Fonctionnalités :

- Choix du mode : **Mod primorial** ou **Complet**
- Choix du modulo : 30, 210, 2310, 30030
- Entrée d’une liste de valeurs $$(N)$$
- Export automatique :
  - CSV
  - Markdown
  - Graphiques PNG

------

### **Exemples de résultats**

Goldbach complet

| N           | G(N)      | C₂(N) |
| ----------- | --------- | ----- |
| 1 000       | 28        | 0.668 |
| 10 000      | 127       | 0.538 |
| 1 000 000   | 5402      | 0.515 |
| 500 000 000 | 1 219 610 | 0.489 |

------

### **Documents recommandés**

Pour comprendre la démarche :

- `Reformulation_Goldbach_mod30.md`
- `Loi_p-e_Monfette.md`
- `Cube_Orbit_Theory.md`
- `goldbach_full_rapport_*.md`
- `goldbach_mod_rapport_*.md`

------

### **Licence**

Projet libre d’étude et de recherche.
 Toute reproduction doit citer l’auteur : **Michel Monfette**.

