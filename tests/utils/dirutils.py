import os


def make_and_clear_directory(dirbase: str):
    import shutil
    safety_file = os.path.join(dirbase, "generated")
    if os.path.exists(dirbase):
        if not os.path.exists(safety_file):
            raise FileExistsError("{} not found in test directory".format(safety_file))
        shutil.rmtree(dirbase)
    os.makedirs(dirbase)
    with open(os.path.join(dirbase, "generated"), "w") as f:
        f.write("Generated for safety.  Must be present for test to remove this directory.")