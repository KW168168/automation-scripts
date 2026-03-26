from pathlib import Path


def batch_rename(folder: str, prefix: str = "file") -> None:
    path = Path(folder)
    if not path.exists() or not path.is_dir():
        raise ValueError(f"Invalid folder: {folder}")

    for index, item in enumerate(sorted(path.iterdir()), start=1):
        if item.is_file():
            new_name = f"{prefix}_{index:03d}{item.suffix}"
            target = item.with_name(new_name)
            item.rename(target)
            print(f"Renamed: {item.name} -> {target.name}")


if __name__ == "__main__":
    folder = input("Folder path: ").strip()
    prefix = input("Prefix (default=file): ").strip() or "file"
    batch_rename(folder, prefix)
