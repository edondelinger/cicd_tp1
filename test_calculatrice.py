import pytest
from appli import calculer_interets, calculer_mensualite

def test_calculer_interets_classique():
    # Test d'un calcul d'intérêts standard
    # 10 000€ à 5% sur 2 ans = 1 000€ d'intérêts
    assert  calculer_interets(10000, 5, 2) == 1000.0

def test_calculer_mensualite_taux_zero():
    # Test du cas limite : crédit sans intérêt
    # 12 000€ sur 12 mois à 0% = 1 000€ par mois
    assert calculer_mensualite(12000, 0, 12) == 1000.0

def test_calculer_interets_valeur_negative_leve_erreur():
    # On vérifie que notre application se défend bien si on met une valeur négative
    with pytest.raises(ValueError):
        calculer_interets(-1000, 5, 2)