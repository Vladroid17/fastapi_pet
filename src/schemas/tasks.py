from pydantic import BaseModel


class TaskScema(BaseModel):
    id: int
    title: str
    author_id: int
    assignee_id: int
    
    class Config:
        from_attribures = True
        
        
class TaskSchemaAdd(BaseModel):
    title: str
    author_id: int
    assignee_id: int