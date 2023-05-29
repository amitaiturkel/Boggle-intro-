from helper_functions import *
from boggle_board_randomizer import *
import copy
from typing import List, Tuple, Iterable, Optional

Board = List[List[str]]
Path = List[Tuple[int, int]]



def is_valid_path(board: Board, path: Path, words: List):
    """ This function receives a board, a path and a List of words, check if the path is legal and
    if so, returns the word we formed, if it exists in the words dictionary """
    word = board[path[0][0]][path[0][1]]
    for step in range(len(path)):
        if step == len(path) -1:
            if word in words:
                return word
            return
        if path[step + 1] not in possible_moves(path[step], path[:step + 1], (len(board) - 1, len(board[0]) - 1)):
            return
        else:
            word += str(board[path[step+1][0]][path[step+1][1]])
    return word


def find_length_n_paths(n: int, board: Board, words: List):
    """ This function returns all the paths of size n that form a legal word """
    new_words = list(filter(lambda word: len(word) >= n, words))
    list_of_paths = []
    for start_loc in start_coord(board):
        list_of_paths =  find_length_helper(n, start_loc, list_of_paths, [], new_words, new_words, board, False)
    return list_of_paths



def find_length_helper(n: int, loc: Tuple[int, int], list_of_paths: List[Path], this_path: Path,\
    words: List, filtered_words: List, board: Board, checking_word_length: bool):
    """ This function finds all possible combinations for words of length n, OR for paths of length n"""
    this_path.append(loc)
    filtered_words = filtered(filtered_words, form_word(this_path, board))
    # If there are no words starting with this string, go back
    if len(filtered_words) == 0: 
        return list_of_paths
    # Check if we found a word
    if (checking_word_length and len(form_word(this_path, board)) == n) or (not checking_word_length and len(this_path) == n): 
        if is_word(this_path, board, words):
            list_of_paths.append(copy.deepcopy(this_path))
        return list_of_paths
    else:
        # Go over every possibility for this particular coordinate
        for next_loc in possible_moves(loc, this_path, (len(board), len(board[0]))):
            list_of_paths = find_length_helper(n, next_loc, list_of_paths, this_path, words, filtered_words, board, checking_word_length)
            this_path.pop() # Cleaning up
    return list_of_paths
            

def find_length_n_words(n: int, board: Board, words: List):
    """ This function returns all the possible paths for each word in the words dictionary """
    new_words = List[filter(lambda word: len(word) >= n, words)]
    list_of_paths = []
    for start_loc in start_coord(board):
        list_of_paths =  find_length_helper(n, start_loc, list_of_paths, [], new_words, new_words, board, True)
    return list_of_paths



def max_score_paths(board: Board, words: List):
    """ This function returns the maximal possible score for all the path in the words dictionary """
    list_of_paths = []
    words_left = []
    for index in range(16, 0, -1):
        new_words = List[filter(lambda word: len(word) == index, words)] + words_left
        if len(new_words) > 0:
            words_left = new_words
            for start_loc in start_coord(board):
                list_of_paths, words_left =  find_score_helper(index, start_loc, list_of_paths, [], words_left, words_left, board)
    return list_of_paths



def find_score_helper(n: int, loc: Tuple, list_of_paths: List[Path], this_path: Path, \
    words: List, filtered_words: List, board: Board):
    """ This function finds all possible combinations of path and returns a score """
    # Backtracking - check there are words starting with those letters, else return
    this_path.append(loc)
    filtered_words = filtered(filtered_words, form_word(this_path, board))
    # If there are no more options, return
    if len(words) == 0 or len(filtered_words) == 0:
        return list_of_paths, words
    #If we found a word, add and return
    if len(form_word(this_path, board)) == n: 
        if is_word(this_path, board, words):
            words = remove_word(words, form_word(this_path, board))
            list_of_paths.append(copy.deepcopy(this_path))
        return list_of_paths, words
    else:
        for next_loc in possible_moves(loc, this_path, (len(board), len(board[0]))):
            list_of_paths, words = find_score_helper(n, next_loc, list_of_paths, this_path, words, filtered_words, board)
            this_path.pop() # Cleaning up
    return list_of_paths, words


def init_game(board: Board, words: List):
    """ This function receives a board and reutrns all the legal paths inside this board """
    paths = []
    for n in range(1, 17):
        new_paths = find_length_n_paths(n, board, words)
        if len(new_paths) > 0:
            paths.extend(new_paths)
    return paths

    
    
