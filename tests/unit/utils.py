import logging
import os
import re
import subprocess

from typing import List, Dict, Optional

LOG = logging.getLogger(__name__)

def run_command(command: str, cwd: Optional[str] = None) -> str:
    """Runs the provided command and captures its output.

    Args:
        command: The command to run.
        cwd: The working directory.

    Returns:
        The captured output of the command.
    """
    try:
        result = subprocess.run(command, cwd=cwd, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        LOG.error(f"Failed to run command: {command}")
        LOG.error(f"Error: {e.stderr}")
        raise

def run_command_with_env(command: str, env_vars: Dict[str, str], cwd: Optional[str] = None) -> str:
    """Runs the provided command in an environment with the provided environment variables.

    Args:
        command: The command to run.
        env_vars: A dictionary of environment variables to set.
        cwd: The working directory.

    Returns:
        The captured output of the command.
    """
    env = os.environ.copy()
    env.update(env_vars)
    try:
        result = subprocess.run(command, cwd=cwd, shell=True, env=env, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        LOG.error(f"Failed to run command: {command}")
        LOG.error(f"Error: {e.stderr}")
        raise

def make_sure_dir_exists(path: str) -> None:
    """Makes sure the directory exists.

    Args:
        path: The path to the directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def get_first_match(pattern: str, string: str) -> Optional[str]:
    """Gets the first match for a regular expression pattern in a string.

    Args:
        pattern: The regular expression pattern.
        string: The string to search in.

    Returns:
        The first match, or None if no match is found.
    """
    match = re.search(pattern, string)
    if match:
        return match.group()
    else:
        return None