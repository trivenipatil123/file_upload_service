from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, file_processing, schemas
import os

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid image format")

    file_data = await file.read()
    file_path = f"uploaded_images/{file.filename}"
    processed_file_path = file_processing.process_image(file_data, file_path)

    file_metadata = schemas.FileMetadataCreate(
        filename=file.filename,
        file_type=file.content_type,
        file_path=processed_file_path,
        upload_time=schemas.datetime.utcnow()
    )

    db_file = crud.create_file_metadata(db, file_metadata)
    return {"filename": db_file.filename, "file_path": db_file.file_path}


@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Invalid CSV file format")

    file_data = await file.read()
    processed_data = file_processing.process_csv(file_data)

    return {"data": processed_data}
