import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from adjustText import adjust_text

# 1. Daten (Deine Werte für Impact & Frequency)
data = {
    "Faktor": [
        "USA Retreat", "Human Rights", "AI Investments", "Inflation", 
        "Recession Indication", "Fake News", "Process Auto.", "Cloud Dataleaks", 
        "Hardware Prices", "Slow Gov. AI Laws", "Strict Licensing", 
        "Pollution (War/AI)", "Energy (Nuclear/Fossil)"
    ],
    "Kategorie": [
        "Political", "Social", "Economic", "Economic", "Economic", 
        "Social", "Technological", "Technological", "Technological", 
        "Legal", "Legal", "Environmental", "Environmental"
    ],
    "Impact": [11, 9, 16, 10, 8, 18, 10, 7, 6, 20, 4, 13, 10],
    "Frequency": [4, 6, 9, 8, 5, 9, 8, 7, 5, 9, 3, 5, 8]
}

df = pd.DataFrame(data)

# 2. Visuelles Setup (Dark Mode)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(14, 9))

# Farben exakt nach PESTEL wie im Vorbild
colors = {
    'Political': '#5c5cff',      # Blau
    'Economic': '#2ecc71',       # Grün
    'Social': '#f39c12',         # Orange
    'Technological': '#00cec9',  # Türkis
    'Legal': '#e74c3c',          # Rot
    'Environmental': '#9b59b6'   # Lila
}

# 3. Punktwolke zeichnen
for cat in df['Kategorie'].unique():
    subset = df[df['Kategorie'] == cat]
    ax.scatter(
        subset['Frequency'], 
        subset['Impact'],
        s=120, # Feste, gut sichtbare Größe
        c=colors[cat], 
        label=cat,
        edgecolors='#ffffff', # Weißer Rand wie im Vorbild
        linewidth=1.5,
        zorder=3 # Punkte im Vordergrund
    )

# 4. Die "Scenario Boundary Curve" (Gestrichelte Trennlinie)
# Eine berechnete Kurve, die sich von oben links nach unten rechts zieht
x_curve = np.linspace(0.1, 10.5, 100)
y_curve = 25 * np.exp(-0.3 * x_curve) + 3 
ax.plot(x_curve, y_curve, color='#a0a0a0', linestyle='--', linewidth=2, zorder=1)

# 5. Labels (Automatisch angeordnet, OHNE Überlappung)
texts = []
for i, row in df.iterrows():
    # Wir fügen den Faktor und den Impact-Wert in Klammern hinzu
    t = ax.text(row['Frequency'], row['Impact'], f"{row['Faktor']} ({row['Impact']})", 
                fontsize=9, fontweight='bold', color='white')
    texts.append(t)

# adjustText sortiert die Labels automatisch und zieht kleine Linien zu den Punkten!
adjust_text(texts, ax=ax, force_points=0.2, force_text=0.2,
            expand_points=(1.2, 1.2), expand_text=(1.2, 1.2),
            arrowprops=dict(arrowstyle="-", color='#a0a0a0', lw=1, alpha=0.8))

# 6. Text-Boxen aus dem Netflix-Bild hinzufügen
# Oben rechts (Hochrelevant)
ax.text(9.8, 23, "Hochrelevante Faktoren,\nGegenstand weiterer Analyse ->", 
        fontsize=10, color='white', ha='right', va='top',
        bbox=dict(facecolor='#1e1e1e', edgecolor='#555555', boxstyle='round,pad=0.8', alpha=0.8))

# Unten rechts (Weniger relevant)
ax.text(9.8, 2, "Weniger relevante Faktoren,\nweniger relevant für weitere Analyse ->", 
        fontsize=10, color='#a0a0a0', ha='right', va='bottom',
        bbox=dict(facecolor='#1e1e1e', edgecolor='#555555', boxstyle='round,pad=0.8', alpha=0.8))

# Unten Mitte (Info)
ax.text(5, -1.5, "💡 Drag nodes across the dashed boundary line to reclassify them! (Mockup)", 
        fontsize=10, color='#a0a0a0', ha='center', va='top')

# 7. Achsen beschriften und stylen
ax.set_title("Relevance & Frequency Matrix\nTime Horizon: 5 Years | PESTEL Analysis", 
             fontsize=16, pad=20, fontweight='bold', loc='left', color='white')

ax.set_xlabel("FREQUENCY / OCCURRENCE (X-AXIS) ──────> HIGH", 
              fontsize=11, fontweight='bold', color='#a0a0a0', labelpad=15)
ax.set_ylabel("RELEVANCE / IMPACT (Y-AXIS) ──────> HIGH", 
              fontsize=11, fontweight='bold', color='#a0a0a0', labelpad=15)

# Gitterlinien subtil im Hintergrund (wie beim Original)
ax.grid(True, color='#333333', linestyle='-', linewidth=0.5, zorder=0)

# Achsenbegrenzungen setzen (leicht über den Rand hinaus für Abstand)
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 25.5)

# Legende oben zentriert
ax.legend(title="PESTEL Dimensionen", loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=6, frameon=False, fontsize=9, title_fontsize=10)

plt.tight_layout()
plt.show()