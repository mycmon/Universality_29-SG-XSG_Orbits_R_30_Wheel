import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt
from sympy import isprime
import csv
import datetime
import os

# ── CONFIGURATION ────────────────────────────────────────────────────────────
MODES = {
    "mod 30":    30,
    "mod 210":   210,
    "mod 2310":  2310,
    "mod 30030": 30030
}

C2_THEO = 0.6601683
RESULTS_DIR = "goldbach_results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# ── OUTILS PRIMES ────────────────────────────────────────────────────────────

def get_primes_up_to(n):
    if n < 2: return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i]]

# ── GOLDACH MOD PRIMORIAL ───────────────────────────────────────────────────
def goldbach_mod(N, MOD):
    if N < 4 or N % 2 != 0: return None
    R = [x for x in range(1, MOD) if math.gcd(x, MOD) == 1]
    admissible = []
    seen = set()
    for a in [2,3,5,7,11] + R:
        for b in [2,3,5,7,11] + R:
            if (a + b) % MOD == N % MOD:
                key = (min(a,b), max(a,b))
                if key not in seen:
                    seen.add(key)
                    admissible.append((a,b))
    primes = get_primes_up_to(N)
    prime_set = set(primes)
    realizations = []
    for p in primes:
        if p > N//2: break
        q = N - p
        if q in prime_set:
            realizations.append((p, q))
    return {
        'N': N,
        'admissible_count': len(admissible),
        'realization_count': len(realizations),
        'ratio': len(realizations) / len(admissible) if len(admissible) > 0 else 0
    }

# ── GOLDACH COMPLET ─────────────────────────────────────────────────────────
def goldbach_full(N):
    """
    G(N) complet : nombre total de représentations N = p+q sans filtrage modulaire.
    """
    if N < 4 or N % 2 != 0:
        return None
    primes = get_primes_up_to(N)
    prime_set = set(primes)
    G = 0
    for p in primes:
        if p > N // 2:
            break
        q = N - p
        if q in prime_set:
            G += 1
    return {
        'N': N,
        'G': G
    }


def C2_empirique(N, G):
    lnN = math.log(N)
    return G * (lnN ** 2) / (2 * N)

# ── APPLICATION TKINTER ─────────────────────────────────────────────────────
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Goldbach – Mod primorial & Complet")
        self.geometry("1380x780")
        self._build_ui()

    def _build_ui(self):
        top = ttk.Frame(self)
        top.pack(fill="x", padx=10, pady=8)

        # Choix type de calcul
        ttk.Label(top, text="Type :").pack(side="left")
        self.calc_type = ttk.Combobox(top, values=["Mod primorial", "Complet"], state="readonly", width=15)
        self.calc_type.current(0)
        self.calc_type.pack(side="left", padx=5)

        # Choix modulo (pour mode mod primorial)
        ttk.Label(top, text="Mode :").pack(side="left", padx=(20,5))
        self.mode_box = ttk.Combobox(top, values=list(MODES.keys()), state="readonly", width=10)
        self.mode_box.current(3)
        self.mode_box.pack(side="left", padx=5)

        ttk.Label(top, text="N (séparés par virgule) :").pack(side="left", padx=(20,5))
        self.entry_multi = ttk.Entry(top, width=65)
        self.entry_multi.insert(0, "1000,10000,100000,1000000,10000000,50000000,100000000,200000000,500000000")
        self.entry_multi.pack(side="left", padx=5)

        ttk.Button(top, text="Lancer", command=self.run_multi).pack(side="left", padx=8)

        self.output = tk.Text(self, height=26, font=("Consolas", 10))
        self.output.pack(fill="both", expand=True, padx=10, pady=5)

    def run_multi(self):
        self.output.delete("1.0", tk.END)
        try:
            ns = [int(x.strip()) for x in self.entry_multi.get().split(",") if x.strip()]
        except:
            messagebox.showerror("Erreur", "Liste N invalide")
            return

        calc_type = self.calc_type.get()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.output.insert(tk.END, f"Type : {calc_type}\n")
        self.output.insert(tk.END, f"Date : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        data = []

        if calc_type == "Mod primorial":
            MOD = MODES[self.mode_box.get()]
            self.output.insert(tk.END, f"Mode : {self.mode_box.get()} (MOD = {MOD})\n")
            self.output.insert(tk.END, "="*110 + "\n")
            for N in ns:
                res = goldbach_mod(N, MOD)
                if res:
                    ratio = res['ratio']
                    data.append((N, ratio, res['realization_count'], res['admissible_count']))
                    self.output.insert(tk.END,
                        f"N = {N:12,} | Admissibles = {res['admissible_count']:4} | "
                        f"Réalisations = {res['realization_count']:8,} | Ratio = {ratio:10.4f}\n")
            if data:
                self.plot_modular(data, timestamp)
                self.export_csv_modular(data, timestamp, MOD)
                self.export_md_modular(data, timestamp, MOD)
                self.compute_weighted_C2_modular(data)

        else:  # Complet
            self.output.insert(tk.END, "="*110 + "\n")
            for N in ns:
                res = goldbach_full(N)
                if res:
                    G = res['G']
                    c2_emp = C2_empirique(N, G)
                    data.append((N, G, c2_emp))
                    self.output.insert(tk.END,
                        f"N = {N:12,} | G(N) = {G:10,} | C₂(N) = {c2_emp:10.6f}\n")
            if data:
                self.plot_full(data, timestamp)
                self.export_csv_full(data, timestamp)
                self.export_md_full(data, timestamp)
                self.compute_weighted_C2_full(data)

    # ── MOD PRIMORIAL : PLOT & EXPORT & C2 ───────────────────────────────────
    def compute_weighted_C2_modular(self, data):
        total_weight = 0.0
        weighted_sum = 0.0
        for N, ratio, real, adm in data:
            if N > 10000:
                lnN = math.log(N)
                weight = N / (lnN ** 2)
                # C2 empirique à partir de G(N) complet (ici real)
                c2_emp = real * (lnN ** 2) / (2 * N)
                weighted_sum += c2_emp * weight
                total_weight += weight
        if total_weight > 0:
            c2_weighted = weighted_sum / total_weight
            self.output.insert(tk.END, "\n" + "="*110 + "\n")
            self.output.insert(tk.END, f"C₂ moyen pondéré (mod primorial) : {c2_weighted:.6f}\n")
            self.output.insert(tk.END, f"Écart avec C₂ théorique ({C2_THEO:.6f}) : {abs(c2_weighted - C2_THEO)*100:.3f} %\n")

    def plot_modular(self, data, timestamp):
        Ns = [d[0] for d in data]
        ratios = [d[1] for d in data]
        logNs = [math.log10(n) for n in Ns]

        theo = []
        for (N, ratio, real, adm) in data:
            lnN = math.log(N)
            if adm > 0:
                G_theo = 2 * C2_THEO * N / (lnN ** 2)
                theo.append(G_theo / adm)
            else:
                theo.append(0)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
        fig.suptitle(f"Goldbach Ratio - {self.mode_box.get()}", fontsize=14, fontweight='bold')

        ax1.plot(Ns, ratios, 'bo-', label='Observé', linewidth=2)
        ax1.plot(Ns, theo, 'r--', label=f'Théorique C₂={C2_THEO:.5f}', linewidth=2)
        ax1.set_xlabel("N"); ax1.set_ylabel("Ratio"); ax1.legend(); ax1.grid(True)

        ax2.plot(logNs, ratios, 'bo-', label='Observé', linewidth=2)
        ax2.plot(logNs, theo, 'r--', label='Théorique', linewidth=2)
        ax2.set_xlabel("log₁₀(N)"); ax2.set_ylabel("Ratio"); ax2.legend(); ax2.grid(True)

        plt.tight_layout()
        fig.savefig(f"{RESULTS_DIR}/goldbach_mod_graph_{timestamp}.png", dpi=300)
        plt.close(fig)

    def export_csv_modular(self, data, timestamp, MOD):
        filename = f"{RESULTS_DIR}/goldbach_mod_results_{timestamp}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["N", "Admissibles", "Realisations", "Ratio"])
            for n, r, real, adm in data:
                writer.writerow([n, adm, real, r])
        self.output.insert(tk.END, f"→ CSV (mod primorial) : {filename}\n")

    def export_md_modular(self, data, timestamp, MOD):
        filename = f"{RESULTS_DIR}/goldbach_mod_rapport_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Rapport Goldbach – Mod primorial – {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Mode** : {self.mode_box.get()} (MOD = {MOD})\n\n")
            f.write("## Tableau des résultats\n\n")
            f.write("| N | Admissibles | Réalisations | Ratio |\n|---|---|---|---|\n")
            for n, r, real, adm in data:
                f.write(f"| {n:,} | {adm} | {real} | {r:.4f} |\n")
            f.write(f"\n**C₂ théorique** : {C2_THEO:.6f}\n")
        self.output.insert(tk.END, f"→ Rapport Markdown (mod primorial) : {filename}\n")

    # ── COMPLET : PLOT & EXPORT & C2 ─────────────────────────────────────────
    def compute_weighted_C2_full(self, data):
        total_weight = 0.0
        weighted_sum = 0.0
        for N, G, c2_emp in data:
            if N > 10000:
                lnN = math.log(N)
                weight = N / (lnN ** 2)
                weighted_sum += c2_emp * weight
                total_weight += weight
        if total_weight > 0:
            c2_weighted = weighted_sum / total_weight
            self.output.insert(tk.END, "\n" + "="*110 + "\n")
            self.output.insert(tk.END, f"C₂ moyen pondéré (complet) : {c2_weighted:.6f}\n")
            self.output.insert(tk.END, f"Écart avec C₂ théorique ({C2_THEO:.6f}) : {abs(c2_weighted - C2_THEO)*100:.3f} %\n")

    def plot_full(self, data, timestamp):
        Ns = [d[0] for d in data]
        Gs = [d[1] for d in data]
        C2s = [d[2] for d in data]
        logNs = [math.log10(n) for n in Ns]

        # Théorique G(N)
        G_theo = [2 * C2_THEO * N / (math.log(N) ** 2) for N in Ns]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
        fig.suptitle("Goldbach complet", fontsize=14, fontweight='bold')

        ax1.plot(Ns, Gs, 'bo-', label='G(N) observé', linewidth=2)
        ax1.plot(Ns, G_theo, 'r--', label='G(N) théorique', linewidth=2)
        ax1.set_xlabel("N"); ax1.set_ylabel("G(N)"); ax1.legend(); ax1.grid(True)

        ax2.plot(Ns, C2s, 'bo-', label='C₂(N) empirique', linewidth=2)
        ax2.axhline(C2_THEO, color='r', linestyle='--', label=f'C₂ théorique={C2_THEO:.5f}')
        ax2.set_xlabel("N"); ax2.set_ylabel("C₂(N)"); ax2.legend(); ax2.grid(True)

        plt.tight_layout()
        fig.savefig(f"{RESULTS_DIR}/goldbach_full_graph_{timestamp}.png", dpi=300)
        plt.close(fig)

    def export_csv_full(self, data, timestamp):
        filename = f"{RESULTS_DIR}/goldbach_full_results_{timestamp}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["N", "G(N)", "C2_empirique"])
            for n, G, c2 in data:
                writer.writerow([n, G, c2])
        self.output.insert(tk.END, f"→ CSV (complet) : {filename}\n")

    def export_md_full(self, data, timestamp):
        filename = f"{RESULTS_DIR}/goldbach_full_rapport_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Rapport Goldbach – Complet – {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## Tableau des résultats\n\n")
            f.write("| N | G(N) | C₂(N) |\n|---|---|---|\n")
            for n, G, c2 in data:
                f.write(f"| {n:,} | {G} | {c2:.6f} |\n")
            f.write(f"\n**C₂ théorique** : {C2_THEO:.6f}\n")
        self.output.insert(tk.END, f"→ Rapport Markdown (complet) : {filename}\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()
