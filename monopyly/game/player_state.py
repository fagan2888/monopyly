import copy
from ..squares import Street


class PlayerState(object):
    '''
    Holds data for one player, such as the amount of money that have and
    which properties they own.

    Note: The player algorithm is not in this class (or in a derived class).
    '''

    def __init__(self):
        '''
        The 'constructor'.
        '''

        # The square the player is currently on (0 = Go, 39 = Mayfair etc).
        # This can be used as an index into the squares property of the board...
        self.square = 0

        # The amount of money owned by the player...
        self.cash = 1500

        # The collection of properties owned by the player.
        # This is held as a set of integers, each of which is an index
        # to one of the squares on the board. The squares themselves hold
        # information about how many houses are on them, whether they are
        # mortgages and so on...
        # TODO: Change to collection of properties
        self.property_indexes = set()

        # Get Out Of Jail Free cards the player is holding...
        self.get_out_of_jail_free_cards = []

        # Whether the player is in jail, and if so how many turns they
        # have been there...
        self.is_in_jail = False
        self.number_of_turns_in_jail = 0

        # The collection of complete unmortgaged sets owned by this player.
        # The items in the collection are Property.Set 'enums'.
        self.owned_sets = set()

    def get_number_of_houses_and_hotels(self, board):
        '''
        Returns the number of houses and hotels owned by this player.
        '''
        number_of_houses = 0
        number_of_hotels = 0
        for index in self.property_indexes:
            # We find the square for this index and check if
            # it is a street (ie, not a station or utility)...
            square = board.get_square_by_index(index)
            if type(square) != Street:
                continue

            if square.number_of_houses == 5:
                # Five houses is a hotel...
                number_of_hotels += 1
            else:
                number_of_houses += square.number_of_houses

        return number_of_houses, number_of_hotels

    @property
    def number_of_get_out_of_jail_free_cards(self):
        '''
        The number of GOOJF cards the player has.
        '''
        return len(self.get_out_of_jail_free_cards)


