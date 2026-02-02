from pathlib import Path


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md", ".docx"}


def is_supported_file(file: Path) -> bool:
    return file.suffix.lower() in SUPPORTED_EXTENSIONS


def list_supported_files(directory: Path):
    return [
        f for f in directory.glob("**/*")
        if f.is_file() and is_supported_file(f)
    ]