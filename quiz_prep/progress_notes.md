# quiz prep notes

tasks from claude (tutor), i predict the output on paper, then check.

## sat 10.10 (~4h)
- w4 notebook too much at once -> switched to tiny examples, 1 new thing each
- did: types + type(), list vs tuple, for loops, errors, / // % **
- stuck longest on for loops: thought print 1 runs for all elems, then print 2
- actually whole block runs per elem. table on paper fixed it (round/var/output)
- indentation: inside loop vs after
- 7 % 2 = 1 not 0.5 (remainder, like %% in R)
- 8 / 2 = 4.0, / always float
- type("True") is str, quotes = str

## sun 11.10 (~2.5h)
- warm up from memory: forgot dict, int("250"), print(a, b) has no comma
- topic 1 mutability, code in t1_mutability_uebungen.py
- s.upper() doesnt change s, need s = s.upper() (same as R)
- b = a is no copy, b = a.copy() is. == content, is same object
- append/sort change the list and return None, confused me at first
- sorted() makes new list. kept adding later appends to it, 3 tries
- single steps ok, mixed tasks bad (1/4 first try). table per name helps
- output: forgot [ ] on lists, wrote comma in print(a, b)

## sun 11.10 afternoon (~1.5h)
- review ok: sorted() before append right. but 7 // 2 = 3 not 3.0, // stays int
- topic 2, code in t2_slicing_dict_uebungen.py
- index from 0, [-1] last. slice [1:4] stop not included
- nums[2] = element, nums[2:3] = list with 1 elem. mixed this up 2x
- output: str alone has no quotes, quotes only inside [ ]. wrong 4x
- fruit[1] vs fruits[1] in loop: lost, writing out each round helped
- dict, nested dict, .get(k, 0), KeyError: went ok
- mix t1 + t2 (alias + slice + dict) wrong 2x, skipped the table again

## todo
- redo alias vs slice (only bare name is alias), with table
- conditionals, functions/range, write code by hand
