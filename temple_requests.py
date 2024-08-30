import requests
from bs4 import BeautifulSoup


def get_academic_programs() -> list:
    program_list = []

    try:
        req = requests.get("https://bulletin.temple.edu/academic-programs/")
        soup = BeautifulSoup(req.content, "lxml")

        # The body containing all the programs/degrees
        main_body = soup.find("tbody", class_="fixedTH", id="degree_body")

        # Iterate through each program in the body
        for program_element in main_body.find_all("tr"):
            # Children contain program name and degree types
            program_children = program_element.find_all("td")
            program_name = program_children[0].get_text(strip=True)

            for index in range(1, 4):
                child = program_children[index]
                program_degrees = child.get_text(strip=True)
                program_link = child.find("a").get("href") if child.find("a") else ""

                if program_degrees:
                    degrees = program_degrees.split(",")
                    for degree in degrees:
                        program_list.append(
                            {
                                "program": f"{program_name} {degree.strip()}",
                                "link": program_link,
                            }
                        )
        return program_list

    except Exception as e:
        print(f"Error fetching data: {e}")
        return program_list
