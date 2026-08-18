from enum import StrEnum
from contracts.services.operations.operation_pb2 import OperationStatus, OperationType


class OperationTestType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    REVERSAL = "REVERSAL"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationTestStatus(StrEnum):
    FAILED = "FAILED"
    REVERSED = "REVERSED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


def from_proto_status(status: OperationStatus) -> OperationTestStatus:
    status_dict = {
        OperationStatus.OPERATION_STATUS_FAILED: OperationTestStatus.FAILED,
        OperationStatus.OPERATION_STATUS_REVERSED: OperationTestStatus.REVERSED,
        OperationStatus.OPERATION_STATUS_COMPLETED: OperationTestStatus.COMPLETED,
        OperationStatus.OPERATION_STATUS_IN_PROGRESS: OperationTestStatus.IN_PROGRESS,
        OperationStatus.OPERATION_STATUS_UNSPECIFIED: OperationTestStatus.UNSPECIFIED
    }

    return status_dict[status]


def from_proto_type(proto_type: OperationType) -> OperationTestType:
    type_dict = {
        OperationType.OPERATION_TYPE_FEE: OperationTestType.FEE,
        OperationType.OPERATION_TYPE_TOP_UP: OperationTestType.TOP_UP,
        OperationType.OPERATION_TYPE_PURCHASE: OperationTestType.PURCHASE,
        OperationType.OPERATION_TYPE_CASHBACK: OperationTestType.CASHBACK,
        OperationType.OPERATION_TYPE_TRANSFER: OperationTestType.TRANSFER,
        OperationType.OPERATION_TYPE_REVERSAL: OperationTestType.REVERSAL,
        OperationType.OPERATION_TYPE_BILL_PAYMENT: OperationTestType.BILL_PAYMENT,
        OperationType.OPERATION_TYPE_CASH_WITHDRAWAL: OperationTestType.CASH_WITHDRAWAL
    }
    return type_dict[proto_type]
