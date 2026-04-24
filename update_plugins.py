import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from os import path

# --- Globals ----------------------------------------------
PLUGINS = """
auto-pairs https://github.com/jiangmiao/auto-pairs
ale https://github.com/dense-analysis/ale
vim-yankstack https://github.com/maxbrunsfeld/vim-yankstack
ack.vim https://github.com/mileszs/ack.vim
bufexplorer https://github.com/jlanzarotta/bufexplorer
ctrlp.vim https://github.com/ctrlpvim/ctrlp.vim
mayansmoke https://github.com/vim-scripts/mayansmoke
nerdtree https://github.com/preservim/nerdtree
nginx.vim https://github.com/chr4/nginx.vim
open_file_under_cursor.vim https://github.com/amix/open_file_under_cursor.vim
tlib https://github.com/tomtom/tlib_vim
vim-addon-mw-utils https://github.com/MarcWeber/vim-addon-mw-utils
vim-bundle-mako https://github.com/sophacles/vim-bundle-mako
vim-coffee-script https://github.com/kchmck/vim-coffee-script
vim-colors-solarized https://github.com/altercation/vim-colors-solarized
vim-indent-object https://github.com/michaeljsmith/vim-indent-object
vim-less https://github.com/groenewege/vim-less
vim-pyte https://github.com/therubymug/vim-pyte
vim-snipmate https://github.com/garbas/vim-snipmate
vim-snippets https://github.com/honza/vim-snippets
vim-surround https://github.com/tpope/vim-surround
vim-expand-region https://github.com/terryma/vim-expand-region
vim-multiple-cursors https://github.com/terryma/vim-multiple-cursors
vim-fugitive https://github.com/tpope/vim-fugitive
vim-rhubarb https://github.com/tpope/vim-rhubarb
goyo.vim https://github.com/junegunn/goyo.vim
vim-zenroom2 https://github.com/amix/vim-zenroom2
vim-repeat https://github.com/tpope/vim-repeat
vim-commentary https://github.com/tpope/vim-commentary
vim-gitgutter https://github.com/airblade/vim-gitgutter
gruvbox https://github.com/morhetz/gruvbox
vim-flake8 https://github.com/nvie/vim-flake8
vim-pug https://github.com/digitaltoad/vim-pug
lightline.vim https://github.com/itchyny/lightline.vim
lightline-ale https://github.com/maximbaz/lightline-ale
vim-abolish https://github.com/tpope/vim-abolish
rust.vim https://github.com/rust-lang/rust.vim
vim-markdown https://github.com/plasticboy/vim-markdown
vim-gist https://github.com/mattn/vim-gist
vim-ruby https://github.com/vim-ruby/vim-ruby
typescript-vim https://github.com/leafgarland/typescript-vim
vim-javascript https://github.com/pangloss/vim-javascript
vim-python-pep8-indent https://github.com/Vimjas/vim-python-pep8-indent
vim-indent-guides https://github.com/nathanaelkane/vim-indent-guides
mru.vim https://github.com/vim-scripts/mru.vim
editorconfig-vim https://github.com/editorconfig/editorconfig-vim
dracula https://github.com/dracula/vim
copilot.vim https://github.com/github/copilot.vim
""".strip()

SOURCE_DIR = path.join(path.dirname(__file__), "sources_non_forked")


def update(plugin):
    name, github_url = plugin.split(" ")
    plugin_path = path.join(SOURCE_DIR, name)

    try:
        if path.exists(plugin_path):
            if path.exists(path.join(plugin_path, ".git")):
                result = subprocess.run(
                    ["git", "-C", plugin_path, "pull"],
                    capture_output=True, text=True, check=True
                )
                if "Already up to date" in result.stdout:
                    print("Already up to date: {}".format(name))
                else:
                    print("Updated {}".format(name))
            else:
                shutil.rmtree(plugin_path)
                subprocess.run(
                    ["git", "clone", github_url, plugin_path],
                    capture_output=True, text=True, check=True
                )
                print("Cloned {} (replaced non-git dir)".format(name))
        else:
            subprocess.run(
                ["git", "clone", github_url, plugin_path],
                capture_output=True, text=True, check=True
            )
            print("Cloned {}".format(name))
    except Exception as exp:
        print("Could not update {}. Error was: {}".format(name, str(exp)))


if __name__ == "__main__":
    plugins = PLUGINS.splitlines()
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(update, p): p for p in plugins}
        for future in as_completed(futures):
            future.result()
