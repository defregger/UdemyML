import gym
import numpy as np
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical


class Agent:
    def __init__(self, env):
        self.env = env
        self.num_obersvations = self.env.observation_space.shape[0]
        self.num_actions = self.env.action_space.n
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(units=100, input_dim=self.num_obersvations))
        model.add(Activation("relu"))
        model.add(Dense(units=self.num_actions))
        model.add(Activation("softmax"))
        model.summary()
        model.compile(
            loss="categrocial_crossentropy",
            optimizer="Adam",
            metrics=["accuracy"]
        )
        return model

    def get_action(self, state):
        state = state.reshape(1, -1)
        action_prob = self.model(state).numpy()[0]
        action = np.random.choice(self.num_actions, p=action_prob)
        return action

    def get_samples(self, num_episodes):
        rewards = [0.0 for _ in range(num_episodes)]
        episodes = [[] for _ in range(num_episodes)]

        for episode in range(num_episodes):
            state = self.env.reset()
            total_reward = 0.0

            while True:
                action = self.get_action(state)
                new_state, reward, done, _ = self.env.step(action)
                total_reward += reward
                episodes[episode].append((state, action))
                state = new_state
                if done:
                    rewards[episode] = total_reward
                    break

    def filter_episodes(self, rewards, episodes, percentile):
        pass

    def train(self, percentile, num_iterations, num_episodes):
        for _ in range(num_iterations):
            rewards, episodes = self.get_samples(num_episodes)

    def play(self, num_episodes, render = True):
        pass


if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    agent = Agent(env)
    # agent.train()
    # agent.play()
