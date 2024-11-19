import sys

def solve_auf_tup_puzzle(word1, word2, sum_word):
    """
    Solve the Auf and Tup puzzle using a more efficient constraint-based approach.

    Args:
    word1 (str): First word in the puzzle
    word2 (str): Second word in the puzzle
    sum_word (str): Sum word in the puzzle

    Returns:
    dict: Mapping of letters to digits if a solution is found, None otherwise
    """
    # Get unique letters
    letters = list(set(word1 + word2 + sum_word))

    # If more than 10 unique letters, no solution is possible
    if len(letters) > 10:
        return None

    def is_valid_solution(assignment):
        """
        Check if the current letter-to-digit assignment is valid.
        """
        # Ensure no leading zeros
        if any(assignment[word[0]] == 0 for word in [word1, word2, sum_word]):
            return False

        # Convert words to numbers
        num1 = int(''.join(str(assignment[letter]) for letter in word1))
        num2 = int(''.join(str(assignment[letter]) for letter in word2))
        sum_num = int(''.join(str(assignment[letter]) for letter in sum_word))

        # Check if sum condition is met
        return num1 + num2 == sum_num

    def backtrack(index, assignment, used_digits):
        """
        Backtracking algorithm to find a valid assignment.

        Args:
        index (int): Current letter index being assigned
        assignment (dict): Current letter-to-digit mapping
        used_digits (set): Digits already used in the assignment

        Returns:
        dict or None: Valid assignment or None if no solution exists
        """
        # If all letters are assigned, check if solution is valid
        if index == len(letters):
            return assignment if is_valid_solution(assignment) else None

        # Try digits 0-9 for the current letter
        current_letter = letters[index]
        for digit in range(10):
            # Skip if digit is already used
            if digit in used_digits:
                continue

            # Try this digit
            assignment[current_letter] = digit
            used_digits.add(digit)

            # Recursively try to assign remaining letters
            result = backtrack(index + 1, assignment, used_digits)
            if result:
                return result

            # Backtrack
            del assignment[current_letter]
            used_digits.remove(digit)

        # No solution found
        return None

    # Solve the puzzle
    solution = backtrack(0, {}, set())
    return solution


def print_solution(word1, word2, sum_word):
    """
    Find and print the solution to the Auf and Tup puzzle.

    Args:
    word1 (str): First word in the puzzle
    word2 (str): Second word in the puzzle
    sum_word (str): Sum word in the puzzle
    """
    solution = solve_auf_tup_puzzle(word1, word2, sum_word)

    if solution:
        print("Solution found!")
        # Convert the dictionary to a sorted list for consistent output
        sorted_solution = sorted(solution.items(), key=lambda x: x[0])
        for letter, digit in sorted_solution:
            print(f"{letter}: {digit}")

        # Verify the solution
        num1 = int(''.join(str(solution[letter]) for letter in word1))
        num2 = int(''.join(str(solution[letter]) for letter in word2))
        sum_num = int(''.join(str(solution[letter]) for letter in sum_word))

        print(f"\n{word1}: {num1}")
        print(f"{word2}: {num2}")
        print(f"{sum_word}: {sum_num}")
        print(f"Verification: {num1} + {num2} == {sum_num} is {num1 + num2 == sum_num}")
    else:
        print("No solution found.")


def main():
    """
    Main function to handle command-line arguments and solve the puzzle.
    """
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <word1> <word2> <sum_word>")
        print("Example: python script.py SEND MORE MONEY")
        sys.exit(1)
    
    # Get words from command-line arguments
    word1 = sys.argv[1].upper()
    word2 = sys.argv[2].upper()
    sum_word = sys.argv[3].upper()
    
    # Solve and print the puzzle
    print(f"Solving puzzle: {word1} + {word2} = {sum_word}")
    print_solution(word1, word2, sum_word)


if __name__ == "__main__":
    main()
