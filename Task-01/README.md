# Overall Difficulties Faced
Throughout the Terminal Voyage, the main difficulty was that the answers were not directly given. I had to investigate the repository, understand the clues, inspect files and Git history, and connect information from different levels.
Some of the difficulties I faced were:
-Understanding the structure of the repository and navigating through different directories.
-Learning Linux terminal commands that I had not used before.
-Understanding how Git branches, commits, and different timelines worked.
-Finding hidden information inside files and scripts.
-Understanding file permissions and executable files.
-Dealing with encoded or obfuscated information.
-Extracting information from archives and following clues between different locations.
-Understanding how different Git histories could contain different versions of the same information.
-Resolving the final conflicting histories instead of simply choosing one version.
-Understanding how to inspect previous versions of files using Git.
-Keeping track of clues and connecting information discovered in different levels.

# What I Learned Throughout the Task
## Level 1 — Loguetown Reef
I learned the basics of navigating a repository using the Linux terminal and exploring its directory and file structure.
### Learned:
- cd, ls, cat and other basic terminal commands.
- How to explore an unfamiliar repository.
- How to carefully read clues instead of assuming the answer.
## Level 2 — Whiskey Peak
I started working more deeply with Git and repository history. I investigated files, commits and branches and discovered the Devil Fruit information and its Awakening Signature.
### Learned:
- Git branches and commits.
- git log, git show, git diff.
- File permissions and executable files.
- How changes between commits can reveal hidden information.
- The importance of examining a file's history rather than only its current content.
## Level 3 — Little Garden
The investigation became more about searching through files and understanding the structure of the repository.
### Learned:
- Searching through directories efficiently.
- Reading logs and unusual files.
- Following clues across different parts of a repository.
- Being patient when the obvious file does not contain the answer.
## Level 4 — Water 7
This level introduced more complicated work. I had to investigate the recovered blueprints and extract information from them.
### Learned:
- Working with compressed/archive files.
- Extracting files from archives.
- Understanding multiple layers of information hiding.
- Using terminal tools to inspect unfamiliar files.
- Connecting information from extracted files to later clues.
## Level 5 — Enies Lobby
I worked with the Poneglyph-related files and an encoded message. This required understanding how the provided script processed the information.
### Learned:
- Base64 encoding/decoding.
- Understanding Python scripts provided in a repository.
- Following a chain of clues instead of treating each file separately.
- Understanding how cryptographic/encoding techniques can be used to protect information.
- Using Git and the terminal together during an investigation.
## Level 6 — The Great Merge War at Laugh Tale
This was the most challenging level because the information existed in different Git histories.
I found:
treasure/key_part_1.txt
treasure/key_part_2.txt
and then checked their histories using:
git log --all --oneline -- treasure/key_part_1.txt
git log --all --oneline -- treasure/key_part_2.txt
I discovered that the files had multiple historical versions. I then used git show to inspect those versions and compare the conflicting records.
This taught me that Git history is not just a record of changes—it can also preserve information that is no longer visible in the current version of a file.
Finally, I reconstructed the password:
**TheGrandLineRemembers**
and used victory.sh to verify the solution.

## Overall Learning
The biggest thing I learned from this task is how to investigate instead of just searching for an answer.
I became more comfortable with:
- Linux terminal
- Git branches
- Git commits and history
-  Searching and inspecting files
- Comparing different versions
- Archives and extraction
- Encoding and decoding
- Reading basic Python scripts
- Understanding hashes and verification
- Problem-solving through clues
- Documenting my investigation

Most importantly, I learned that a repository can contain a story in its history. Sometimes the current file is not enough; previous commits, branches, permissions, and deleted or changed information can all be part of the solution.
##  Final Reflection
The greatest lesson from Terminal Voyage was not simply learning Git or Linux, but learning how to investigate, connect clues, recover information, and understand the history behind a repository.
