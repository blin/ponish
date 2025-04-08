# Editor's notes for Ponish Manual

## Differences from original

- Simplification to single-size vs double-size glyph choice is adopted: if the
  glyph in I/Y position is followed by a consonant, it is single-sized .
  - The original manual has a simple to describe but hard to implement choice:
    "if a chunk fits, glyphs can be double-sized".
  - One rule that can bring current mechanised implementation closer to the
    original is "if glyph ends in the top side of an imaginary glyph box
    (one-leg-A, E, L, P, R, U, V) it can be double-sized even if followed by a
    consonant.
- In lesson 3 the "success" example implies that the starting point of the S-S
  symbol is at the bottom of the circle. Drawing S-S from the bottom requires
  one and a half circle-strokes and one line-stroke or one circle-stroke and two
  line-strokes (one up and one down). "No wrong spelling", so I consider S-S
  starting point to be at the top of the circle.
- Only one version of "fect" and "logy" is implemented K-line/L-line second
  forms are used when affix precedes K or L, so that the combination forms a
  sine wave.

## Comments on the original

## Part 1 Lesson 1

- one leg A - ![A](./manual/alphabet/A-one-leg.svg) - can be distinguished from
  T - ![T](./manual/alphabet/T.svg) - by the direction of drawing, A is drawn
  from bottom to top, T is drawn from top to bottom.
