# OC Projet7 AlgoInvest-Trade

Ce projet s'inscrit dans le parcours "Développeur d'application Python" sur OpenClassrooms. Il consiste à optimiser les stratégies d'investissement à l'aide d'algorithmes et de données au format CSV. Les fichiers CSV se trouvent dans le dossier data, et chaque fichier comporte trois colonnes: nom de l'action, coût, et performance sur deux ans.

L'objectif est de déterminer les actions à acheter pour un montant de portefeuille fixe afin de maximiser la plus-value. Pour cela, j'ai implémenté trois algorithmes (brute force, glouton et knapsack) afin de comparer leurs forces et faiblesses et de choisir la meilleure solution.
***
## Installation
1. Cloner le dépôt
```bash
git clone https://github.com/PVL06/OC_projet7_AlgoInvest-Trade.git
```
2. Créer l'environnement virtuel
```bash
cd OC_projet7_AlgoInvest-Trade
python -m venv env
```

3. Activation de l'environnement
Windows: ```bash env/Script/activate``` 
Linus, macOs: ```bash source env/bin/activate```  

4. Installer les dépendances (Numpy)
```bash
pip install -r requirements.txt
``` 
***
## Lancement des algorithmes
1. Algorithme de force brute (uniquement avec le fichier csv contenant 20 actions)
```bash
python brutforce.py
```
2. Algorithme glouton
```bash
python glouton.py
```
3. Algorithme Knapsack
```bash
python optimized.py
```