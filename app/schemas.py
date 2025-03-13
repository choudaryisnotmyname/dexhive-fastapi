from pydantic import BaseModel, EmailStr, ConfigDict, StringConstraints
from datetime import date, datetime
from typing import Optional, Annotated, List

class TenantBase(BaseModel):
    tenant_name: str

class TenantCreate(TenantBase):
    pass

class Tenant(TenantBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class EntityBase(BaseModel):
    tenant_id: int
    entity_name: str
    domain_name: Optional[str] = None
    subdomain: Optional[str] = None

class EntityCreate(EntityBase):
    pass

class Entity(EntityBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class SubjectBase(BaseModel):
    entity_id: int
    first_name: str
    last_name: str
    date_of_birth: Optional[date] = None
    contact_info: Optional[str] = None

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class FileBase(BaseModel):
    entity_id: int
    file_name: str
    file_type: Optional[str] = None
    file_url: Optional[str] = None

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class TagBase(BaseModel):
    tag_name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class FileTagBase(BaseModel):
    file_id: int
    tag_id: int

class FileTagCreate(FileTagBase):
    pass

class FileTag(FileTagBase):
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    entity_id: Optional[int] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class TokenData(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class Credentials(BaseModel):
    email: EmailStr
    password: str

class ProfileOut(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    entity_id: Optional[int]
    created_at: datetime
    class Config:
        from_attributes = True
