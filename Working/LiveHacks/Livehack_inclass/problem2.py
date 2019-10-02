print("""
-------------------------------------------------------------------------------
Name:       problem2.py

Purpose:    To determine how many chicken pieces Mr. Fabroa and each of his
            students get.

Author:     Zhu.D

Created:    02/10/2019
-------------------------------------------------------------------------------
""")
# takes the number of students and chicken pieces , stores it in a variable
students = int(input("Number of students in the class: "))
chicken_pieces = int(input("Number of chicken pieces : "))


# this function will divide the number the chicken pieces by the number of
# students, then round down, with Mr. Fabroa taking the rest.
def chicken_distribution(students, chicken_pieces):
    if students <= chicken_pieces:
        per_student = chicken_pieces//students
        mrfabroa_pieces = chicken_pieces % students
        return print("Each student gets", per_student,
                     "chicken piece(s) and Mr. Fabroa gets", mrfabroa_pieces,
                     "piece(s).")
# if there are not enough chicken pieces, it will return this message
    if students > chicken_pieces:
        return print("The students get nothing and Mr.Fabroa takes all",
                     chicken_pieces, "pieces!")

# calls on the function chicken_distrubution
chicken_distribution(students, chicken_pieces)
