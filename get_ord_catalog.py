from pathlib import Path
import csv
import requests
from ord_schema import datasets


HF_API = (
    "https://huggingface.co/api/datasets/"
    "open-reaction-database/ord-data/tree/main"
)

OUTPUT = "ord_dataset_catalog.csv"
RAW_DATA_VOLUME = Path("/Volumes/chemdata/raw/raw_data")


def list_files(path="data", recursive=True):
    """List files in the ORD Hugging Face repository."""
    params = {
        "path": path,
        "recursive": str(recursive).lower(),
        "expand": "false",
    }

    r = requests.get(HF_API, params=params)
    r.raise_for_status()

    return r.json()


def download_file(repo_path):
    """Download one Parquet file."""
    url = (
        "https://huggingface.co/datasets/"
        "open-reaction-database/ord-data/resolve/main/"
        + repo_path
    )

    local_path = RAW_DATA_VOLUME / Path(repo_path).name

    if not local_path.exists():
        print(f"Downloading {repo_path}")
        r = requests.get(url, stream=True)
        r.raise_for_status()

        with open(local_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

    return local_path


def main():
    RAW_DATA_VOLUME.mkdir(exist_ok=True)

    files = list_files()

    parquet_files = [
        x["path"]
        for x in files
        if x["type"] == "file"
        and x["path"].endswith(".parquet")
    ]

    print(f"Found {len(parquet_files)} Parquet datasets")

    rows = []

    for i, repo_path in enumerate(parquet_files, 1):
        print(f"[{i}/{len(parquet_files)}] {repo_path}")

        local_path = download_file(repo_path)

        # IMPORTANT:
        # load_dataset() returns a DatasetView for Parquet.
        # It reads metadata/footer without materializing reactions.
        dataset = datasets.load_dataset(local_path)

        rows.append({
            "dataset_id": dataset.dataset_id,
            "name": dataset.name,
            "description": dataset.description,
            "reaction_count": len(dataset.reactions),
            "file": repo_path,
        })

    rows.sort(key=lambda x: x["dataset_id"])

    with open(
        OUTPUT,
        "w",
        newline="",
        encoding="utf-8",
    ) as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "dataset_id",
                "name",
                "description",
                "reaction_count",
                "file",
            ],
        )

        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote {len(rows)} datasets to {OUTPUT}")


if __name__ == "__main__":
    main()