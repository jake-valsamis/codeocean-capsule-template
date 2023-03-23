# This is an example Python script that will output a random value to
# CodeOcean (CO) results. You can add any number of scripts to your CodeOcean
# capsule, and a number of different runtimes are supported by the
# starter environments.
#
# This is the entry point of "reproducible runs" as defined in the adjacent
# `run` script.
#
# See https://docs.codeocean.com/user-guide/compute-capsule-basics/structure-of-a-compute-capsule/environment/starter-environment.

import logging
import math
import os
from random import random


def main() -> None:
    """
    Compute a value and save it to the results folder.
    """
    logging.info("Generating a random value between 0 and 1000...")
    val = math.floor(random() * 1001)

    logging.info("Creating results directory if doesn't exist...")
    # For CO to pick up results, they need to be saved to `/results`
    # Note that that's `/`, as in the root of the file system!
    os.makedirs("/results", exist_ok=True)

    logging.info("Writing random value...")
    with open("/results/random.txt", "w") as f:
        f.write(str(val))

    logging.info("Done!")


if __name__ == "__main__":
    main()
