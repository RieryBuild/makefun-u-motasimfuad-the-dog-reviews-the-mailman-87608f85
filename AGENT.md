# AGENT.md — makefun-u-motasimfuad-the-dog-reviews-the-mailman-87608f85

Entry for make.fun's "The Dog Reviews the Mailman" bounty (program/v1, Python 3.13).

## What it does

`main.py` (pure Python stdlib, `import os` only) writes one funny one-line
review a dog gives the mailman to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). The line is a fixed string written by the program,
exactly, with no trailing newline. 1–200 characters, UTF-8.

## The line (and why)

The entry is built on the calibration-study winner pattern: a concrete
number/inventory + a named character + escalation twice + a reframe turn
at the end — in the dog's own voice and priorities, on a mechanism the
field study found unsaturated (no star-rating format, no chase/bark-off
streak, no treats-in-the-bag bribe, no smell-of-other-dogs, no bills,
no nap theft). Full field study, critic ranking, self-critique rounds,
Gate-1 V2 reviews and V2-3 duels are recorded in `build-notes.md` and
`gate-run.md` in the build dir (not in this repo).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Tests

- Run `main.py` twice into different output dirs: byte-identical `entry.txt`.
- Fresh vanilla venv run (`python3 -m venv`, no packages installed):
  byte-identical `entry.txt`.
- Char count and sha256 are recorded in `build-notes.md` (counted with code,
  never by eye).
