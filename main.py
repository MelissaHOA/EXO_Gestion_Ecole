from address import Address  # Importation de la classe Address
# from person import Person  # Importation commentée
from student import Student  # Importation de la classe Student
from parent import Parent  # Importation de la classe Parent
from academicrecord import AcademicRecord  # Importation de la classe AcademicRecord
from teacher import Teacher  # Importation de la classe Teacher
from lesson import Lesson  # Importation de la classe Lesson
# from absence import Absence  # Importation commentée
from datetime import date  # Importation de la classe date pour la gestion des dates

# Bloc d'exécution principal pour tester les classes
if __name__ == "__main__":
    # Création d'une adresse pour l'enseignant
    address = Address("rue des glaieuls", "Toulouse", "31400")

    # Création d'un enseignant avec les informations personnelles et l'adresse
    JohnDoe = Teacher("Marie", "Martin", 40, address, 555666777, "marie.martin@example.com", date.today(), [], [])

    #Création d'une autre adresse et d'un autre enseignant
    other_address = Address("Rue des pinçons", "Toulouse","31200")
    JackSmith = Teacher("Bernard", "Durand", 40, other_address, 444888222, "marie.martin@example.com", date.today(), [], [])

    # Création d'une adresse pour l'élève
    address = Address("rue du May", "Toulouse", "31000")

    # Création d'un parent (père de l'élève) avec les informations personnelles et l'adresse
    papapierre = Parent("Jacques", "Dupont", 40, address, 645789754, "bibi@example.org", date.today(), [])

    # Création de l'élève avec les informations personnelles, l'adresse, le parent et le professeur tuteur
    student = Student("Pierre", "Dupont", 20, address, 987654321, "pierre.dupont@example.com", date.today(), papapierre,
                      JohnDoe, 42)

    # Ajout du parent à la liste des parents de l'élève
    student.add_parent(papapierre)

    # Ajout de l'élève à la liste des enfants du parent
    papapierre.add_child(student)

    # Ajout de l'élève à la liste des élèves suivis par l'enseignant (relation tuteur/élève)
    JohnDoe.add_pupil(student)

    # Création d'un cours (leçon) avec une matière, des dates de début et de fin, et un professeur
    cursus = Lesson("Philosophie", date.today(), date(2025, 6, 30), JohnDoe)

    # Création d'un autre cours
    cursus2 = Lesson("Mathématiques", date.today(), date(2025, 6, 30), JackSmith)

    # Création d'un enregistrement académique pour l'élève dans ce cours
    academic_record = AcademicRecord(pupil=student, course=cursus)

    # Création d'une autre fiche de suivi scolaire
    academic_record2 = AcademicRecord(pupil=student, course=cursus2)


    # Ajout du professeur au cours
    cursus.prof = JohnDoe
    
    # Ajout d'un prof à l'autre cursus
    
    cursus2.prof = JackSmith

    # Définition de la note obtenue par l'élève
    academic_record.set_note(95)
    
    # definition d'une note à l'autre cours
    academic_record2.set_note(85)

    # Ajout d'un commentaire sur la performance de l'élève
    academic_record.set_comment("Des débuts prometteurs. Révisez les classiques")

    # Ajout d'un commentaire sur la performance de l'élève
    academic_record2.set_comment("Quelques la cunes à combler en faisant tous les exercices prescrits")

    # Affichage des détails de l'élève
    print(student.get_details())

    # Affichage des détails du parent
    print(papapierre.get_details())

    # Affichage des détails d'un enseignant
    print(JohnDoe.get_details())
    
    # Affichage des détails d'un autre enseignant
    print(JackSmith.get_details())

    # Affichage des détails du cours (leçon)
    print(cursus.get_details())

    # Affichage de toutes les adresses enregistrées
    print("Voici les adresses enregistrées")
    for lieu in Address.liste_d_adresses:
        position: Address = lieu
        print("- " + position.to_string)

    # Création d'une absence (commentée, car la classe Absence est importée mais non utilisée)
    # absence = Absence(date(2024, 11, 15), "Maladie")

    # Ajout, modification, suppression et consultation d'une absence (commentées, car non implémentées)
    # absence.add_absence()
    # absence.modify_absence()
    # absence.delete_absence()
    # absence.consult_absence()
