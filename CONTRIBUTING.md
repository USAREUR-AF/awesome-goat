# Contributing

This list shows work that other people and organizations have built on goat. Anyone who has built such work may add it, including companies with commercial or proprietary products.

## Add an entry

1. Check that the work fits: it uses goat as its substrate, meaning it depends on goat's mesh, identity and data fabric together. See [What belongs here](README.md#what-belongs-here).
2. Fork this repository and add one line to the section of `README.md` that fits, at the end of that section. Remove the line "No entries yet" if yours is the first.
3. Use this form:

   ```markdown
   - [Name](https://example.org/product) - One sentence on what it does. Uses goat for: mesh, identity, fabric. By: Organization.
   ```

   - **Name and link.** The link goes to a public page about the work: a repository, documentation, a product page or a recorded demonstration. It must load without a sign-in.
   - **One sentence.** Say what the work does, in plain words. No slogans and no comparisons with other entries.
   - **Uses goat for.** Name the parts of goat the work depends on.
   - **By.** The organization or person responsible for the work.
4. Run `python3 tools/check.py` to check the format. Add `--links` to check that every link loads.
5. Commit and open a pull request. Say in the pull request how you are connected to the work.

If you prefer not to open a pull request, use the [entry form](https://github.com/USAREUR-AF/awesome-goat/issues/new?template=add-entry.yml) and a maintainer will add the entry.

## Rules for entries

- You are the author of the work, or you have the author's agreement to list it.
- A product does not have to be open source. Say so in the pull request if a reader needs a license or a contract to use it.
- The entry is true on the day it is added. If the work is withdrawn or stops working with goat, open a pull request to remove it; the maintainers also remove entries whose links stop loading.
- No entry names a person, host or address of a real deployment unless the organization that owns it has agreed in the pull request.
- A listing is not an endorsement by the U.S. Army or the U.S. Government, and an entry may not say or suggest that it is.

## Commits

- A [Conventional Commits](https://www.conventionalcommits.org/) subject, for example `docs(list): add <name>`.
- A DCO sign-off and a verified signature on every commit: `git commit -S -s`. A pull request with an unsigned commit cannot merge. Setting up signing is described in the [goatcore contributor guide](https://github.com/USAREUR-AF/goatcore/blob/main/CONTRIBUTING.md#commits).
- A pull request from someone outside the maintainers is reviewed by a maintainer before it merges.

## Licence

Portions written by U.S. Federal government employees within the scope of their employment are not subject to copyright in the U.S.; in countries where copyright is recognized, they and all other contributions are licensed under the [Apache License 2.0](LICENSE). See [INTENT.md](INTENT.md). Contributions are accepted under the [Policy](#policy) below.

**NOTE: This CONTRIBUTING.md is for software contributions. You do not need to follow the Developer's Certificate of Origin (DCO) process for commenting on this repository's documentation, such as CONTRIBUTING.md, INTENT.md, etc. or for submitting issues.**

## Policy

### 1. Introduction

The project maintainer for this Project will only accept contributions using the Developer's Certificate of Origin 1.1 located at [developercertificate.org](https://developercertificate.org) ("DCO"). The DCO is a legally binding statement asserting that you are the creator of your contribution, or that you otherwise have the authority to distribute the contribution, and that you are intentionally making the contribution available under the license associated with the Project ("License").

### 2. Developer Certificate of Origin Process

Before submitting contributing code to this repository for the first time, you'll need to sign a Developer Certificate of Origin (DCO) (see below). To agree to the DCO, add a `Signed-off-by` line to every commit with `git commit -s`. At a high level, signing off tells us that you have the right to submit the work you're contributing and indicates that you consent to our treating the contribution in a way consistent with the license associated with this software (as described in [LICENSE](LICENSE) and [INTENT.md](INTENT.md)) and its documentation ("Project").

### 3. Important Points

Pseudonymous or anonymous contributions are permissible, but you must be reachable at the email address provided in the Signed-off-by line.

If your contribution is significant, you are also welcome to add your name and copyright date to the source file header.

U.S. Federal law prevents the government from accepting gratuitous services unless certain conditions are met. By submitting a pull request, you acknowledge that your services are offered without expectation of payment and that you expressly waive any future pay claims against the U.S. Federal government related to your contribution.

If you are a U.S. Federal government employee and use a `*.mil` or `*.gov` email address, we interpret your Signed-off-by to mean that the contribution was created in whole or in part by you and that your contribution is not subject to copyright protections.

### 4. DCO Text

The full text of the DCO is included below and is available online at [developercertificate.org](https://developercertificate.org):

```txt
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
1 Letterman Drive
Suite D4700
San Francisco, CA, 94129

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```
