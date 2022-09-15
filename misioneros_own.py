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

# cantidad de misioneros, cantidad de canibales, orilla canoa (0 -> lado izquierdo)
INICIAL = (3, 3, 0)

# cantidad de misioneros, cantidad de canibales, orilla canoa (1 -> lado derecho)
GOAL = (0, 0, 1)

# cada accion es una tupla: (misioneros que viajan, canibales que viajan)
ACCIONES = (
    (2, 0),
    (0, 2),
    (1, 1),
    (1, 0),
    (0, 1),
)

class MisionerosProblem(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        return state == GOAL

    def actions(self, state):
        available_actions = []

        for action in ACCIONES:
            misioneros_izquierda_result, canibales_izquierda_result, _ = self.result(state, action)

            lado_izquierdo = (misioneros_izquierda_result, canibales_izquierda_result)
            lado_derecho = (3 - misioneros_izquierda_result, 3 - canibales_izquierda_result)

            todo_bien = True
            for misioneros, canibales in (lado_izquierdo, lado_derecho):
                todos_vivos = misioneros == 0 or canibales <= misioneros
                gente_suficiente = misioneros >= 0 and canibales >= 0
                
                if not (todos_vivos and gente_suficiente):
                    todo_bien = False
                    break
                
            if todo_bien:
                available_actions.append(action)
        
        return available_actions

    def result(self, state, action):
        misioneros_izquierda, canibales_izquierda, orilla_canoa = state
        misioneros_mover, canibales_mover = action

        if orilla_canoa == 0:
            orilla_canoa = 1

            misioneros_izquierda = misioneros_izquierda - misioneros_mover
            canibales_izquierda = canibales_izquierda - canibales_mover
        
        else:
            orilla_canoa = 0
            
            misioneros_izquierda = misioneros_izquierda + misioneros_mover
            canibales_izquierda = canibales_izquierda + canibales_mover
        
        return misioneros_izquierda, canibales_izquierda, orilla_canoa

    def heuristic(self, state):
        misioneros_izquierda, canibales_izquierda, _ = state
        return misioneros_izquierda + canibales_izquierda - 1

if __name__ == "__main__":
    viewer = BaseViewer()
    #result = depth_first(MisionerosProblem(INICIAL)), graph_search=True, viewer=viewer)
    #result = breadth_first(MisionerosProblem(INICIAL), graph_search=True, viewer=viewer)
    result = astar(MisionerosProblem(INICIAL))#, viewer=viewer)

    for action, state in result.path():
        print("Haciendo", action, "llegué a:")
        print(state)

    print("Profundidad:", len(list(result.path())))
    print("Stats:")
    print(viewer.stats)
