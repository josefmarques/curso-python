from app.use_cases.category import CategoryUseCases
from app.db.models import Category as CategoryModel
from app.schemas.category import Category


def test_add_category_us(db_session):
    uc = CategoryUseCases(db_session)
    
    uc.add_category()
