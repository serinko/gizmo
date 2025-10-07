# SSH & git Beginner Tutorial

This how to guide is for people who want to start working with remote repostiories using [SSH (Secure Shell)](https://www.ssh.com/academy/ssh) and [git](https://git-scm.com). It's written in a step-by-step detailed form to understand the basics while it abstracts away the complexity of these tools. Therefore this tutorial contains a bit of information and reference while not going too deep to confuse the user. 

**The aim is to make a user familiar with remote collaborative work, where all files are locally stored in the users computer. This knowledge allows for working offline and in parallel from other contributors, creating own branches, merging them via Pull requests back to the remote repository.**

## Requirements

To begin you need a laptop / desktop and approx 60-90 min to have time to get familiar of the flow. All the tools needed will be downloaded and configured as a part of the flow. These tools will be:

- Terminal (shell) 
- Local password manager - We will use [KeepassXC](https://keepassxc.org/download/#linux) in this guide
- Text editor - We will use [VS Codium](https://vscodium.com/) in this guide
- SSH key pair - We generate one in [SSH](#ssh) chapter
- git version control tool - We will set it up in [git](#git) chapter

## SSH

Secure Shell is a protocol that uses encryption to secure the connection between a client and a server - your computer and a remote computer. All user authentication, commands, output, and file transfers are encrypted to protect against attacks in the network. Server can be self hosted macvhine or for example a Github repository. 

Basic SSH diagram taken from [SSH documentation page](https://www.ssh.com/academy/ssh):

![](https://www.ssh.com/hubfs/Imported_Blog_Media/SSH_simplified_protocol_diagram-2.png)

**We use SSH to download (`git clone` or `git pull`) the work  done by others and upload (`git push`) the changes done by us.**

### SSH Setup

Before we begin to setup a SSH keypair, let's make sure we have installed and opened a password manager. In case you don't use any, start with [downloading KeePassXC](https://keepassxc.org/download/).

Then generate your SSH key and store the access in you KeePassXC, following these steps:

1. **Create a KeepassXC database if you don't have one already:**
- Open KeePassXC, click on top on create new database, follow the steps in the application

2. **Create a new entry for you SSH key:**
- Click on the `+` icon on top
- `Title` field: Name it something like `ssh-<IDENTITY>-ed25519`, for example: `ssh-mygithubkey-ed25519`
- Generate a password in the `Password` field using the dice icon on the right side of the field
- Add your email into `Username` field - Note this email can be completely made up if you don't want to use your real email

3. **Ensure SSH config directory (`$HOME/.ssh`) exists:**
- Run this command that finds out and create it if needed:
```sh
mkdir -p ~/.ssh
```

4. **Create your SSH key pair:**
- Open a terminal window and run the command bellow, replace values with the ones we stored in the KeePassXC for the given key:
    - `<EMAIL>` with the one in `Username` field
    - `<SSH-KEY-NAME>` with the one from `Title` field  
```sh
ssh-keygen -t ed25519 -C "<EMAIL>" -f ~/.ssh/<SSH-KEY-NAME>
```
- The process will prompt you for a password, copy-paste the one from `Password` field in the KeePassXC for the given key

5. **Configure SSH key in your KeePassXC:**
> This setting is optional but highly recommended as it means that your key will work automatically but only when your KeePassXC is unlocked
- In the key entry click on `SSH Agent` on the left side bar
- On top tick these boxes:
    - `Addkey to agent when database is opened`
    - `Remove key from agent when database is locked`
- In `Private Key` pane, add a key by `External file` clicking on `Browse` and navigating to `.ssh/` choosing the key you just created
- Click on `Add to agent`
> On the bottom you see a block called `Public key`. Often people who want to *add your key to the repo* will ask you for your ssh public key, just copy-paste this block and send it to them

Congratulation, you just created your SSH key pair.

## git

> Git is a [free and open source](https://git-scm.com/about/free-and-open-source) distributed version control system designed to handle everything from small to very large projects with speed and efficiency. 

We use git as it's the most commonly known tool for distriburted collaboartion. You can read more about [git on their page](https://git-scm.com/).

### Install git

Most systems already have git installed by default, check it out with entering this command to your terminal:
```sh
git --version
```

If git doesn't exist in your system, [downloand and install it](https://git-scm.com/downloads), or use your package management system (the place from where you install tools). For Debian based systems run
```sh
sudo apt install git
```

### Download git Repository

After your public SSH key was added to the repository, you can start to work remotely from your local computer. 

- Open your terminal in the place where your want to have the root directory of the repository, commonly used is `$HOME/src/`
- Use this command to download (`clone`) the repository to that folder, where exchange:
    - `<REPOSTIORY_URL>` with the actual repository url
    - `<USER>` and `<REPO>` with the host username and repo name - these two are only needed in self-hosted instances
```sh
git clone git@<REPOSTIORY_URL>:<USER>/<REPO>.git
```
- Example of cloning this repo would be:
```sh
git clone git@github.com:serinko/gizmo.git
```
- Now you can open any file from that repostiry directly in your computer and edit the files

### Configure git

Right after you download repository, it's good to configure it to prevent for example using a wrong nick name or email, as those will be seen by other contributors and in case of public repo - by everyone. 

Every repository has a config git folder in its root directory called `.git`. The most important file is then `.git/config`. 

- Navigate to the top directory of the repository and open the `.git/config` in your favourite text editor. 

- There should be a part called `[user]`, looking like this:
```toml
[user]
        email = some@email.me
        name = serinko
```
- Change the values to the ones you want to have displayed next to your commits in this particular repository, save and exit

> Note that we do this per repository and *not* globally in your `$HOME/.gitconfig`. Like this you will prevent having the same displayed identity across multiple repositories. 

### Working with git Repository

#### The most commonly used git syntax, jargon and examples

| Name | Function | Command Syntax |Command Example |
| :-- | :-- | :-- | :-- |
| *Clone* | Download repository for the first time | `git clone git@<REPOSTIORY_URL>:<USER>/<REPO>.git` | `git clone git@github.com:serinko/gizmo.git` |
| *Status* | Shows a state of my work in relation to the git repository | `git status` | `git status` |
| *Pull* | Download latest remote changes of the repository | `git pull` | `git pull origin master` |
| *Branch off / Fork* | Creates a new branch separated from the main one | `git checkout -b "<NEW_BRANCH_NAME>"` |  `git checkout -b "serinko/feature/new-tutorial"` |
| *Add* | Adds or removes file(s) from git tracking | `git add <PATH_TO_FILE>` | `git add .` |
| *Commit* | Store your changes on the current branch | `git commit -am "<SHORT_DESCRIPTION>"` | `git commit -am "intialise ssh git tutorial"` |
| *Push* | Uploads my commits up to the remote so others can see them | `git push origin <MY_BRANCH_NAME>` | `git push origin serinko/feature/new-tutorial` |

#### Simple Work Flow

Once we cloned the repository, it stays in our computer. However, other people have been making changes on it on their computers, pushing it up to the remote. Therefore for this to work in the cleanest way possible, we need to follow a common logic. In the simpliest form it goes like this:

1. `git status` - Always start with informing yourself about the current state of the repository. In case your status shows your last working branch - make sure to switch to the main working one first:
- `git checkout <MAIN_COMMON_BRANCH>` - For example `git checkout master` or `git checkout main` - depends what's the baseline branch for the repostiry 
2. `git pull` - Pull the current state of the common branch
3. `git checkout -b "<NEW_BRANCH_NAME>"` - Branch off from the latest common state into your own branch
4. Make changes
5. If you added or removed files run `git add .` from the root repo directory
6. `git commit -am "<SHORT_DESCRIPTION>"` - After every significant change and file save, record it to git using commits
7. Repeat steps 4-6 as many times as needed
8. `git push origin <NEW_BRANCH_NAME>` - When you want your branch to be visible to others (or public in case of puclic repo) push the changes up

#### Example: Flow with Github

There are many instances of git web hosting interfaces like [Codeberrg](https://codeberg.org/), [GitLab](https://about.gitlab.com/), [NoLog](https://code.nolog.cz/) and [Github](https://github.com). From privacy and free software point of view, Codeberg or NoLog may be the best options. I will use Github for this example as this is where this repository lives and it's the most commonly used one. 

I will demonstrate adding this file to the repository, using the [flow documented above](#simple-work-flow). Because I already have the repostory, I skip the [download](#download-git-repository) and [configure](#configure-git) partsa and go straight to it.

You can use the in-build terminal in your VS Codium or just any terminal

1. In terminal: Navigate to the root folder of the repo:
```sh
cd $HOME/src/gizmo
```
- Note: `cd` command stands for change directory and it's one of the most commonly used terminal commands

2. `git status` to check the repository status, my output is:
```
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
- Great! I am on `master` without any untrailed changes

3. `git checkout -b "feature/ssh-git-101-tutorial"` to create a new branch called `feature/ssh-git-101-tutorial`, the output is:
```
Switched to a new branch 'feature/ssh-git-101-tutorial'
```

4. Do my changes:
- Create `tutorials` directory - you can do it in your file system or by this command:
```sh
mkdir tutorials
```
- Open a text editor and create a file called `ssh_git_101.md`, save it directly empty
- Write my initial version of text to this point and save it

3. Add this new file (and directory) - open terminal (standalone or in codium), make sure it's in `gizmo` repo directory and run:
```sh
# to add all new or removed files in all sub-directories:
git add .

# alternatively add just this one file
git add tutorials/ssh_git_101.md
```

4. Commit my changes:
```sh
git commit -am "intialise ssh git tutorial"
```
- The output:
```
[feature/ssh-git-101-tutorial a82141a] intialise ssh git tutorial
 1 file changed, 199 insertions(+)
 create mode 100644 tutorials/ssh_git_101.md
```

5. Do more work - like writing this and next point and follow the flow of:
- Save file
- Commit changes

6. Push: When my writing is finished for the day I will push it up:
```sh
git push origin feature/ssh-git-101-tutorial
```
- The output:
```
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (8/8), 5.24 KiB | 5.24 MiB/s, done.
Total 8 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
remote:
remote: Create a pull request for 'feature/ssh-git-101-tutorial' on GitHub by visiting:
remote:      https://github.com/serinko/gizmo/pull/new/feature/ssh-git-101-tutorial
remote:
To ssh://github_serinko/serinko/gizmo.git
 * [new branch]      feature/ssh-git-101-tutorial -> feature/ssh-git-101-tutorial
```
- Note the message with the generated link: [https://github.com/serinko/gizmo/pull/new/feature/ssh-git-101-tutorial(https://github.com/serinko/gizmo/pull/new/feature/ssh-git-101-tutorial)]

7. Create a Pull Request (PR): Visit the Github url and edit the PR description:
- On the first landing, I can see initial rather empty description
![](images/github-pr-landing-view)
- I will edit it so there is:
    - A simple Title and useful description of the PR
    - Assing myself to finish this PR
    - If the repo had a reviewer I would chose them
    - Added a Label
    - Ensure that comparison on top is to the right base branch where I eventually want to merge to
    - Change `Create pull request` to `Draft pull request` as I do want to publish this state but don't want it to be reviewed just yet
- The result

![](images/github-pr-edited-view)

8. Finish my works: save, add (as I created a new dir with images isnce the last commits), commit, push ... repeat steps above as many times as I need on as many files within the repo as needed

9. Click on `Ready for Review`

10. Notify the reviewer and wait for their comments if there is something to be changed