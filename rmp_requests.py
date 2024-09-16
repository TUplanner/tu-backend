import requests
from rmp_configuration import URL, HEADERS, FULL_QUERY, create_payload


def get_rmp_professor(professor_name):
    try:
        payload = create_payload(FULL_QUERY, professor_name)
        # print(payload)
        response = requests.post(URL, json=payload, headers=HEADERS)
        data = response.json()
        # Limited to 1 teacher as specified in rmp_configuration
        teachers = data["data"]["newSearch"]["teachers"]["edges"]
        teacher = teachers[0]["node"]

        return teacher

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


# get_rmp_professor("je-wei chen")
# print(get_rmp_professor("je-wei chen"))
