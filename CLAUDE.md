# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is "The Ultimate vimrc" — a Vim configuration distribution (originally by amix/vimrc) that Derek has forked and customized. It is installed to `~/.vim_runtime/` and works by sourcing a chain of VimScript files from a generated `~/.vimrc`.

## Installation

```sh
# Awesome version (with plugins)
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh

# Basic version (single file, no plugins)
sh ~/.vim_runtime/install_basic_vimrc.sh

# Multi-user install
sh install_awesome_parameterized.sh /opt/vim_runtime user0 user1
```

## Updating Plugins

Plugins in `sources_non_forked/` are managed by `update_plugins.py`, which downloads each plugin's GitHub master zip and replaces the local copy:

```sh
python update_plugins.py   # or python3
```

To add a new plugin, add a line `plugin-name https://github.com/owner/repo` to the `PLUGINS` string in `update_plugins.py`, then run the script.

## Repository Structure

- **`vimrcs/`** — Core configuration files sourced in order:
  - `basic.vim` — General settings, key mappings, and UI options
  - `filetypes.vim` — Filetype-specific indentation and options
  - `plugins_config.vim` — Plugin-specific configuration
  - `extended.vim` — Additional mappings and functions
- **`sources_non_forked/`** — Plugin source managed by `update_plugins.py` (do not edit manually)
- **`sources_forked/`** — Plugins that have been forked and modified locally
- **`autoload/pathogen.vim`** — Pathogen plugin manager (loads everything in `sources_non_forked/` and `my_plugins/`)
- **`my_plugins/`** — User-specific plugins installed via `git clone` (gitignored content)
- **`temp_dirs/`** — Swap, backup, and undo file storage

## User Customization

Personal customizations go in `~/.vim_runtime/my_configs.vim` (not tracked — sourced with `try/catch` so absence is safe). Personal plugins go in `my_plugins/` via pathogen or in `pack/plugins/start/` for native Vim 8+ packages.

## Key Conventions

- Leader key is `,`
- `<leader>w` — fast save; `<leader>bd` — close buffer; `<C-f>` — CtrlP fuzzy finder
- Installed colorschemes: peaksea (default), dracula, solarized, ir_black, mayansmoke, pyte, gruvbox
- The generated `~/.vimrc` has a "DO NOT EDIT" header; all real config lives in `vimrcs/`
