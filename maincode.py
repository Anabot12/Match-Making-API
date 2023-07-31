def gale_shapley(person1, person2, compatibility):
    """
    Perform the Gale-Shapley algorithm for match-making between two groups of people.
    person1: List of persons from the first group.
    person2: List of persons from the second group.
    compatibility: Compatibility score between the two persons.
    """
    engagements = {person1[i]: person2[i] for i in range(len(person1))}
    return engagements
