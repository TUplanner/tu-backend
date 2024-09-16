# Configuration


def create_payload(query, professor):
    """
    Constructs the payload for the GraphQL request.

    Args:
        query (str): The GraphQL query string to use.
        professor (str): The name of the professor to search for.

    Returns:
        dict: The payload for the request, including the GraphQL query and variables.
    """
    variables = {
        "query": {
            "text": professor,
            "schoolID": "U2Nob29sLTk5OQ==",
        },
    }
    return {"query": query, "variables": variables}


# Constants for GraphQL request
URL = "https://www.ratemyprofessors.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Basic dGVzdDp0ZXN0",
}


# GraphQL queries
FULL_QUERY = """
query NewSearchTeachersQuery($query: TeacherSearchQuery) {
    newSearch {
        teachers(query: $query) {
            didFallback
            edges {
                cursor
                node {
                    id
                    firstName
                    lastName
                    avgRating
                    numRatings
                    department
                    departmentId
                    legacyId
                    lockStatus
                    wouldTakeAgainPercentRounded
                    mandatoryAttendance {
                        neither
                        no
                        total
                        yes
                    }
                    ratingsDistribution {
                        r1
                        r2
                        r3
                        r4
                        r5
                        total
                    }
                    school {
                        id
                        legacyId
                        name
                    }
                    takenForCredit {
                        neither
                        no
                        total
                        yes
                    }
                }
            }
        }
    }
}
"""

TEACHER_QUERY = """
query NewSearchTeachersQuery($query: TeacherSearchQuery!, $count: Int) {
    newSearch {
        teachers(query: $query, first: $count) {
            edges {
                node {
                    id
                    firstName
                    lastName
                    department
                    avgRating
                    numRatings
                    wouldTakeAgainPercentRounded
                }
            }
        }
    }
}
"""
