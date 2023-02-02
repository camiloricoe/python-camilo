def solution(students):
    students.sort(key=lambda lastname: lastname.split()[-1])
    return students