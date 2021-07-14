#!/usr/bin/env python3
import os
from updater import main as updater

import subprocess

HOOKS_FILE = os.path.join(os.path.dirname(__file__), "..", ".pre-commit-hooks.yaml")


class Colors:
    GREEN = "\033[32m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def _get_current_version() -> str:
    major, minor, patch = (
        subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0", "HEAD"],
            stdout=subprocess.PIPE,
        )
        .stdout.decode()
        .strip()[1:]
        .split(".")
    )

    return f"{int(major)}.{int(minor)}.{int(patch)}"


def _get_next_version(current_version: str) -> str:
    major, minor, patch = current_version.split(".")

    return f"{int(major)}.{int(minor)}.{int(patch)+1}"


def main() -> None:
    print(f"{Colors.BOLD}Running update-script:{Colors.RESET}")

    updater()

    print(f"\n\n{Colors.BOLD}Pushing updates if required:{Colors.RESET}")

    print("==> Staging hook-file.")
    subprocess.run(
        ["git", "add", HOOKS_FILE],
        stdout=subprocess.DEVNULL,
    )

    changed = bool(
        subprocess.run(
            ["git", "diff-index", "--exit-code", "HEAD", HOOKS_FILE],
            stdout=subprocess.DEVNULL,
        ).returncode,
    )

    if not changed:
        print(f"{Colors.GREEN}==> No changes have been performed.{Colors.RESET}")
        return

    current_version = _get_current_version()
    next_version = _get_next_version(current_version)

    print("==> Configuring git.")
    subprocess.run(
        ["git", "config", "--global", "user.name", "GitHub Actions"],
        stdout=subprocess.DEVNULL,
    )
    subprocess.run(
        ["git", "config", "--global", "user.email", "actions@github.com"],
        stdout=subprocess.DEVNULL,
    )

    print("==> Committing changes.")
    subprocess.run(
        ["git", "commit", "--message", "updated packages"],
        stdout=subprocess.DEVNULL,
    )

    commit_sha = (
        subprocess.run(
            ["git", "rev-parse", "HEAD"],
            stdout=subprocess.PIPE,
        )
        .stdout.decode()
        .strip()
    )
    commit_date = (
        subprocess.run(
            ["git", "show", "--no-patch", "--no-notes", "--pretty='%aI'", commit_sha],
            stdout=subprocess.PIPE,
        )
        .stdout.decode()
        .strip()
    )

    print(f"==> Adding tag v{next_version} to commit {commit_sha}.")
    subprocess.run(
        [
            "git",
            "tag",
            "--annotate",
            f"v{next_version}",
            commit_sha,
            "--message",
            f"Version {next_version}",
        ],
        env={
            "GIT_COMMITTER_DATE": commit_date,
            **os.environ,
        },
        stdout=subprocess.DEVNULL,
    )

    print("==> Pushing changes and tags.")
    subprocess.run(["git", "push"])
    subprocess.run(["git", "push", "--tags"])

    print(f"{Colors.GREEN}==> Pushed changes ({current_version} → {next_version}){Colors.RESET}")


if __name__ == "__main__":
    main()
