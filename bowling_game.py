class Game(object):
    '''
    This describes a game of bowling.
    '''
    rolls = [0] * 21
    current_roll = 0

    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def score(self):
        game_score = 0
        frame_index = 0
        for frame in range(10):
            if self.is_strike(frame_index=frame_index):
                game_score += 10 + self.strike_bonus(frame_index=frame_index)
                frame_index += 1
            elif self.is_spare(frame_index=frame_index):
                game_score += 10 + self.spare_bonus(frame_index=frame_index)
                frame_index += 2
            else:
                game_score += self.sum_of_balls_in_frame(frame_index=frame_index)
                frame_index += 2
        return game_score

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def sum_of_balls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
