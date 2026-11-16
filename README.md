# tiny-chess-01

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/tiny-chess-01)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A chess engine in at most 4,096 bytes of Python, built for the
[make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01):
write the strongest chess engine you can in 4 KB of Python and play it
against a gauntlet of eight house engines.

## Engine

`main.py` is the whole engine: a 0x88 board, full legal move generation
(castling, en passant, promotion), negamax alpha-beta with iterative
deepening to a fixed 100,000-node budget, quiescence search (captures and
promotions, with check evasions), a transposition table, MVV-LVA move
ordering, null-move pruning, and a formula piece-square-table evaluation
with tapered king safety (pawn shield) and bishop-pair bonus. No clock,
no randomness: the same position always gets the same move, so replays
match.

It talks to the trial env at `MAKEFUN_ENV_URL` (`POST /game`, `/move`),
plays in UCI, and never calls a model or any other service.

The source is packed as an LZMA payload with its unpacker (allowed by
the rules; the payload and unpacker together are under 4,096 bytes) —
the unpacked source is the engine above, nothing else.

## Build

`main.py` is produced from the working source by LZMA + base85 packing.
Verified with perft (all 5 standard positions to depth 3–4), mate-in-1/2
tests, and local practice trials against the kit's own env server
(best: Elo 1364 on the 6-game practice gauntlet, vs ~1365 for the
house sunfish baseline).

## License

MIT. See [LICENSE](LICENSE).

---
Built for the make.fun bounty — [try make.fun](https://make.fun/r/vky0ybyt)
