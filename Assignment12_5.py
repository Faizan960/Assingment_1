#navigate to site file
import webbrowser

def navigate_to_site():
    try:
        site_url = input("Enter the URL of the site you want to navigate to: ")
        webbrowser.open_new_tab(site_url)
    except Exception as e:
        print("Error occurred while navigating to the site:", str(e))
3