import itertools

def solve_cryptarithmetic(puzzle):
    letters = set(letter for word in puzzle for letter in word if letter.isalpha())
    if len(letters) > 10:
        return "Invalid puzzle: More than 10 distinct letters"

    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if all(mapping[word[0]] != 0 for word in puzzle if len(word) > 1) and \
           sum(int("".join(str(mapping[letter]) for letter in word)) for word in puzzle[:-1]) == int("".join(str(mapping[letter]) for letter in puzzle[-1])):
            return mapping

    return "No solution found"

if __name__ == "__main__":
    puzzle = ["SEND", "MORE", "MONEY"]
    solution = solve_cryptarithmetic(puzzle)
    if isinstance(solution, dict):
        print("Solution found:")
        for word in puzzle:
            print(word, "=", "".join(str(solution[letter]) for letter in word))
    else:
        print(solution)
