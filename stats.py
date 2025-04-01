def character_counts(all_words):
    character_count = {}
    for word in all_words:
        for character in word:
            if character.lower() in character_count:
                character_count[character.lower()] += 1
            else:
                character_count[character.lower()] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def get_num_words(file_contents):
    all_words = file_contents.split()
    total_words = len(all_words)
    character_count = character_counts(all_words)
    return character_count, total_words

def sort_dict(character_count):
    dict_list = []
    for key in character_count:
        temp_dict = {}
        temp_dict["name"] = key
        temp_dict["num"] = character_count[key]
        dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list





