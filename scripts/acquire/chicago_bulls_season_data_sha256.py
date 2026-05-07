from pathlib import Path
import hashlib
import os


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "bulls_data.csv"
CHECKSUM_PATH = PROJECT_ROOT / "data" / "raw" / "bulls_data.sha256"


def compute_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def write_checksum(data_path, checksum_path):
    checksum = compute_sha256(data_path)
    with open(checksum_path, "w") as f:
        f.write(f"{checksum}  {os.path.basename(data_path)}\n")

    print("Checksum saved to:", checksum_path)
    print("SHA-256:", checksum)


def main():
    write_checksum(DATA_PATH, CHECKSUM_PATH)


if __name__ == "__main__":
    main()
