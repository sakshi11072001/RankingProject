from pydantic import BaseModel

class user_profiles(BaseModel):
    user_id : int
    points : float
    highest_points : float
    created_at : float
    updated_at : float
    deleted_at : float
    
    
class badge_group(BaseModel):
    id_a : int 
    badge_group_name : str
    user_id : int
    points : float
    highest_points : float
    created_at : float
    updated_at : float
    deleted_at : float    
    
    
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
    

class points_response(BaseModel):
    points : float
    highest_points : float
    
    class Config():
        orm_mode = True
        
class badge_response(BaseModel):
    badge_group_name : str
    highest_points : float
    
    class Config():
        orm_mode = True
