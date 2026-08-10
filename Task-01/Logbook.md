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
