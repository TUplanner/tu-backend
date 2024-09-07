import requests
from rmp_configuration import URL, HEADERS, TEACHER_QUERY, create_payload


def get_rmp_professor(professor_name):
    """
    Fetches data from the Rate My Professors API for a given professor.

    Args:
        professor_name (str): The name of the professor to search for.

    Returns:
        dict: A dictionary containing details of the first teacher found or an error message if an exception occurs.
    """
    try:
        response = requests.post(
            URL, json=create_payload(TEACHER_QUERY, professor_name), headers=HEADERS
        )
        data = response.json()
        # Limited to 1 teacher as specified in rmp_configuration
        teachers = data["data"]["newSearch"]["teachers"]["edges"]
        teacher = teachers[0]["node"]

        return teacher

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
