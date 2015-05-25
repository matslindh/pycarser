"""
    This file is generated by running bin/generate_classes.py and should not be edited manually.
"""
import ctypes

SHARED_MEMORY_VERSION = 5

STRING_LENGTH_MAX = 64

STORED_PARTICIPANTS_MAX = 64

TYRE_FRONT_LEFT = 0
TYRE_FRONT_RIGHT = 1
TYRE_REAR_LEFT = 2
TYRE_REAR_RIGHT = 3
TYRE_MAX = 4

VEC_X = 0
VEC_Y = 1
VEC_Z = 2
VEC_MAX = 3

GAME_EXITED = 0
GAME_FRONT_END = 1
GAME_INGAME_PLAYING = 2
GAME_INGAME_PAUSED = 3
GAME_MAX = 4

SESSION_INVALID = 0
SESSION_PRACTICE = 1
SESSION_TEST = 2
SESSION_QUALIFY = 3
SESSION_FORMATION_LAP = 4
SESSION_RACE = 5
SESSION_TIME_ATTACK = 6
SESSION_MAX = 7

RACESTATE_INVALID = 0
RACESTATE_NOT_STARTED = 1
RACESTATE_RACING = 2
RACESTATE_FINISHED = 3
RACESTATE_DISQUALIFIED = 4
RACESTATE_RETIRED = 5
RACESTATE_DNF = 6
RACESTATE_MAX = 7

SECTOR_INVALID = 0
SECTOR_START = 1
SECTOR_SECTOR1 = 2
SECTOR_SECTOR2 = 3
SECTOR_FINISH = 4
SECTOR_STOP = 5
SECTOR_MAX = 6

FLAG_COLOUR_NONE = 0
FLAG_COLOUR_GREEN = 1
FLAG_COLOUR_BLUE = 2
FLAG_COLOUR_WHITE = 3
FLAG_COLOUR_YELLOW = 4
FLAG_COLOUR_DOUBLE_YELLOW = 5
FLAG_COLOUR_BLACK = 6
FLAG_COLOUR_CHEQUERED = 7
FLAG_COLOUR_MAX = 8

FLAG_REASON_NONE = 0
FLAG_REASON_SOLO_CRASH = 1
FLAG_REASON_VEHICLE_CRASH = 2
FLAG_REASON_VEHICLE_OBSTRUCTION = 3
FLAG_REASON_MAX = 4

PIT_MODE_NONE = 0
PIT_MODE_DRIVING_INTO_PITS = 1
PIT_MODE_IN_PIT = 2
PIT_MODE_DRIVING_OUT_OF_PITS = 3
PIT_MODE_IN_GARAGE = 4
PIT_MODE_MAX = 5

PIT_SCHEDULE_NONE = 0
PIT_SCHEDULE_STANDARD = 1
PIT_SCHEDULE_DRIVE_THROUGH = 2
PIT_SCHEDULE_STOP_GO = 3
PIT_SCHEDULE_MAX = 4

CAR_HEADLIGHT = ( 1 << 0 )
CAR_ENGINE_ACTIVE = ( 1 << 1 )
CAR_ENGINE_WARNING = ( 1 << 2 )
CAR_SPEED_LIMITER = ( 1 << 3 )
CAR_ABS = ( 1 << 4 )
CAR_HANDBRAKE = ( 1 << 5 )

TYRE_ATTACHED = ( 1 << 0 )
TYRE_INFLATED = ( 1 << 1 )
TYRE_IS_ON_GROUND = ( 1 << 2 )

TERRAIN_ROAD = 0
TERRAIN_LOW_GRIP_ROAD = 1
TERRAIN_BUMPY_ROAD1 = 2
TERRAIN_BUMPY_ROAD2 = 3
TERRAIN_BUMPY_ROAD3 = 4
TERRAIN_MARBLES = 5
TERRAIN_GRASSY_BERMS = 6
TERRAIN_GRASS = 7
TERRAIN_GRAVEL = 8
TERRAIN_BUMPY_GRAVEL = 9
TERRAIN_RUMBLE_STRIPS = 10
TERRAIN_DRAINS = 11
TERRAIN_TYREWALLS = 12
TERRAIN_CEMENTWALLS = 13
TERRAIN_GUARDRAILS = 14
TERRAIN_SAND = 15
TERRAIN_BUMPY_SAND = 16
TERRAIN_DIRT = 17
TERRAIN_BUMPY_DIRT = 18
TERRAIN_DIRT_ROAD = 19
TERRAIN_BUMPY_DIRT_ROAD = 20
TERRAIN_PAVEMENT = 21
TERRAIN_DIRT_BANK = 22
TERRAIN_WOOD = 23
TERRAIN_DRY_VERGE = 24
TERRAIN_EXIT_RUMBLE_STRIPS = 25
TERRAIN_GRASSCRETE = 26
TERRAIN_LONG_GRASS = 27
TERRAIN_SLOPE_GRASS = 28
TERRAIN_COBBLES = 29
TERRAIN_SAND_ROAD = 30
TERRAIN_BAKED_CLAY = 31
TERRAIN_ASTROTURF = 32
TERRAIN_SNOWHALF = 33
TERRAIN_SNOWFULL = 34
TERRAIN_MAX = 35

CRASH_DAMAGE_NONE = 0
CRASH_DAMAGE_OFFTRACK = 1
CRASH_DAMAGE_LARGE_PROP = 2
CRASH_DAMAGE_SPINNING = 3
CRASH_DAMAGE_ROLLING = 4
CRASH_MAX = 5

class ParticipantInfo(ctypes.Structure):
    _fields_ = [
        ('mIsActive', ctypes.c_bool),
        ('mName', ctypes.c_char * STRING_LENGTH_MAX),
        ('mWorldPosition', ctypes.c_float * VEC_MAX),
        ('mCurrentLapDistance', ctypes.c_float),
        ('mRacePosition', ctypes.c_uint),
        ('mLapsCompleted', ctypes.c_uint),
        ('mCurrentLap', ctypes.c_uint),
        ('mCurrentSector', ctypes.c_uint),
    ]
    

class GameInstance(ctypes.Structure):
    _fields_ = [
        ('mVersion', ctypes.c_uint),
        ('mBuildVersionNumber', ctypes.c_uint),
        ('mGameState', ctypes.c_uint),
        ('mSessionState', ctypes.c_uint),
        ('mRaceState', ctypes.c_uint),
        ('mViewedParticipantIndex', ctypes.c_int),
        ('mNumParticipants', ctypes.c_int),
        ('mParticipantInfo', ParticipantInfo * STORED_PARTICIPANTS_MAX),
        ('mUnfilteredThrottle', ctypes.c_float),
        ('mUnfilteredBrake', ctypes.c_float),
        ('mUnfilteredSteering', ctypes.c_float),
        ('mUnfilteredClutch', ctypes.c_float),
        ('mCarName', ctypes.c_char * STRING_LENGTH_MAX),
        ('mCarClassName', ctypes.c_char * STRING_LENGTH_MAX),
        ('mLapsInEvent', ctypes.c_uint),
        ('mTrackLocation', ctypes.c_char * STRING_LENGTH_MAX),
        ('mTrackVariation', ctypes.c_char * STRING_LENGTH_MAX),
        ('mTrackLength', ctypes.c_float),
        ('mLapInvalidated', ctypes.c_bool),
        ('mBestLapTime', ctypes.c_float),
        ('mLastLapTime', ctypes.c_float),
        ('mCurrentTime', ctypes.c_float),
        ('mSplitTimeAhead', ctypes.c_float),
        ('mSplitTimeBehind', ctypes.c_float),
        ('mSplitTime', ctypes.c_float),
        ('mEventTimeRemaining', ctypes.c_float),
        ('mPersonalFastestLapTime', ctypes.c_float),
        ('mWorldFastestLapTime', ctypes.c_float),
        ('mCurrentSector1Time', ctypes.c_float),
        ('mCurrentSector2Time', ctypes.c_float),
        ('mCurrentSector3Time', ctypes.c_float),
        ('mFastestSector1Time', ctypes.c_float),
        ('mFastestSector2Time', ctypes.c_float),
        ('mFastestSector3Time', ctypes.c_float),
        ('mPersonalFastestSector1Time', ctypes.c_float),
        ('mPersonalFastestSector2Time', ctypes.c_float),
        ('mPersonalFastestSector3Time', ctypes.c_float),
        ('mWorldFastestSector1Time', ctypes.c_float),
        ('mWorldFastestSector2Time', ctypes.c_float),
        ('mWorldFastestSector3Time', ctypes.c_float),
        ('mHighestFlagColour', ctypes.c_uint),
        ('mHighestFlagReason', ctypes.c_uint),
        ('mPitMode', ctypes.c_uint),
        ('mPitSchedule', ctypes.c_uint),
        ('mCarFlags', ctypes.c_uint),
        ('mOilTempCelsius', ctypes.c_float),
        ('mOilPressureKPa', ctypes.c_float),
        ('mWaterTempCelsius', ctypes.c_float),
        ('mWaterPressureKPa', ctypes.c_float),
        ('mFuelPressureKPa', ctypes.c_float),
        ('mFuelLevel', ctypes.c_float),
        ('mFuelCapacity', ctypes.c_float),
        ('mSpeed', ctypes.c_float),
        ('mRpm', ctypes.c_float),
        ('mMaxRPM', ctypes.c_float),
        ('mBrake', ctypes.c_float),
        ('mThrottle', ctypes.c_float),
        ('mClutch', ctypes.c_float),
        ('mSteering', ctypes.c_float),
        ('mGear', ctypes.c_int),
        ('mNumGears', ctypes.c_int),
        ('mOdometerKM', ctypes.c_float),
        ('mAntiLockActive', ctypes.c_bool),
        ('mLastOpponentCollisionIndex', ctypes.c_int),
        ('mLastOpponentCollisionMagnitude', ctypes.c_float),
        ('mBoostActive', ctypes.c_bool),
        ('mBoostAmount', ctypes.c_float),
        ('mOrientation', ctypes.c_float * VEC_MAX),
        ('mLocalVelocity', ctypes.c_float * VEC_MAX),
        ('mWorldVelocity', ctypes.c_float * VEC_MAX),
        ('mAngularVelocity', ctypes.c_float * VEC_MAX),
        ('mLocalAcceleration', ctypes.c_float * VEC_MAX),
        ('mWorldAcceleration', ctypes.c_float * VEC_MAX),
        ('mExtentsCentre', ctypes.c_float * VEC_MAX),
        ('mTyreFlags', ctypes.c_uint * TYRE_MAX),
        ('mTerrain', ctypes.c_uint * TYRE_MAX),
        ('mTyreY', ctypes.c_float * TYRE_MAX),
        ('mTyreRPS', ctypes.c_float * TYRE_MAX),
        ('mTyreSlipSpeed', ctypes.c_float * TYRE_MAX),
        ('mTyreTemp', ctypes.c_float * TYRE_MAX),
        ('mTyreGrip', ctypes.c_float * TYRE_MAX),
        ('mTyreHeightAboveGround', ctypes.c_float * TYRE_MAX),
        ('mTyreLateralStiffness', ctypes.c_float * TYRE_MAX),
        ('mTyreWear', ctypes.c_float * TYRE_MAX),
        ('mBrakeDamage', ctypes.c_float * TYRE_MAX),
        ('mSuspensionDamage', ctypes.c_float * TYRE_MAX),
        ('mBrakeTempCelsius', ctypes.c_float * TYRE_MAX),
        ('mTyreTreadTemp', ctypes.c_float * TYRE_MAX),
        ('mTyreLayerTemp', ctypes.c_float * TYRE_MAX),
        ('mTyreCarcassTemp', ctypes.c_float * TYRE_MAX),
        ('mTyreRimTemp', ctypes.c_float * TYRE_MAX),
        ('mTyreInternalAirTemp', ctypes.c_float * TYRE_MAX),
        ('mCrashState', ctypes.c_uint),
        ('mAeroDamage', ctypes.c_float),
        ('mEngineDamage', ctypes.c_float),
        ('mAmbientTemperature', ctypes.c_float),
        ('mTrackTemperature', ctypes.c_float),
        ('mRainDensity', ctypes.c_float),
        ('mWindSpeed', ctypes.c_float),
        ('mWindDirectionX', ctypes.c_float),
        ('mWindDirectionY', ctypes.c_float),
        ('mCloudBrightness', ctypes.c_float),
    ]
    

