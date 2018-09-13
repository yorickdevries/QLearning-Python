import traceback
import sys
from main.Action import Action
from main.State import State


class Maze:

    def __init__(self, file):
        # to build a 2-d maze from a file
        up = Action("up")
        down = Action("down")
        left = Action("left")
        right = Action("right")
        self.actions = [up, down, left, right]
        # read in file
        try:
            f = open(file, "r")
            lines = f.read().splitlines()
            dimensions = lines[0].split(" ")
            w = int(dimensions[0])
            h = int(dimensions[1])
            self.states = []
            y = 0
            for i in range(1, h + 1):
                line = lines[i].split(" ")
                states = []
                self.states.append(states)
                x = 0
                for j in range(0, w):
                    if line[j] != "":
                        state = State(x, y, line[j])
                        states.append(state)
                        x += 1
                y += 1
        except FileNotFoundError:
            print("Error reading maze file " + file)
            traceback.print_exc()
            sys.exit()
        print("Ready reading maze file " + file)
        self.rewards = {}


"""
	
	private boolean isWalkable(State s) {
		//the maze's way to check if you can walk on a particular state
		//you dont need to use this directly, use the method getValidActions()
		return s.type.equals("1");
	}
	
	public ArrayList<Action> getValidActions(Agent r) {
		//use this method to retrieve the list of possible actions for an agent
		//the method checks if surrounding states are "walkable" and if the agent is not going out of the maze dimensions.
		//The method returns the list of actions
		ArrayList<Action>actionList=new ArrayList<Action>();
		if (r.y>0 && isWalkable(states[r.y-1][r.x]))
			actionList.add(actions[0]);
		if (r.y<states.length-1 && isWalkable(states[r.y+1][r.x]))
			actionList.add(actions[1]);
		if (r.x>0 && isWalkable(states[r.y][r.x-1]))
			actionList.add(actions[2]);
		if (r.x<states[r.y].length-1 && isWalkable(states[r.y][r.x+1]))
			actionList.add(actions[3]);
		return actionList;
	}
	
	public void setR(State s, double r) {
		//use this method to set the reward of the end state to the value in teh excercise
		//you can also play around with setting other states to a non-0 reward.
		//this is called reward shaping, and you can speed up the learning but also 
		//teach the agent a suboptimal solution inadvertible.
		R.put(s,  new Double(r));
	}
	
	public double getR(State s) {
		//use this method te retreive the reward for a particular state
		if (R.containsKey(s))
			return R.get(s).doubleValue();
		return 0;
	}
	
	public State getState(int x, int y) {
		//simply returns the state at the location the agent is at
		//use this to find the current state of the agent, or use Agent.getState(Maze m)
		return states[y][x];
	}
}
"""