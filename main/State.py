class State:
    def __init__(self, state_type):
        # the type of the state is a 0 or a 1, 1 being path, 0 being the wall
        self.type = str(state_type)