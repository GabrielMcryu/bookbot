def character_counts(all_words):
    character_count = {}
    for word in all_words:
        for character in word:
            if character.lower() in character_count:
                character_count[character.lower()] += 1
            else:
                character_count[character.lower()] = 1
    return character_count

def get_num_words(file_contents):
    all_words = file_contents.split()
    character_count = character_counts(all_words)
    return character_count

