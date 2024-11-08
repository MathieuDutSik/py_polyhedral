import os
import ast
import subprocess
import tempfile

def get_binary_path(the_bin):
    """
    Gets the binary to use for the computation
    """
    # Get the directory of the current file (inside the package)
    bin_dir = os.path.join(os.path.dirname(__file__), 'bin')
    binary_path = os.path.join(bin_dir, the_bin)
    if not os.path.exists(binary_path):
        raise FileNotFoundError(f"Binary {binary_path} not found in {bin_dir}")
    return binary_path

def write_matrix_file(file_name, M):
    n_row = len(M)
    n_col = len(M[0])
    f = open(file_name, 'w')
    f.write(str(n_row) + " " + str(n_col) + '\n')
    for i_row in range(n_row):
        for i_col in range(n_col):
            f.write(" " + str(M[i_row][i_col]))
        f.write("\n")
    f.close()

def write_list_matrix_file(file_name, ListMM):
    n_mat = len(ListM)
    n_row = len(ListM[0])
    n_col = len(ListM[0][0])
    f = open(file_name, 'w')
    f.write(str(n_mat) + '\n')
    for i_mat in range(n_mat):
        f.write(str(n_row) + " " + str(n_col) + '\n')
        for i_row in range(n_row):
            for i_col in range(n_col):
                f.write(" " + str(ListM[i_mat][i_row][i_col]))
            f.write("\n")
    f.close()

def write_group_file(file_name, l_gen, n_act):
    n_gen = len(l_gen)
    f = open(file_name, 'w')
    f.write(str(n_act) + " " + str(n_gen) + '\n')
    for e_gen in l_gen:
        for i_act in range(n_act):
            f.write(" " + str(e_gen[i_act]))
        f.write("\n")
    f.close()

def ast_read(file_name):
    """
    Read a Python object from a text file
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"Output file {file_name} does not exist")
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return ast.literal_eval(content)

def run_and_check(list_comm):
    """
    Run a command and process what is happening. Stop if an error is detected
    """
    result = subprocess.run(list_comm, capture_output=True, text=True)
    if result.returncode != 0:
        print("result=", result)
        print("returncode=", result.returncode)
        print("list_comm=", list_comm)
        raise RuntimeError("The running of the program went wrongly")

def compute_isotropic_vector(M):
    """
    Computes the isotropic vector of a matrix
    :param M the matrix as input
    :return: The isotropic vector or None is none exists
    """
    binary_path = get_binary_path("LATT_FindIsotropic")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    run_and_check([binary_path, "rational", input_file, "PYTHON", output_file])
    return ast_read(output_file)

def compute_canonical_form(M):
    """
    Computes the canonical form of positive definite matrix
    :param M the matrix as input
    :return: The dictionary containing, the vector configuration, the reduced matrix and the unimodular transformation
    """
    binary_path = get_binary_path("LATT_Canonicalize")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    run_and_check([binary_path, "gmp", input_file, "PYTHON", output_file])
    return ast_read(output_file)

def test_copositivity(M):
    """
    Tests whether the matrix is copositive
    :param M the matrix as input
    :return: The dictionary containing the answer and if not copositive the certificate for it.
    """
    binary_path = get_binary_path("CP_TestCopositivity")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    run_and_check([binary_path, "gmp", input_file, "PYTHON", output_file])
    return ast_read(output_file)

def test_complete_positivity(M):
    """
    Tests whether the matrix is completely positive
    :param M the matrix as input
    :return: The dictionary containing, the answer and the certificate
    """
    binary_path = get_binary_path("CP_TestCompletePositivity")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    run_and_check([binary_path, "gmp", input_file, "PYTHON", output_file])
    return ast_read(output_file)

def indefinite_form_automorphism_group(M):
    """
    Computes the automorphism group of an indefinite form
    :param M the matrix as input
    :return: The list of generators
    """
    binary_path = get_binary_path("INDEF_FORM_AutomorphismGroup")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    run_and_check([binary_path, "gmp", input_file, "PYTHON", output_file])
    return ast_read(output_file)

def indefinite_form_test_equivalence(M1, M2):
    """
    Computes the equivalence of indefinite forms
    :param M1 the indefinite form as input
    :param M2 the indefinite form as input
    :return: The equivalence if one exists and None otherwise
    """
    binary_path = get_binary_path("INDEF_FORM_TestEquivalence")
    arr_input1 = tempfile.NamedTemporaryFile()
    arr_input2 = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input1_file = arr_input1.name
    input2_file = arr_input2.name
    output_file = arr_output.name
    write_matrix_file(input1_file, M1)
    write_matrix_file(input2_file, M2)
    run_and_check([binary_path, "gmp", input1_file, input2_file, "PYTHON", output_file])
    return ast_read(output_file)

def indefinite_form_get_orbit_representative(M, eNorm):
    """
    Computes the orbits of representatives of vectors of the given norm
    :param M the matrix as input
    :return: The list of generators
    """
    binary_path = get_binary_path("INDEF_FORM_GetOrbitRepresentative")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    run_and_check([binary_path, "gmp", input_file, str(eNorm), "PYTHON", output_file])
    return ast_read(output_file)

def indefinite_form_isotropic_k_stuff(M, k, nature):
    """
    Computes the orbits of isotropic k-plane or k-flag
    :param M the matrix as input
    :return: The list of generators
    """
    binary_path = get_binary_path("INDEF_FORM_GetOrbit_IsotropicKplane")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    run_and_check([binary_path, "gmp", input_file, str(k), nature, "PYTHON", output_file])
    return ast_read(output_file)

def indefinite_form_isotropic_k_plane(M, k):
    """
    Computes the orbits of isotropic k-plane
    :param M the matrix as input
    :return: The list of generators
    """
    return indefinite_form_isotropic_k_stuff(M, k, "plane")

def indefinite_form_isotropic_k_flag(M, k):
    """
    Computes the orbits of isotropic k-flag
    :param M the matrix as input
    :return: The list of generators
    """
    return indefinite_form_isotropic_k_stuff(M, k, "flag")

def dual_description(EXT, GRP):
    """
    Computes the orbits of facets of the polytope
    :param EXT the matrix as input
    :param GRP the permutation group being used.
    :return The list of orbit representatives
    """
    binary_path = get_binary_path("POLY_DirectSerialDualDesc")
    arr_inpEXT = tempfile.NamedTemporaryFile()
    arr_inpGRP = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    inpEXT_file = arr_inpEXT.name
    inpGRP_file = arr_inpGRP.name
    output_file = arr_output.name
    write_matrix_file(inpEXT_file, EXT)
    write_group_file(inpGRP_file, GRP, len(EXT))
    run_and_check([binary_path, "rational", inpEXT_file, inpGRP_file, "PYTHON", output_file])
    return ast_read(output_file)

def lorentzian_reflective_edgewalk(M):
    """
    Computes the fundamental domain if the lattice is reflective. If not then reports it.
    :param M the lorentzian matrix
    :return: A dictionary with the relevant information
    """
    binary_path = get_binary_path("LORENTZ_ReflectiveEdgewalk")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    run_and_check([binary_path, "gmp", input_file, "PYTHON", output_file])
    return ast_read(output_file)

def polytope_face_lattice(EXT, GRP, LevSearch):
    """
    Computes the faces up to some level by linear programming
    :param EXT the matrix as input
    :param GRP the permutation group being used.
    :param The maximum dimension of orbits
    :return The list of orbit representatives
    """
    binary_path = get_binary_path("POLY_DirectFaceLattice")
    arr_inpEXT = tempfile.NamedTemporaryFile()
    arr_inpGRP = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    inpEXT_file = arr_inpEXT.name
    inpGRP_file = arr_inpGRP.name
    output_file = arr_output.name
    write_matrix_file(inpEXT_file, EXT)
    write_group_file(inpGRP_file, GRP)
    run_and_check([binary_path, "rational", inpEXT_file, inpGRP_file, str(LevSearch), "PYTHON", output_file])
    return ast_read(output_file)

def lattice_compute_delaunay(M):
    """
    Computes the orbits of lattice Delaunay polytopes of the lattice.
    :param M the lorentzian matrix
    :return: A dictionary with the relevant information
    """
    binary_path = get_binary_path("LATT_SerialComputeDelaunay")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_matrix_file(input_file, M)
    run_and_check([binary_path, "gmp", input_file, "PYTHON", output_file])
    return ast_read(output_file)

def lattice_iso_delaunay_domains(ListM):
    """
    Computes the orbits of iso Delaunay domains
    :param ListM the space of matrices
    :return: A dictionary with the relevant information
    """
    binary_path = get_binary_path("LATT_SerialLattice_IsoDelaunayDomain")
    arr_input = tempfile.NamedTemporaryFile()
    arr_output = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    output_file = arr_output.name
    write_list_matrix_file(input_file, ListM)
    run_and_check([binary_path, "gmp", input_file, "PYTHON", output_file])
    return ast_read(output_file)

