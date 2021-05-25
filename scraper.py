import requests
import lxml.html as lh
from bs4 import BeautifulSoup
import re
import json

# Resources:
# https://stackoverflow.com/questions/13147914/how-to-simulate-http-post-request-using-python-requests-module

def gender_genie(text, genre):
    url = 'https://app.rockgympro.com/b/widget/?a=equery'

    form_data = {
        # 'reventChromeAutocomplete':'',
        'widget_guid': '2224a8b95d0e4ca7bf20012ec34b8f3e',
        'random': '6050412acb071',
        # 'iframeid:,
        'mode': 'p',
        'fctrl_1': 'offering_guid',
        'offering_guid': '484c1a7ca09145419ef258eeb894c38f',
        'fctrl_2': 'course_guid',
        # 'course_guid': '',
        'fctrl_3': 'limited_to_course_guid_for_offering_guid_484c1a7ca09145419ef258eeb894c38f',
        # 'limited_to_course_guid_for_offering_guid_484c1a7ca09145419ef258eeb894c38f':,
        'fctrl_4': 'show_date',
        'show_date': '2021-05-28',
        'ftagname_0_pcount-pid-1-751460': 'pcount',
        'ftagval_0_pcount-pid-1-751460': 1,
        'ftagname_1_pcount-pid-1-751460': 'pid',
        'ftagval_1_pcount-pid-1-751460': '751460',
        'fctrl_5': 'pcount-pid-1-751460',
        'pcount-pid-1-751460': 0,
        'ftagname_0_pcount-pid-1-1190943': 'pcount',
        'ftagval_0_pcount-pid-1-1190943': 1,
        'ftagname_1_pcount-pid-1-1190943': 'pid', 'ftagval_1_pcount-pid-1-1190943': '1190943',
        'fctrl_6': 'pcount-pid-1-1190943',
        'pcount-pid-1-1190943': 0,
        'ftagname_0_pcount-pid-1-4455667': 'pcount',
        'ftagval_0_pcount-pid-1-4455667': 1,
        'ftagname_1_pcount-pid-1-4455667': 'pid',
        'ftagval_1_pcount-pid-1-4455667': '4455667',
        'fctrl_7': 'pcount-pid-1-4455667',
        'pcount-pid-1-4455667': 0,
        'ftagname_0_pcount-pid-1-4582326': 'pcount',
        'ftagval_0_pcount-pid-1-4582326': 1,
        'ftagname_1_pcount-pid-1-4582326': 'pid',
        'ftagval_1_pcount-pid-1-4582326': '4582326',
        'fctrl_8': 'pcount-pid-1-4582326',
        'pcount-pid-1-4582326': 0,
    }

    res = requests.post(url, data=form_data)
    schedule = res.json()["event_list_html"]
    soup = BeautifulSoup(schedule, 'html.parser')
    # print(soup.prettify())

    rows = soup.select('table tr')
    # print(rows)

    # TODO: take in user input for start time
    for row in rows:
        if len(row.select('.offering-page-schedule-list-time-column:-soup-contains("9:15 AM to")')) == 0:
            continue

        if len(row.select('.book-now-button')) > 0:
            # The timeslot is available!!
            # TODO: fire a text message


    return "hi"

def is_available(html, start_time):
    return true


if __name__ == '__main__':
    print(gender_genie('I have a beard!', 'blog'))