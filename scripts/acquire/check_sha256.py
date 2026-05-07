from pathlib import Path
import hashlib


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CHECKS = [
    (
        PROJECT_ROOT / "data" / "raw" / "chicago_draft_data.csv",
        PROJECT_ROOT / "data" / "raw" / "chicago_draft_data.sha256",
    ),
    (
        PROJECT_ROOT / "data" / "raw" / "bulls_data.csv",
        PROJECT_ROOT / "data" / "raw" / "bulls_data.sha256",
    ),
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def read_expected(checksum_file):
    with open(checksum_file, "r") as f:
        line = f.readline().strip()
    return line.split()[0]


def verify(data_path, checksum_path):
    actual = sha256(data_path)
    expected = read_expected(checksum_path)

    print(f"Checking: {data_path}")
    # print(f"Expected: {expected}")
    # print(f"Actual:   {actual}")

    if actual == expected:
        print("MATCH - file is correct.\n")
        return True

    print("MISMATCH - file was modified or corrupted.\n")
    return False


def main():
    all_matched = True

    for data_path, checksum_path in DEFAULT_CHECKS:
        all_matched = verify(data_path, checksum_path) and all_matched

    if not all_matched:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
