from typing import AnyStr

import git


def get_git_signature(path: AnyStr = None):

    # Get SHA git signature from current project directory
    if path is None:
        try:
            repo = git.Repo(search_parent_directories=True)
            sha = repo.head.object.hexsha
            return sha
        except git.exc.InvalidGitRepositoryError:
            return 'no Git repository found'
