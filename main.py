from genetic_code import GeneticCode

import random


def main(rows, columns, no_of_color, chromosome_count, best_parents):
    """Loop over number of color options to check for optimal solution. If the number of colors do not return optimal solution those will be ignored. Color values with optimal solution
    will return number of colors, generation number and an example of solved grid selected randomly from selected chromosomes.

    Args:
        rows (_type_): _description_
        columns (_type_): _description_
        no_of_color (_type_): _description_
        chromosome_count (_type_): _description_
        best_parents (_type_): _description_

    Returns:
        _type_: _description_
    """

    best_chromosomes = {}
    for i in range(1, no_of_color + 1):
        dd = GeneticCode(rows, columns, i, chromosome_count, best_parents)
        best_chrom, gen_number = dd.optimized_list(i)

        if best_chrom is None:
            pass

        else:
            optimal_color_list = []
            for j in range(len(best_chrom)):
                optimal_color = best_chrom[j][1]["Chromosome"]
                optimal_color_list.append(optimal_color)

            best_chromosomes[i] = {"Color Lists": optimal_color_list, "Generation Number": gen_number}

    def grid(row_num, col_num, list):
        grid = []
        for i in range(row_num):
            row = []
            for j in range(col_num):
                element = list[i * row_num + j]
                row.append(element)
            grid.append(row)

        return grid

    for key in best_chromosomes:
        colors = key
        gen = best_chromosomes[key]["Generation Number"]
        rand_list_index = random.randint(0, len(best_chromosomes[key]["Color Lists"]) - 1)
        rand_list = best_chromosomes[key]["Color Lists"][rand_list_index]
        result_grid = grid(rows, columns, rand_list)

        print()
        print(f"Optimal solution for {colors} colors achieved at {gen} generations.....")
        print()
        print("Example Result Grid")
        print()
        for row in result_grid:
            print(row)
        print()


if __name__ == "__main__":
    main(10, 10, 8, 1000, 100)
