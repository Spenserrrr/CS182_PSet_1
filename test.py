import search
import os
import searchAgents
import pacman

def read_lay_file(file):
    folder_path = 'layouts'
    filepath = os.path.join(folder_path, file)
    with open(filepath, 'r') as file:
        grid = []
        for line in file: 
            row = list(line.strip())
            grid.append(row)

    return grid

arr1 = dir(search)
arr2 = dir(searchAgents)
arr1.sort()
arr2.sort()
print(arr1)
print(arr2)

### Sample Test Cases ###
# Run the following assert statements below to test your function, all should run without raising an assertion error 

prob1 = searchAgents.FoodSearchProblem(read_lay_file('maze1.lay'))
prob2 = searchAgents.FoodSearchProblem(read_lay_file('maze2.lay'))
prob3 = searchAgents.FoodSearchProblem(read_lay_file('maze3.lay'))

assert(search.depthFirstSearch(prob1) == ['West', 'West', 'West', 'West', 'South', 'South', 'East', 'West', 'East', 'West', 'East', 'West', 'East', 'South', 'East', 'East', 'North', 'East', 'North', 'North', 'West', 'West', 'West', 'East', 'East', 'East', 'South', 'South', 'West', 'South', 'West', 'West', 'South', 'West'])
assert(prob1._expanded == 62)
assert(search.depthFirstSearch(prob2) == ['West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'South', 'East', 'East', 'West', 'West', 'East', 'South', 'South', 'South', 'West', 'West', 'West', 'West', 'West', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'North', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'East', 'East', 'North', 'East', 'East', 'South', 'South', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'North', 'West', 'West', 'West', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'North', 'East', 'East', 'East', 'South', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'North', 'North', 'North', 'West', 'West', 'South', 'West', 'West', 'North', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'West', 'West', 'North', 'North', 'North', 'West', 'North', 'West', 'West', 'West', 'West', 'East', 'West', 'East', 'East', 'East', 'East', 'South', 'East', 'East', 'West', 'East', 'West', 'East', 'West', 'East', 'West', 'East', 'West', 'South', 'South', 'South', 'East', 'East', 'North', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'North', 'North', 'East'])
assert(prob2._expanded == 286)
assert(search.depthFirstSearch(prob3) == ['West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'East', 'East', 'East', 'North', 'North', 'North', 'North', 'North', 'North', 'North', 'East', 'East', 'South', 'South', 'South', 'South', 'South', 'South', 'East', 'East', 'North', 'North', 'North', 'North', 'North', 'North', 'East', 'East', 'South', 'South', 'South', 'South', 'East', 'East', 'North', 'North', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'East', 'West', 'North', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'South', 'East', 'East', 'East', 'South', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'South', 'West', 'West', 'West', 'West', 'West', 'South', 'West', 'West', 'West', 'West', 'West', 'South', 'South', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'North', 'East', 'East', 'East', 'East', 'East', 'North', 'North', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'West', 'West', 'West', 'West', 'South', 'South', 'West', 'West', 'West', 'West', 'West', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West'])
assert(prob3._expanded == 244)

print("All sample test cases for DepthFirstSearch passed!")

prob1 = searchAgents.FoodSearchProblem(read_lay_file('maze1.lay'))
prob2 = searchAgents.FoodSearchProblem(read_lay_file('maze2.lay'))
prob3 = searchAgents.FoodSearchProblem(read_lay_file('maze3.lay'))

assert(search.breadthFirstSearch(prob1) == ['South', 'South', 'West', 'South', 'West', 'West', 'North', 'South', 'South', 'West'])
assert(prob1._expanded == 46)
assert(search.breadthFirstSearch(prob2) == ['East', 'South', 'South', 'West', 'West', 'West', 'East', 'East', 'East', 'North', 'North', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'South', 'North', 'West', 'West', 'West', 'East', 'East', 'East', 'South', 'East', 'East', 'West', 'South', 'South', 'South', 'West', 'West', 'West', 'East', 'East', 'East', 'East', 'East', 'North', 'East', 'East', 'East', 'East', 'South', 'South', 'West', 'West', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West'])
assert(prob2._expanded == 12752)
assert(search.breadthFirstSearch(prob3) == ['West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'East', 'East', 'South', 'South', 'South', 'West', 'West', 'West', 'North', 'West', 'West', 'West', 'West', 'South', 'South', 'South', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West'])
assert(prob3._expanded == 1174)

print("All sample test cases for BreadthFirstSearch passed!")

prob1 = searchAgents.FoodSearchProblem(read_lay_file('maze1.lay'))
prob2 = searchAgents.FoodSearchProblem(read_lay_file('maze2.lay'))
prob3 = searchAgents.FoodSearchProblem(read_lay_file('maze3.lay'))

assert(search.aStarSearch(prob1, searchAgents.simpleHeuristic) == ['South', 'South', 'West', 'South', 'West', 'West', 'North', 'South', 'South', 'West'])
assert(prob1._expanded == 42)
assert(search.aStarSearch(prob2, searchAgents.simpleHeuristic) == ['East', 'South', 'South', 'West', 'West', 'West', 'East', 'East', 'East', 'North', 'North', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'South', 'North', 'West', 'West', 'West', 'East', 'East', 'East', 'South', 'East', 'East', 'West', 'South', 'South', 'South', 'West', 'West', 'West', 'East', 'East', 'East', 'East', 'East', 'North', 'East', 'East', 'East', 'East', 'South', 'South', 'West', 'West', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West'])
assert(prob2._expanded == 12035)
assert(search.aStarSearch(prob3, searchAgents.simpleHeuristic) == ['West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'East', 'East', 'South', 'South', 'South', 'West', 'West', 'West', 'North', 'West', 'West', 'West', 'West', 'South', 'South', 'South', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West'])
assert(prob3._expanded == 1128)

print("All sample test cases for AStarSearch passed!")

prob1 = searchAgents.FoodSearchProblem(read_lay_file('maze1.lay'))
prob2 = searchAgents.FoodSearchProblem(read_lay_file('maze2.lay'))
prob3 = searchAgents.FoodSearchProblem(read_lay_file('maze3.lay'))


def test_win(maze_number):
    pacmanParams = "-l maze" + str(maze_number) + " -p SearchAgent -a fn=astar,heuristic=foodHeuristic -q"
    g = pacman.runGames(** pacman.readCommand(pacmanParams.split(' ')))[0]
    return g.state.isWin()

assert(len(search.aStarSearch(prob1, searchAgents.foodHeuristic)) == 10)
assert(prob1._expanded < 42)
assert(test_win(1))

assert(len(search.aStarSearch(prob2, searchAgents.foodHeuristic)) == 69)
assert(prob2._expanded < 12035)
assert(test_win(2))

assert(len(search.aStarSearch(prob3, searchAgents.foodHeuristic)) == 80)
assert(prob3._expanded < 1128)
assert(test_win(3))

print("All sample test cases for custom heuristic passed!")

