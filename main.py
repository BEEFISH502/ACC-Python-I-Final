##student registration function##
''''inputs students, and grades
apends to dict 3 quizzes and lab score'''

## final score function###

## pass fail function##

##report card function##

#Make sure names are formatted nicely#
def clean_name(name):
    name = name.strip().title()

    return name

def get_score(class_count, grading_mode):
    #Initiate gradebook dictionary#
    students = []
    for student in range(class_count):
        #Student[ID,name,and quiz/lab score] inputs#
        ID =(int(input('Enter student ID: ')))
        name = clean_name(str(input('Enter student name: ')))
        quizzes = []
        #q1, q2, q3#
        for quiz in range(3):
            score = float(input(f'Enter quiz {quiz+1} score (0-100): '))
            while score < 0 or score > 100:
                print('Must be between 0 and 100')
                score = float(input(f'Enter quiz {quiz+1} score (0-100): '))
            quizzes.append(score)
        # lab score #
        score = float(input(f'Enter lab score (0-100): '))
        while score < 0 or score > 100:
            print('Must be between 0 and 100')
            score = float(input(f'Enter lab score (0-100): '))
        quizzes.append(score)
        # hx, and binary function calls, append to dictionary#
        hx = hex_num(ID)
        bi = bi_num(ID)
        # calculate quiz avg and final score with grade. append to student record#
        final = final_score(quizzes, grading_mode)
        student_record = {"ID": ID,
                          "bi": bi,
                          "hx": hx,
                          "name": name,
                          "final_score": final[0],
                          "result": final[1]
                          }
        students.append(student_record)
    return students


def final_score(quizzes, grading_mode):
    #calculate grade averages, and final score
    grade = []
    quiz_avg = sum(quizzes[:3]) / 3
    final = (float(quiz_avg * 0.70)) + (float(quizzes[-1]) * 0.30)
    #Letter grade mode#
    if grading_mode == 'L':
        if 90 <= final <= 100:
            grade.append(final)
            return final, 'A'
        elif 80 <= final <= 89:
            grade.append(final)
            return final, 'B'
        elif 70 <= final <= 79:
            grade.append(final)
            return final, 'C'
        elif 60 <= final <= 69:
            grade.append(final)
            return final, 'D'
        else:
            grade.append(final)
            return final, 'F'
    #pass/ fail mode#
    if grading_mode == 'P':
        pass_fail = []
        if final >= 60:
            pass_fail.append(final)
            return final, 'Pass'
        else:
            pass_fail.append(final)
            return final, 'Fail'
    else:
        return final, 'Invalid Mode'

def bi_num(ID):
    num = ID
    bits = []
    while num > 0:
        bits.append(str(num % 2))
        num //= 2
    return ''.join(reversed(bits))

def hex_num(ID):
    num = ID
    hex_bits = []
    hex_dig = "0123456789ABCDEF"
    while num > 0:
        hex_bits.append(str(num % 16))
        num //= 16
    for num in hex_bits:
        hex_bits[hex_bits.index(num)] = hex_dig[int(num)]

    return ''.join(reversed(hex_bits))

def main():
    #main function gets initial inputs to start the program#
    class_count = int(input('How many students? '))
    grading_mode = ''
    while grading_mode == '':
        grading_mode = input('Enter report mode: L=Letter, P=Pass/Fail: ')
        if grading_mode == 'L' or grading_mode =='P':
            print('Entering grading mode: ', grading_mode)
        else:
            print('Invalid mode, enter L or P. ')
            grading_mode = ''
    # single function call for all students#
    students = get_score(class_count, grading_mode)
    print(f'--- Report Cards ---')
    #for loop to print all student report cards#
    for student in students:
        print(f'ID: {student["ID"]} | Binary: {student["bi"]} | Hex: {student["hx"]}\n'
              f'Name: {student["name"]}\nFinal score: {student["final_score"]:.2f}\n'
              f'Result: {student["result"]}')

#call main function to run prgram#
main()



