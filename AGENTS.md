# py-box — agent instructions

## Entrypoints

- **WSGI server:** `python srv.py` (port 8000); uses `main.py` which imports `data` from `str_methods.py`
- **Package demo:** `python packages/main.py` (run from repo root)

Run both from repo root.

## Packages demo structure

`packages/` is an educational sample of Python packages, not a monorepo:

- `sp/` and `drill/` are subpackages using relative imports (`from .const import ...`)
- Must be run from repo root so Python resolves `packages` as a top-level package

## Fragile import chain in root

`main.py` ← `str_methods.py` ← `str_slices.py` (wildcard import `*`). Moving or renaming these files breaks the server.

## Dockerfile

Located at `packages/dockerfile` (not repo root). Build with:

```
docker build -f packages/dockerfile .
```

## Tooling

No linters, formatters, tests, or CI config. No pre-commit hooks. Python 3.13.5, venv in `venv/`.
