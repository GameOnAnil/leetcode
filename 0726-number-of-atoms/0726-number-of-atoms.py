class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Length of the formula
        n = len(formula)

        # Current index. It should be global as needs
        # to be updated in the recursive function
        self.index = 0

        # Recursively parse the formula
        def parse_formula():
            # To save the count of atoms in the formula
            curr_map = defaultdict(int)

            # Iterate until the right parenthesis or end of the formula
            while self.index < n and formula[self.index] != ")":
                # If left parenthesis, do recursion
                if formula[self.index] == "(":
                    self.index += 1
                    nested_map = parse_formula()
                    for atom in nested_map:
                        curr_map[atom] += nested_map[atom]

                # Otherwise, it should be UPPERCASE LETTER
                # Extract the atom and count in one go.
                else:
                    curr_atom = formula[self.index]
                    self.index += 1
                    while self.index < n and formula[self.index].islower():
                        curr_atom += formula[self.index]
                        self.index += 1

                    curr_count = ""
                    while self.index < n and formula[self.index].isdigit():
                        curr_count += formula[self.index]
                        self.index += 1

                    if curr_count == "":
                        curr_map[curr_atom] += 1
                    else:
                        curr_map[curr_atom] += int(curr_count)

            # If the right parenthesis, extract the multiplier
            # and multiply the count of atoms in the curr_map
            self.index += 1
            multiplier = ""
            while self.index < n and formula[self.index].isdigit():
                multiplier += formula[self.index]
                self.index += 1

            if multiplier:
                multiplier = int(multiplier)
                for atom in curr_map:
                    curr_map[atom] *= multiplier

            return curr_map

        # Parse the formula
        final_map = parse_formula()

        # Sort the final map
        final_map = dict(sorted(final_map.items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans