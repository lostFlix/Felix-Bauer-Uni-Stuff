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

## mon 12.10
- brain dump t0-t2 on paper, reading = clicks, recalling = not
- alias vs slice control task right 1st try
- t3: if/elif first hit, multiple if = separate chains, code in t3_conditionals_uebungen.py
- truthiness: "False" truthy, [0] truthy, 0 falsy (got 0 wrong 1x)
- or returns a value: "" or "Nudeln" -> Nudeln

## tue 13.10
- t4: def, print vs return (no return -> None), range, accumulator, code in t4_functions_uebungen.py
- default arg by=1, x only changes where x = stands
- ternary: middle first, middle never printed
- increment task (quiz recap) totally wrong w/o table
- mal variant: applied condition to return value, printed bool
- after ~2h45 mix tasks drop off

## wed 14.10
- ternary check: logic right, mapped to wrong i (4 10 4 vs 10 4 10)
- t4: param = alias of arg, items.append changes caller list, items = [] doesn't
- add_city/reset_cities, rein/weg, tausch mostly right after 2 rules
- filter fn blueprint: result list before loop, return after loop
- review t0-t3: t0 clean, t2/t3 mix weaker (dict key vs value, .get default, elif first hit)
- still mixing up what happens vs what's returned (.append/.sort -> None, sorted -> new list)
- [ ] missing on slice/list results, 7x now

## todo
- k1/k2 (.get with 0 + or, two if chains), write nur_gerade myself, mock quiz
