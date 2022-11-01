from enum import Enum


class UserIntent(Enum):
    """ User's current intent """

    """ User wants to add his address"""
    PickAddAddress = 1

    """ User wants to save this address"""
    NewAddress = 2

    """ User wants to see his addresses"""
    SeeAllAddresses = 3
