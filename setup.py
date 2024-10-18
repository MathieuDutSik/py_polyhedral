import os
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class BuildCppWithCMake(build_ext):
    def run(self):
        print("Starting of run command of py_polyhedral")
        repo_url = "https://github.com/MathieuDutSik/polyhedral_common"
        clone_dir = "cpp_code_repo"

        if not os.path.exists(clone_dir):
            print(f"Cloning repository from {repo_url}...")
            subprocess.check_call(['git', 'clone', '--recursive', repo_url, clone_dir])

        # Step 2: Run CMake to build the C++ project
        build_dir = os.path.join(clone_dir, 'build')
        print("build_dir=", build_dir)

        if not os.path.exists(build_dir):
            os.makedirs(build_dir)

        print("Configuring CMake project...")
        subprocess.check_call(['cmake', '..'], cwd=build_dir)

        print("Building the C++ code...")
        subprocess.check_call(['cmake', '--build', '.'], cwd=build_dir)

        # Step 3: Copy the generated binaries (artifacts) to the Python package directory
        binaries = ["POLY_SerialDualDesc", "CP_TestCopositivity", "CP_TestCompletePositivity", "LORENTZ_FundDomain_AllcockEdgewalk", "POLY_FaceLatticeGen", "INDEF_FORM_AutomorphismGroup", "INDEF_FORM_TestEquivalence", "INDEF_FORM_GetOrbitRepresentative", "INDEF_FORM_GetOrbit_IsotropicKplane", "LATT_canonicalize", "LATT_FindIsotropic"]
        target_bin_dir = os.path.join('py_polyhedral', 'bin')
        print("target_bin_dir={}", target_bin_dir)

        if not os.path.exists(target_bin_dir):
            os.makedirs(target_bin_dir)

        print("Copying the binaries ...")
        for binary in binaries:
            # Assuming the binaries are located in the 'build' directory
            binary_path = os.path.join(build_dir, binary)
            if os.path.exists(binary_path):
                subprocess.check_call(['cp', binary_path, target_bin_dir])
            else:
                raise MissingBinaryError(f"Error: {binary} was not found in {build_dir}")

        # Now, let setuptools do its normal build_ext stuff (optional if you have other extensions)
        print("Running super.run ...")
        super().run()

setup(
    name='py_polyhedral',
    version='0.1.1',
    packages=['py_polyhedral'],
    cmdclass={
        'build_ext': BuildCppWithCMake,  # Use the custom command to build the C++ code
    },
    install_requires=[
        # Add any Python dependencies here
    ],
)
