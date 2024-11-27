from pydantic import BaseModel
from datetime import datetime


class FileMetadataBase(BaseModel):
    filename: str
    file_type: str
    upload_time: datetime
    file_path: str


class FileMetadataCreate(FileMetadataBase):
    pass


class FileMetadata(FileMetadataBase):
    id: int

    class Config:
        orm_mode = True
