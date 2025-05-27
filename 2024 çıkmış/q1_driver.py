# -*- coding: utf-8 -*-
"""
Created on Mon May 26 23:50:09 2025

@author: omrky
"""

import q1_ben as C

def main():
    my_player= C.Player("Fabian", "Delph", 22, "England")
    my_player.print_player()
    print("\n")
    
    my_player_2= C.LeaguePlayer("Tony", "Parker", 28, "France", "Basketball", 36, 17, 19, 22)
    my_player_2.print_player()
    my_player_2.statistics()
    print("Player points: ",my_player_2.points(),"\n")
    
    my_player_3= C.NationalPlayer("Jordan", "Larson", 22, "USA", "Volleyball", 21, 16, 5, 36, 8, 3)
    my_player_3.print_player()
    my_player_3.statistics()
    my_player_3.points()

main()
    
    