#!/usr/bin/env python3
"""
=============================================================================
MONFETTE CORPUS 2026 — BILINGUAL ANALYSIS & AUTO-VERIFICATION
=============================================================================
Projet : Conjecture Générale (Monfette) v2
Auteur : Michel Monfette
Localisation : Chicoutimi, Saguenay, Québec
=============================================================================
"""
import sys
import time
from statistics import median
from sympy import isprime

# --- Configuration ---200_000_000
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000_000
OUTPUT_FILE = "resultats_monfette_2026.txt"
SG_RES = {11, 23, 29}
R30 = [1, 7, 11, 13, 17, 19, 23, 29]

def log_and_print(txt_fr, txt_en, file_handle):
    """Affiche et sauvegarde le texte dans les deux langues."""
    output = f"FR: {txt_fr}\nEN: {txt_en}"
    print(output)
    file_handle.write(output + "\n")

def log_line(char, length, file_handle):
    line = char * length
    print(line)
    file_handle.write(line + "\n")

# --- Début du traitement ---
with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    
    log_line("=", 85, f)
    log_and_print("RAPPORT D'ANALYSE : CONJECTURE GÉNÉRALE (MONFETTE)", 
                 "ANALYSIS REPORT: GENERAL CONJECTURE (MONFETTE)", f)
    log_and_print(f"DATE ET HEURE : {ts}", f"DATE AND TIME: {ts}", f)
    log_and_print(f"LIMITE N      : {N:,}", f"LIMIT N       : {N:,}", f)
    log_line("=", 85, f)

    t0 = time.time()
    
    # --- 1. Précalcul / Precomputation ---
    FAM = {}
    print("\n[1/3] Calcul des familles / Computing families...")
    for rp in R30:
        if rp in SG_RES:
            FAM[rp] = [p for p in range(rp, N+1, 30) if isprime(p) and isprime(2*p+1)]
        else:
            FAM[rp] = [p for p in range(rp, N+1, 30) if isprime(p)]
    
    # --- 2. Orbites / Orbits Definition ---
    orbites = [
        (11, 1, 12), (11, 7, 18), (11, 11, 22), (11, 13, 24), (11, 17, 28), (11, 19, 0), (11, 23, 4), (11, 29, 10),
        (23, 1, 24), (23, 7, 0), (23, 11, 4), (23, 13, 6), (23, 17, 10), (23, 19, 12), (23, 23, 16), (23, 29, 22),
        (29, 1, 0), (29, 7, 6), (29, 11, 10), (29, 13, 12), (29, 17, 16), (29, 19, 18), (29, 23, 22), (29, 29, 28),
        (1, 1, 2), (1, 7, 8), (1, 13, 14), (1, 19, 20), (7, 19, 26)
    ]

    # --- 3. Analyse & Vérification ---
    log_and_print("ANALYSE DES 29 ORBITES", "ANALYSIS OF THE 29 ORBITS", f)
    header = f"{'Orbite/Orbit':<15} {'2n≡':>4} {'Tested':>10} {'Success':>10} {'Cov%':>8} {'p_med':>8}"
    print(header)
    f.write(header + "\n")
    log_line("-", 65, f)

    results_data = []
    total_valid = 0

    for (rp, rq, r2n) in orbites:
        sg_list = FAM[rp]
        start = r2n if r2n >= max(rp+rq, 8) else r2n + 30
        while start < rp + rq + 2: start += 30

        echecs, p_mins = [], []

        for n2 in range(start, N+1, 30):
            trouve = False
            for p in sg_list:
                if p >= n2: break
                q = n2 - p
                if q > 1 and q % 30 == rq and isprime(q):
                    p_mins.append(p)
                    trouve = True
                    break
            if not trouve:
                echecs.append(n2)

        count = len(range(start, N+1, 30))
        success = count - len(echecs)
        total_valid += success
        couv = (success / count * 100) if count else 0
        p_med = int(median(p_mins)) if p_mins else 0
        
        typ = "SG" if rp in SG_RES else "XSG"
        row = f"{typ}({rp:2d})→{rq:<3} {r2n:>4} {count:>10} {success:>10} {couv:>7.2f}% {p_med:>8}"
        print(row)
        f.write(row + "\n")

        results_data.append({'rp': rp, 'echecs': echecs, 'p_med': p_med})

    # --- 4. Bilan Final & Vérification Automatique ---
    log_line("=", 85, f)
    log_and_print("BILAN FINAL & VÉRIFICATION AUTOMATIQUE", "FINAL SUMMARY & AUTO-VERIFICATION", f)
    log_line("=", 85, f)

    # Vérification de la Loi Monfette (2n >= 200)
    critical_failures = [r for r in results_data if any(e >= 200 for e in r['echecs'])]
    
    if not critical_failures:
        log_and_print("✅ STATUT : CONJECTURE VALIDÉE (2n ≥ 200)", 
                     "✅ STATUS: CONJECTURE VALIDATED (2n ≥ 200)", f)
    else:
        log_and_print("❌ STATUT : CONTRE-EXEMPLE DÉTECTÉ", 
                     "❌ STATUS: COUNTER-EXAMPLE DETECTED", f)

    log_and_print(f"Paires Goldbach totales : {total_valid:,}", 
                 f"Total Goldbach pairs: {total_valid:,}", f)
    log_and_print(f"Temps d'exécution : {time.time()-t0:.2f}s", 
                 f"Execution time: {time.time()-t0:.2f}s", f)
    log_line("=", 85, f)
    f.write("\n\n")
    
