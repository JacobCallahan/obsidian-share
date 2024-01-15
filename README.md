# obsidian-share
A collection of things we think others might like to use in Obsidian

## How to Use
The easiest way to use the contents of this repo is to clone it locally and copy files/directories into your local obsidian directory.

Additionally, you could just copy the contents of individual files directly from GitHub, but be careful of formatting and extra characters (view raw will help).

## Templates
Some of the templates in this repository have been generalized from what many of us use personally.

They are intended to be a baseline for you to personalize and make them fit your specific needs.

## .obsidian files
These files typically consist of plugins and their configuration.

Like templates, you can copy these directly into your .obsidian directory, then tailor as desired.

### Notable Config Changes

**Hotkeys**
- Alt + ArrowUp: Moves the current line up
- Alt + ArrowDown: Moves the current line down

### Plugins
See the .obsidian/plugins directory's README.md for a description of each plugin and notable config changes.

### CSS Snippets
See the .obsidian/snippets directory's README.md for a description of each plugin and notable config changes.

## Automatic Git Backups
To perform automatic git backups, configure your .obsidian directory to be a git directory.

It is recommended that your origin point to a private GitHub repository or other private repo.

- Copy the auto_push.sh script to some local directory, likely your obsidian directory
- Make the script executable with `chmod +x auto_push.sh`
- Edit the script's `cd` path to where you copied the auto_push.sh script
- Install cron if not already installed
- Run `crontab -e` to edit your cron file
- Add an entry for your auto_push.sh script, I recommend `0 17 * * * /path/to/auto_push.sh`

## Contributing
Do you have any great templates or plugins you think are handy? Submit a pull request!
