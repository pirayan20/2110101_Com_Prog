
kid_to_dad = {"Tony": "John",
        "Steve": "John",
        "Eren": "Tony",
        "Annie": "Tony",
        "Ben": "Steve",
        "Historia": "Steve",
        "Mike": "Ben"}

def get_newphews_and_nieces(kid_to_dad,name):
    dad_to_kid = {}
    for kid in kid_to_dad:
        if kid_to_dad[kid] not in dad_to_kid:
            dad_to_kid[kid_to_dad[kid]] = []
        dad_to_kid[kid_to_dad[kid]].append(kid)

    if name not in dad_to_kid and name not in kid_to_dad:
        return []

    if name not in kid_to_dad:
        return []
    
    dad = kid_to_dad[name]
    
    if len(dad_to_kid[dad]) == 1:
        return []
    else:
        answer = []
        for siblings in dad_to_kid[dad]:
            if siblings != name:
                if siblings in dad_to_kid:
                    for nephew in dad_to_kid[siblings]:
                        answer.append(nephew)
        return sorted(answer)

print(get_newphews_and_nieces(kid_to_dad,"Peter"))