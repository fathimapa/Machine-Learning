import random
import copy


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn

        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        counts = {}
        for ball in drawn_balls:
            counts[ball] = counts.get(ball, 0) + 1

        result = True
        for color, amount in expected_balls.items():
            if counts.get(color, 0) < amount:
                result = False
                break

        if result:
            success += 1

    return success / num_experiments
