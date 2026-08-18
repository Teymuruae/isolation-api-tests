import uuid

import allure
from pydantic import UUID4

from tests.assertions.base import assert_equal
from tests.clients.postgres.operations.model import OperationsTestModel
from tests.schema.operations import (
    OperationEventTestSchema,
    GetOperationsResponseTestSchema
)
from tests.tools.logger import get_test_logger
from contracts.services.operations.operation_pb2 import Operation
from tests.types.operations import from_proto_status, from_proto_type
from tests.tools.date import to_proto_test_datetime
from contracts.services.operations.rpc_get_operation_pb2 import GetOperationResponse
from contracts.services.operations.rpc_get_operations_pb2 import GetOperationsResponse

logger = get_test_logger("OPERATIONS_ASSERTIONS")


@allure.step("Check operation from event")
def assert_operation_from_event(
        actual: Operation,
        expected: OperationEventTestSchema
) -> None:
    logger.info("Check operation from event")

    assert_equal(from_proto_type(actual.type), expected.type, "type")
    assert_equal(from_proto_status(actual.status), expected.status, "status")
    assert_equal(actual.amount, expected.amount, "amount")
    assert_equal(UUID4(actual.user_id), expected.user_id, "user_id")
    assert_equal(UUID4(actual.card_id), expected.card_id, "card_id")
    assert_equal(actual.category, expected.category, "category")
    assert_equal(actual.created_at, to_proto_test_datetime(expected.created_at), "created_at")
    assert_equal(UUID4(actual.account_id), expected.account_id, "account_id")


@allure.step("Check operation from model")
def assert_operation_from_model(
        actual: Operation,
        expected: OperationsTestModel
) -> None:
    logger.info("Check operation from model")

    assert_equal(uuid.UUID(actual.id), expected.id, "id")
    assert_equal(from_proto_type(actual.type).value, expected.type, "type")
    assert_equal(from_proto_status(actual.status).value, expected.status, "status")
    assert_equal(actual.amount, expected.amount, "amount")
    assert_equal(uuid.UUID(actual.user_id), expected.user_id, "user_id")
    assert_equal(uuid.UUID(actual.card_id), expected.card_id, "card_id")
    assert_equal(actual.category, expected.category, "category")
    assert_equal(actual.created_at, to_proto_test_datetime(expected.created_at), "created_at")
    assert_equal(uuid.UUID(actual.account_id), expected.account_id, "account_id")


@allure.step("Check get operations response from events")
def assert_get_operations_response_from_events(
        actual: GetOperationsResponse,
        expected: list[OperationEventTestSchema]
) -> None:
    logger.info("Check get operations response from events")

    assert_equal(len(actual.operations), len(expected), "operations count")
    for index, event in enumerate(expected):
        assert_operation_from_event(actual.operations[index], event)


@allure.step("Check get operations response from models")
def assert_get_operations_response_from_models(
        actual: GetOperationsResponse,
        expected: list[OperationsTestModel]
) -> None:
    logger.info("Check get operations response from models")

    assert_equal(len(actual.operations), len(expected), "operations count")
    for index, model in enumerate(expected):
        assert_operation_from_model(actual.operations[index], model)
