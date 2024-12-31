# Mass Git Changes

Unrefined scripts for retrieving many git repos and then pushing changes back to server.

## Why?

These are really git org maintenance tools. For instance, if you need to make a change across a lot of different files in a git repo, say swap out a license or update contributor terms, these scripts can help.

## Prerequisites

- git
- A list of git URLs
- Authorized connection to the git server(s) for the URLs

## Scripts

+--+--+--+
| File | Description | Parameter(s) |
+--+--+--+
|`clone-repos.py`| Based on the list in `repourls.txt` clone a bunch of git repos.| _none_ |
|`push-all.py`| Iterate over all directories in the `repos` directory to `add`/`commit`/`push` changes to `README.md`.| `working_branch`|
+--+--+--+


## Contributions

This is such a piddly little thing I'm not expecting any contributions, but if you want to, I'm open to a PR. But I won't be following this closely, so please be patient with response times.
