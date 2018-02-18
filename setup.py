import os
from setuptools import setup, find_packages


# Declare your non-python data files:
# Files underneath configuration/ will be copied into the build preserving the
# subdirectory structure if they exist.
data_files = []
for root, dirs, files in os.walk('configuration'):
    data_files.append((os.path.relpath(root, 'configuration'),
                       [os.path.join(root, f) for f in files]))

setup(
    name="CambarrFightgame",
    version="1.0",

    # declare your packages
    packages=find_packages(where="src", exclude=("test",)),
    package_dir={"": "src"},

    # include data files
    data_files=data_files,

    # set up the shebang
    options={
        # make sure the right shebang is set for the scripts - use the
        # environment default Python
        'build_scripts': {
            'executable': '/apollo/sbin/envroot "$ENVROOT/bin/python"',
        },
    },

    # declare your scripts
    # If you want to create any Python executables in bin/, define them here.
    # This is a three-step process:
    #
    # 1. Create the function you want to run on the CLI in src/cambarr_fightgame/cli.py
    #    For convenience I usually recommend calling it main()
    #
    # 2. Uncomment this section of the setup.py arguments; this will create
    #    bin/CambarrFightgame (which you can obviously change!) as a script
    #    that will call your main() function, above.
    #
    # entry_points="""\
    # [console_scripts]
    # CambarrFightgame = cambarr_fightgame.cli:main
    # """,
    #
    # 3. Add a dependency on BrazilPython-setuptools = default into the
    #    dependencies section of your Config. This is necessary for the script
    #    generated by setuptools to find its function.

    # Because the live versionset ships CPython 3.4 by default, we want to add
    # its scripts to `bin/`. *If* you want a different set of scripts in bin,
    # or your versionset is configured for a different CPython, then you can
    # change this accordingly.
    # 
    # Ship the python 3.4 script in $ROOT/bin. Remove this flag to skip
    # installing scripts into $ROOT/bin/
    #
    # Note that if your versionset doesn't build for 3.4, this won't do the
    # right thing!
    root_script_source_version="python3.4",

    # When we have something that's only for one version, use 3.4.
    default_python="python3.4",

    # Use the pytest brazilpython runner. Provided by BrazilPython-Pytest.
    test_command='brazilpython_pytest',

    # Use custom sphinx command which adds an index.html that's compatible with
    # code.amazon.com links.
    doc_command='amazon_doc_utils_build_sphinx',
)
