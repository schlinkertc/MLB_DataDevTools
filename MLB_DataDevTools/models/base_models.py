# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_models.base_models.ipynb (unless otherwise specified).

__all__ = ['MLBEndpointBase', 'MLBEndpointReference', 'CustomInt', 'PositionBase', 'PlayerHandedness', 'PersonBase',
           'MLBPerson', 'Coordinates', 'TimeZone', 'VenueLocation', 'TurfType', 'RoofType', 'FieldInfo']

# Internal Cell

from pydantic import (
    BaseModel,
    HttpUrl,
    validator,
    constr
)
from enum import Enum
from typing import Optional

# Cell

class MLBEndpointBase(BaseModel):

    link: HttpUrl

    @validator('link',pre=True)
    def add_base_url_to_link(cls,link):
        return 'https://statsapi.mlb.com'+link

class MLBEndpointReference(MLBEndpointBase):
    id: int
    name: Optional[str]=None

# Cell

class CustomInt(str):

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate


    @classmethod
    def validate(cls, v):
        if v == '-':
            return None
        else:
            return int(v)

# Cell

class PositionBase(BaseModel):
    code: str
    name: str
    type: str
    abbreviation: str

class PlayerHandedness(BaseModel):
    code: constr(max_length=1)
    description: str

# Cell

class PersonBase(MLBEndpointReference):

    class Config:
        fields = {
            'name':{
                'alias':'fullName'
            }
        }

class MLBPerson(PersonBase):
    firstName: str
    lastName: str

    height: str
    weight: int
    Optiactive: bool
    primaryPosition: PositionBase
    useName: str

    boxscoreName: str
    gender: str
    isPlayer: bool
    isVerified: bool

    nameSlug: str




# Cell

class Coordinates(BaseModel):
    latitude: float
    longitude: float

class TimeZone(BaseModel):
    id: str
    offset: int
    tz: str

class VenueLocation(BaseModel):
    city: str
    state: str
    stateAbbrev: str
    defaultCoordinates: Coordinates

# Cell

class TurfType(str,Enum):
    Grass = 'Grass'
    Artificial = 'Artificial'
class RoofType(str,Enum):
    Open = 'Open'
    Dome = 'Dome'
    Retractable = 'Retractable'

class FieldInfo(BaseModel):
    capacity: int
    turfType: TurfType
    roofType: RoofType
    leftLine: int
    leftCenter: int
    center: int
    rightCenter: int
    rightLine: int

# Internal Cell

class AbstractGameState(str,Enum):
    Final = 'Final'
    Live = 'Live'
    Other = 'Other'
    Preview = 'Preview'
class AbstractGameCode(str,Enum):
    F='F'
    L='L'
    O='O'
    P='P'

# Internal Cell

class GameType(str,Enum):
    spring_training = 'S'
    regular_season = 'R'
    wild_card_game = 'F'
    division_series = 'D'
    league_championship_series = 'L'
    world_series = 'W'
    championship = 'C'
    nineteenth_centure_series = 'N'
    playoffs = 'P'
    all_star_game = 'A'
    intrasquad = 'I'
    exhibition = 'E'



# Internal Cell

class GamedayType(str,Enum):
    box_score_only = 'B'
    pitch_by_pitch = 'D'
    enhanced = 'E'
    linescore_only = 'L'
    play_by_play = 'N'
    premium = 'P'
    score_only = 'S'
    regular = 'Y'