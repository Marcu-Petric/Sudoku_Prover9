import re

def to_mace4_input(m):
    """
    Converts a 2D matrix into f(i,j) = x format for Mace4

    :param m: 2D list representing an UNSOLVED Sudoku puzzle.
    :return: Mace4 input functions string.
    """
    inputs = ""
    for i, row in enumerate(m):
        for j, element in enumerate(row):
            if element:
                inputs += f"f({i},{j}) = {element-1}.\n"
    return inputs


def insert_input_in_file_content(mace4functions, file_content):
    """
    Inserts the Mace4 input into the file content.

    :param mace4functions: Mace4 input functions string.
    :param file_content: Original file content.
    :return: Updated file content.
    """
    return file_content.replace(
        "TODO: insert input here",
        f"{mace4functions}"
    )


def put_in_input_file(gui_matrix, path):
    """
    Reads a file, inserts Mace4 input, and saves the updated content.

    :param gui_matrix: 2D list representing a Sudoku puzzle.
    :param path: Path to the input file.
    """
    with open(path, "r") as file:
        file_content = file.read()

    mace4Input = to_mace4_input(gui_matrix)
    file_with_input = insert_input_in_file_content(mace4Input, file_content)

    with open(path, "w") as file:
        file.write(file_with_input)


def to_grid(file_content, size):
    """
    Converts file content into a 2D matrix.

    :param file_content: The content of the Mace4 output file.
    :param size: Nr. of rows and column of the wanted matrix (e.g., 9 for a 9x9 Sudoku).
    :return: 2D matrix.
    """
    pattern = r"function\(f\(_,_\), \[([^\]]+)\]\)"
    match = re.search(pattern, file_content)
    outputMatrix = []
    if match:
        numbers = list(map(lambda x: int(x) + 1, match.group(1).replace('\n', '').replace('\t', '').split(',')))
        for i in range(0, len(numbers), size):
            outputMatrix.append(numbers[i:i + size])

    return outputMatrix


def get_from_output_file(path):
    """
    Reads the output file and returns it as a 2D matrix.

    :param path: Path to the output file.
    :return: 2D matrix of the SOLVED Sudoku puzzle.
    """
    with open(path, "r") as file:
        content = file.read()

    return to_grid(content, 9)



if __name__ == '__main__':
    matrix = [
        [2, 0, 0, 3, 0, 0, 4, 0, 0],
        [0, 3, 0, 0, 4, 0, 0, 5, 0],
        [0, 0, 4, 0, 0, 5, 0, 0, 6],

        [7, 0, 0, 5, 0, 0, 6, 0, 0],
        [0, 8, 0, 0, 6, 0, 0, 7, 0],
        [0, 0, 9, 0, 0, 7, 0, 0, 8],

        [9, 0, 0, 1, 0, 0, 8, 0, 0],
        [0, 1, 0, 0, 2, 0, 0, 9, 0],
        [0, 0, 2, 0, 0, 3, 0, 0, 5]
    ]

    put_in_input_file(matrix, "../Resources/sudoku.in")

    # result = getFromInputFile(r"Resources/sudoku.out")
    #
    # [print(row) for row in result]
    string = '''
    test
    '''
