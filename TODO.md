# TODO

- Alphabet drawing with stroke direction arrows
  - Needed in the beginning of lesson 1, but is also generally nice
- Phonetic writing
- Compute `start_pos` from shape
- Prevent glyph chunk overlap, like in "jest" is "suggestive"
- Lesson 1
  - Add "side by side" views for examples
- Lesson 2
  - Update last 3 examples before passage to not do within-line splits
  - Update "side by side" views to have same width
- Lesson 3
  - Add "side by side" views for examples
- Implement "if a chunk fits, glyphs can be double-sized" rule.
  - Implement "if glyph ends in the top side of an imaginary glyph box" as a
    stop-gap solution
- Quotes, like in "aww, thank you!"
- Brackets, like around Bellerophon
- Do "X-from-left" automatically in cases like "NX"
- Do "TH-top-start" or "TH-left-start" automatically in cases like "forth"
- Make `M$(PL)` look better. Currently the circle in `$(PL)` goes below "M"` it
  should go above "M".
- Make `$(AP)` look better. Currently the circle in `$(AP)` goes to the left of
  "A", it should go to the right of "A".
- Make `$(other)$(THING)`
- Implement both "L-line" and "K-line" for "fect" and "super" and choose the
  right one automatically
- Implement numbers in circles
- Add a "quote mode" for spelling names, abbreviations and the like
- Fix chunking for "our"
