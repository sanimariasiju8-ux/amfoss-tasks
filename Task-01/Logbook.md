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

### Screenshots

- Screenshot of the Devil Fruit files
- Screenshot showing the permission comparison
- Screenshot of the `eat.sh` script
- Screenshot showing the awakening signature
