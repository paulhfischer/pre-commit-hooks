#!/usr/bin/env python3
import json
import os
from urllib.request import Request
from urllib.request import urlopen

import yaml

HOOKS_FILE = os.path.join(os.path.dirname(__file__), "..", ".pre-commit-hooks.yaml")


class Colors:
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    RED = "\033[1;31m"
    RESET = "\033[0;0m"


def _node_get_latest_version(package: str) -> str:
    request = Request(
        f"https://registry.npmjs.org/{package}",
        headers={"Accept": "application/vnd.npm.install-v1+json"},
    )
    with urlopen(request) as response:
        return str(json.loads(response.read().decode())["dist-tags"]["latest"])


def main() -> None:
    replace = set()

    with open(HOOKS_FILE, "r") as file:
        for hook in yaml.safe_load(file):
            if hook["language"] == "node" and "additional_dependencies" in hook:
                for dependency in hook["additional_dependencies"]:
                    if "@^" in dependency:
                        package, version = dependency.split("@^")
                        latest_version = _node_get_latest_version(package)

                        if version == latest_version:
                            print(
                                f"{Colors.GREEN}"
                                f"==> {package} is up to date ({version})."
                                f"{Colors.RESET}",
                            )
                        else:
                            print(
                                f"{Colors.YELLOW}"
                                f"==> {package} needs update ({version} → {latest_version})."
                                f"{Colors.RESET}",
                            )
                            replace.add((dependency, f"{package}@^{latest_version}"))
                    elif not dependency.startswith("-"):
                        print(
                            f"{Colors.RED}"
                            f"==> Failed to get version for {dependency}."
                            f"{Colors.RESET}",
                        )

    with open(HOOKS_FILE, "r") as file:
        hooks = file.read()
        for old, new in replace:
            hooks = hooks.replace(old, new)

    with open(HOOKS_FILE, "w") as file:
        file.write(hooks)
        print(
            f"\n{Colors.GREEN}==> Updated {len(replace)} dependencies.{Colors.RESET}",
        )


if __name__ == "__main__":
    main()
