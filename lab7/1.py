students = {
    "Віталій_Сидоренко": [11, 9, 8, 9, 4, 6, 7, 4, 11, 9],
    "Дмитро_Мельник": [11, 9, 8, 4, 5, 6, 3, 2, 11, 3],
    "Михайло_Захарченко": [11, 2, 3, 5, 4, 4, 2, 6, 4, 3],
    "Максим_Коваленко": [11, 3, 9, 6, 4, 7, 2, 2, 4, 6],
    "Вікторія_Савченко": [9, 9, 9, 8, 9, 8, 9, 7, 6, 11],
    "Андрій_Петренко": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8],
    "Оксана_Литвиненко": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10],
    "Нікіта_Шевченко": [6, 7, 8, 9, 10, 10 , 10, 10, 10 ,9],
    "Карина_Коваленко": [2, 3, 5, 4, 5, 4, 3, 3, 5 ,8],
    "Євгенія_Білоус": [12, 12, 12, 10, 10, 9, 8, 9, 9 , 8]
}

min_size = 5
max_size = 10

def print_students(students):
    for i in students:
        print(f"Оцінки {i} - {students[i]}")

def print_sorted_students(students):
    temp_arr = sorted(students)
    for i in temp_arr:
        print(f"Оцінки {i} - {students[i]}")

def check_grades(grade):
    grade = int(grade)
    if grade > 12 or grade < 1:
        raise TypeError('Incorrect grade')
    return grade

def add_student():
    if len(students.keys()) == max_size:
        print("Словник заповнено, додати новий запис неможливо")
        return

    name = input("Введіть імя учня: ")
    surname = input("Введіть прізвище учня: ")
    if f"{name}_{surname}" in students.keys():
        print("Такий учень вже є у словнику")
        return

    while(1):
        try:
            grades = list(map(check_grades, input("Введіть оцінки учня з десяти предметів через пробіл: ").split()))
            break
        except:
            print("Введено некоректні оцінки, спробуйте ще раз")
                
    students[f"{name}_{surname}"] = grades
    print(f"Додано учня {name}_{surname} з оцінками {grades}")

def remove_student():
    if len(students.keys()) == min_size:
        print("Словник вже має мінімальний розмір, видалити запис неможливо")
        return

    name = input("Введіть імя учня: ")
    surname = input("Введіть прізвище учня: ")
    if f"{name}_{surname}" not in students.keys():
        print("Такого учня немає у словнику")
        return
    
    del students[f"{name}_{surname}"]
    print(f"Видалено учня {name}_{surname}")

def max_grade_student():
    max_grade = 0
    for student, grades in students.items():
        grade = sum(grades)
        if grade > max_grade:
            max_grade = grade
            result = student
    print(result.split("_")[1])

def min_grade_student():
    min_grade = sum(students[list(students)[0]])
    for student, grades in students.items():
        grade = sum(grades)
        if grade < min_grade:
            min_grade = grade
            result = student
    print(result.split("_")[1])

def menu():
    while(1):
        print("\nОберіть дію\
              \n1. Вивести на екран всіх учнів\
              \n2. Додати нового учня до словника\
              \n3. Видалити учня зі словника\
              \n4. Вивести на екран відсортований словник\
              \n5. Вивести прізвище учня з найбільшою сумою оцінок\
              \n6. Вивести прізвище учня з найменшою сумою оцінок"\
              "\n7. Вихід")
        try:
            choice = int(input('\n'))
            if choice > 7 or choice < 1:
                raise ValueError("Incorrect action")
        except:
            print("Невірна дія")
            continue
        
        match choice:
            case 1:
                print_students(students)

            case 2:
                add_student()
            
            case 3:
                remove_student()

            case 4:
                print_sorted_students(students)
            
            case 5:
                max_grade_student()

            case 6:
                min_grade_student()
            
            case 7:
                break

menu()
