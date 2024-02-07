from pydantic import BaseModel, ConfigDict

class UrlCreate(BaseModel):
    base_url: str


class Url(UrlCreate):
    model_config = ConfigDict(from_attributes=True)
    shortened_url: str 
