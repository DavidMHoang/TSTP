my_dict = { "height":
            "170cm",
            "fav_color":
            "black",
            "fav_author":
            "there is not one" }

answer = input("enter height, fav_color, or fav_author: ")
if answer in my_dict:
    result = my_dict[answer]
    print(result)
