class Garden:

    def get_groups(self, diagram):
        rows = diagram.split('\n')
        groups = []
        f = 0
        s = 2
        for r in rows:
            groups.append(''.join(rows[0][f:s]+rows[1][f:s]))
            f += 2
            s += 2
        return groups



    def plants(self, student):
        list = {
            'R':'Radishes',
            'G':'Grass',
            'C':'Clover',
            'V':'Violets'}

        group_index = self.students.index(student)
        print(group_index)
        student_group = self.get_groups(self.diagram)[group_index]
        print(student_group)
        students_plants = []

        for i in student_group:
            print(i)
            for k, v in list.items():
                if i == k:
                    students_plants.append(v)

        print(students_plants)
        return students_plants


    def __init__(self, diagram, students):
        self.students = sorted(students)
        self.diagram = diagram
