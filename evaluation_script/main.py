import random
from .pyneogame.gym import Gym
from .pyneogame.Agent.GreedyAgent import GreedyAgent
from .pyneogame.Agent.DeepQAgent import DeepQAgent
from .pyneogame.Agent.RandomAgent import RandomAgent
from .pyneogame.Engine import Game
from pathlib import Path


def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")

    output = {}
    output["result"] = [
    {
        "test_split": {
        }
    }
    ]

    N_GAMES = 1000
    DQ_FILE = str(Path(__file__).parent.absolute())+'/models/dq_agent.h5'

    print("Evaluating model: {}".format(user_submission_file))

    game = Game()
    player = DeepQAgent(state_size=len(game.get_player_state()),
                           actions=game.get_actions())
    player.load(user_submission_file)
    random_agent = RandomAgent()
    greedy_agent = GreedyAgent()
    dq_agent = DeepQAgent(state_size=len(game.get_player_state()),
                         actions=game.get_actions()).load(DQ_FILE)

    agent_list = [random_agent, greedy_agent, dq_agent]
    total_score = 600

    for agent in agent_list:
        gym = Gym(player, agent)
        agent_name = agent.get_name()
        gym.test(N_GAMES)
        n_wins, n_losses = gym.get_results()
        output["result"][0]["test_split"][agent_name + "_wins"] = n_wins
        output["result"][0]["test_split"][agent_name + "_losses"] = n_losses
        total_score += n_wins - n_losses

    output["result"][0]["test_split"]["Total"] = total_score
    output["submission_result"] = output["result"][0]

    print(output)
    return output


if __name__ == "__main__":
    print("main")
    evaluate(None, "models/dq_agent.h5", "test")