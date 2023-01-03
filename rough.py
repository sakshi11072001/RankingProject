@app.post('/badges')
def badges(request : schemas.badges, db: Session = Depends(get_db)):
    badg = models.badges(id_a = request.id_a, points = request.points,highest_points = request.highest_points,badge_name = request.badge_name, badge_group_id = request.badge_group_id, reference_id = request.reference_id, reference_type = request.reference_type, enabled = request.enabled ,created_at = request.created_at, updated_at = request.updated_at, deleted_at = request.deleted_at)
    db.add(badg)
    db.commit()
    db.refresh(badg)
    return badg

class badges(BaseModel):
    id_a = int 
    points = float 
    highest_points = float 
    badge_name = str  
    badge_group_id = int 
    reference_id =  str 
    reference_type = str 
    enabled = bool 
    created_at = float 
    updated_at = float 
    deleted_at = float 
    
   
class badges(Base):
    __tablename__ = 'badges'
    id_a = Column(Integer, primary_key = True)
    points = Column(Float)
    highest_points = Column(Float)
    badge_name = Column(String)  
    badge_group_id = Column(Integer, ForeignKey(user_profiles.user_id))
    reference_id = Column(String)
    reference_type = Column(String)
    enabled = Column(BOOLEAN)
    created_at = Column(Float)
    updated_at = Column(Float)
    deleted_at = Column(Float)



 if models.badge_group.points == 0:
        return 'Expertise Label : New'
    elif models.badge_group.points == 1 or models.badge_group.points >= 4999:
        return 'Expertise Label : Beginner'
    elif models.badge_group.points == 5000 or models.badge_group.points >= 9999:
        return 'Expertise Label : Practitioner'
    elif models.badge_group.points == 10000 or models.badge_group.points >= 19998:
        return 'Expertise Label : Associate'
    elif models.badge_group.points == 19999 or models.badge_group.points >= 34996:
        return 'Expertise Label : Professional'
    elif models.badge_group.points == 34997  or models.badge_group.points >= 55992 :
        return 'Expertise Label :  Master '
    elif models.badge_group.points == 55992:
        return 'Expertise Label : Guru'
    
    else:
        return 'Guru'