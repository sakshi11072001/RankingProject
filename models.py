from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP, VARCHAR, BOOLEAN
from sqlalchemy.orm import relationship

class user_profiles(Base):
    __tablename__ = 'user_profiles'
    user_id = Column(Integer, primary_key = True)
    points = Column(Float)
    highest_points = Column(Float)
    created_at = Column(Float)
    updated_at = Column(Float)
    deleted_at = Column(Float)


class badge_group(Base):
    __tablename__ = 'badge_group'
    id_a = Column(Integer, primary_key = True)
    badge_group_name = Column(String)
    user_id = Column(Integer, ForeignKey(user_profiles.user_id))
    points = Column(Float)
    highest_points = Column(Float)
    created_at = Column(Float)
    updated_at = Column(Float)
    deleted_at = Column(Float)  
    
    
class badges(Base):
    __tablename__ = 'badges'
    id_a = Column(Integer, primary_key = True)
    points = Column(Float)
    highest_points = Column(Float)
    badge_name = Column(String)  
    badge_group_id = Column(Integer, ForeignKey(user_profiles.user_id))
    reference_id = Column(String)
    reference_type = Column(String)
    enabled = Column(String)
    created_at = Column(Float)
    updated_at = Column(Float)
    deleted_at = Column(Float)