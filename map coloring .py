from constraint import Problem

def map_coloring():
    problem = Problem()

    # Define variables (regions) and their possible colors
    regions = ['WA', 'NT', 'SA', 'QL', 'NSW', 'VIC', 'TAS']
    colors = ['red', 'green', 'blue']

    # Add variables to the problem
    for region in regions:
        problem.addVariable(region, colors)

    # Define constraints (adjacent regions cannot have the same color)
    problem.addConstraint(lambda wa, nt: wa != nt, ('WA', 'NT'))
    problem.addConstraint(lambda wa, sa: wa != sa, ('WA', 'SA'))
    problem.addConstraint(lambda nt, sa: nt != sa, ('NT', 'SA'))
    problem.addConstraint(lambda nt, ql: nt != ql, ('NT', 'QL'))
    problem.addConstraint(lambda sa, ql: sa != ql, ('SA', 'QL'))
    problem.addConstraint(lambda sa, nsw: sa != nsw, ('SA', 'NSW'))
    problem.addConstraint(lambda sa, vic: sa != vic, ('SA', 'VIC'))
    problem.addConstraint(lambda nsw, vic: nsw != vic, ('NSW', 'VIC'))

    # Solve the problem
    solutions = problem.getSolutions()

    # Print solutions
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    map_coloring()
