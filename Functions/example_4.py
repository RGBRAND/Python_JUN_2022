# waf to calulate the grad of students based on the total marks 
def generate_marks(totalmarks):
    if totalmarks >= 90:
        return 'A'
    elif totalmarks >= 80:
        return 'B'
    elif totalmarks >= 70:
        return 'C'
    elif totalmarks >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':

    grade = generate_marks(78)
    print(f'you got grade: {grade}')