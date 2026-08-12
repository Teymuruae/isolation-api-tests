from enum import StrEnum

from libs.base.enums import ProtoEnum


class CardTestType(ProtoEnum, StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"


class CardTestStatus(ProtoEnum, StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"


class CardTestPaymentSystem(ProtoEnum, StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"
