# search.py
# ---------
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

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from helpers.game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # Stack for DFS
    # Stack stores tuples of (state, path)
    stack = util.Stack()
    start_state = problem.getStartState()
    stack.push((start_state, []))
    
    # Set to prevent re-expansion
    visited = set()
    while stack:
        state, path = stack.pop()
        
        # Return if we find a goal state
        if problem.isGoalState(state):
            return path
        
        # Avoid repetition in path
        if state in visited:
            continue
        visited.add(state)
        
        # Add successors to stack
        for successor, action, _ in problem.getSuccessors(state):
            stack.push((successor, path + [action]))
            
    return []

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    # Queue for BFS
    # Queue stores tuples of (state, path)
    queue = util.Queue()
    start_state = problem.getStartState()
    queue.push((start_state, []))
    
    # Set to prevent re-expansion
    visited = set()
    while queue:
        state, path = queue.pop()
        
        # Return if we find a goal state
        if problem.isGoalState(state):
            return path
        
        # Avoid repetition in path
        if state in visited:
            continue
        visited.add(state)
        
        # Add successors to stack
        for successor, action, _ in problem.getSuccessors(state):
            queue.push((successor, path + [action]))
            
    return []


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    pq = util.PriorityQueue()  # Priority queue for A*
    start_state = problem.getStartState()
    # Push (current cost, path, current cost g(n)) with proper priority
    pq.push((start_state, [], 0), 0 + heuristic(start_state, problem))
    
    # Set to prevent re-expansion
    visited = {}
    while pq:
        state, path, current_cost = pq.pop()
        
        # Return if we find a goal state
        if problem.isGoalState(state):
            return path
        
        # Avoid repetition in path
        if state in visited and visited[state] <= current_cost:
            continue

        visited[state] = current_cost
        
        # Add successors to stack
        for successor, action, step_cost in problem.getSuccessors(state):
            new_cost = current_cost + step_cost
            f_value = new_cost + heuristic(successor, problem)
            pq.push((successor, path + [action], new_cost), f_value)
            
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch