# Captain's Logbook — Task 01

## Level 1 — Awakening at Loguetown Reef

### Initial Observation

The Loguetown Reef contained four storage sectors:

- sector_A
- sector_B
- sector_C
- sector_D

Each sector contained multiple Devil Fruit files.

### Investigation

I inspected the files in the four sectors. The files contained the
same message, so the content itself did not identify the genuine fruit.

While inspecting Sector C, I noticed that `devil_fruit_6.txt` appeared
in green in the terminal.

I compared its file permissions with another Devil Fruit:

- `devil_fruit_5.txt` → `-rw-rw-r--`
- `devil_fruit_6.txt` → `-rwxrwxr-x`

The important difference was the `x` (execute) permission.

### Investigating eat.sh

I inspected `eat.sh` using:

`cat eat.sh`

The script checks whether the supplied file has execute permission
using:

`[[ -x "$FRUIT" ]]`

This confirmed that the execute permission was the property used to
identify the genuine Devil Fruit.

### Verification

I tested a normal replica:

`./eat.sh sector_C/devil_fruit_5.txt`

It reported that it was only a Marine replica.

I then tested:

`./eat.sh sector_C/devil_fruit_6.txt`

This triggered the awakening of the Gito Gito no Mi.

### Awakening Signature

`ONE_PIECE{GITO_GITO_NO_AWAKENING}`

### Conclusion

`devil_fruit_6.txt` was the genuine Devil Fruit because it had execute
permission, which was specifically checked by `eat.sh`.


## Level 2 — The Two Faces of Whiskey Peak

### Investigation

I first inspected `feast_manifest.txt`.

The initial version contained:
- Item 01: 50 Barrels of Bink's Sake
- Item 02: Roasted Sea King Meat

Using Git history, I found two commits:
- `0c60b00` — Level 2: Arrived at peaceful Whiskey Peak
- `bc5aff3` — Level 2: Implemented

Comparing the versions showed that Bink's Sake was changed to
Sleep Powder Infused Sake.

The later commit also contained a hidden vault script:
`.baroque_works_cache/unlock_vault.sh`

The script required my Level 1 awakening signature.

I exported:

`AWAKENING_SIGNATURE='ONE_PIECE{GITO_GITO_NO_AWAKENING}'`

The vault generated two files:
- `marine_intercept.log`
- `bounty_hunter_feed.log`

I compared them using:

`diff marine_intercept.log bounty_hunter_feed.log`

The difference appeared at line 42.

### Discovery

`BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}`

This was the hidden Level 2 transmission/flag.

### Approach

I used Git history to investigate the changed file, discovered the
hidden vault script, supplied the awakening signature from Level 1,
and compared the generated transmission files using `diff`.

### Review

This level taught me how Git history can contain important information
that is not present in the current working directory, and how `diff`
can reveal a small but important change between two files.

##LEVEL 3 — THE WAX LABYRINTH OF LITTLE GARDEN

### Discovery

While investigating the Wax Jungle, I found several intercepted reports and searched the sector directories for an Executive report.

The file:

"sector_beta/outpost/watchtower/storage/archive/agent_manifest.log"

contained a BAROQUE WORKS EXECUTIVE REPORT.

It also contained a "SECURITY TAG" and the first Poneglyph cipher fragment.

### Approach

The Level 2 Executive Transmission Code was:

"BAROQUE_DIAL[SPLIT_TIMELINE_MISDIRECTION]"

The Security Tag was Base64 encoded. I decoded it using:

"echo 'SECURITY_TAG' | base64 -d"

The decoded value matched the Level 2 Executive Transmission Code.

This confirmed that the report was the genuine Baroque Works Executive transmission.

### Discovery

The genuine report contained:

"PONEGLYPH_FRAGMENT_I = "KjY2MjF4bw0lKzYqNyBsIS0vbTAtJTcnL""

This is the first cipher fragment.

### Review

This level taught me how encoded identifiers can be used to identify the genuine report among many misleading files. I also learned how to recognize and decode Base64 data and verify the result against information discovered in an earlier level

## Level 4 — The Camouflaged Blueprints of Water 7

### Approach
 
- Switched to the "canonical_timeline" branch to access Water 7.
- Navigated to "GrandLine/Water_7/galley_la_company".
- Found the disguised file "puffing_tom_blueprints".
- Used the "file" command and discovered that it was actually gzip-compressed data associated with "step2_blueprints.tar".
- Extracted the archive and found "step1_blueprints.zip".
- Extracted the ZIP and found "hull-design" and "secret-link.txt".
- Investigated "hull-design/frame-specs.dat"; it contained "DECOY-DATA-01", confirming that it was a decoy.
- Inspected "secret-link.txt" and recovered the second Poneglyph fragment:

### Discovery

"PONEGLYPH_FRAGMENT_II="SwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA=""

### Review

Poneglyph Fragment II successfully recovered.

Level 5 requires the two recovered fragments to be restored together before attempting to decipher the inscription.

# Level 5 — The Buster Call Timeline Recovery

### Approach 

- Inspected the Git history using `git log --oneline --all`.
- Found the `Level 5 : Vault Sealed` commit: `d4e7bf5`.
- Investigated the later `Vaults REMOVED, Evidences ERASED` commits and walked backward through Git history.
- At commit `d4e7bf5`, confirmed that the Enies Lobby CP9 secure vault and all five vault decoder files existed.
- Inspected `.cp9_secure_vault/poneglyph.py` and discovered the decoding method:
  Base64 decoding followed by XOR with key `0x42`.
- Recovered Poneglyph Fragment I:
  `KjY2MjF4bw0lKzYqNyBsIS0vbTAtJTcnL`
- Combined it with Poneglyph Fragment II recovered in Level 4:
  `SwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA=`
- Restored the Poneglyph inscription and obtained:
  `https:-github.com/rogueone-x/Laugh-Tale-Merge-War`

## Result

Poneglyph Fragment I and Fragment II were recovered and restored using the historical decoding method.

# Level 6 — The Great Merge War at Laugh Tale

### Approach

In this level, I worked in the Laugh-Tale-Merge-War repository. First, I checked the treasure folder and found two Poneglyph fragments:
cat treasure/key_part_1.txt
which gave:
PONEGLYPH FRAGMENT α

Recovered Inscription:

Line

Then:
cat treasure/key_part_2.txt
which gave:
PONEGLYPH FRAGMENT β

Recovered Inscription:

bers

Since the task mentioned that the Poneglyphs had conflicting versions, I checked their Git history instead of relying only on the current files.
I used:
git log --all --oneline -- treasure/key_part_1.txt
and:
git log --all --oneline -- treasure/key_part_2.txt
This showed that both files had multiple versions across different commits:
8835d14  Recovered ancient history
091591f  Current pirate records
34b8f9a  Initial Laugh Tale records
I then used git show to inspect the contents of the files at those earlier commits:
git show 34b8f9a:treasure/key_part_1.txt
git show 34b8f9a:treasure/key_part_2.txt

git show 091591f:treasure/key_part_1.txt
git show 091591f:treasure/key_part_2.txt
By comparing the different historical versions, I was able to reconcile the conflicting records and recover the Pirate King's Password:
TheGrandLineRemembers
Finally, I ran:
./victory.sh
entered the password, and successfully completed Level 6.
