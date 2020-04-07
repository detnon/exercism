from pprint import pprint

class Garden:

    student_list = [
        'Alice','Bob','Charlie','David',
        'Eve','Fred','Ginny','Harriet',
        'Ilena','Joseph','Kincaid','Larry']

    plant_list = {
        'R':'Radishes',
        'G':'Grass',
        'C':'Clover',
        'V':'Violets'}

    def get_groups(self, diagram):
        rows = diagram.split('\n')
        groups = []
        f=0
        s=2
        for r in range(int(len(rows[0]) / 2)):
            groups.append(''.join(rows[0][f:s]+rows[1][f:s]))
            f+=2
            s+=2
        return groups


    def plants(self, student):
        student_plant_map = dict(zip( self.students, self.get_groups(self.diagram)))
        pprint(student)
        pprint(student_plant_map)
        pprint(student_plant_map.get(student))

        return [v for i in student_plant_map.get(student)
                  for k,v in self.plant_list.items()
                  if i == k ]


    def __init__(self, diagram, students=student_list):
        self.students = sorted(students)
        self.diagram = diagram
