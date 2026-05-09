#!/usr/bin/env python3
"""
=============================================================================
MONFETTE CORPUS 2026 — ANALYSE BILINGUE & VÉRIFICATION AUTOMATIQUE
=============================================================================
Projet  : Conjecture Générale (Monfette) v3
Auteur  : Michel Monfette — Chicoutimi, Saguenay, Québec
Usage   : python3 monfette_2026_v3.py [N]  (défaut N=200_000)
=============================================================================

CORRECTIONS vs version précédente :
  - Crible de Ératosthène : accélération 15-50× pour grands N
  - Fichier horodaté (pas d'accumulation indéfinie)
  - Terminologie épistémique correcte (vérification ≠ preuve)
  - Tableau enrichi : 𝔖, p₁%, rejetés
  - Séparateurs visuels entre familles SG(11)/SG(23)/SG(29)/XSG
  - Rapport Markdown séparé pour publication
=============================================================================
"""

import sys, time, os
from math import log
from statistics import median
from sympy import primerange

# ── Configuration ─────────────────────────────────────────────────────────────
N       = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000_000
TS      = time.strftime('%Y%m%d_%H%M%S')
OUT_TXT = f"monfette_2026_{TS}.txt"
OUT_MD  = f"monfette_2026_{TS}.md"
R30     = [1, 7, 11, 13, 17, 19, 23, 29]
SG_RES  = {11, 23, 29}

# ── Helpers bilingues ─────────────────────────────────────────────────────────
def bilingual(fr, en):
    """Affiche et retourne une ligne bilingue."""
    line = f"  FR: {fr}\n  EN: {en}"
    print(line)
    return line + "\n"

def section(title_fr, title_en, char="═", width=80):
    line = char * width
    out = f"\n{line}\n  {title_fr} / {title_en}\n{line}"
    print(out)
    return out + "\n"

def subsection(title, width=70):
    out = f"\n  ── {title} {'─'*(width-len(title)-5)}"
    print(out)
    return out + "\n"

# ── Crible de Ératosthène ─────────────────────────────────────────────────────
def build_sieve(n):
    """Crible de Ératosthène — retourne un bytearray de booléens."""
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(s[i*i::i]))
    return s

# ── Série singulière HL ───────────────────────────────────────────────────────
def serie_singulieres(rp, rq, is_sg):
    sp = 2*rp + 1
    forms = [(30, rp), (60, sp), (30, rq)] if is_sg else [(30, rp), (30, rq)]
    k = len(forms)
    S = 1.0
    for l in primerange(2, 300):
        forbidden = set()
        total_obs = False
        for (a, b) in forms:
            am, bm = a % l, b % l
            if am == 0:
                if bm == 0: total_obs = True; break
            else:
                forbidden.add((-bm * pow(am, -1, l)) % l)
        if total_obs: return 0.0
        S *= (1 - len(forbidden)/l) * (1 - 1/l)**(-k)
    return S

# ── Définition des 29 orbites ─────────────────────────────────────────────────
ORBITES = [
    # SG(11) ──────────────────────────────────────────────────────────
    (11, 1, 12, 'SG'), (11, 7,  18, 'SG'), (11, 11, 22, 'SG'),
    (11, 13, 24, 'SG'), (11, 17, 28, 'SG'), (11, 19,  0, 'SG'),
    (11, 23,  4, 'SG'), (11, 29, 10, 'SG'),
    # SG(23) ──────────────────────────────────────────────────────────
    (23,  1, 24, 'SG'), (23,  7,  0, 'SG'), (23, 11,  4, 'SG'),
    (23, 13,  6, 'SG'), (23, 17, 10, 'SG'), (23, 19, 12, 'SG'),
    (23, 23, 16, 'SG'), (23, 29, 22, 'SG'),
    # SG(29) ──────────────────────────────────────────────────────────
    (29,  1,  0, 'SG'), (29,  7,  6, 'SG'), (29, 11, 10, 'SG'),
    (29, 13, 12, 'SG'), (29, 17, 16, 'SG'), (29, 19, 18, 'SG'),
    (29, 23, 22, 'SG'), (29, 29, 28, 'SG'),
    # XSG ─────────────────────────────────────────────────────────────
    ( 1,  1,  2, 'XSG'), ( 1,  7,  8, 'XSG'), ( 1, 13, 14, 'XSG'),
    ( 1, 19, 20, 'XSG'), ( 7, 19, 26, 'XSG'),
]

# ── Programme principal ───────────────────────────────────────────────────────
def main():
    lines = []  # buffer pour fichiers de sortie

    def out(txt):
        lines.append(txt)

    # Entête
    out(section("RAPPORT MONFETTE 2026", "MONFETTE 2026 REPORT"))
    out(bilingual(f"Date       : {time.strftime('%Y-%m-%d %H:%M:%S')}",
                  f"Date       : {time.strftime('%Y-%m-%d %H:%M:%S')}"))
    out(bilingual(f"Limite N   : {N:,}", f"Limit N    : {N:,}"))

    t_total = time.time()

    # ── Étape 1 : Crible ────────────────────────────────────────────────────
    out(subsection("Étape 1 / Step 1 : Crible de Ératosthène / Sieve of Eratosthenes"))
    t0 = time.time()
    sieve = build_sieve(N)
    t_sieve = time.time() - t0
    nb_primes = sum(sieve[2:])
    out(bilingual(f"Crible [2,{N:,}] : {nb_primes:,} premiers  [{t_sieve:.2f}s]",
                  f"Sieve [2,{N:,}] : {nb_primes:,} primes  [{t_sieve:.2f}s]"))

    # ── Étape 2 : Familles ─────────────────────────────────────────────────
    out(subsection("Étape 2 / Step 2 : Familles / Families"))
    t0 = time.time()
    FAM = {}
    for rp in R30:
        if rp in SG_RES:
            FAM[rp] = [p for p in range(rp, N+1, 30)
                       if sieve[p] and (2*p+1 <= N and sieve[2*p+1])]
        else:
            FAM[rp] = [p for p in range(rp, N+1, 30) if sieve[p]]
    t_fam = time.time() - t0

    for rp in sorted(FAM):
        typ = "SG " if rp in SG_RES else "non-SG"
        p1  = FAM[rp][0] if FAM[rp] else '—'
        p2  = FAM[rp][1] if len(FAM[rp]) > 1 else '—'
        out(bilingual(
            f"  F({rp:2d}) [{typ}] : {len(FAM[rp]):6,} éléments  p₁={p1}  p₂={p2}",
            f"  F({rp:2d}) [{typ}] : {len(FAM[rp]):6,} elements  p₁={p1}  p₂={p2}"))
    out(bilingual(f"Temps / Time : {t_fam:.2f}s", f"Time: {t_fam:.2f}s"))

    # ── Étape 3 : Orbites ─────────────────────────────────────────────────
    out(section("TABLEAU DES 29 ORBITES", "TABLE OF 29 ORBITS", "─"))

    hdr = (f"  {'Orbite/Orbit':<15} {'2n≡':>5} {'★':>2} "
           f"{'Testés':>9} {'Succès':>9} {'Couv%':>7} "
           f"{'p_méd':>7} {'p₁%':>7} {'𝔖':>8} {'Rejetés':>9}")
    print(hdr); out(hdr + "\n")
    sep = "  " + "─"*85
    print(sep); out(sep + "\n")

    resultats = []
    total_paires = 0
    current_fam = None

    t0 = time.time()
    for (rp, rq, r2n, typ) in ORBITES:

        # Séparateur entre familles
        fam_key = (rp, typ)
        if fam_key != current_fam:
            current_fam = fam_key
            sep_line = f"  ── {typ}({rp}) {'─'*60}"
            print(sep_line); out(sep_line + "\n")

        sg_list = FAM.get(rp, [])
        if not sg_list:
            continue

        # Premier 2n valide
        start = r2n
        while start <= rp + rq: start += 30
        if start < 8: start += 30

        echecs, p_mins, rejetes = [], [], 0

        for n2 in range(start, N+1, 30):
            trouve = False
            for p in sg_list:
                if p >= n2: break
                q = n2 - p
                if q > 2 and q % 30 == rq:
                    if sieve[q]:
                        p_mins.append(p); trouve = True; break
                    else:
                        rejetes += 1
            if not trouve:
                echecs.append(n2)

        total   = len(range(start, N+1, 30))
        success = total - len(echecs)
        total_paires += success
        couv    = success / total * 100 if total else 0
        p_med   = int(median(p_mins)) if p_mins else 0
        p1_pct  = (sum(1 for p in p_mins if p==sg_list[0])/len(p_mins)*100
                   if p_mins else 0)
        S       = serie_singulieres(rp, rq, typ=='SG')
        sg_sg   = "★" if rp in SG_RES and rq in SG_RES else " "
        couv_s  = "100%" if couv >= 100 else f"{couv:.2f}%"

        row = (f"  {typ}({rp:2d})→{rq:<3}{sg_sg}   {r2n:>4}  {sg_sg} "
               f"{total:>9,} {success:>9,} {couv_s:>7} "
               f"{p_med:>7} {p1_pct:>6.1f}% {S:>8.1f} {rejetes:>9,}")
        print(row); out(row + "\n")

        resultats.append(dict(rp=rp, rq=rq, r2n=r2n, typ=typ,
            total=total, echecs=echecs, couv=couv,
            p_med=p_med, p1_pct=p1_pct, S=S, rejetes=rejetes))

    t_orbites = time.time() - t0
    print(sep); out(sep + "\n")
    out(bilingual("★ = paire SG-SG  |  𝔖 = série singulière HL  "
                  "|  Rejetés = candidats q composés",
                  "★ = SG-SG pair  |  𝔖 = HL singular series  "
                  "|  Rejected = composite q candidates"))

    # ── Étape 4 : Bilan & Vérification ────────────────────────────────────
    out(section("BILAN & VÉRIFICATION", "SUMMARY & VERIFICATION"))

    # Invariants universels
    out(subsection("Invariants universels / Universal Invariants"))
    for rp_fam in [11, 23, 29, 1, 7]:
        g = [r for r in resultats if r['rp']==rp_fam]
        meds = set(r['p_med'] for r in g if r['p_med'] > 0)
        p1s  = [r['p1_pct'] for r in g if r['p1_pct'] > 0]
        typ  = "SG" if rp_fam in SG_RES else "XSG"
        p2   = FAM[rp_fam][1] if len(FAM[rp_fam]) > 1 else '?'
        med_ok = len(meds) == 1 and list(meds)[0] == p2
        p1_ok  = all(18 < t < 38 for t in p1s) if p1s else True
        p1_moy = f"{sum(p1s)/len(p1s):.1f}%" if p1s else "—"
        out(bilingual(
            f"  F({rp_fam:2d}) [{typ}] : p_méd={meds}  {'✓' if med_ok else '≈'}  "
            f"p₁%={p1_moy}  {'✓' if p1_ok else '≈'}",
            f"  F({rp_fam:2d}) [{typ}] : p_med={meds}  {'✓' if med_ok else '≈'}  "
            f"p₁%={p1_moy}  {'✓' if p1_ok else '≈'}"))

    # Vérification critique
    out(subsection("Vérification de la Conjecture G / Conjecture G Verification"))
    echecs_critiques = [r for r in resultats if any(e >= 200 for e in r['echecs'])]
    echecs_triviaux  = [r for r in resultats if r['echecs'] and
                        all(e < 200 for e in r['echecs'])]
    all_S_pos = all(r['S'] > 0 for r in resultats)

    if not echecs_critiques:
        out(bilingual(
            "✅ VÉRIFICATION EMPIRIQUE RÉUSSIE — Aucun contre-exemple pour 2n ≥ 200",
            "✅ EMPIRICAL VERIFICATION PASSED — No counter-example for 2n ≥ 200"))
    else:
        out(bilingual(
            f"❌ CONTRE-EXEMPLE DÉTECTÉ : {[(r['rp'],r['rq']) for r in echecs_critiques]}",
            f"❌ COUNTER-EXAMPLE DETECTED: {[(r['rp'],r['rq']) for r in echecs_critiques]}"))

    if echecs_triviaux:
        trivs = [(r['rp'],r['rq'],r['echecs']) for r in echecs_triviaux]
        out(bilingual(f"ℹ Échecs triviaux (2n<200) : {trivs}",
                      f"ℹ Trivial failures (2n<200): {trivs}"))

    out(bilingual(
        f"𝔖 > 0 pour les 29 orbites : {'✓' if all_S_pos else '✗'}",
        f"𝔖 > 0 for all 29 orbits   : {'✓' if all_S_pos else '✗'}"))
    out(bilingual(
        f"Paires Goldbach totales    : {total_paires:,}",
        f"Total Goldbach pairs       : {total_paires:,}"))
    out(bilingual(
        f"Candidats rejetés totaux   : {sum(r['rejetes'] for r in resultats):,}",
        f"Total rejected candidates  : {sum(r['rejetes'] for r in resultats):,}"))
    out(bilingual(
        "⚠ NOTE ÉPISTÉMIQUE : Vérification empirique ≠ preuve mathématique.",
        "⚠ EPISTEMIC NOTE  : Empirical verification ≠ mathematical proof."))

    # Temps total
    out(bilingual(
        f"Temps total : {time.time()-t_total:.2f}s  "
        f"(crible:{t_sieve:.1f}s  familles:{t_fam:.1f}s  orbites:{t_orbites:.1f}s)",
        f"Total time  : {time.time()-t_total:.2f}s  "
        f"(sieve:{t_sieve:.1f}s  families:{t_fam:.1f}s  orbits:{t_orbites:.1f}s)"))

    out("═" * 80 + "\n")

    # ── Sauvegarde ───────────────────────────────────────────────────────────
    content = "\n".join(
        l if isinstance(l, str) else str(l)
        for l in lines
    )
    with open(OUT_TXT, 'w', encoding='utf-8') as fh:
        fh.write(content)

    # Rapport Markdown
    with open(OUT_MD, 'w', encoding='utf-8') as fh:
        fh.write(f"# Monfette 2026 — Rapport / Report\n\n")
        fh.write(f"**N = {N:,}** | {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        fh.write("## Tableau des 29 orbites / Table of 29 orbits\n\n")
        fh.write("| Orbite | 2n≡ | ★ | Testés | Succès | Couv% | p_méd | p₁% | 𝔖 | Rejetés |\n")
        fh.write("|--------|-----|---|--------|--------|-------|-------|-----|---|--------|\n")
        for r in resultats:
            typ = r['typ']
            rp, rq, r2n = r['rp'], r['rq'], r['r2n']
            sg = "★" if rp in SG_RES and rq in SG_RES else ""
            couv_s = "100%" if r['couv'] >= 100 else f"{r['couv']:.2f}%"
            fh.write(f"| {typ}({rp})→{rq} | {r2n} | {sg} | "
                     f"{r['total']:,} | {r['total']-len(r['echecs']):,} | {couv_s} | "
                     f"{r['p_med']} | {r['p1_pct']:.1f}% | {r['S']:.1f} | "
                     f"{r['rejetes']:,} |\n")
        fh.write("|------------------------------------------------------------------|\n")
        fh.write(content)
    print(f"\n  Fichiers sauvegardés / Files saved:")
    print(f"    {OUT_TXT}")
    print(f"    {OUT_MD}")

if __name__ == "__main__":
    main()
