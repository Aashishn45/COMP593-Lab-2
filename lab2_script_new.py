def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Aashish Neupane",
        "student_id": 10316514,
        "pizza_toppings": ["SAUSAGE", "CABBAGE", "BACON"],
        "movies": [
           {
               "title": "indiana jones",
               "genre": "mystery",
           },
           
           {
               "title": "titanic",
               "genre": "romance",
           }, 
        ],

    }
    
    # TODO: Step 3 - Add another movie to the data structure
    about_me["movies"].append({"title": "avengers", "genre": "sc-fi"})
    
    print_student_name_and_id(about_me)

    print_pizza_toppings(about_me)
    
    add_pizza_toppings(about_me, ("tomato", "chicken"))
    
    print_pizza_toppings(about_me)

    print_movie_genres(about_me)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f'My name is {full_name}, but you can call me Sir {first_name}.\nMy student ID is {student_id}.')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me["pizza_toppings"] = [topping.lower() for topping in about_me["pizza_toppings"]]
    about_me["pizza_toppings"].sort()
    return


# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
     print('\nMy favorite pizza toppings are:')
     for topping in about_me["pizza_toppings"]:
      print(f'-{topping}') 
     return


# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    list = []
    for movie in about_me['movies']:
     if isinstance(movie, dict):  
        list.append(movie['genre'])

    print(f"\nI like to watch {list[0]}, {list[1]}, and {list[2]} movies.")

    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):



    return

    
if __name__ == '__main__':
    main()