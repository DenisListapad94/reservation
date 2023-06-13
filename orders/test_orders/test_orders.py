import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from main import app
#
# @pytest.mark.parametrize(("first_value", "second_value", "third_value"),(
#                          (1, 1, 2),
#                          (2, 3, 5),
#                          (4, 5, 9),
#                          (10, -2, 8)
#                     ))
# def test_simple_equal(first_value, second_value, third_value):
#     assert first_value + second_value == third_value
#
# @pytest.mark.skip("api doesn't work")
# def test_skip():
#     assert  1 == 1

# client = TestClient(app)
#
# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}
#     print(response.content)

# @pytest.mark.anyio
# async def test_root():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}

# from main import app
# import pytest
# from httpx import AsyncClient
#
@pytest.mark.anyio
async def test_add_waiter(ac: AsyncClient):
    response = await ac.post("/order/add_waiter", json={
        "waiter_id": 1,
        "name": "Jho",
        "last_name": "Philips",
        "age": 26,
    })
    assert response.status_code == 200

@pytest.mark.anyio
async def test_get_waiter(ac: AsyncClient):
    response = await ac.get("/order/waiters")

    assert response.status_code == 200
    # assert response.json()["status"] == "success"
    # assert len(response.json()["data"]) == 1