from ariadne import ObjectType
from rmp_requests import get_professor


new_search = ObjectType("NewSearch")


@new_search.field("teacher")
def resolve_teacher(parent, info, fullName):
    return get_professor(fullName)  # Returns object of type "Teacher"
