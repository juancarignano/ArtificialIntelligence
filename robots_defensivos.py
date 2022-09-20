from math import ceil
from itertools import combinations

from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    uniform_cost,
    greedy,
    astar,
)
from simpleai.search.viewers import WebViewer, BaseViewer

# posición en la grilla (x,y)
INITIAL = (1, 0)
GOAL = (2, 3)

NO_ACCESIBLE = (
    (2, 0),
    (3, 1),
    (1, 2)
)

ACCIONES = (
    (1, 0),  # Arriba
    (-1, 0), # Abajo
    (0, 1),  # Derecha
    (0, -1), # Izquierda
)


class RobotsDefensivos(SearchProblem):
    def cost(self, state1, action, state2):
        return 1
    
    def is_goal(self, state):
        return state == GOAL

    def actions(self, state):
        acciones_disponibles = []
        dentro_grilla = True

        for accion in ACCIONES:
            result_state = self.result(state, accion)
            robot_x, robot_y = result_state

            if(0 > robot_x < 5 or 0 > robot_y < 5):
                dentro_grilla = False
                break
            
            if(dentro_grilla and result_state not in NO_ACCESIBLE):
                acciones_disponibles.append(accion)

        return acciones_disponibles

    def result(self, state, action):
        robot_x, robot_y = state
        action_x, action_y = action

        return robot_x + action_x, robot_y + action_y


if __name__ == "__main__":
    viewer = BaseViewer()
    result = depth_first(RobotsDefensivos(INITIAL), graph_search=True, viewer=viewer)
    #result = breadth_first(MisionerosProblem(INITIAL), graph_search=True, viewer=viewer)
    #result = astar(RobotsDefensivos(INITIAL), viewer=viewer)

    for action, state in result.path():
        print("Haciendo", action, "llegué a:")
        print(state)

    print("Profundidad:", len(list(result.path())))
    print("Stats:")
    print(viewer.stats)
