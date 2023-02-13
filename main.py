import io
from selenium import webdriver
import eel

eel.init('web')

@eel.expose
def generate_events(data):
    # Specify the path to the Chrome binary
    # chrome_binary_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_binary_path = 'chromx/Google/Chrome/Application/chrome.exe'

    # Create a new Chrome webdriver
    driver = webdriver.Chrome(service_args=['--binary={}'.format(chrome_binary_path)])

    # Use the webdriver to load the page
    driver.get(data)

    # Find the elements containing the event titles in the left sidebar
    event = driver.find_elements(by='xpath',
                                 value='//*[@id="immersive_desktop_root"]/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/ul/li/div/div[1]/div[2]/div')[
            :10]
    # Create an empty list to store the data
    data_list = []
    # Iterate through the event titles
    for event_title in event:
        # Bring the event title into view
        driver.execute_script("arguments[0].scrollIntoView(true);", event_title)
        # Click on the event to select it
        event_title.click()

        # Find the element containing the title in the right sidebar
        title = driver.find_elements(by='xpath',
                                     value='//*[@id="tl_ditc"]/div/g-sticky-content-container/div/div[1]/div[2]')

        # Find the element containing the URL in the right sidebar
        url = driver.find_elements(by='xpath',
                                   value='//*[@id="tl_ditc"]/div/g-sticky-content-container/div/div[4]/multi-source/div[1]/div/div/a[2]')

        # Find the element containing the event URL in the right sidebar
        event_url = driver.find_elements(by='xpath',
                                         value='//*[@id="_3pOxY9GKG6Lsz7sP__y_2Ag_42"]/div[2]/span/div/div/div/div[8]')

        # Extract the text from the event titles
        titles = [titles.text for titles in title]
        # Extract the href attribute of the url element
        url_link: list[str] = [url_link.get_attribute('href') for url_link in url]
        # Extract the href attribute of the event_url element
        event_url_link = [event_url_link.text for event_url_link in event_url]

        # Strip the data
        titles = str(titles).replace('[', '').replace(']', '').replace('"', '').replace("'", '')
        url_link = str(url_link).replace('[', '').replace(']', '').replace('"', '').replace("'", '')
        event_url_link = str(event_url_link).replace('[', '').replace(']', '').replace('"', '').replace("'", '')

        # Print the event details
        # print((titles, url_link, event_url_link))

        # Append the data for this event title to the list
        data_list.append((titles, url_link, event_url_link))

    # Close the webdriver
    driver.close()

    # Return the list of data to JavaScript
    return data_list


# Start GUI
eel.start('index.html', size=(1920, 1080))
