class Agent:

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.x = start_x
        self.y = start_y
        self.nr_of_actions_since_reset = 0

"""
package tudelft.rl;

public class Agent {
	public int x,y;
	private int startX, startY;
	public int nrOfActionsSinceReset=0;
	
	public Agent(int startX, int startY) {
		this.startX=startX;
		this.startY=startY;
		x=startX;
		y=startY;
	}
	public State getState(Maze m) {
		return m.getState(this.x, this.y);
	}
	
	public State doAction(Action a, Maze m) {
		//executes an action and returns the new State the agent is in according to the Maze
		nrOfActionsSinceReset++;
		if (a.id.equals("up"))
			y--;
		if (a.id.equals("down"))
			y++;
		if (a.id.equals("left"))
			x--;
		if (a.id.equals("right"))
			x++;
		return getState(m);
	}
	
	public void reset() {
		System.out.println(nrOfActionsSinceReset);
		x=startX;
		y=startY;
		nrOfActionsSinceReset=0;
	}
}

"""