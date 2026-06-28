def calculer_interets(capital: float, taux: float, annees: int) -> float:
    """Calcule les intérêts simples d'un capital."""
    if capital < 0 or taux < 0 or annees < 0:
        raise ValueError("Les valeurs doivent être positives.")
    return capital * (taux / 100) * annees


def calculer_mensualite(capital: float, taux_annuel: float, mois: int) -> float:
    """Calcule la mensualité fixe pour un remboursement de prêt."""
    if capital <= 0 or mois <= 0:
        raise ValueError("Le capital et la durée doivent être supérieurs à 0.")

    # Si le taux est nul, c'est un crédit à taux zéro
    if taux_annuel == 0:
        return round(capital / mois, 2)

    taux_mensuel = (taux_annuel / 100) / 12

    # Formule mathématique du crédit à mensualité constante
    mensualite = (capital * taux_mensuel) / (1 - (1 + taux_mensuel) ** -mois)
    return round(mensualite, 2)


if __name__ == "__main__":
    # Simulation d'une exécution classique
    print("--- Simulation Crédit Étudiant ---")
    cap = 10000
    tx = 2.5
    duree = 24
    print(f"Pour un prêt de {cap}€ à {tx}% sur {duree} mois :")
    print(f"Mensualité = {calculer_mensualite(cap, tx, duree)}€")
