import re
import requests
from bs4 import BeautifulSoup


def get_academic_programs() -> list:
    program_list = []

    try:
        response = requests.get("https://bulletin.temple.edu/academic-programs/")
        soup = BeautifulSoup(response.content, "lxml")

        main_body = soup.find("tbody", class_="fixedTH", id="degree_body")

        for row in main_body.find_all("tr"):
            columns = row.find_all("td")

            program_name = columns[0].get_text()

            for column in columns[1:4]:
                program_degrees = column.get_text()

                if program_degrees:
                    degrees = program_degrees.split(",")
                    links = [a["href"] for a in column.find_all("a")]

                    for degree, link in zip(degrees, links):
                        program = re.sub(r"\s+", " ", f"{program_name} {degree}")

                        if link:
                            program_list.append({"program": program, "link": link})

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

    return program_list


def get_curriculum(program_url: str) -> list:
    curriculum = set()

    try:
        response = requests.get(
            f"https://bulletin.temple.edu/{program_url}#requirementstext"
        )
        soup = BeautifulSoup(response.content, "lxml")
        main_body = soup.find("div", id="requirementstextcontainer")

        rows = main_body.find_all("tr", class_=["even", "odd"])

        for row in rows:
            course_code_html = row.find("a", class_="bubblelink code")
            if course_code_html:
                course_code = course_code_html.get_text(strip=True)
                columns = row.find_all("td")
                course_name = columns[1].get_text(strip=True)
                curriculum.add((course_code, course_name))

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

    return list(curriculum)
