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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    *Instrucciones: 
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    > abajo < 
    """ 

    """
    *Informacion util:
    problem.getStartState = posicion actual del agente
    problem.isGoalState   = verifica que sea la meta
    problem.getSuccessors = obtiene los caminos disponibles basado en posicion
    
    con getSuccessors se obtiene una lista, cada elemento con 3 elementos
    internos. 
    El primero representa posicion,
    el segundo representa direccion,
    el tercero representa peso.
    
    """

    # Posicion del agente

    pos, dir, peso = 0, 1, 2

    posicion = problem.getStartState()

    # stack que  
    stack = util.Stack() # posicion y direccion
    visitados = []

    stack.push([posicion, []]) # agregamos la posicion inicial

    while not stack.isEmpty():

        posicion_actual, direccion = stack.pop()

        if posicion_actual in visitados:
            continue

        visitados.append(posicion_actual)

        if problem.isGoalState(posicion_actual):
            return direccion
        
        vecinos = problem.getSuccessors(posicion_actual)
        for vecino in vecinos:
            if vecino[pos] not in visitados:
                nueva_direccion = direccion + [vecino[dir]]
                stack.push((vecino[pos], nueva_direccion))
    
    # en caso de no encontrar solucion
    return  []
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    pos, dir, peso = 0, 1, 2
    posicion = problem.getStartState()

    print(posicion)
    

    queue = util.Queue()        # iniciailizar cola vacia
    queue.push([posicion, []])  # agregar primer posicion inicial a la cola 
    
    
    visitados = []            
    visitados.append(posicion)

    while not queue.isEmpty():
        posicion_actual, direccion = queue.pop()

        if problem.isGoalState(posicion_actual):
            return direccion

        vecinos = problem.getSuccessors(posicion_actual)

        for vecino in vecinos:
            if vecino[pos] in visitados:
                continue

            visitados.append(vecino[pos])
            nueva_direccion = direccion + [vecino[dir]]
            queue.push((vecino[pos], nueva_direccion))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """
    util cuando hay costos variables de nodo a nodo.
    El objetivo es encontrar el camino con menor costo posible

    Este algoritmo utiliza *Priority queue*, estructura que permite 
    expandir primero a los nodos con menor costo.
    """

    pos, dir, peso = 0, 1, 2
    posicion = problem.getStartState()
    
    queue = util.PriorityQueue()        # inicializar cola vacia
    queue.push([posicion, []], -1)  # agregar primer posicion inicial a la cola 
    
    
    visitados = []            
    visitados.append(posicion)

    while not queue.isEmpty():
        posicion_actual, direccion = queue.pop()
        
        if problem.isGoalState(posicion_actual):
            return direccion

        vecinos = problem.getSuccessors(posicion_actual)

        #? ver como proporcionar la prioridad

        for vecino in vecinos:
            print(vecino)
            if vecino[pos] in visitados:
                continue
            
            visitados.append(vecino[pos])
            nueva_direccion = direccion + [vecino[dir]]
            queue.push((vecino[pos], nueva_direccion), vecino[peso])

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
