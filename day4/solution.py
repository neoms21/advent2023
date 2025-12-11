from pprint import pprint

# Create 2D list (Matrix)
# two_dim_input=[]


def find_closest_eight(x_index, y_index):
    # Returns a list of tuples (x, y) representing coordinates
    return [
        (x_index, y_index + 1),
        (x_index, y_index - 1),
        (x_index + 1, y_index + 1),
        (x_index + 1, y_index),
        (x_index - 1, y_index),
        (x_index - 1, y_index + 1),
        (x_index - 1, y_index - 1),
        (x_index + 1, y_index - 1),
    ]

def find_neighbours(r,c, two_dim_input):
    rows = len(two_dim_input)
    cols = len(two_dim_input[0]) if rows > 0 else 0

    neighbor_points = find_closest_eight(r, c)

    current_cell_neighbors = []
    coordinates=[]

    for x, y in neighbor_points:
        # Check boundaries strictly
        # 1. 0 <= x < rows: Ensures x is valid and NOT negative
        # 2. 0 <= y < cols: Ensures y is valid and NOT negative
        if 0 <= x < rows and 0 <= y < cols and two_dim_input[x][y] != ".":
            # current_cell_neighbors.get("neighbours").append(two_dim_input[x][y])
            current_cell_neighbors.append((x,y))

    # pprint(current_cell_neighbors )

    return current_cell_neighbors
grand_total = 0
def find_total_from_matrix(two_dim_input, find_all=False):
    modified_matrix = []
    total = 0
    global grand_total
    for r_idx, row in enumerate(two_dim_input):
        modified_matrix.append([])
        for c_idx, val in enumerate(row):
            modified_matrix[r_idx].append(val)
            if val != ".":
                if len(find_neighbours(r_idx, c_idx, two_dim_input)) < 4:
                    modified_matrix[r_idx][c_idx] = "."
                    total += 1

    # pprint(total)
    if total !=0 and find_all==True:
        grand_total += total
        return find_total_from_matrix(modified_matrix, find_all)
    return total

def solution(rows):
    two_dim_input = [list(row) for row in rows]
    part1 = find_total_from_matrix(two_dim_input)
    find_total_from_matrix(two_dim_input, True)

    pprint(part1)
    pprint(grand_total)