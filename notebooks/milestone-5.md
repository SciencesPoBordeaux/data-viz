# Instructions — Infographie Finale

## Date limite : 10 avril

---

## Objectif

Produire une **infographie complète et professionnelle** permettant de répondre à une question de recherche en sciences politiques à partir des données de l'ANES 2024.

---

## Étape 1 — Créer un nouveau notebook

1. Ouvrez **Google Colab** ou votre environnement Jupyter
2. Créez un **nouveau notebook** vide
3. Nommez-le `infographie_finale.ipynb`

---

## Étape 2 — Installer les bibliothèques et charger les données

Copiez et exécutez le code d'installation vu dans les premiers notebooks :

```python
# Installation des bibliothèques
%pip install "vegafusion[embed]>=1.5.0" "vl-convert-python>=1.6.0"

import pandas as pd
import altair as alt

# Configuration d'Altair
alt.data_transformers.enable("vegafusion")
alt.data_transformers.disable_max_rows()

# Chargement des données ANES 2024
data_url = "https://raw.githubusercontent.com/datamisc/ts-2024/main/data.csv"
df = pd.read_csv(data_url, compression="gzip", low_memory=False)
```

---

## Étape 3 — Choisir une question de recherche

Avant de sélectionner vos variables, définissez une question de recherche claire.

**Exemples de questions :**

- Comment l'intérêt politique varie-t-il selon le niveau d'éducation ?
- Quel est le lien entre la confiance dans les médias et le parti politique privilégié ?
- Les jeunes voters ont-ils des attitudes différentes envers la démocratie ?

---

## Étape 4 — Explorer et sélectionner les variables

Consult le codebook de l'ANES 2024 :
- [Codebook en ligne](https://sda.berkeley.edu/sdaweb/docs/anes2024full/DOC/hcbkh01.htm)
- [PDF officiel](https://electionstudies.org/wp-content/uploads/2025/08/anes_timeseries_2024_userguidecodebook_20250808.pdf)

**Conseil :** Regardez les notebooks précédents pour voir comment les variables ont été recodées et nettoyées.

---

## Étape 5 — Préparer les données

Dans votre notebook, procédez comme dans les séances précédentes :

1. **Filtrez** les observations pertinentes
2. **Recodez** les valeurs en modalités lisibles (ex. : 1 → "Oui", -9 → NaN)
3. **Créez** des variables dérivées si nécessaire (ex. : polarisation, fort intérêt politique)

---

## Étape 6 — Créer la visualisation

Construisez votre graphique en suivant les critères de qualité vus en cours :

| Élément | Exigence |
|---------|----------|
| **Titre** | Explicite, précis, accrocheur |
| **Sous-titre** | Explique comment lire le graphique |
| **Source** | Précise la source des données |
| **Mise en forme** | Lisibilité, couleurs adaptées, proportions correctes |

**Types de visualisation possibles (selon vos données) :**

- Barplot / Histogramme
- Boxplot
- Scatterplot
- Courbe temporelle
- Carte (si données géographiques)

---

## Étape 7 — Exporter la figure

Enregistrez votre visualisation dans un format adapté :

```python
votre_graphique.save("infographie.png", scale_factor=2)
# ou
votre_graphique.save("infographie.pdf")
```

---

## Critères d'évaluation

Votre infographie doit comporter :

- ✅ Du code **reproductible** de bout en bout
- ✅ Un **chargement de la base de données**
- ✅ Une **identification et préparation** des variables
- ✅ Un **titre explicite**
- ✅ Un **sous-titre** avec un exemple de lecture
- ✅ Une **source** (ANES 2024)
- ✅ Une **mise en forme soignée**
- ✅ Un **fichier exporté** (PNG ou PDF)

---

## Ressources utiles

- [From Data to Viz](https://www.data-to-viz.com/) — Choisir le bon type de graphique
- [Altair Documentation](https://altair-viz.github.io/)
- [Codebook ANES 2024](https://sda.berkeley.edu/sdaweb/docs/anes2024full/DOC/hcbkh01.htm)

---

## Remise

Envoyez votre notebook `.ipynb` **et** le fichier image exporté à l'enseignant·e.

**Objet du mail :** `DECA - Infographie Finale - Nom Prénom`