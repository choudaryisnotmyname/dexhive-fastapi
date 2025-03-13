from sqlalchemy import (
    Column, Integer, String, Boolean, Date, DateTime, func, ForeignKey
)
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    entity_id = Column(Integer, ForeignKey("entities.id"))
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Entity(Base):
    __tablename__ = "entities"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    entity_name = Column(String(255), nullable=False)
    domain_name = Column(String(255))
    subdomain = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True)
    tenant_name = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, ForeignKey("entities.id"), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    date_of_birth = Column(Date)
    contact_info = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, ForeignKey("entities.id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_type = Column(String(255))
    file_url = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class FileTag(Base):
    __tablename__ = "file_tags"
    file_id = Column(Integer, ForeignKey("files.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)

class EntityAdmin(Base):
    __tablename__ = "entity_admins"
    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, ForeignKey("entities.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, ForeignKey("entities.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Practitioner(Base):
    __tablename__ = "practitioners"
    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, ForeignKey("entities.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SME(Base):
    __tablename__ = "smes"
    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, ForeignKey("entities.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
