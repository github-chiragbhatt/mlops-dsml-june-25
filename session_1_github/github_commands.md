# Basic GitHub Commands

```bash
# Configure user information
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize a new repository
git init

# Clone an existing repository
git clone <repository_url>

# Check repository status
git status

# Add files to staging area
git add <file_name>
git add .   # Add all files

# Commit changes
git commit -m "Commit message"

# View commit history
git log

# Push changes to remote repository
git push origin <branch_name>

# Pull latest changes from remote
git pull origin <branch_name>

# Create a new branch
git branch <branch_name>

# Switch to a branch
git checkout <branch_name>

# Merge a branch into current branch
git merge <branch_name>
```