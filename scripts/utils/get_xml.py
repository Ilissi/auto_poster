import requests
import os

url = 'https://4kporn.xxx/admin/feeds/reddit/?csv_columns=title%7Cdescription%7Clink%7Cmain_screenshot%7Ctags&feed_format=csv&csv_separator=%7C&csv_list_separator=%2C&csv_quote=1&limit=5&sorting=post_date+desc&screenshot_format=320x180&hd=1&min_rating=60&max_rating=100&utm_source=reddit&utm_medium=plugs&utm_campaign=username'

def get_list(url):
    xml_text = requests.get(url)
    return xml_text.text.split('\n')

def generate_tags(string_with_elements):
    how_to_get = string_with_elements.replace(' ', '_').split(',')
    return ' '.join([str('#' + elem) for elem in how_to_get])

def get_os_path():
    return os.environ['PYTHONPATH'].split(os.pathsep)

def save_image(url_for_save):
    response = requests.get(url_for_save)
    path = f'{get_os_path()}/{}'
    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

def string_to_dict_post_reddit(data):
    keys_list = ['title', 'description', 'url', 'img', 'tags']
    list_for_generate_dict = data.replace('"', '').split("|")

    return {keys_list[i]: list_for_generate_dict[i] for i in range(len(keys_list))}

def string_to_send_tweet(data):
    list_for_generate_dict = data.replace('"', '').split("|")
    list_for_generate_dict[4] = generate_tags(list_for_generate_dict[4])
    list_for_generate_dict.pop(3)
    return '\n'.join([str(elem) for elem in list_for_generate_dict])




print(len("""Lady jasoos web series EP3
Bhahi banged! nude all alone inside Beauty bed harder into night dree


#fuck_harder #fucking #hot_fuck #hottest #ladies #lady #naked_fuck #series #web #web_series #one_night #in_bed #la_e #banged_hard #hard_bang #hard_inside #hard"""))


print(get_os_path())
xml_list = get_list(url)
for c in xml_list[:-1]:
    print(string_to_send_tweet(c))
print(generate_tags('stepson,la el,step son,la e,min min,winter,coming,with,pamela'))