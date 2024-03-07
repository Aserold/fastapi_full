from fastapi import APIRouter, Depends, BackgroundTasks

from src.auth.base_config import current_user
from src.tasks.tasks import send_email_report_dashboard

router = APIRouter(prefix='/report', tags=['report'])


@router.get('/dashboard')
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    return {
        'status': 200,
        'data': 'Message sent',
        'details': None
    }
