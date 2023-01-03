from fastapi import FastAPI, Depends
import models 
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
        
    finally:
        db.close()

#Create API to get user ID and return user points and highest points and expertise label.
@app.get('/userprofile/{id}', response_model = schemas.points_response)
def points(id, db:Session = Depends(get_db)):
    profile = db.query(models.user_profiles).filter(models.user_profiles.user_id == id).all()
    if models.user_profiles.points == 0:
        return 'Expertise Label : New'
    elif models.user_profiles.points == 1 or models.user_profiles.points >= 4999:
        return 'Expertise Label : Beginner'
    elif models.user_profiles.points == 5000 or models.user_profiles.points >= 9999:
        return 'Expertise Label : Practitioner'
    elif models.user_profiles.points == 10000 or models.user_profiles.points >= 19998:
        return 'Expertise Label : Associate'
    elif models.user_profiles.points == 19999 or models.user_profiles.points >= 34996:
        return 'Expertise Label : Professional'
    elif models.user_profiles.points == 34997  or models.user_profiles.points >= 55992:
        return 'Expertise Label :  Master '
    elif models.user_profiles.points == 55992:
        return 'Expertise Label : Guru'
    
    else:
        return 'Guru'
    return profile


#2. Create API to get user ID and return their badge groups with name, points and highest points and expertise label.

@app.get('/badge_group/{id}', response_model = schemas.badge_response)
def points(id, db:Session = Depends(get_db)):
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
    
    badge = db.query(models.badge_group).filter(models.badge_group.user_id == id).first()
    return badge
