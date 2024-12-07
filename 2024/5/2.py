from pprint import pprint

mission = """--- Part Two ---
While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?
"""


input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

input = open('input.txt').read()

[rules, updates] = input.split('\n\n')

rules = rules.split('\n')
rules = [i.split('|') for i in rules]

updates = updates.split('\n')
updates = [i.split(',') for i in updates]

bad_updates = []
for update in updates:
    update_ok = True
    rules_broken = []
    for rule in rules:
        part_rules = [u for u in update if u in rule]
        if len(part_rules) == 2 and part_rules != rule:
            rules_broken.append(rule)
    if len(rules_broken) > 0:
        bad_updates.append(update)


# create a map of what must be after what
must_be_after_map = {}
for [before, after] in rules:
    if after not in must_be_after_map:
        must_be_after_map[after] = []
    must_be_after_map[after].append(before)

for ui, update in enumerate(bad_updates):
    i = 0
    while i < len(update):
        page = update[i]
        must_be_before = must_be_after_map.get(page, [])
        is_after = update[i+1:] 
        bad_ordered_numbers= [nr for nr in is_after if nr in must_be_before]

        if len(bad_ordered_numbers) > 0:
            last_offender = bad_ordered_numbers[-1]
            index = update.index(last_offender)

            bad_updates[ui].pop(i)
            bad_updates[ui].insert(index, page)
            i = 0
        else:
            i += 1

_sum = 0
for update in bad_updates:
    _sum += int(update[len(update)//2])
print(_sum)