mission = """--- Part Two ---
The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
192: 17 8 14 can be made true using 17 || 8 + 14.
Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?"""


input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

input = open('input.txt').read()

input = input.split("\n")

equations = []
for eq in input:
    [res, *nums] = eq.split(" ")
    res = res[:-1]
    nums = [int(num) for num in nums]
    equations.append((int(res), nums))



def rec_solver(parts, sum, res):
    parts = parts.copy()
    if len(parts) == 0:
        return sum == res

    part = parts.pop(0)

    # check add
    if rec_solver(parts, sum + part, res):
        return True

    # check multiply
    if rec_solver(parts, sum * part, res):
        return True

    # check string concat
    if rec_solver(parts, int(str(sum) + str(part)), res):
        return True

    return False


good_sum = 0
for i, [res, parts] in enumerate(equations):
    sum = parts.pop(0)
    if rec_solver(parts, sum, res):
        good_sum += res

print(good_sum)

