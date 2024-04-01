from dataclasses import dataclass
from pathlib import Path


#create custom Return type
@dataclass(frozen=True)
class DataIngestionConfig:
    """
    represent the configuration required for data ingestion tasks
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path