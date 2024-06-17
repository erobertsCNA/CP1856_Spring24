# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:33:54 2024

@author: Arun.Rameshbabu
"""

movies_list = []

def add_movie(movies):
    movie = input('Name: ')
    movies.append(movie)
    print(f'{movie} was added')

def main():
    add_movie(movies_list)

if __name__ == '__main__':
    main()