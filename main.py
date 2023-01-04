from fastapi import FastAPI, Depends
import models 
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import json

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
    if profile.points == 0:
        return 'Expertise Label : New'
    elif profile.points == 1 or profile.points >= 4999:
        return 'Expertise Label : Beginner'
    elif profile.points == 5000 or profile.points >= 9999:
        return 'Expertise Label : Practitioner'
    elif profile.points == 10000 or profile.points >= 19998:
        return 'Expertise Label : Associate'
    elif profile.points == 19999 or profile.points >= 34996:
        return 'Expertise Label : Professional'
    elif profile.points == 34997  or profile.points >= 55992:
        return 'Expertise Label :  Master '
    elif profile.point == 55992:
        return 'Expertise Label : Guru'
    
    else:
        return 'Guru'
    
    value = {"points" : profile.points, 
             "highest points" : profile.highest_points}
    return json.dumps(value)

#2. Create API to get user ID and return their badge groups with name, points and highest points and expertise label.

@app.get('/badge_group/{id}', response_model = schemas.badge_response)
def points(id, db:Session = Depends(get_db)):
    badge = db.query(models.badge_group).filter(models.badge_group.user_id == id).all()
    
    if badge.points == 0:
        return 'Expertise Label : New'
    elif badge.points == 1 or badge.points >= 4999:
        return 'Expertise Label : Beginner'
    elif badge.points == 5000 or badge.points >= 9999:
        return 'Expertise Label : Practitioner'
    elif badge.points == 10000 or badge.points >= 19998:
        return 'Expertise Label : Associate'
    elif badge.points == 19999 or badge.points >= 34996:
        return 'Expertise Label : Professional'
    elif badge.points == 34997  or badge.points >= 55992 :
        return 'Expertise Label :  Master '
    elif badge.points == 55992:
        return 'Expertise Label : Guru'
    
    else:
        return 'Guru'
    
    
    value = {"badge_groups_name":badge. badge_group_name,
             "points" :badge.points, 
             "highest points":badge.highest_points, 
             }
    return json.dumps(value)

#3.Create API to get user ID and return number of badges earned in each badge groups and count of total badges.
@app.get('/badge_group/{id}')
def no_of_badges(id, db:Session = Depends(get_db)):
    badge = db.query(models.badge_group).filter(models.badge_group.user_id == id).all()
    # number of badges earned in each badge groups
    d = dict()
    for i in badge.badge_group_name:
        if ( i in d):
            d[i] = d[i] + 1
        else:
            d[i] = 1
        for key in list(d.keys()):
            return { key + " : "+ d[key]}
    
    # count of total badges
    sum = 0
    for i in d.keys():
        sum = sum + i
 
    return sum
