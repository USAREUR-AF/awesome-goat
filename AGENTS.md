# AGENTS.md

Instructions for AI coding agents, and a short version for anyone working here. [CONTRIBUTING.md](CONTRIBUTING.md) is the full process.

## What this repository is

awesome-goat is a list of work that other people and organizations have built on [goat](https://github.com/USAREUR-AF/goatcore), including commercial and proprietary products. It holds no goat source code. The list is `README.md`.

## Adding an entry

Add one line at the end of the fitting section of `README.md`, in this form:

```markdown
- [Name](https://example.org/product) - One sentence on what it does. Uses goat for: mesh, identity, fabric. By: Organization.
```

An entry is only for work that uses goat's mesh, identity and data fabric together. Do not add goat's own repositories. Do not write an entry for work whose author has not asked for it.

## Before you push

```bash
python3 tools/check.py          # entry format, sections, no duplicates
python3 tools/check.py --links  # also loads every link
```

## Rules

1. **Commits.** Conventional Commits subject of 100 characters or fewer. Every commit is signed off (`git commit -s`, the DCO) and signed with a key GitHub verifies (`-S`).
2. **One entry per pull request.**
3. **Nothing from a real deployment** (hostname, address, person) unless its owner agreed in the pull request.
4. **Vulnerabilities** go through [SECURITY.md](SECURITY.md), never a public issue.
