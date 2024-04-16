# import blackjack

# from ... import will automatically take note of protected methods
# and won't import them
from blackjack import *

# Make a sorted copy of the globals() dictionary
# so that it can be iterated through without running into
# errors (as the iterating variable is also a global variable,
# which changes the global() dictionary)
g = sorted(globals())
for x in g:
    print(x)

# # blackjack won't run here because __main__ is the __name__ attribute
# # of import_test.py and not for blackjack.py
# print(__name__)

# # Running a protected method.
# # Still able to run, but shouldn't be done
# blackjack._deal_card(blackjack.dealer_card_frame)
# blackjack.play()
# print(blackjack.cards)


# '_' is a throwaway variable that's not intended to be used
personal_details = ("Tim", 24, "Australia")

name, _, country = personal_details
print(name, country)
print(_)