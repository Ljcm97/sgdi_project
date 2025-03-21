from flask import Blueprint
from app.utils.auth import check_permission

template_filters_bp = Blueprint('template_filters', __name__)

@template_filters_bp.app_context_processor
def utility_processor():
    return dict(check_permission=check_permission)
