# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:52:42 2024

@author: Arun.Rameshbabu
"""

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program\n")
    

def add_movie(movies):
    """
    Add a movie to the movies list provided

    Parameters
    ----------
    movies : list
        List that contains movies.

    Returns
    -------
    None.

    """
    movie = input('Name: ')
    year = input('Year: ')
    movies.append([movie, year])
    print(f'{movie} was added\n')


def list_movies(movies):
    """
    Prints the list of movies

    Parameters
    ----------
    movies : list
        List that contains movies.

    Returns
    -------
    None.

    """
    # for i in range(len(movies)):
    #     print(f"{i+1}. {movies[i][0]} ({movies[i][1]})")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()


def delete_movie(movies):
    num = int(input("Number: "))
    if (num < 1) or (num > len(movies)):
        print("Invalid movie number.\n")
    else:
        movie = movies.pop(num-1)
        print(f"{movie[0]} was deleted.\n")


def main():
    """
    Main function for the Basic Movies Program

    Returns
    -------
    None.

    """
    # Creating an empty list
    movies_list = [['Monty Python and the Holy Grail', '1975'], ['On the Waterfront','1954'], ['Cat on a hot tin roof', '1958']]
    display_menu()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies_list)
        elif command.lower() == 'add':
            add_movie(movies_list)
        elif command.lower() == 'del':
            delete_movie(movies_list)
        elif command.lower() == 'exit':
            break
        else:
            print("Invalid command. Please try again.\n")
    print("Bye!")
    
if __name__ == "__main__":
    main()