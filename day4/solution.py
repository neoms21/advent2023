from pprint import pprint

# Create 2D list (Matrix)
two_dim_input=[]


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


# Get dimensions for boundary checking


def find_neighbours(r,c):
    rows = len(two_dim_input)
    cols = len(two_dim_input[0]) if rows > 0 else 0

    neighbor_points = find_closest_eight(r, c)

    current_cell_neighbors = []

    for x, y in neighbor_points:
        # Check boundaries strictly
        # 1. 0 <= x < rows: Ensures x is valid and NOT negative
        # 2. 0 <= y < cols: Ensures y is valid and NOT negative
        if 0 <= x < rows and 0 <= y < cols and two_dim_input[x][y] != ".":
            current_cell_neighbors.append(two_dim_input[x][y])
        # else:
        #     current_cell_neighbors.append("")

    return len(current_cell_neighbors)

    # all_neighbors_matrix.append(row_neighbors)


def solution(rows):
    global two_dim_input
    two_dim_input = [list(row) for row in rows]
    # print(two_dim_input)
    total = 0
    for r_idx, row in enumerate(rows):
        vals = ([*row])
        for c_idx, val in enumerate(vals):
            if val != ".":
                if find_neighbours(r_idx, c_idx)<4:
                    total += 1


    print(total)