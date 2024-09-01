import requests


def get_terms() -> list:
    url = (
        "https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/courseSearch/getTerms"
    )
    params = {"searchTerm": "", "offset": 1, "max": 6}

    try:
        response = requests.get(url, params=params)
        terms = response.json()

        filtered_terms = [
            term for term in terms if "Orientation" not in term.get("description", "")
        ]

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    return filtered_terms
