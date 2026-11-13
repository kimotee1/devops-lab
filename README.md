# Linux & DevOps Learning Path

## Day 1 — Linux Fundamentals

### 1. Terminal Navigation

| Command | Description |
|---|---|
| `pwd` | Displays the current working directory |
| `ls` | Lists files and directories |
| `ls -a` | Displays hidden files |
| `ls -l` | Displays detailed file information |
| `ls -la` | Displays all files with detailed information |
| `cd` | Changes the current directory |

### 2. File and Directory Management

| Command | Description |
|---|---|
| `mkdir` | Creates a new directory |
| `touch` | Creates an empty file |

### 3. Reading Files and Searching Text

| Command | Description |
|---|---|
| `cat` | Displays file contents |
| `grep` | Searches for specific text inside files |

Example:

```bash
grep "started" app.log
```

### 4. Editing Files

Command:

```bash
nano app.log
```

Useful shortcuts:

- `Ctrl + O` — Save changes
- `Enter` — Confirm filename
- `Ctrl + X` — Exit
- `Ctrl + K` — Cut the current line

### 5. Writing and Appending Text

```bash
echo "Application started" > app.log
```

- `>` — Writes text and overwrites existing content.

```bash
echo "Application stopped" >> app.log
```

- `>>` — Appends text without removing existing content.

### 6. Clearing File Contents

```bash
truncate -s 0 app.log
```

- Clears the file contents.
- Keeps the file itself.

### 7. Important Notes

- Linux commands are case-sensitive.
- Hidden files usually start with a dot (`.`).
- `.` represents the current directory.
- `..` represents the parent directory.
- `rm` removes files and should be used carefully.

### 8. Practical Experience

Created a project structure:

```text
devops-lab/
├── logs/
│   └── app.log
├── scripts/
├── backup/
├── reports/
└── README.md
```

**Day 1 Status:** CompletedMy first Linux project


## Day 2 — File Management

### 1. Copying Files

```bash
cp source destination
```

Example:

```bash
cp logs/app.log backup/
```

- `cp` copies files.
- The original file remains in its location.

### 2. Moving and Renaming Files

```bash
mv source destination
```

Examples:

```bash
mv logs/app.log backup/
mv old-name.txt new-name.txt
mv logs/app.log backup/server.log
```

- `mv` moves files and directories.
- `mv` can also rename files.
- `mv -i` asks for confirmation before overwriting an existing file.

### 3. Removing Files and Directories

| Command | Description |
|---|---|
| `rm file.txt` | Removes a file |
| `rm -i file.txt` | Asks before removing a file |
| `rmdir folder` | Removes an empty directory |
| `rm -r folder` | Removes a directory and its contents |
| `rm -ri folder` | Asks for confirmation during recursive removal |

**Warning:** `rm -r` can permanently delete files and directories.

### 4. Directory Structure

```bash
tree
tree -L 2
tree -a
tree -d
```

- `tree` displays directory structures.
- `-L` limits directory depth.
- `-a` includes hidden files.
- `-d` displays directories only.

### 5. Finding Files

```bash
find . -name "*.log"
find . -type f
find . -type d
find . -type f -size +10M
find . -type f -size -1k
```

- `find` searches for files and directories.
- `-name` searches by filename.
- `-type f` searches for files.
- `-type d` searches for directories.
- `-size` searches by file size.

### 6. Searching Text with Grep

```bash
grep -r "Application" backup/
grep -i "application" app.log
grep -n "Application" app.log
grep -rin "application" backup/
```

- `-r` searches recursively.
- `-i` ignores uppercase and lowercase differences.
- `-n` displays line numbers.

### 7. Practical Experience

- Copied log files into the backup directory.
- Moved and renamed files.
- Explored directory structures using `tree`.
- Searched for log files using `find`.
- Searched file contents using `grep`.
- Combined multiple search options.

**Day 2 Status:** Completed
Git practice
Another Git change
Login feature
GitHub Pull Practice
