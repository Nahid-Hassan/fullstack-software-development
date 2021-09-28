from bs4 import BeautifulSoup


with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    # get h5 tag
    # tags = soup.find('h5') # return first occurences
    courses_html_tags = soup.find_all('h5')  # return all occurences as list

    for course in courses_html_tags:
        print(course)
