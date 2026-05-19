# **Conjecture G — Version 2 (2026)**

## **Universalité des 29 orbites SG/XSG sur la roue R₃₀**

### *Document technique + visuel — Style Monfette*

------

# **Résumé exécutif**

La **Conjecture G v2** établit l’universalité des **29 orbites** (24 SG + 5 XSG) sur la roue mod 30, confirmée empiriquement jusqu’à
 [ 2n = 200,000,000. ]

Les trois invariants universels — **p_médian**, **taux p₁%**, **couverture totale** — sont confirmés sur les 29 orbites.
 Les 5 orbites XSG complètent exactement les 5 résidus non couverts par les familles SG.

Les résultats empiriques couvrent **193 333 305 décompositions valides**, sans aucun contre‑exemple pour (2n \ge 200).

------

# **1. Introduction**

La structure modulaire des nombres premiers modulo 30 révèle trois familles SG fondamentales :

- **SG(11)**
- **SG(23)**
- **SG(29)**

Chacune définit 8 orbites vers les résidus admissibles
 [ R_0 = {1,7,11,13,17,19,23,29}. ]

À ces 24 orbites SG s’ajoutent **5 orbites XSG**, couvrant les résidus pairs non accessibles aux familles SG.

La Conjecture G v2 affirme que :

- les 29 orbites sont **universelles**,
- chacune atteint **100% de couverture**,
- les invariants statistiques sont **identiques** pour toutes les orbites d’une même famille,
- la structure est **entièrement déterminée par la famille source**, jamais par la cible.

------

# **2. Les 29 orbites SG/XSG**

## **2.1 Les 24 orbites SG**

Chaque famille SG(rₚ) génère 8 orbites vers les résidus de R₀.

### **Figure — Carte complète des 24 orbites SG sur R₃₀**

```
[Il semble que le résultat n’était pas sûr à afficher. Changeons un peu et essayons autre chose !]
```

------

## **2.2 Les 5 orbites XSG**

Elles couvrent exactement les résidus :

[ {2,8,14,20,26} \pmod{30} ]

### **Figure — Classes admissibles pour les 5 résidus non couverts par SG**

```
[Il semble que le résultat n’était pas sûr à afficher. Changeons un peu et essayons autre chose !]
```

------

# **3. Couverture des 15 résidus de 2n**

Les 24 orbites SG couvrent exactement **10 résidus sur 15**.
 Les 5 restants sont couverts par les orbites XSG.

### **Figure — Couverture des 15 résidus de 2n**

```
[Il semble que le résultat n’était pas sûr à afficher. Changeons un peu et essayons autre chose !]
```

------

# **4. Résultats empiriques jusqu’à 200 000 000**

Les 29 orbites ont été testées sur :

- **6 666 665 valeurs de 2n** chacune
- soit **193 333 305 décompositions valides**
- aucune exception pour (2n \ge 200)

Les trois invariants universels sont confirmés.

------

# **5. Invariants universels (version 2)**

## **Invariant I — p_médian**

Le p_médian est **constant par famille**, et correspond au **3ᵉ élément** de la famille à (N = 2\times10^8).

| Famille | p₁   | p₂   | p₃ = p_médian | Variation |
| ------- | ---- | ---- | ------------- | --------- |
| SG(11)  | 11   | 41   | **131**       | +1 rang   |
| SG(23)  | 23   | 53   | **83**        | +1 rang   |
| SG(29)  | 29   | 89   | **179**       | +1 rang   |
| XSG(1)  | 31   | 61   | **151**       | +1 rang   |
| XSG(7)  | 7    | 37   | **67**        | +1 rang   |

### **Figure — p_médian universel par famille**

```
[Il semble que le résultat n’était pas sûr à afficher. Changeons un peu et essayons autre chose !]
```

------

## **Invariant II — Taux p₁%**

À (N = 2\times10^8), le taux d’utilisation du premier élément de la famille est :

[ p_1% = 20.8% ]

Universel sur les 29 orbites.

------

## **Invariant III — Couverture totale**

Les 29 orbites atteignent **100% de couverture** jusqu’à (2n = 200,000,000).

------

# **6. Conjecture G — Version 2 (formulation formelle)**

## **Partie I — Combinatoire (inconditionnelle)**

Pour tout (r_p \in {11,23,29}) et tout (r_q \in R_0), l’orbite SG(rₚ)→r_q est admissible pour
 [ 2n \equiv r_p + r_q \pmod{30}. ]

Les 24 orbites couvrent exactement 10 résidus.

## **Partie II — Analytique (sous GEH)**

La série singulière de chaque orbite est strictement positive :
 [ \mathfrak{S}(\text{orbite}) > 0. ]

## **Partie III — Invariants universels**

- p_médian constant par famille
- taux p₁% universel
- couverture totale

## **Partie IV — Empirique**

Aucun contre‑exemple jusqu’à (2\times10^8).

------

# **7. Loi p‑e et loi p‑k**

## **Loi p‑e (cas SG)**

Pour les familles SG :

[ S_{n+1} = S_n (p_{n+1} - 2) ]

Identité exacte.

## **Loi p‑k (généralisation)**

Pour une constellation de k contraintes :

[ \operatorname{Res}*k(P*{n+1}) = \operatorname{Res}*k(P_n)(p*{n+1} - k) ]

------

# **8. Fausses paires Goldbach**

Sur 200M :

- **0 fausse paire stricte**
- **719 370 587 candidats rejetés** (q composé)
- **193 333 305 vraies paires** validées

------

# **9. Discussion**

La Conjecture G v2 révèle une structure :

- **rigide**,
- **universelle**,
- **indépendante de la cible**,
- **déterminée uniquement par la famille source**.

Les orbites SG/XSG forment une **partition complète** des résidus pairs modulo 30.

------

# **10. Annexes**

## **Table complète des 29 orbites (résultats à 200M)**

*(Tableau complet identique à celui fourni dans ton document v2 — je peux l’insérer ici si tu veux.)*

------

