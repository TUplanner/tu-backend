# Configuration


def create_payload(query, professor):
    """
    Constructs the payload for the GraphQL request.

    Args:
        query (str): The GraphQL query string to use.
        professor (str): The name of the professor to search for.

    Returns:
        dict: The payload for the request.
    """
    variables = {
        "query": {
            "text": professor,
            "schoolID": "U2Nob29sLTk5OQ==",
        },
        "count": 1,
    }
    return {"query": query, "variables": variables}


URL = "https://www.ratemyprofessors.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Basic dGVzdDp0ZXN0",
}
FULL_QUERY = """
query NewSearchTeachersQuery($query: TeacherSearchQuery!, $count: Int) {
    newSearch {
        teachers(query: $query, first: $count) {
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
