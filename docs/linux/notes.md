# Linux Notes
## Grep for multiple strings with different logic (AND, OR, NOT)
To [grep multiple strings](https://www.thegeekstuff.com/2011/10/grep-or-and-not-operators/) with the OR, AND or NOT.

### OR Logic:
`grep -E 'pattern1|pattern2' filename`

`egrep 'pattern1|pattern2' filename`

### AND Logic:
`grep -E 'pattern1.*pattern2' filename`

`grep -E 'pattern1.*pattern2|pattern2.*pattern1' filename`
### NOT Logic:
`grep -v 'pattern1' filename`

