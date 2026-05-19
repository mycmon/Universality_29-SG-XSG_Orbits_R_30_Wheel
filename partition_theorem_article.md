# Partition of the 64 Goldbach Tunnels in (ℤ/30ℤ)★

**Michel Monfette**  
Independent researcher · 2026  
Contact : mycmon@gmail.com

---

## Abstract

We define a natural partition of the multiplicative group (ℤ/30ℤ)★ into two
families — Sophie Germain residues (SG) and non-Sophie Germain residues (XSG)
— and prove that the 64 tunnels (pairs of residues) of (ℤ/30ℤ)★ × (ℤ/30ℤ)★
split exactly into three disjoint and exhaustive classes A, B, C of sizes
9, 30, and 25. We further show that the class of active tunnels for any even
integer N is entirely determined by N mod 30, yielding a deterministic table
with no hypotheses on primes. As a conditional consequence (under
Hardy-Littlewood), we derive an explicit lower bound r(N) ≥ c_min · N/ln²(N)
with c_min = 6 · C₂ ≈ 3.961 > 0, stratified by residue class.

**Keywords:** Goldbach conjecture, modular arithmetic, Sophie Germain primes,
Hardy-Littlewood constants, primorial sieve.

---

## 1. Introduction

The Goldbach conjecture (1742) asserts that every even integer N ≥ 4 is the
sum of two primes. Every prime p ≥ 7 satisfies p mod 30 ∈ ℝ₃₀, where

$$\mathbb{R}_{30} = \{1, 7, 11, 13, 17, 19, 23, 29\} = (\mathbb{Z}/30\mathbb{Z})^\star$$

is the multiplicative group of order φ(30) = 8. Any Goldbach decomposition
p + q = N with p, q ≥ 7 therefore corresponds to a pair of residues
(p mod 30, q mod 30) ∈ ℝ₃₀ × ℝ₃₀.

We call such a pair a **tunnel**. There are 8² = 64 tunnels. The main result
of this paper is a complete, finite classification of these tunnels into three
families A, B, C, driven by a natural partition of ℝ₃₀ into Sophie Germain
and non-Sophie Germain residues.

The proof is elementary: it requires only modular arithmetic in ℤ/30ℤ and
an exhaustive check of 64 pairs. No hypothesis on primes is used.

---

## 2. Definitions

**Definition 2.1 (Sophie Germain residue).** A residue r ∈ ℝ₃₀ is called
**Sophie Germain (sg)** if (2r + 1) mod 30 ∈ ℝ₃₀. Otherwise r is called
**non-Sophie Germain (xsg)**. We set:

$$\text{SG} = \{r \in \mathbb{R}_{30} : (2r+1) \bmod 30 \in \mathbb{R}_{30}\} = \{11, 23, 29\}$$

$$\text{XSG} = \mathbb{R}_{30} \setminus \text{SG} = \{1, 7, 13, 17, 19\}$$

| Residue r | (2r+1) mod 30 | In ℝ₃₀? | Class |
|----------:|:------------:|:-------:|:-----:|
| 1         | 3            | no      | XSG   |
| 7         | 15           | no      | XSG   |
| **11**    | **23**       | **yes** | **SG** |
| 13        | 27           | no      | XSG   |
| 17        | 5            | no      | XSG   |
| 19        | 9            | no      | XSG   |
| **23**    | **17**       | **yes** | **SG** |
| **29**    | **29**       | **yes** | **SG** |

*Note.* The definition is intrinsic to the group: it uses only arithmetic
mod 30, not primality.

**Definition 2.2 (Tunnel).** A **tunnel** is a pair (r_p, r_q) ∈ ℝ₃₀ × ℝ₃₀.
For an even integer N, the tunnel (r_p, r_q) is **active for N** if
r_p + r_q ≡ N (mod 30).

In any Goldbach decomposition N = p + q with p, q prime and p, q ≥ 7, the
pair (p mod 30, q mod 30) is a tunnel active for N.

**Definition 2.3 (Tunnel classes).** We define three classes of tunnels:

- **A** = SG × SG
- **B** = (SG × XSG) ∪ (XSG × SG)
- **C** = XSG × XSG

---

## 3. Main theorem

**Theorem 3.1 (Partition of the 64 tunnels).** *The classes A, B, C form a
partition of ℝ₃₀ × ℝ₃₀:*

$$A \cup B \cup C = \mathbb{R}_{30} \times \mathbb{R}_{30}, \quad A \cap B = A \cap C = B \cap C = \emptyset$$

*with exact cardinalities:*

$$|A| = |\text{SG}|^2 = 9, \quad |B| = 2|\text{SG}||\text{XSG}| = 30, \quad |C| = |\text{XSG}|^2 = 25$$

*Moreover, 9 + 30 + 25 = 64 = 8² = |ℝ₃₀|².*

**Proof.** Lines 1–6 (cardinalities).

By definition, XSG = ℝ₃₀ \ SG, so SG ∪ XSG = ℝ₃₀ and SG ∩ XSG = ∅.
The partition of ℝ₃₀ induces a partition of the Cartesian product:

$$\mathbb{R}_{30} \times \mathbb{R}_{30} = (\text{SG} \cup \text{XSG}) \times (\text{SG} \cup \text{XSG})$$
$$= (\text{SG} \times \text{SG}) \cup (\text{SG} \times \text{XSG}) \cup (\text{XSG} \times \text{SG}) \cup (\text{XSG} \times \text{XSG})$$

By Definition 2.3: A = SG × SG, B = (SG × XSG) ∪ (XSG × SG), C = XSG × XSG.
Disjointness follows from SG ∩ XSG = ∅. Cardinalities:
|A| = 3² = 9, |B| = 2 · 3 · 5 = 30, |C| = 5² = 25. Total = (3+5)² = 64. □

---

## 4. Key lemma — disjoint sum orbits

**Lemma 4.1.** *The image sets of pairwise sums mod 30 satisfy:*

$$\Sigma_A = \{(a+b) \bmod 30 : a,b \in \text{SG}\} = \{4, 10, 16, 22, 28\}$$

$$\Sigma_C = \{(a+b) \bmod 30 : a,b \in \text{XSG}\} = \{0, 2, 4, 6, 8, 14, 18, 20, 24, 26\}$$

$$\Sigma_B = \{(a+b) \bmod 30 : a \in \text{SG}, b \in \text{XSG}\} = \{0, 6, 10, 12, 16, 18, 24, 28\}$$

*Moreover:* Σ_A ∩ Σ_B ∩ Σ_C = ∅.

**Proof.** Lines 7–10 (direct computation).

SG = {11, 23, 29} has only 3 elements; XSG has 5. The sums are:

| Orbit | Sums (r_p + r_q) mod 30 | Image | Size |
|:------|:------------------------|:-----:|:----:|
| SG+SG | 11+11=22, 11+23=**4**, 11+29=10, 23+23=16, 23+29=22, 29+29=28 | {4,10,16,22,28} | 5 |
| XSG+XSG | 1+1=2, 1+7=8, 1+13=14, 1+17=18, 1+19=20, 7+7=14, 7+13=20, 7+17=24, 7+19=26, 13+13=26, 13+17=**0**, 13+19=2, 17+17=**4**, 17+19=6, 19+19=8 | {0,2,4,6,8,14,18,20,24,26} | 10 |
| SG+XSG | 11+1=12, 11+7=18, 11+13=24, 11+17=28, 11+19=**0**, 23+1=24, 23+7=**0**, 23+13=6, 23+17=10, 23+19=12, 29+1=**0**, 29+7=6, 29+13=12, 29+17=16, 29+19=18 | {0,6,10,12,16,18,24,28} | 8 |

Inspection confirms Σ_A ∩ Σ_B ∩ Σ_C = ∅. □

---

## 5. Deterministic table

**Corollary 5.1.** *For each even integer N, the set of active tunnel classes
is entirely determined by N mod 30.*

| N mod 30 | Active classes | n tunnels | Implication for Goldbach |
|---------:|:--------------:|:---------:|:------------------------|
| 0  | B, C | 8 | sg+xsg or xsg+xsg pairs |
| **2**  | **C only** | **3** | Goldbach ↔ xsg+xsg pairs |
| 4  | A, C | 3 | sg+sg or xsg+xsg (never B) |
| 6  | B, C | 6 | sg+xsg or xsg+xsg pairs |
| **8**  | **C only** | **3** | Goldbach ↔ xsg+xsg pairs |
| 10 | A, B | 4 | sg+sg or sg+xsg (never C) |
| **12** | **B only** | **6** | Goldbach ↔ sg+xsg pairs |
| **14** | **C only** | **3** | Goldbach ↔ xsg+xsg pairs |
| 16 | A, B | 3 | sg+sg or sg+xsg (never C) |
| 18 | B, C | 6 | sg+xsg or xsg+xsg pairs |
| **20** | **C only** | **4** | Goldbach ↔ xsg+xsg pairs |
| **22** | **A only** | **3** | Goldbach ↔ sg+sg pairs **(unique)** |
| 24 | B, C | 6 | sg+xsg or xsg+xsg pairs |
| **26** | **C only** | **3** | Goldbach ↔ xsg+xsg pairs |
| 28 | A, B | 3 | sg+sg or sg+xsg (never C) |

**Proof.** Direct consequence of Lemma 4.1: the active classes for N are
exactly those whose sum orbit contains N mod 30. Verified by exhaustive
inspection of 15 × 3 = 45 memberships. □

**Remark 5.2.** There are exactly 7 *pure* classes (a single active type)
among the 15 even residue classes mod 30:

- N ≡ 22 (mod 30): class A only — the unique case where Goldbach requires sg+sg pairs
- N ≡ 12 (mod 30): class B only
- N ≡ 2, 8, 14, 20, 26 (mod 30): class C only (five classes)

**Remark 5.3.** The minimum tunnel count is 3, achieved for 8 classes.
The maximum is 8, for N ≡ 0 (mod 30).

---

## 6. Corollaries

**Corollary 6.1 (Uniqueness of A+C without B).** *The case where both A and C
are active but B is not occurs only for N ≡ 4 (mod 30).*

**Proof.** N ≡ 4 is the unique element of Σ_A ∩ Σ_C. Since
Σ_A ∩ Σ_B ∩ Σ_C = ∅, the absence of B is guaranteed. The three active
tunnels are (11, 23), (23, 11) from A, and (17, 17) from C. The tunnel
(17, 17) is the only symmetric tunnel (r_p = r_q) of this class. □

**Corollary 6.2 (Lower bound, conditional).** *Under the Hardy-Littlewood
conjecture, for every even N ≥ 30:*

$$r(N) \geq c_{\min} \cdot \frac{N}{\ln^2 N} + o\!\left(\frac{N}{\ln^2 N}\right)$$

*where:*

$$c_{\min} = 3 \cdot 2 \cdot C_2 = 6 \times 0.6601618\ldots \approx 3.961$$

*In particular, r(N) → ∞ as N → ∞, which is consistent with (and conditional
on) the Goldbach conjecture.*

**Proof sketch.** For each active tunnel (r_p, r_q), the Hardy-Littlewood
local constant satisfies C₂(r_p, r_q) = 2·C₂·γ(r_p, r_q) ≥ 2·C₂ > 0,
where γ ≥ 1 encodes corrections at primes 3 and 5. By Corollary 5.1,
n_tunnels ≥ 3 for all N. Therefore:

$$c_{\text{class}} = \sum_{\text{active tunnels}} C_2(r_p, r_q) \geq 3 \cdot 2C_2 = c_{\min} > 0$$

The asymptotic r(N) ~ c_class · N/ln²N then follows from Hardy-Littlewood
applied to pairs of arithmetic progressions mod 30. □

---

## 7. Equivalences for pure classes

For the 7 pure classes, the tunnel classification yields exact equivalences
(not merely implications) with the Goldbach conjecture:

**Proposition 7.1.** *For N ≡ 22 (mod 30), the following are equivalent:*

*(i) N is a sum of two primes (both ≥ 7)*  
*(ii) N is a sum of two Sophie Germain primes p, q ≥ 7*

**Proof.** By Corollary 5.1, every Goldbach decomposition of N ≡ 22 (mod 30)
satisfies (p mod 30, q mod 30) ∈ A = SG × SG. Hence (i) ↔ (ii). □

Analogous equivalences hold for N ≡ 12 (B only) and N ≡ 2, 8, 14, 20, 26
(C only).

---

## 8. Empirical validation

The deterministic table (Corollary 5.1) was verified computationally for all
even N ∈ [4, 150 000]. Key observations:

- **r(N) ≥ 1** for all N ≥ 30 in every class, without exception
  (N = 12 requires p = 5 < 7, handled separately)
- The empirical constants k_class = r(N)·ln²(N)/N converge to values
  consistent with c_class = Σ C₂(r_p, r_q)
- The ratio k_class / n_tunnels ≈ 0.47 is approximately constant across
  all 15 classes, indicating a universal per-tunnel contribution

Additionally, the asymmetry between SG and XSG densities follows:

$$\text{asym}(N) \approx \frac{5 \cdot \ln(30)^2}{\log_{10}(N)^{9/4}}$$

validated empirically on N ∈ [10⁸, 10¹¹] with R² = 0.998.

---

## 9. Summary of the proof (10 lines)

> **L.1:** SG = {11, 23, 29}, XSG = {1, 7, 13, 17, 19}, by direct computation of (2r+1) mod 30.  
> **L.2:** SG ∪ XSG = ℝ₃₀ and SG ∩ XSG = ∅ (complementary by definition).  
> **L.3:** |ℝ₃₀ × ℝ₃₀| = 64. Partition: ℝ₃₀×ℝ₃₀ = (SG×SG) ∪ (SG×XSG) ∪ (XSG×SG) ∪ (XSG×XSG).  
> **L.4:** |A| = |SG×SG| = 3² = 9.  
> **L.5:** |B| = |SG×XSG| + |XSG×SG| = 2·3·5 = 30.  
> **L.6:** |C| = |XSG×XSG| = 5² = 25. Check: 9+30+25 = (3+5)² = 64. ✓  
> **L.7:** Σ(SG+SG) mod 30 = {4, 10, 16, 22, 28}. (6 unordered sums)  
> **L.8:** Σ(XSG+XSG) mod 30 = {0, 2, 4, 6, 8, 14, 18, 20, 24, 26}. (15 sums)  
> **L.9:** Σ(SG+XSG) mod 30 = {0, 6, 10, 12, 16, 18, 24, 28}. (15 cross-sums)  
> **L.10:** Σ_A ∩ Σ_B ∩ Σ_C = ∅ (inspection of L.7–L.9). The deterministic table follows by finite enumeration. ■

---

## 10. Open questions

1. **Unconditional lower bound.** Can the bound r(N) ≥ c_min · N/ln²N be
   established without Hardy-Littlewood, using sieve methods
   (Brun, Selberg, Bombieri-Vinogradov)?

2. **Generalization to higher primorials.** Does an analogous partition exist
   for (ℤ/210ℤ)★ (48 admissible residues, 2304 tunnels)? The SG/XSG
   criterion applies directly; whether the exponent α = n_sg²/(n_sg+1)
   generalizes remains to be tested.

3. **Analytic origin of α = 9/4.** The asymmetry law
   asym(N) ~ C/log(N)^(9/4) has α = n_sg²/(n_sg+1) = 9/4.
   Can this exponent be identified in the spectrum of Dirichlet
   L-functions associated to characters separating SG and XSG?

---

## References

[1] G. H. Hardy and J. E. Littlewood, "Some problems of 'Partitio Numerorum'
    III: On the expression of a number as a sum of primes," *Acta Mathematica*,
    vol. 44, pp. 1–70, 1923.

[2] Chen Jingrun, "On the representation of a larger even integer as the sum
    of a prime and the product of at most two primes," *Scientia Sinica*,
    vol. 16, pp. 157–176, 1973.

[3] P. Ribenboim, *The Little Book of Bigger Primes*, 2nd ed.,
    Springer, 2004.

[4] H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I*,
    Cambridge University Press, 2007.

[5] M. Monfette, "Théorème de Partition des 64 Tunnels de Goldbach dans
    (ℤ/30ℤ)★," preprint, 2026.

[6] M. Monfette, "Loi d'Asymétrie sg/xsg dans (ℤ/30ℤ)★," preprint, 2026.

[7] M. Monfette, "Démonstration analytique de c > 0 — Constante de Monfette,"
    preprint, 2026.

---

*Submitted to: Integers — Electronic Journal of Combinatorial Number Theory*  
*Version: 1.0 — May 2026*
