# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/elpablo61/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/elpablo61/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A chess engine in at most 4,096 bytes of Python, built for the
[make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01):
write the strongest chess engine you can in 4 KB of Python and play it
against a gauntlet of eight house engines.

## Engine

`main.py` is the whole engine: a 0x88 board, full legal move generation
(castling, en passant, promotion), negamax PVS with iterative deepening
to a fixed 100,000-node budget, aspiration windows at the root,
quiescence search (captures, promotions, and check evasions), a
transposition table, MVV-LVA + killer + history move ordering,
null-move pruning, LMR, mate-distance scoring, and a tapered PeSTO
evaluation (two piece-square tables per piece, phase-interpolated from
remaining material). No clock, no randomness: the same position always
gets the same move, so replays match.

It talks to the trial env at `MAKEFUN_ENV_URL` (`POST /game`, `/move`),
plays in UCI, and never calls a model or any other service.

The source is packed as an LZMA payload with its unpacker (allowed by
the rules; the payload and unpacker together are under 4,096 bytes) —
the unpacked source is the engine above, nothing else.

## Build

`main.py` is produced from the working source by the official kit
(`makefun compress engine_src.py --out main.py` — stub makefun-compress/v1
+ LZMA).
Verified with perft (6 standard positions to depth 3), a mate-in-1 test,
self-play, and local practice trials against the kit's own env server:
trial-0 Elo 2112 (the scorer cap), 6W/0D/0L, reproduced move-identically
on a re-run; trial-1 and trial-2 Elo 1364 each, 3W/1D/2L; 3-trial
average Elo 1613 (v1 scored 1364 on trial-0).

## License

MIT. See [LICENSE](LICENSE).

---
Built for the make.fun bounty — [try make.fun](https://make.fun/r/vky0ybyt)
