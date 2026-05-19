import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math


# ============================================================
#  MOTEUR OPTIMISÉ GOLDACH + CRIBLE + FILTRES MOD 30 / 210
# ============================================================

MAX_N = 1_000_000

def sieve(n):
    """Crible d'Ératosthène ultra-rapide."""
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for p in range(2, int(n**0.5) + 1):
        if s[p]:
            step = p
            start = p * p
            s[start:n+1:step] = [False] * (((n - start) // step) + 1)
    return s

# Crible global (1 million en 0.05 sec)
PRIME = sieve(MAX_N)

# Résidus admissibles mod 30
R30 = {1, 7, 11, 13, 17, 19, 23, 29}

# Résidus admissibles mod 210 (48 résidus)
R210 = [n for n in range(210) if math.gcd(n, 210) == 1]
R210_SET = set(R210)


def goldbach_fast(N):
    """
    Version optimisée :
    - utilise le crible
    - filtre mod 30
    - filtre mod 210
    - retourne la liste des paires (p,q)
    """
    pairs = []
    half = N // 2

    for p in range(7, half + 1, 2):  # seulement impairs
        if p % 30 not in R30:
            continue
        if p % 210 not in R210_SET:
            continue

        q = N - p
        if q % 30 not in R30:
            continue
        if q % 210 not in R210_SET:
            continue

        if PRIME[p] and PRIME[q]:
            pairs.append((p, q))

    return pairs




def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

class MonfetteAppPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Station Monfette Pro - Analyseur de Stabilité Orbitale")
        self.root.geometry("1600x950")
        self.R30 = {1, 7, 11, 13, 17, 19, 23, 29}
        self.couleurs_R = {1:'#FF0000', 7:'#FF7F00', 11:'#FFFF00', 13:'#00FF00', 
                           17:'#0000FF', 19:'#4B0082', 23:'#9400D3', 29:'#FFFFFF'}
        self.rotating = tk.BooleanVar(value=False)
        self.angle = 0
        self.running = True
        self.history_density = []
        
        self.setup_ui()
        self.update_plot()
        self.rotate_loop()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self):
        toolbar = tk.Frame(self.root, bg="#1e1e1e", pady=10)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        tk.Label(toolbar, text="N:", fg="white", bg="#1e1e1e").pack(side=tk.LEFT, padx=5)
        self.n_combo = ttk.Combobox(toolbar, values=["210", "2310", "30030", "31292"], width=10)
        self.n_combo.set("31292")
        self.n_combo.pack(side=tk.LEFT, padx=5)
        
        tk.Button(toolbar, text="🔍 Scanner de Stabilité", command=self.run_critical_scan, 
                  bg="#FF9800", fg="black", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=15)
        
        tk.Button(toolbar, text="Calculer & Tracer", command=self.update_plot, bg="#0078D7", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(toolbar, text="Rotation", variable=self.rotating, fg="white", bg="#1e1e1e").pack(side=tk.LEFT, padx=5)
        
        self.stat_label = tk.Label(toolbar, text="Diagnostic: Prêt", fg="#00FF00", bg="#1e1e1e", font=("Consolas", 10))
        self.stat_label.pack(side=tk.RIGHT, padx=20)

        self.fig = plt.figure(figsize=(15, 8), facecolor='#111111')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def run_critical_scan(self):
        try:
            start_n = int(self.n_combo.get())
            scan_range = 600 
            local_history = []
            
            self.stat_label.config(text="Analyse de stabilité...", fg="orange")
            self.root.update()

            for n_test in range(start_n, start_n + scan_range, 2):
                count = 0
                pairs = goldbach_fast(n_test)
                count = len(pairs)

                density = count / n_test
                local_history.append((n_test, density))
            
            self.history_density = local_history
            
            # CORRECTION ICI : On extrait uniquement la valeur N (le premier élément du tuple)
            worst_case_tuple = min(local_history, key=lambda x: x[1])
            worst_n = worst_case_tuple[0]
            worst_density = worst_case_tuple[1]
            
            self.n_combo.set(str(worst_n)) # On ne met que le nombre N dans le champ
            self.update_plot()
            
            messagebox.showinfo("Diagnostic de Stabilité", 
                                f"Analyse terminée sur {scan_range} points.\n\n"
                                f"Point Critique détecté : N = {worst_n}\n"
                                f"Densité minimale : {worst_density:.6f}\n\n"
                                f"La ligne jaune confirme la résilience orbitale.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du scan: {e}")


    def update_plot(self):
        try:
            n_val = int(self.n_combo.get())
            self.fig.clear()
            
            ax3d = self.fig.add_subplot(131, projection='3d')
            ax_dens = self.fig.add_subplot(132) 
            ax_zoom = self.fig.add_subplot(133, projection='3d')
            
            sols_count = 0
            theta_n = (n_val % 360) * (np.pi / 180)
            
            # 1. Perspective 3D (Autoroutes)
            z_line = np.linspace(0, n_val + 20, 100)
            for r in self.R30:
                theta = (z_line % 360) * (np.pi / 180)
                ax3d.plot(r * np.cos(theta), r * np.sin(theta), z_line, color=self.couleurs_R[r], alpha=0.6, lw=0.6)
            
            # 2. Calcul des tunnels pour N
            pairs = goldbach_fast(n_val)
            sols_count = len(pairs)
            
            for p, q in pairs:
                rp, rq = p % 30, q % 30
                xp, yp = rp*np.cos(theta_n), rp*np.sin(theta_n)
                xq, yq = rq*np.cos(theta_n), rq*np.sin(theta_n)
                ax3d.plot([xp, xq], [yp, yq], [n_val, n_val], color='orange', lw=1, alpha=0.4)
                ax_zoom.plot([xp, xq], [yp, yq], [n_val, n_val], color='orange', lw=1.5)
        
                xp, yp = rp*np.cos(theta_n), rp*np.sin(theta_n)
                xq, yq = rq*np.cos(theta_n), rq*np.sin(theta_n)
                ax3d.plot([xp, xq], [yp, yq], [n_val, n_val], color='orange', lw=1, alpha=0.4)
                ax_zoom.plot([xp, xq], [yp, yq], [n_val, n_val], color='orange', lw=1.5)
            
            # 3. COURBE DE DENSITÉ + LIGNE DE STABILITÉ
            if self.history_density:
                n_x, d_y = zip(*self.history_density)
                ax_dens.plot(n_x, d_y, color='#00FF00', lw=1, alpha=0.6, label='Densité brute')
                
                # Calcul de la moyenne mobile (Stabilité)
                window = 20
                if len(d_y) > window:
                    moving_avg = np.convolve(d_y, np.ones(window)/window, mode='valid')
                    ax_dens.plot(n_x[window-1:], moving_avg, color='#FFFF00', lw=2, label='Ligne de Stabilité')
                
                ax_dens.scatter(n_val, sols_count/n_val, color='red', s=50, zorder=5)
                ax_dens.set_title("Stabilité de la Résonance", color='white', fontsize=10)
                ax_dens.tick_params(colors='white', labelsize=8)
                ax_dens.legend(fontsize=7, facecolor='black', labelcolor='white')

            for ax in [ax3d, ax_zoom, ax_dens]: 
                ax.set_facecolor('#111111')
            ax_zoom.view_init(elev=90, azim=0)
            self.canvas.draw()
            self.stat_label.config(text=f"N={n_val} | Tunnels={sols_count}", fg="#00FF00")
        except Exception as e: print(e)

    def rotate_loop(self):
        if not self.running: return
        if self.rotating.get():
            self.angle = (self.angle + 2) % 360
            self.axes_3d = [self.fig.axes, self.fig.axes] # Accès aux axes 3D
            for ax in self.axes_3d:
                if hasattr(ax, 'view_init'): ax.view_init(elev=20, azim=self.angle)
            self.canvas.draw_idle()
        self.root.after(50, self.rotate_loop)

    def on_closing(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MonfetteAppPro(root)
    root.mainloop()
