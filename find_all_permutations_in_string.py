def find_all_permutations(string):

    permutations = []

    if len(string) == 2:

        permutations = [string, string[1] + string[0]]
        return permutations

    else:

        for _ in range(len(string)):

            string = string[1:] + string[0]
            last_permutations = find_all_permutations(string[1:])

            for permutation in last_permutations:

                permutations.append(string[0] + permutation)

        return permutations


print(*find_all_permutations("abcd"), sep=", ")
