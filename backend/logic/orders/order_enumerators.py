from enum import Enum

class InRestaurantOrderState(Enum):
    LOGGING = 1,
    INQUEUE = 2,
    PREPARING = 3,
    READYTOSERVE = 4,
    COMPLETE = 5,

class TakeawayOrderState(Enum):
    LOGGING = 1,
    INQUEUE = 2,
    PREPARING = 3,
    READYFORPICKUP = 4,
    COMPLETE = 5,

class DeliveryOrderState(Enum):
    LOGGING = 1,
    INQUEUE = 2,
    PREPARING = 3,
    READYFORDELIVERY = 4,
    SENT = 5,
    COMPLETE = 6,
