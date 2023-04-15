"""Console script for {{cookiecutter.pkg_name}}."""

import hydra
from x2r.cli import main


if __name__ == "__main__":
    main = hydra.main(
        version_base=None, config_path="../configs", config_name="config"
    )(main)

    main()
