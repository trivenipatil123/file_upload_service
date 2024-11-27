from sqlalchemy.orm import Session
from app.models import FileMetadata
from app.schemas import FileMetadataCreate


def create_file_metadata(db: Session, file_metadata: FileMetadataCreate):
    db_file_metadata = FileMetadata(**file_metadata.dict())
    db.add(db_file_metadata)
    db.commit()
    db.refresh(db_file_metadata)
    return db_file_metadata
