# searchAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
#
# This code has been modified and extended for CS 1820 at Harvard University, 
# with adjustments tailored to align with the course curriculum and objectives.

from helpers.game import Directions
from helpers.game import Agent
import time
import search
import os
import sys


#######################################################
# This portion is written for you, but will only work #
#       after you fill in parts of search.py          #
#######################################################
class SearchAgent(Agent):
    """
    This very general search agent finds a path using a supplied search
    algorithm for a supplied search problem, then returns actions to follow that
    path.

    Note: You should NOT change any code in SearchAgent
    """

    def __init__(self, fn='depthFirstSearch', prob='FoodSearchProblem', heuristic='nullHeuristic'):
        # Warning: some advanced Python magic is employed below to find the right functions and problems

        # Get the search function from the name and heuristic
        if fn not in dir(search):
            raise AttributeError(fn + ' is not a search function in search.py.')
        func = getattr(search, fn)
        if 'heuristic' not in func.__code__.co_varnames:
            print('[SearchAgent] using function ' + fn)
            self.searchFunction = func
        else:
            if heuristic in globals().keys():
                heur = globals()[heuristic]
            elif heuristic in dir(search):
                heur = getattr(search, heuristic)
            else:
                raise AttributeError(heuristic + ' is not a function in searchAgents.py or search.py.')
            print('[SearchAgent] using function %s and heuristic %s' % (fn, heuristic))
            # Note: this bit of Python trickery combines the search algorithm and the heuristic
            self.searchFunction = lambda x: func(x, heuristic=heur)

        # Get the search problem type from the name
        if prob not in globals().keys() or not prob.endswith('Problem'):
            raise AttributeError(prob + ' is not a search problem type in SearchAgents.py.')
        self.searchType = globals()[prob]
        print('[SearchAgent] using problem type ' + prob)

    def registerInitialState(self, state):
        """
        This is the first time that the agent sees the layout of the game
        board. Here, we choose a path to the goal. In this phase, the agent
        should compute the path to the goal and store it in a local variable.
        All of the work is done in this method!

        state: a GameState object (pacman.py)
        """
        layout = str(state.data.layout)
        # Split the string into lines
        lines = layout.splitlines()

        # Create the 2D array
        game_grid = []
        for line in lines:
            game_grid.append(list(line))

        if self.searchFunction == None: raise Exception("No search function provided for SearchAgent")
        starttime = time.time()
        
        problem = self.searchType(game_grid) # Makes a new search problem
        self.actions  = self.searchFunction(problem) # Find a path
        print(self.actions)
        if self.actions == None:
            self.actions = []
        totalCost = problem.getCostOfActions(self.actions)
        print('Path found with total cost of %d in %.1f seconds' % (totalCost, time.time() - starttime))
        if '_expanded' in dir(problem): print('Search nodes expanded: %d' % problem._expanded)

    def getAction(self, state):
        """
        Returns the next action in the path chosen earlier (in
        registerInitialState).  Return Directions.STOP if there is no further
        action to take.

        state: a GameState object (pacman.py)
        """
        if 'actionIndex' not in dir(self): self.actionIndex = 0
        i = self.actionIndex
        self.actionIndex += 1
        if i < len(self.actions):
            return self.actions[i]
        else:
            return Directions.STOP

folder_path = 'layouts' 

#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################
class FoodSearchProblem(search.SearchProblem):
    """
    Fill in these methods to define the pacman food search as a search problem.
    Refer to the definition of a search problem in search.py to help implement the methods.
    Feel free to use any data type/structure to define your states though.
    """
   
    def __init__(self, game_grid, visualize=True):
        """Read the game grid and initialize all necessary variables for the search problem"""
        self.game_grid = game_grid
        
        # Setting up structure to store basic info
        self.row_len = len(game_grid)
        self.col_len = len(game_grid[0])
        self.start_position = None
        self.food_positions = set()
        self.ghost_positions = set()
        self.energizer_positions = set()
        
        # Parse the matrix into game info
        for col in range(self.col_len):
            for row in range(self.row_len):
                if game_grid[row][col] == 'P':
                    self.start_position = (row, col)
                elif game_grid[row][col] == 'G':
                    self.ghost_positions.add((row, col))
                elif game_grid[row][col] == '.':
                    self.food_positions.add((row, col))
                elif game_grid[row][col] == 'o':
                    self.energizer_positions.add((row, col))
        
        # Use frozenset for hashing purposes in DFS and BFS
        self.start_state = (self.start_position, frozenset(self.food_positions), 0)

        # For display purposes DO NOT CHANGE
        self.init_display(visualize)

    def getCurrentPosition(self, state):
         """Make sure to return a tuple (row, column) of where Pacman is in on the game_grid, for display purposes"""
         return state[0]       

    def getStartState(self):
        return self.start_state

    def isGoalState(self, state):
        isGoal = False
        if len(state[1]) == 0:
            isGoal = True

        # For display purposes DO NOT CHANGE
        self.goal_display(state, isGoal)
        return isGoal


    def getSuccessors(self, state):
        "Returns successor states, the actions they require, and a cost of 1."
        successors = []
        # Potential four movements Pacman can take
        actions = [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]
        moving_dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        pacman_pos, remaining_food, energized_time = state
        cur_row, cur_col = pacman_pos
        
        for action, (row_change, col_change) in zip(actions, moving_dir):
            new_row, new_col = cur_row + row_change, cur_col + col_change
        
            # Check for invalid move
            # Out of bound
            if not (0 <= new_row < self.row_len and 0 <= new_col < self.col_len):
                continue
            # Hit wall
            if self.game_grid[new_row][new_col] == '%':
                continue
            # Encounter a ghost when not energized
            if (new_row, new_col) in self.ghost_positions and energized_time == 0:
                continue
            
            new_food = set(remaining_food)
            new_energized_time = max(0, energized_time - 1)
            
            # Remove food dot if Pacman encounter one
            if (new_row, new_col) in remaining_food:
                new_food.remove((new_row, new_col))
                
            # Add energized time if Pacaman encounter an energizer
            if (new_row, new_col) in self.energizer_positions:
                new_energized_time = 10
                
            new_state = ((new_row, new_col), frozenset(new_food), new_energized_time)
            successors.append((new_state, action, 1))
        
        # Bookkeeping for display purposes DO NOT CHANGE
        self.successor_display(state)

        return successors

    def getCostOfActions(self, actions):
        """Returns the cost of a particular sequence of actions."""
        return len(actions)

    ### Helper Methods DO NOT CHANGE

    def init_display(self, visualize): 
        self.visualize = visualize
        self._visited, self._visitedlist, self._expanded = {}, [], 0 
        self.rows = len(self.game_grid)

    def goal_display(self, state, isGoal): 
        r, c = self.getCurrentPosition(state)
        x = c
        y = self.rows - r - 1
        if isGoal and self.visualize:
            self._visitedlist.append((x, y))
            import __main__
            if '_display' in dir(__main__):
                if 'drawExpandedCells' in dir(__main__._display): #@UndefinedVariable
                    __main__._display.drawExpandedCells(self._visitedlist) #@UndefinedVariable
        
    def successor_display(self, state):
        self._expanded += 1
        r, c = self.getCurrentPosition(state)
        x = c
        y = self.rows - r - 1
        if (x, y) not in self._visited:
            self._visited[(x, y)] = True
            self._visitedlist.append((x, y))
    
        

class AStarFoodSearchAgent(SearchAgent):
    "A SearchAgent for FoodSearchProblem using A* and your foodHeuristic"
    def __init__(self):
        self.searchFunction = lambda prob: search.aStarSearch(prob, foodHeuristic)
        self.searchType = FoodSearchProblem

def simpleHeuristic(state, problem: FoodSearchProblem):
     return len(state[1])

def foodHeuristic(state, problem: FoodSearchProblem):
    position, remaining_food, energized_time = state

    if not remaining_food:
        return 0
    
    subproblem = FoodSearchProblem(problem.game_grid, visualize=True)
    subproblem.start_state = (position, frozenset(remaining_food), energized_time)
    
    def bfs_search(problem):
        queue = []
        start_state = problem.getStartState()
        queue.append((start_state, 0))
        visited = set()
        visited.add(start_state)
        while queue:
            state, cost = queue.pop(0)
            
            # Return if we find a goal state
            if problem.isGoalState(state):
                return cost
                        
            # Add successors to queue
            for successor, _, step_cost in problem.getSuccessors(state):
                if successor in visited:
                    continue
                visited.add(successor)
                queue.append((successor, cost + step_cost))
        
        return 0
    
    return bfs_search(subproblem)

"""
Below is a real heuristic that use MST
def foodHeuristic(state, problem: FoodSearchProblem):
    position, remaining_food, _ = state

    if not remaining_food:
        return 0

    # Include Pacman's position in MST computation
    all_points = [position]
    for food in remaining_food:
        all_points.append(food)

    def prim_mst(points, problem):
        if not points:
            return 0

        num_nodes = len(points)
        edges = {i: [] for i in range(num_nodes)}

        # Compute all pairs of Manhattan distances
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges[i].append((distance, j))
                edges[j].append((distance, i))

        # Prim's algorithm
        mst_cost = 0
        visited = set()
        min_edge_cost = [float("inf")] * num_nodes
        min_edge_cost[0] = 0 

        while len(visited) < num_nodes:
            # Find the unvisited node with smallest edge cost
            min_cost = float("inf")
            min_node = None
            for i in range(num_nodes):
                if i not in visited and min_edge_cost[i] < min_cost:
                    min_cost = min_edge_cost[i]
                    min_node = i

            if min_node is None:
                break

            visited.add(min_node)
            mst_cost += min_cost

            # Update edge costs for unvisited ones
            for cost, neighbor in edges.get(min_node, []):
                if neighbor not in visited and cost < min_edge_cost[neighbor]:
                    min_edge_cost[neighbor] = cost

        return mst_cost

    return prim_mst(all_points, problem)  # Compute MST cost manually
"""