# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:09:12 2015

@author: Dani Bento
"""

# código do jogo da forca - Daniela Bento P. da Cunha

import turtle
window = turtle.Screen() 
window.title("Jogo da Forca!")
window.bgcolor("skyblue")

tortugaL = turtle.Turtle()
tortugaL.pen(shown =False,fillcolor="purple",pencolor="purple")
tortugaL.penup()

arquivo = open("entrada.txt", encoding="utf-8")
p = arquivo.readlines()
lpalavras = []
for i in p:
    g = i.strip()
    if g != "":
        lpalavras.append(g)

n = len(lpalavras)-1

from random import randint

pn = randint(0,n)
palavra = lpalavras[pn]
PALAVRA = palavra.upper()
del lpalavras[pn]

x = len(palavra)
gap = []

LETRA = ["A","Ã","Á","B","C","D","E","É","Ê","F","G","H","I","Í","J","K","L","M","N","O","Õ","Ô","Ó","P","Q","R","S","T","U","Ú","V","W","X","Y","Z"]

letra = ["a","ã","á","b","c","d","e","é","ê","f","g","h","i","í","j","k","l","m","n","o","õ","ó","ô","p","q","r","s","t","u","ú","v","w","x","y","z"]

comeca = 0
while comeca != -1:
    comeca = palavra.find(" ", comeca)
    gap.append(comeca)
    if comeca!= -1:
        comeca += 1
        
del gap[-1]

tortugah = turtle.Turtle()
tortugah.penup()
tortugah.pen(shown =False,fillcolor="purple",pencolor="purple")
tortugah.pensize(3)
tortugah.setpos(-250, -250)
tortugah.pendown()
tortugah.left(90)
tortugah.forward(300)
tortugah.right(90)
tortugah.forward(100)
tortugah.right(90)
tortugah.forward(55)
tortugah.penup()

tortugae = turtle.Turtle()
tortugae.pen(shown =False,fillcolor="black",pencolor="black")

letras = []
i = 0
t = 0
acertos = 0
erros = 0
tents = []

cabeca = 0
tronco = 0
braco1 = 0
braco2 = 0
perna1 = 0 
perna2 = 0

while t != x:
    letras.append(palavra[t].upper())
    t = t+1

tortugaT = turtle.Turtle()
tortugaT.speed(10)
tortugaT.pen(shown =False,fillcolor="black",pencolor="black")
tortugaT.penup()
tortugaT.setpos(-350, 10)
tortugaT.color("purple")

while i != x:
    tortugaT.setpos(i*28-x*15,-200)
    if palavra[i] == " " :
        tortugaT.write(" ", False, align="center",font=("Arial",17))
    else:
        tortugaT.write(" _   ", False, align="center",font=("Arial",17))
    i = i+1
