# -*- coding: utf-8 -*-
"""
Created on Mon May 26 23:24:11 2025

@author: omrky
"""

class Player():
    def __init__(self, firstName, lastName, age, nation):
        self.__firstName=firstName
        self.__lastName=lastName
        self.age=age
        self.nation=nation
        
    def set_firstName(self, fName):
        self.__firstName=fName
    def set_lastName(self, lName):
        self.__lastName=lName
    def set_age(self, age):
        self.age=age
    def set_nation(self, nation):
        self.nation=nation
        
    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def get_age(self):
        return self.age
    def get_nation(self):
        return self.nation
        
    def print_player(self):
        print("First Name: ",self.get_firstName())
        print("Last Name: ",self.get_lastName())
        print("Age: ",self.get_age())
        print("Nation: ",self.get_nation())
        
class LeaguePlayer(Player):
    def __init__(self, firstName, lastName, age, nation, branch, game_num, win_num, lost_num, player_score):
       Player.__init__(self, firstName, lastName, age, nation)
       
       self.__branch=branch
       self.__game_num=game_num
       self.__win_num=win_num
       self.__lost_num=lost_num
       self.__player_score=player_score
    
    def set_branch(self, branch):
        self.__branch=branch    
    def set_game_num(self, game_num):
        self.__game_num=game_num
    def set_win_num(self, win_num):
        self.__win_num=win_num
    def set_lost_num(self, lost_num):
        self.__lost_num=lost_num
    def set_player_score(self, player_score):
        self.__player_score=player_score
    
    def get_branch(self):
        return self.__branch 
    def get_game_num(self):
        return self.__game_num
    def get_win_num(self):
        return self.__win_num
    def get_lost_num(self):
        return self.__lost_num
    def get_player_score(self):
        return self.__player_score
    
    def print_player(self):
        super().print_player()
        print("Branch: ",self.get_branch())
        print("Number of played league game: ",self.get_game_num())
        print("Number of win league game: ",self.get_win_num())
        print("Number of lost league game: ",self.get_lost_num())
        print("Number of player score: ",self.get_player_score())
    
    def statistics(self):
        statistics = self.get_player_score() / self.get_game_num()
        print("Score per league game: ",statistics)
    
    def points(self):
        points=10*self.get_game_num()+3*self.get_win_num()-2*self.get_lost_num()
        return points
    
class NationalPlayer(LeaguePlayer):
    def __init__(self, firstName, lastName, age, nation, branch, game_num, win_num, lost_num, player_score, nationalGame_num, nationalPlayer_score):
        LeaguePlayer.__init__(self, firstName, lastName, age, nation, branch, game_num, win_num, lost_num, player_score)
        self.__nationalGame_num=nationalGame_num
        self.__nationalPlayer_score=nationalPlayer_score
        
    def set_nationalGame_num(self,nationalGame_num):
        self.__nationalGame_num=nationalGame_num
    def set_nationalPlayer_score(self,nationalPlayer_score):
        self.__nationalPlayer_score=nationalPlayer_score

    def get_nationalGame_num(self):
        return self.__nationalGame_num
    def get_nationalPlayer_score(self):
        return self.__nationalPlayer_score

    def print_player(self):
        super().print_player()
        print("Number of played national game: ",self.get_nationalGame_num())
        print("Number of played national score: ",self.get_nationalPlayer_score())
    def statistics(self):
        statistics = self.get_nationalPlayer_score() / self.get_nationalGame_num()
        print("Scores per national game: ",statistics)
    
    def points(self):
        points=15*self.get_nationalGame_num()+10*self.get_game_num()+3*self.get_win_num()-2*self.get_lost_num()
        print("Player Points: ",points)
