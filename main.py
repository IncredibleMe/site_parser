from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import difflib

def download_page(url, filename):
    service = Service(executable_path='./chromedriver')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Open the website in the browser
    driver.get(url)

    # Get the HTML content of the page
    html_content = driver.page_source

    # Save the HTML content to a file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

    # Close the browser window
    driver.quit()

def compare_files(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1:
        file1_content = file1.readlines()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        file2_content = file2.readlines()
    differ = difflib.Differ()

    diff = list(differ.compare(file1_content, file2_content))

    common = difflib.SequenceMatcher(None, file1_content, file2_content).ratio()
    percentage_difference = (1 - common) * 100

    print(f"\nPercentage Difference: {percentage_difference:.2f}%")


def main():
    download_page("https://www.rakuten.co.jp/", 'webpage.html')
    download_page("https://www.rakuten.co.jp/", 'webpage2.html')
    compare_files('webpage.html', 'webpage2.html')


if __name__=="__main__":
    main()