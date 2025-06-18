from prologger import Logger
from .processor import Processor

from ehir.tree import EHIR_ProjectTree
from pathlib import Path
import sys


def cli_entrypoint():
    main(*sys.argv)


def main(*args):
    args = list(map(str, args))
    
    logger = Logger(0)
    processor = Processor()
    
    project_tree = EHIR_ProjectTree(processor)
    project_tree.build_from(Path().resolve() / "main.ehir")


if __name__ == "__main__":
    cli_entrypoint()
