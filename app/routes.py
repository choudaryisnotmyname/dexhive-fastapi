from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.database import get_db
from app.models import *
from app.schemas import *
from app.settings import PUBLIC, PRIVATE, MIDDLE

router = APIRouter()

@router.post("/tenants", response_model=Tenant)
async def create_tenant(tenant: TenantCreate, db: AsyncSession = Depends(get_db)):
    db_tenant = Tenant(**tenant.model_dump())
    db.add(db_tenant)
    await db.commit()
    await db.refresh(db_tenant)
    return db_tenant

@router.get("/tenants", response_model=List[Tenant])
async def get_tenants(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tenant))
    return result.scalars().all()

@router.post("/entities", response_model=Entity)
async def create_entity(entity: EntityCreate, db: AsyncSession = Depends(get_db)):
    db_entity = Entity(**entity.model_dump())
    db.add(db_entity)
    await db.commit()
    await db.refresh(db_entity)
    return db_entity

@router.get("/entities", response_model=List[Entity])
async def get_entities(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Entity))
    return result.scalars().all()

@router.post("/subjects", response_model=Subject)
async def create_subject(subject: SubjectCreate, db: AsyncSession = Depends(get_db)):
    db_subject = Subject(**subject.model_dump())
    db.add(db_subject)
    await db.commit()
    await db.refresh(db_subject)
    return db_subject

@router.get("/subjects", response_model=List[Subject])
async def get_subjects(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Subject))
    return result.scalars().all()

@router.post("/files", response_model=File)
async def create_file(file: FileCreate, db: AsyncSession = Depends(get_db)):
    db_file = File(**file.model_dump())
    db.add(db_file)
    await db.commit()
    await db.refresh(db_file)
    return db_file

@router.get("/files", response_model=List[File])
async def get_files(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(File))
    return result.scalars().all()

@router.post("/tags", response_model=Tag)
async def create_tag(tag: TagCreate, db: AsyncSession = Depends(get_db)):
    db_tag = Tag(**tag.model_dump())
    db.add(db_tag)
    await db.commit()
    await db.refresh(db_tag)
    return db_tag

@router.get("/tags", response_model=List[Tag])
async def get_tags(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tag))
    return result.scalars().all()

@router.post("/file-tags", response_model=FileTag)
async def create_file_tag(file_tag: FileTagCreate, db: AsyncSession = Depends(get_db)):
    db_file_tag = FileTag(**file_tag.model_dump())
    db.add(db_file_tag)
    await db.commit()
    await db.refresh(db_file_tag)
    return db_file_tag

@router.get("/file-tags", response_model=List[FileTag])
async def get_file_tags(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(FileTag))
    return result.scalars().all()

@router.post("/entity-admins", response_model=EntityAdmin)
async def create_entity_admin(entity_id: int, user_id: int, subject_id: int, db: AsyncSession = Depends(get_db)):
    db_admin = EntityAdmin(entity_id=entity_id, user_id=user_id, subject_id=subject_id)
    db.add(db_admin)
    await db.commit()
    await db.refresh(db_admin)
    return db_admin

@router.get("/entity-admins", response_model=List[EntityAdmin])
async def get_entity_admins(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(EntityAdmin))
    return result.scalars().all()

@router.post("/owners", response_model=Owner)
async def create_owner(entity_id: int, user_id: int, subject_id: int, db: AsyncSession = Depends(get_db)):
    db_owner = Owner(entity_id=entity_id, user_id=user_id, subject_id=subject_id)
    db.add(db_owner)
    await db.commit()
    await db.refresh(db_owner)
    return db_owner

@router.get("/owners", response_model=List[Owner])
async def get_owners(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Owner))
    return result.scalars().all()

@router.post("/practitioners", response_model=Practitioner)
async def create_practitioner(entity_id: int, user_id: int, subject_id: int, db: AsyncSession = Depends(get_db)):
    db_pract = Practitioner(entity_id=entity_id, user_id=user_id, subject_id=subject_id)
    db.add(db_pract)
    await db.commit()
    await db.refresh(db_pract)
    return db_pract

@router.get("/practitioners", response_model=List[Practitioner])
async def get_practitioners(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Practitioner))
    return result.scalars().all()

@router.post("/smes", response_model=SME)
async def create_sme(entity_id: int, user_id: int, subject_id: int, db: AsyncSession = Depends(get_db)):
    db_sme = SME(entity_id=entity_id, user_id=user_id, subject_id=subject_id)
    db.add(db_sme)
    await db.commit()
    await db.refresh(db_sme)
    return db_sme

@router.get("/smes", response_model=List[SME])
async def get_smes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(SME))
    return result.scalars().all() 