

# Internal Cell

from pydantic import BaseSettings,Field
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

# Internal Cell

from pydantic import BaseSettings,Field
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

# Internal Cell

from pydantic import BaseSettings,Field
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

# Internal Cell

class PlayResult(ModelWithEventType):
    type: str
    event: str
    eventType: EventType
    description: str
    rbi: conint(ge=0)
    awayScore: conint(ge=0)
    homeScore: conint(ge=0)


# Internal Cell

class HalfInning(str,Enum):
    top='top'
    bottom='bottom'

class PlayAbout(BaseModel):
    atBatIndex: conint(ge=0)
    halfInning: HalfInning
    inning: conint(ge=0)
    startTime: dt.datetime
    endTime: dt.datetime
    isComplete: bool
    isScoringPlay: bool
    hasReview: bool
    hasOut: bool
    captivatingIndex: int

# Internal Cell

class Count(BaseModel):
    balls: conint(ge=0,le=4)
    strikes: conint(ge=0,le=3)
    outs: conint(ge=0,le=3)

# Internal Cell

class MenOnBase(str,Enum):
    Empty='Empty'
    Men_On='Men_On'
    RISP='RISP'

class BatterSplit(str,Enum):
    vs_RHP='vs_RHP'
    vs_LHP='vs_LHP'
class PitcherSplit(str,Enum):
    vs_RHB='vs_RHB'
    vs_LHB='vs_LHB'
class Splits(BaseModel):
    batter: BatterSplit
    pitcher: PitcherSplit
    menOnBase: MenOnBase

# Internal Cell

class Matchup(BaseModel):
    batter: PersonBase
    batSide: PlayerHandedness
    pitcher: PersonBase
    pitchHand: PlayerHandedness
    batterHotColdZones: conlist(Any,max_items=0) # I want to see if this ever comes back with items
    pitcherHotColdZones: conlist(Any,max_items=0)
    splits: Splits