
from address import Address
# from person import Person
from student import Student
from parent import Parent
from academicrecord import AcademicRecord
from teacher import Teacher
from lesson import Lesson
# from absence import Absence
from datetime import date

if __name__ == "__main__":
    # Création d'un enseignant
    # Création d'une adresse
    address = Address("rue des glaieuls", "Toulouse", "31400")
    JohnDoe = Teacher("Marie", "Martin", 40, address, 555666777, "marie.martin@example.com", date.today(), [], [])
    # Création d'un élève
    # Création d'une adresse
    address = Address("rue du May", "Toulouse", "31000")
    # Création d'un parent
    papapierre = Parent("Jacques", "Dupont", 40, address, 645789754, "bibi@example.org", date.today(), [])
    # On ne connaît pas encore les enfants de papapierre
    student = Student("Pierre", "Dupont", 20, address, 987654321, "pierre.dupont@example.com", date.today(), papapierre,
                  JohnDoe, 42)
    student.add_parent(papapierre)
    papapierre.add_child(student)
    # Ajout d'une relation tuteur/ élève
    JohnDoe.add_pupil(student)
    # Création d'une leçon
    # lesson = Lesson("Mathématiques", date(2024, 9, 1), date(2025, 6, 30), JohnDoe)

    # Création d'une adresse
    # address = Address("123 Rue de Paris", "Paris", "75000")

    # Création d'une personne
    # person = Person("Jean", "Dupont", 30, address, 123456789, "jean.dupont@example.com", date.today())

    # Création d'un dossier académique
    # On crée d'abord un cursus
    cursus = Lesson("Philosophie", date.today(), date(2025, 6, 30), JohnDoe)
    academic_record: AcademicRecord = AcademicRecord(pupil=student, course=cursus)
    # On adjoint un professeur au cours :
    cursus.prof = JohnDoe
    academic_record.set_note(95)
    academic_record.set_comment("Des débuts prometteurs. Révisez les classiques")

    # Création d'un parent
    # parent = Parent(None)  # L'étudiant sera associé
    # après sa création

    # Création d'un étudiant
    # student=Student("Pierre", "Dupont", address, address, "624785432", "jd@example.net", papapierre,JohnDoe, 42)
    # Associer l'étudiant au parent
    # parent.student = student

    # Affichage des détails de l'étudiant
    print(student.get_details())

    # Affichage des détails du parent
    print(papapierre.get_details())

    # Affichage des détails de l'enseignant
    print(JohnDoe.get_details())


    # Affichage des détails de la leçon
    print(cursus.get_details())

    # Affichage des adresses enregistré
    print("Voici les adresses enregistrées")
    for lieu in Address.liste_d_adresses:
        position:Address = lieu
        print("- " + position.to_string)
    # Création d'une absence
    # absence = Absence(date(2024, 11, 15), "Maladie")

    # Ajout, modification, suppression et consultation d'une absence
    # absence.add_absence()
    # absence.modify_absence()
    # absence.delete_absence()
    # absence.consult_absence()
