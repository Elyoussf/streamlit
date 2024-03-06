import pandas as pd
import numpy as np

# Fonction pour calculer la distance totale d'une tournée
def distance_tour(tour, distances):
    distance = 0
    for i in range(len(tour) - 1):
        distance += distances[tour[i]][tour[i+1]]
    distance += distances[tour[-1]][tour[0]]  # Distance entre la dernière ville et la première
    return distance

# Fonction pour effectuer l'opération 2-opt
def two_opt_swap(tour, i, k):
    new_tour = tour[:i]
    new_tour.extend(reversed(tour[i:k + 1]))
    new_tour.extend(tour[k + 1:])
    return new_tour

# Fonction pour exécuter l'algorithme 2-opt
def two_opt(distances, tour):
    n = len(tour)
    best_tour = tour
    improve = True

    while improve:
        improve = False
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                new_tour = two_opt_swap(best_tour, i, k)
                new_distance = distance_tour(new_tour, distances)
                if new_distance < distance_tour(best_tour, distances):
                    best_tour = new_tour
                    improve = True
                    break
            if improve:
                break

    return best_tour

# Charger le fichier Excel contenant les distances entre les villes
def charger_distances(nom_fichier):
    try:
        distances_df = pd.read_excel(nom_fichier, index_col=0)
        return distances_df.values
    except Exception as e:
        print("Erreur lors du chargement du fichier:", e)

# Exemple d'utilisation
if __name__ == "__main__":
    fichier_distances = input("entrer le lien vers le fichier")
    
    distances = charger_distances(fichier_distances)
    if distances is not None:
        n = len(distances)
        tour_initial = list(range(n))  # Tour initial : 0, 1, 2, ..., n-1
        meilleur_tour = two_opt(distances, tour_initial)
        print("Meilleur tour trouvé:", meilleur_tour)
        print("Distance totale:", distance_tour(meilleur_tour, distances))
