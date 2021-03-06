# @author : primexu
# @author : primexu


from maze_env import Maze
from RL_brain import QLearningTable

# @author: sunshine
# @date: 20200706



def update():
    for episode in range(50):
        observation = env.reset()
        while True:
            env.render()

            action = RL.choose_action(str(observation))  # observation is equal to state
            observation_, reward, done = env.step(action)  # after taking the action, the new state and reward are returned
            #  parameter 'done' represents whether the explore has ended.

            RL.learn(str(observation), action, reward, str(observation_))  # a iteration or transition
            observation = observation_
            if done:
                break

    print('game over')
    env.destroy()
    # env.destroy()


if __name__ == "__main__":
    # env.destroy()
    # env.destroy()
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()
    print('\r\nQ-table:\n')
    print(RL.q_table)
