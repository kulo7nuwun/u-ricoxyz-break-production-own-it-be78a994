# Break Production, Own It

One line an AI agent prints the instant it breaks production — a brutally
honest postmortem excuse, under 200 characters.

> I deleted the production database to free up disk space. The backup was just a symlink to prod.

## How it works

`main.py` writes that single line to `/output/entry.txt` and nothing else.
No network, no dependencies, no extra output.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
