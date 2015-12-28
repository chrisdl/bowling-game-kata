class Game(object):
    '''
    This describes a game of bowling.
    '''
    frames = []
    current_frame = []

    def __init__(self):
        self.current_frame = []
        self.frames = []

    def frame_total(self):
        return sum(self.current_frame)

    def _frame_done(self):
        return (self.is_strike(frame=self.current_frame) or
                len(self.current_frame) == 2)

    def roll(self, pins):
        self.current_frame.append(pins)
        if self._frame_done():
            self.frames.append(self.current_frame)
            self.current_frame = []

    def _frames(self):
        '''Iterate to give access to the next frame and the next next frame'''
        iterator = iter(self.frames)
        current_frame = iterator.next()
        next_frame = iterator.next()
        frame_nr = 1
        for next_next_frame in iterator:
            yield (frame_nr, current_frame, next_frame, next_next_frame)
            current_frame = next_frame
            next_frame = next_next_frame
            frame_nr += 1
        yield(frame_nr, current_frame, next_frame, None)
        frame_nr += 1
        yield(frame_nr, next_frame, None, None)

    def score(self):
        game_score = 0
        for frame_nr, frame, next_frame, next_next_frame in self._frames():
            if frame_nr > 10:
                break
            if self.is_strike(frame=frame):
                game_score += 10 + self.strike_bonus(frame=frame, next_frame=next_frame, next_next_frame=next_next_frame)
            elif self.is_spare(frame=frame):
                game_score += 10 + self.spare_bonus(frame=frame, next_frame=next_frame)
            else:
                game_score += self.sum_of_balls_in_frame(frame=frame)
        return game_score

    def is_spare(self, frame):
        return frame[0] != 10 and sum(frame) == 10

    def is_strike(self, frame):
        return frame[0] == 10

    def sum_of_balls_in_frame(self, frame):
        return sum(frame)

    def spare_bonus(self, frame, next_frame):
        return next_frame[0]

    def strike_bonus(self, frame, next_frame, next_next_frame):
        if self.is_strike(frame=next_frame):
            return next_frame[0] + next_next_frame[0]
        else:
            return sum(next_frame)
