import os
import subprocess
import tempfile


def write_matrix_file(file_name, M):
    n_row = len(M)
    f = open(file_name, 'w')
    n_col = len(M[0])
    f.write(str(n_row) + " " + str(n_col) + '\n')
    for i_row in range(n_row):
        for i_col in range(n_col):
            f.write(" " + str(M[i_row][i_col]))
        f.write("\n")
    f.close()

def read_vector_file(file_name):
    """
    Read a vector from a file
    """
    f = open(file_name, 'r')
    n = int(f.readline().strip())
    vector = list(map(int, f.readline().split()))
    if n != len(vector):
        raise Exception("The length of the vector is not coherent")
    f.close()
    return vector

def read_matrix_file(file_name, matrix):
    """
    Read a matrix from a file
    """
    f = open(file_name, 'r')
    dims = list(map(int, f.readline().split()))
    n_row = dims[0]
    n_col = dims[1]
    matrix = []
    for i_row in range(n_row):
        vector = list(map(int, f.readline().split()))
        if n_col != len(vector):
            raise Exception("The length of the vector is not coherent")
        matrix.add(vector)
    f.close()
    return matrix

def compute_isotropic_vector(M):
    """
    Runs a binary from the 'bin' directory of the package.
    :param binary_name: Name of the binary to run (e.g., 'LATT_FindIsotropic')
    :return: The output from the binary
    """
    # Get the directory of the current file (inside the package)
    bin_dir = os.path.join(os.path.dirname(__file__), 'bin')
    binary_path = os.path.join(bin_dir, "LATT_isotropy")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    if not os.path.exists(binary_path):
        raise FileNotFoundError(f"Binary {binary_name} not found in {bin_dir}")
    result = subprocess.run([binary_path, "rational", input_file, "Python", output_file], capture_output=True, text=True)
    print("result=", result.stdout)
    the_vector = read_vector_file(output_file)
    for val in the_vector:
        if val != 0:
            return the_vector
    # No isotropic vector were found
    return None
