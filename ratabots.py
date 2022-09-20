from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first,
    astar,
    greedy,
)
from simpleai.search.viewers import WebViewer, BaseViewer

LUGARES_NO_PASAR = (
    (0,3),
    (0,5),
    (1,1),
    (1,3),
    (2,2),
    (2,4),
    (3,0),
    (4,1),
    (4,3),
    (4,5),
    (5,3),
)

ACCIONES = (
    (1, 0),   # para derecha
    (-1, 0),  # para izquierda
    (0, 1),   # para arriba 
    (0, -1),  # para abajo
    (0, 0)    # comer
)

# TUPLA CON POSICIONES COMIDAS, POSICIÓN ACTUAL DE LA RATA
INICIAL = ((1,2), (4,0), (3,4)), (3,5)
GOAL = ((), (3,5))

class RataBotsProblem(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        return state == GOAL

    def actions(self, state):
        available_actions = []
        
        for action in ACCIONES:
            _, posicion_rata = self.result(state, action)
            x_rata, y_rata = posicion_rata
            todo_bien = True

            if(x_rata > 5 or y_rata > 5):
                todo_bien = False
                break

            if(0 <= x_rata < 5 and action == (-1, 0) and posicion_rata not in LUGARES_NO_PASAR):
                available_actions.append(action)

            if(0 < x_rata <= 5 and action == (1, 0) and posicion_rata not in LUGARES_NO_PASAR):
                available_actions.append(action)

            if(0 <= y_rata < 5 and action == (0, -1) and posicion_rata not in LUGARES_NO_PASAR):
                available_actions.append(action)

            if(0 < y_rata <= 5 and action == (0, 1) and posicion_rata not in LUGARES_NO_PASAR):
                available_actions.append(action)
            

        return available_actions

    def result(self, state, action):
        posiciones_comidas, posicion_rata = state
        x_rata, y_rata = posicion_rata

        if action == (0,0) and posicion_rata in posiciones_comidas:
            posiciones_comidas_list = list(posiciones_comidas)
            posiciones_comidas_list.remove(posicion_rata)
            return tuple(posiciones_comidas_list), posicion_rata

        else:
            x_rata_actual, y_rata_actual = posicion_rata
            x_mover, y_mover = action
            posicion_rata_nueva = (x_rata_actual + x_mover, y_rata_actual + y_mover)
            return posiciones_comidas, posicion_rata_nueva

    def heuristic(self, state):
        posiciones_comidas, posicion_rata = state
        x_rata, y_rata = posicion_rata
        x_entrada, y_entrada = GOAL[1]

        x_diferencia = abs(x_rata - 3)
        y_diferencia = abs(y_rata - 5)
        distance = x_diferencia + y_diferencia

        return distance

if __name__ == "__main__":
    viewer = BaseViewer()
    result = uniform_cost(RataBotsProblem(INICIAL), graph_search=True, viewer=viewer)
    #result = breadth_first(RataBotsProblem(INICIAL), graph_search=True, viewer=viewer)
    #result = astar(RataBotsProblem(INICIAL), viewer=viewer)

    for action, state in result.path():
        print("Haciendo", action, "llegué a:")
        print(state)

    print("Profundidad:", len(list(result.path())))
    print("Stats:")
    print(viewer.stats)
