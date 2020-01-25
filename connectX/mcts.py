from __future__ import division
import datetime
from random import choice
from math import log
from math import sqrt






class Board(object):
    def __init__(self):
        self.board = create_zero()
        self.turn = 1
        self.tup = tup_base(create_zero())
    def start(self):
        return tup(create_zero())   
    def current_player(self, state):
        return turn_check(board_base(state))
    def next_state(self, state, play):
        return tup_base(fallext(state, play, self.current_player(board_base(state))))
    def legal_plays(self, statehistory):
        state = statehistory[-1]
        b = board_base(state)[0]
        l = []
        for i in range(7):
            if b[i] = 0:
                l.append[i]
        return l
    def winner(self, statehistory):
        state = statehistory[-1]
        w = check_winner()
        if w == 1:
            return 1
        if w == 2:
            return 2
        v = check_valid()
        if v == True:
            return -1
        else:
            return 0


















max_moves = 100
Seconds = 30
C = 1.4

b2 = Board()

def POLICY(state):
  return basic_policy(board_base(state), board.current_player(state))

def VALUE(state):
  return basic_value(board_base(state), board.current_player(state))



policy = POLICY   
value = VALUE 
    
def policy_choice():

    pass

"""notes: rollout needs to be updated to incorporate policy and value       .    Also, fix def winner in board                """

class MonteCarlo2(object):
    #states are tuples
    def __init__(self, board, **kwargs):
        # Takes an instance of a Board and optionally some keyword
        # arguments.  Initializes the list of game states and the
        # statistics tables.
        self.board = board
        self.states = []
        self.leaf_state = 'empty'
        self.leaf_value = 'empty'
        
        seconds = Seconds
        self.calculation_time = datetime.timedelta(seconds=seconds)
        
        
        self.max_moves = max_moves
        
        
        
        self.wins = {}
        self.plays = {}
        self.C = 1.4
        
        
        
        pass

    def update(self, state):
        # Takes a game state, and appends it to the history.
        self.states.append(state)
        pass

    def get_play(self):
        # Causes the AI to calculate the best move from the
        # current game state and return it.
        
        self.max_depth = 0
        state = self.states[-1]
        player = self.board.current_player(state)
        legal = self.board.legal_plays(self.states[:])

        # Bail out early if there is no real choice to be made.
        if not legal:
            return
        if len(legal) == 1:
            return legal[0]

        games = 0
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation()
            games += 1

        moves_states = [(p, self.board.next_state(state, p)) for p in legal]

        # Display the number of calls of `run_simulation` and the
        # time elapsed.
        print (games, datetime.datetime.utcnow() - begin)

        # Pick the move with the highest percentage of wins.
        percent_wins, move = max(
            (self.wins.get((player, S), 0) /
             self.plays.get((player, S), 1),
             p)
            for p, S in moves_states
        )

        # Display the stats for each possible play.
        for x in sorted(
            ((100 * self.wins.get((player, S), 0) /
              self.plays.get((player, S), 1),
              self.wins.get((player, S), 0),
              self.plays.get((player, S), 0), p)
             for p, S in moves_states),
            reverse=True
        ):
            print("{3}: {0:.2f}% ({1} / {2})".format(*x))

        print ("Maximum depth searched:", self.max_depth)

        return move

    def run_simulation(self):
        plays, wins = self.plays, self.wins

        visited_states = set()
        states_copy = self.states[:]
        state = states_copy[-1]
        player = self.board.current_player(state)

        expand = True
        for t in range(1, self.max_moves + 1):
            legal = self.board.legal_plays(states_copy)
            moves_states = [(p, self.board.next_state(state, p)) for p in legal]

            if all(plays.get((player, S)) for p, S in moves_states):
                # If we have stats on all of the legal moves here, use them.
                log_total = log(
                    sum(plays[(player, S)] for p, S in moves_states))
                value, move, state = max(
                    ((wins[(player, S)] / plays[(player, S)]) +
                     self.C * sqrt(log_total / plays[(player, S)]), p, S)
                    for p, S in moves_states
                )
            else:
                # Otherwise, just make an arbitrary decision.
                """Do we want to set the leaf_state before or after??????????"""
                move, state = board.next_state(state, policy_choice(state))
                self.leaf_state = state
                self.leaf_value = value_function(state)

            states_copy.append(state)

            # `player` here and below refers to the player
            # who moved into that particular state.
            if expand and (player, state) not in plays:
                expand = False
                plays[(player, state)] = 0
                wins[(player, state)] = 0
                if t > self.max_depth:
                    self.max_depth = t

            visited_states.add((player, state))

            player = self.board.current_player(state)
            winner = self.board.winner(states_copy)
            if winner:
                if self.leaf_state == 'empty':
                    print('weird')
                    self.leaf_state = state
                    self.leaf_value = value_function(state)
                break

        for player, state in visited_states:
            if (player, state) not in plays:
                continue
            plays[(player, state)] += 1
            if player == winner:
                wins[(player, state)] += mixing + (1-mixing) * self.leaf_value
            if (3-player) == winner:
                wins[(player, state)] += 0 + (1-mixing) * self.leaf_value    
            if winner == -1:
                wins[(player, state)] += (mixing) * 1/2 + (1-mixing) * self.leaf_value


        self.leaf_state = 'empty'
        self.leaf_value = 'empty'        



b = Board()
m = MCTS(b)
m.statehistory = [tup_base(create_zeros())]
move = m.get_play()





