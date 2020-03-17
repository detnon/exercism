class Garden:

    def get_groups(self, diagram):
        rows = diagram.split('\n')
        groups = []
        f = 0
        s = 2
        for r in range(int(len(rows[0]) / 2)):
            groups.append(''.join(rows[0][f:s]+rows[1][f:s]))
            f += 2
            s += 2
        return(groups)


    def plants(self):
        plants = ['Radishes','Grass','Clover','Violets']
        for g in get_groups(diagram):
            if
        if get_groups(diagram):
            plantcronym = ''.join([p[0] for p in plants ])

        # Figure out index of student in list
        # Use this to get the correct plantcronym
        # Reverse the acronym to get the full names of the plants
        # Return it.



    def __init__(self, diagram, students):
        pass
