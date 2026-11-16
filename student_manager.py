def calculate_average(grades):
    """Retourne la moyenne. Lève ValueError si la liste est vide."""
    if not grades:
        raise ValueError("La liste des notes ne peut pas être vide.")
    return sum(grades) / len(grades)
def get_mention(average):
    """Retourne la mention selon la moyenne."""
    if average < 10:
        return "Échec"
    elif average < 12:
        return "Passable"
    elif average < 14:
        return "Assez bien"
    elif average < 16:
        return "Bien"
    elif average < 18:
        return "Très bien"
    else:
        return "Excellent"
def is_admitted(average):
    """Retourne True si moyenne >= 10."""
    return average >= 10
def validate_grades(grades):
    """Retourne True si toutes les notes sont entre 0 et 20."""
    if not grades:
        return False
    return all(0 <= grade <= 20 for grade in grades)
if __name__ == "__main__":
    notes = [12, 15, 18]
    average = calculate_average(notes)
    print("Moyenne :", average)
    print("Mention :", get_mention(average))
    print("Admis :", is_admitted(average))
    print("Notes valides :", validate_grades(notes))