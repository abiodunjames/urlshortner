from pydantic import AnyUrl, BaseModel, ValidationError


class Url(BaseModel):
    id: str
    shorten_url:  str
    original_url: str
    hit : int = 0

class UrlInput(BaseModel):
    url: AnyUrl


class UrlOutput(BaseModel):
    shorten_url: str
    original_url: AnyUrl
