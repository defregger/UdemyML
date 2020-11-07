import gym
import numpy as np
from numpy.lib.function_base import percentile
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
        pass

    def get_sample(self, num_episodes):
        pass

    def filter_episodes(self, rewards, episodes, percentile):
        pass

    def train(self, percentile, num_iterations, num_episodes):
        pass

    def play(self, num_episodes, render = True):
        pass


if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    agent = Agent(env)
    # agent.train()
    # agent.play()
