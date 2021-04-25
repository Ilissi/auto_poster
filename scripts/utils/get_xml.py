import requests
import os
import uuid


def get_list(url):
    xml_text = requests.get(url)
    return xml_text.text.split('\n')

def generate_tags(string_with_elements):
    how_to_get = string_with_elements.replace(' ', '_').split(',')
    return ' '.join([str('#' + elem) for elem in how_to_get])

def get_os_path():
    return os.environ['PYTHONPATH'].split(os.pathsep)

def save_image(url_for_img, dir_for_save):
    response = requests.get(url_for_img)
    path_for_save_file = f'{dir_for_save}/{str(uuid.uuid4())}.png'
    file = open(path_for_save_file, "wb")
    file.write(response.content)
    file.close()
    return path_for_save_file

def string_joiner(first_string, second_string, third_string):
    return first_string + '\n' + second_string + '\n' + third_string

def string_to_dict_post_reddit(data, dir_for_save):
    keys_list = ['title', 'description', 'url', 'img_path', 'tags']
    list_for_generate_dict = data.replace('"', '').split("|")
    list_for_generate_dict[3] = save_image(list_for_generate_dict[3], dir_for_save)
    list_for_generate_dict[4] = generate_tags(list_for_generate_dict[4])
    return {keys_list[i]: list_for_generate_dict[i] for i in range(len(keys_list))}

def cut_tags(first_string, second_string, third_string):
    sum_string = len(first_string + '\n' + second_string + '\n' + third_string + '\n')
    if sum_string >= 255:
        cut_string = len(third_string) - (sum_string - 255)
        return third_string[:cut_string]
    else:
        return third_string


def string_to_send_tweet(data):
    list_for_generate = data.replace('"', '').split("|")
    list_for_generate[4] = generate_tags(list_for_generate[4])
    list_for_generate[4] = cut_tags(list_for_generate[0], list_for_generate[1], list_for_generate[4])
    list_for_generate.pop(3)

    return '\n'.join([str(elem) for elem in list_for_generate])




#print(get_os_path())
#xml_list = get_list(url)
#for c in xml_list[:-1]:
#    print(string_to_dict_post_reddit(c))
