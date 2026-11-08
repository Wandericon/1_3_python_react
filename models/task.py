from pydantic import BaseModel, field_validator


class Category(BaseModel):
    name: str
    color: str


class Task(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    category: Category
    internal_note: str = ""

    @field_validator("title")
    @classmethod
    def check_title(cls, value):
        if len(value.strip()) < 3:
            raise ValueError("Название задачи должно содержать не менее 3 символов")
        return value.strip()


class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    category: Category
