employees = [
    {'name': 'John', 'department': 'IT', 'salary': 250000},
    {'name': 'Mary', 'department': 'HR', 'salary': 180000},
    {'name': 'David', 'department': 'IT', 'salary': 300000},
    {'name': 'Sarah', 'department': 'Finance', 'salary': 220000},
    {'name': 'Peter', 'department': 'IT', 'salary': 150000}
]
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """
    split_it = sentence.split()
    print(split_it)
    extract = split_it[index]
    print(extract)
    if extract.endswith('.'):
        remove = extract.replace('.','')
        print(remove)
        add_en = remove + 'en'
        print(add_en)
    else:
        add_en = extract + 'en'
        return add_en
print(adjective_to_verb('The bread got hard after sitting out.', 3 ))
#'brighten'