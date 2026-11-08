set dotenv-load := true

[default]
_default:
    @just --list

# Generate requirements
[group('dev')]
export:
    uv export -o requirements.txt --all-extras --no-dev --no-hashes --no-editable
    uv export -o dev_reqirements.txt --all-extras --no-hashes

# Format the code
[group('dev')]
format:
    uv run ruff format
    uv run ruff check --fix

# Check formatting and typing
[group('dev')]
check:
    uv run ruff format --check
    uv run ruff check
    uv run pyright

# Run tests
[group('dev')]
test:
    uv run pytest

# Run the app (change command to yours)
[group('main')]
run:
    uv run housemaid
