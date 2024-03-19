morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

# Print out items that does not appear in both sets (symmetric difference)
# possible_courses = morning ^ afternoon # only works for sets
possible_courses = set(morning).symmetric_difference(afternoon) # works for any iterable
print(possible_courses)

possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)