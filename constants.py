import os
from chromadb.config import Settings

#Define the Chroma settings
CHROMA_SETTINGS = Settings(
    chroma_db_impl = 'duckdb+parquet',
    persist_directory = 'db',
    anonyamized_telemetry = False
)
