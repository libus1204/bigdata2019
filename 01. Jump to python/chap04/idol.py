#-*- coding: utf-8 -*-
f=open("./연습생.txt", 'r')
candidate_list = f.readlines()
f.close()

def show_candidates(candidate_list):
    for list in candidate_list:
        print(list, end="")
    print("")

def make_idol(candidate_list):
     for list in candidate_list:
         print("신예 아이돌 "+list[:2]+" 인기 급상승")

def make_world_star(candidate_list):
    for list in candidate_list:
        print("아이돌 "+list[:2]+" 월드스타 등극")

show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)