from ariadne import QueryType

query = QueryType()


@query.field("hello")
def resolve_hello(_, info):
    return "Hello, world!"


@query.field("newSearch")
def resolve_new_search(_, info):
    return {}
