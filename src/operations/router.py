from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from src.database import get_async_session
from src.operations.models import Operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix='/operations',
    tags=['Operation'],
)


@router.get('/')
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Operation).where(Operation.type == operation_type)
    result = await session.execute(query)
    return {
        'status': 'ok',
        'data': result.scalars().all(),
        'details': 'Operation success!'
    }


@router.post('/')
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {
        'status': 'ok',
        'data': None,
        'details': 'Operation success!'
    }
