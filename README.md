<!-- language-switch:start -->
[English](./README.md) | [中文](./README.zh-CN.md)
<!-- language-switch:end -->

# docs

Sparse local workspace for the `joy7758/docs` repository.

This checkout keeps the documentation configuration and the selected editable sources without pulling the full upstream tree into the current workspace.

## What is here

- `AGENTS.md` records the documentation editing rules for this workspace.
- `src/docs.json` contains the Mintlify site configuration.
- `reference/` is reserved for generated reference artifacts.

## What this workspace is for

- review documentation structure
- edit manually maintained docs surfaces when they are included in the sparse checkout
- inspect the site configuration before making documentation changes

## What this workspace is not for

- it is not the full upstream documentation repository checkout
- it is not the generated publish output
- it is not the place to edit auto-generated reference content directly
