def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff", 
                    "Slytherin", 
                    "Ravenclaw", 
                    "Gryffindor", 
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])
    
    """

    houses = set()

    # Code goes here
    file = open(filename)
    for line in file:
        student = line.split("|")
        houses.add(student[2])
    return houses

# print unique_houses("cohort_data.txt")



def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]
    
    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    all_students = [winter_15, spring_15, summer_15, tas]

    file = open(filename)
    for line in file:
        line = line.rstrip()
        student = line.split("|")
        #print student[4]
        student_name = student[0] + " " + student [1]
        if student[4] == "Spring 2015":
            spring_15.append(student_name)
        elif student[4] == "Winter 2015":
            winter_15.append(student_name)
        elif student[4] == "Summer 2015":
            summer_15.append(student_name)
        else:
            tas.append(student_name)
    return all_students
    # print winter_15
    # print spring_15
    # print summer_15
    # print tas


# print sort_by_cohort("cohort_data.txt")




#first_name|last_name|house|TA|season




def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. houses_tas = [ hufflepuff, 
                        gryffindor, 
                        ravenclaw, 
                        slytherin, 
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas 
            ]
    """

   
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    all_students = [gryffindor, hufflepuff, slytherin, ravenclaw, dumbledores_army, order_of_the_phoenix, tas]

    # Code goes here
    file = open(filename)
    for line in file:
        line = line.rstrip()
        student = line.split("|")
        student_name = student [1]
        if student[2] == "Gryffindor":
            gryffindor.append(student_name)
            # gryffindor = sorted(gryffindor)

        elif student[2] == "Hufflepuff":
            hufflepuff.append(student_name)
            # hufflepuff = sorted(hufflepuff)
        elif student[2] == "Slytherin":
            slytherin.append(student_name)
            # slytherin = sorted(slytherin)
        elif student[2] == "Ravenclaw":
            ravenclaw.append(student_name)
            # ravenclaw = sorted(ravenclaw)
        elif student[2] == "Dumbledore's Army":
            dumbledores_army.append(student_name)
            # dumbledores_army = sorted(dumbledores_army)
        elif student[2] == "Order of the Phoenix":
            order_of_the_phoenix.append(student_name)
            # order_of_the_phoenix = sorted(order_of_the_phoenix)
        else:
            tas.append(student_name)
            #tas = sorted(tas)

    gryffindor.sort()
    slytherin.sort()
    ravenclaw.sort()
    dumbledores_army.sort()
    order_of_the_phoenix.sort()
    tas.sort()

    # print gryffindor
    # print hufflepuff
    # print slytherin
    # print ravenclaw
    # print dumbledores_army
    # print order_of_the_phoenix
    # print tas

    # all_students = [gryffindor, hufflepuff, slytherin, ravenclaw, dumbledores_army, order_of_the_phoenix, tas]

   
    for houses in all_students:
        print houses
        print('\n')


    return all_students

# students_by_house("cohort_data.txt")


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    # Code goes here
    file = open(filename)
    for line in file:
        line = line.rstrip()
        student = line.split("|")        
        student_tuple = tuple(student)
        student_list.append(student_tuple)
    return student_list



def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here
    student_tuples = all_students_tuple_list(student_list)
    # print student_tuples

    student_name = raw_input("Type in student's first name: ")

    for student in student_tuples:
        print student
        if student_name == student[0]:
            return student[4]
        else:
            return "Student not found."

print find_cohort_by_student_name('cohort_data.txt')

##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts. 
    Uses set operations (set math) to create a set of these names. 
    NOTE: Do not include staff -- or do, if you want a greater challenge. 

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that, when given a name, returns everyone in
    their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return

