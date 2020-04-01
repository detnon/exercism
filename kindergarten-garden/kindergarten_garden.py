class Garden:

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
        list = {
            'R':'Radishes',
            'G':'Grass',
            'C':'Clover',
            'V':'Violets'}

        print( self.get_groups(self.diagram))
        group_index = self.students.index(student)
        print( group_index)
        student_group = self.get_groups(self.diagram)[group_index]
        students_plants = []

        for i in student_group:
            for k, v in list.items():
                if i == k:
                    students_plants.append(v)
        return students_plants


    def __init__(self, diagram, students=['Alice','Bob','Charlie','David',
                                          'Eve','Fred','Ginny','Harriet',
                                          'Llena','Joseph','Kincaid','Larry']):
        self.students = sorted(students)
        self.diagram = diagram
