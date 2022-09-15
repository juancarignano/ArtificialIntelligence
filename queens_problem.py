from simpleai.search import SearchProblem

# estructura estados
# {0, 1, 3, 5, 2, 7, 5, 2}

# estructura de accion
# {3, 1} (esto cambia la reina de arriba 5 a 6; si hubiera sido -1 iria a 4) quedando {0, 1, 3, 6, 2, 7, 5, 2}


class QueensProblem(SearchProblem):
    def actions(self, state):
        available_actions = []

        for i in range(8):
            queen_row = state[i]
            if queen_row > 0:
                available_actions.append((i, -1))
            if queen_row < 7:
                available_actions.append((i, 1))


        return available_actions

    def result(self, state, action):
        state = list(state) # transformacion para que sea compatible con lib, tuplas no se pueden modificar

        state[action[0]] = state[action[0]] + action[1] # en 0 tengo '3' y en 1 tengo '1' {3, 1}

        return tuple(state)


    def is_goal(self, state):
        for q1 in range(8):
            for q2 in range(8):
                if state[q1] == state[q2]:
                    return False
                
                diff_h = abs(q1 - q2)
                diff_v = abs(state[q1] - state[q2])
                if diff_h == diff_v:
                    return False

        return True

    def cost(self, state, action, state2):
        return 1

    actions((3, 1), (0, 1, 3, 5, 2, 7, 5, 2))
