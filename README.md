# Password-Profiler Generator

Password-Profiler Generator loads user input to make all possible combinations

create a text file containing a user information like -> Name, last, ID, PhoneNumber, birthdate, any info you have on target


# Usage 

```
usage: Password-Profiler.py [-h] --input INPUT --perm PERM --min MIN --max MAX [--test TEST] [--cores CORES] [--leet] [--cap] [--up] [--append APPEND] [--prepend PREPEND]
                            [--getchar GETCHAR]

A simple wordlist generator and mangler written in python.

options:
  -h, --help         show this help message and exit
  --test TEST        Output first N iterations (single process/core)
  --cores CORES      Manually specify processes/cores pool that you want to use
  --leet             Activate l33t mutagen EXAMPLE==> P@ssw0rd
  --cap              Activate capitalize first Letter of a word
  --up               Activate uppercase words
  --append APPEND    Append chosen word (append 'word' to all passwords)
  --prepend PREPEND  Prepend chosen word (prepend 'word' to all passwords)
  --getchar GETCHAR  Extract a substring from words at the specified index to append

required arguments:
  --input INPUT      Input file name
  --perm PERM        Max number of words to be combined on the same line
  --min MIN          Minimum generated password length
  --max MAX          Maximum generated password length

```
