# Mass Git Changes

Unrefined scripts for retrieving many git repos and then pushing changes back to server.

## Prerequisites

- git
- A list of git URLs
- Authorized connection to the git server(s) for the URLs

## Scripts

`clone-repos.py`: Based on the list in `repourls.txt` clone a bunch of git repos.
`push-all.py`: Iterate over all directories in the `repos` directory to `add`/`commit`/`push` changes to `README.md`.

## Contributions

This is such a piddly little thing I'm not expecting any contributions, but if you want to, I'm open to a PR. But I won't be following this closely, so please be patient with response times.
