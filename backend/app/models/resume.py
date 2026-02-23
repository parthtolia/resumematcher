from sqlalchemy import Column, Text, Numeric, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from pgvector.sqlalchemy import Vector
import uuid

Base = declarative_base()

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    file_name = Column(Text, nullable=False)
    file_path = Column(Text, nullable=False)

    full_text = Column(Text, nullable=False)

    skills = Column(Text)
    total_experience = Column(Numeric(4, 2))
    education_level = Column(Text)

    embedding = Column(Vector(384))

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())