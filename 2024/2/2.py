mission = """Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

"""


input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

input = open('input.txt').read()

reports = input.split("\n")

bad_reports = len(reports)

for report in reports:
    report = report.split()
    levels = [int(i) for i in report]

    diffs = [levels[i] - levels[i+1] for i in range(len(levels)-1)]

    # normalize to increasing
    decresing = sum([1 for diff in diffs if diff > 0])
    increasing = sum([1 for i in diffs if i < 0])
    if decresing < increasing:
        levels = [-level for level in levels]

    def find_first_offensive_level_index(levels):
        diffs = [levels[i] - levels[i+1] for i in range(len(levels)-1)]
        first_bad_index = next((i for i,x in enumerate(diffs) if x not in range(1, 4)), None)
        return first_bad_index

    first_bad_index = find_first_offensive_level_index(levels)
    if first_bad_index is None:
        bad_reports -= 1
        continue

    levels_with_removed_1 = levels[:first_bad_index] + levels[first_bad_index+1:]
    levels_with_removed_2 = levels[:first_bad_index+1] + levels[first_bad_index+2:]

    a = find_first_offensive_level_index(levels_with_removed_1)
    b = find_first_offensive_level_index(levels_with_removed_2)

    if a is None or b is None:
        bad_reports -= 1
        continue

print(f'safe reports: {len(reports) - bad_reports}')