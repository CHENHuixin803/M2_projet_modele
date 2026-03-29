import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Rd_list = [0, 100, 200, 300]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# ------------------------------------------------------------------------------------------------------------- //
# ------------------------------------------------------------------------------------------------------------- //
#                                  4(b)  
# ------------------------------------------------------------------------------------------------------------- //
# ------------------------------------------------------------------------------------------------------------- //

# P_in et P_out
plt.figure(figsize=(14, 6))

# P_in
plt.subplot(1, 2, 1)
for Rd, color in zip(Rd_list, colors):
    filename = f"Resultats_Rd_{Rd}.txt"
    df = pd.read_csv(filename, sep='\t')
    plt.plot(df['Time'], df['P_in'], label=f'$R_d = {Rd}$', color=color, linewidth=1.5)

plt.title('Pression moyenne en entrée ($P_{in}$)', fontsize=14)
plt.xlabel('Temps (s)', fontsize=12)
plt.ylabel('Pression', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)

# P_out
plt.subplot(1, 2, 2)
for Rd, color in zip(Rd_list, colors):
    filename = f"Resultats_Rd_{Rd}.txt"
    df = pd.read_csv(filename, sep='\t')
    plt.plot(df['Time'], df['P_out'], label=f'$R_d = {Rd}$', color=color, linewidth=1.5)

plt.title('Pression moyenne en sortie ($P_{out}$)', fontsize=14)
plt.xlabel('Temps (s)', fontsize=12)
plt.ylabel('Pression', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)

plt.tight_layout()
plt.savefig('Evolution_Pression.png', dpi=300)
plt.show()


# Q_in et Q_out
plt.figure(figsize=(14, 6))

# Q_in
plt.subplot(1, 2, 1)
for Rd, color in zip(Rd_list, colors):
    filename = f"Resultats_Rd_{Rd}.txt"
    df = pd.read_csv(filename, sep='\t')
    plt.plot(df['Time'], df['Q_in'], label=f'$R_d = {Rd}$', color=color, linewidth=1.5)

plt.title('Débit en entrée ($Q_{in}$)', fontsize=14)
plt.xlabel('Temps (s)', fontsize=12)
plt.ylabel('Débit', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)

# Q_out
plt.subplot(1, 2, 2)
for Rd, color in zip(Rd_list, colors):
    filename = f"Resultats_Rd_{Rd}.txt"
    df = pd.read_csv(filename, sep='\t')
    plt.plot(df['Time'], df['Q_out'], label=f'$R_d = {Rd}$', color=color, linewidth=1.5)

plt.title('Débit en sortie ($Q_{out}$)', fontsize=14)
plt.xlabel('Temps (s)', fontsize=12)
plt.ylabel('Débit', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)

plt.tight_layout()
plt.savefig('Evolution_Debit.png', dpi=300)
plt.show()
