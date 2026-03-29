import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

target_P = 12 * 13332.2 
Rd_list = [0, 100, 200, 300]
max_p_in_list = []

for Rd in Rd_list:
    filename = f"Resultats_Rd_{Rd}.txt"
    df = pd.read_csv(filename, sep='\t')

    # Calculer la pression maximale(eviter le régime transitoire initial)
    df_stable = df[df['Time'] > 1.0]
    max_p = df_stable['P_in'].max()
    max_p_in_list.append(max_p)
    print(f"Rd = {Rd} 时, la pression maximale est: {max_p:.2f}")


# Ajustement linéaire (y = kx + b)
# np.polyfit renvoie la pente k et l'ordonnée à l'origine b
slope, intercept = np.polyfit(Rd_list, max_p_in_list, 1)
estimated_Rd = (target_P - intercept) / slope

print("-" * 40)
print(f"Relation linéaire trouvée : P_max = {slope:.4f} * Rd + {intercept:.4f}")
print(f"Résultat final: Pour atteindre la pression systolique de {target_P}, la résistance Rd requise est d'environ : {estimated_Rd:.2f}")
print("-" * 40)

# plot
plt.figure(figsize=(8, 6))
plt.plot(Rd_list, max_p_in_list, 'ko', label='Données simulées')
Rd_line = np.linspace(0, estimated_Rd * 1.05, 100)
P_line = slope * Rd_line + intercept
plt.plot(Rd_line, P_line, 'b--', alpha=0.7, label='Ajustement linéaire')
plt.plot(estimated_Rd, target_P, 'b*', markersize=12, label=f'Cible extrapolée ($R_d \\approx {estimated_Rd:.2f}$)')

plt.title("Relation entre la résistance $R_d$ et la pression maximale $P_{in}$", fontsize=13)
plt.xlabel("Résistance $R_d$", fontsize=12)
plt.ylabel("Pression maximale en entrée (Pa)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig('Ajustement_Rd_Pression.png', dpi=300)
print(">> 图片已保存为: Ajustement_Rd_Pression.png")
plt.show()