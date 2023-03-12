def add_new_score(new_score):
    """updates the high score board

    Args:
        new_score (String): the users time for the last game
    """
    f = open("score.txt", "r")
    content = f.read()
    content=content.splitlines()
    split_score =[]
    for i in range(len(content)):
        content1 = content[i].split(":")
        split_score.append(content1)
    # print(x)
    new_score = new_score.split(":")
    split_score.append(new_score)
    sort_score(split_score)
    
    pass


def sort_score(all_scores):
    """Sorts the score in decinding order and removes the lowest score

    Args:
        all_scores (nested list): list of all the high scores
    """    
    # print(all_scores)
    sorted_list = sorted(all_scores, key=lambda x: (int(x[0]), int(x[1]), int(x[2])),reverse=True)
    # print(sorted_list)
    sorted_list.pop()
    # print(sorted_list)
    update_highscores(sorted_list)
    
def update_highscores(sorted_list):
    """updates score.txt in decending order

    Args:
        sorted_list (nested list): _description_
    """    

    for i in range(len(sorted_list)):
        sorted_list[i]= ":".join(sorted_list[i])
        # print(sorted_list)
        with open('score.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
    
        data[i] = f"{sorted_list[i]}\n"
        
        with open('score.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
        pass
    pass


