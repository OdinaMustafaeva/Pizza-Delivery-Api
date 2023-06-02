from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT

from database import Session, engine
from models import User, Order
from schemas import OrderModel

order_router = APIRouter(
    prefix="/orders",
    tags=['orders']
)

session = Session(bind=engine)


@order_router.get('/')
async def get_user_orders(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    user = Authorize.get_jwt_subject()
    current_user = session.query(User).filter(User.username == user).first()

    return jsonable_encoder(current_user.orders)


@order_router.post('/create', status_code=status.HTTP_201_CREATED)
async def place_an_order(order: OrderModel, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    current_user = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.username == current_user).first()

    new_order = Order(
        pizza_size=order.pizza_size,
        quantity=order.quantity
    )

    new_order.user = user
    session.add(new_order)
    session.commit()

    response = {
        "pizza_size": new_order.pizza_size,
        "quantity": new_order.quantity,
        "id": new_order.id,
        "order_status": new_order.order_status
    }

    return jsonable_encoder(response)


@order_router.get('/{id}/')
async def get_specific_order(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")

    subject = Authorize.get_jwt_subject()
    current_user = session.query(User).filter(User.username == subject).first()

    orders = current_user.orders

    for o in orders:
        if o.id == id:
            return jsonable_encoder(o)

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No order with such id")


@order_router.put('/{id}/update/')
async def update_order(id: int, order: OrderModel, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")

    order_to_update = session.query(Order).filter(Order.id == id).first()
    order_to_update.quantity = order.quantity
    order_to_update.pizza_size = order.pizza_size

    session.commit()

    response = {
        "id": order_to_update.id,
        "quantity": order_to_update.quantity,
        "pizza_size": order_to_update.pizza_size,
        "order_status": order_to_update.order_status,
    }

    return jsonable_encoder(order_to_update)


@order_router.delete('/{id}/delete/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_an_order(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")

    order_to_delete = session.query(Order).filter(Order.id == id).first()

    session.delete(order_to_delete)
    session.commit()

    return order_to_delete
