#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 05:53:35 2021

@author: batu
"""

class mean():
    
    def __init__(self,n):
        
        self.n=n
        self.data=[]
        
        for i in range(n):
            
            if (i+1)%20==1:
                self.data.append(int(input("Enter "+str(i+1)+" st data=")))
                
            elif (i+1)%20==2:
                self.data.append(int(input("Enter "+str(i+1)+" nd data=")))
                
            elif (i+1)%20==3:
                self.data.append(int(input("Enter "+str(i+1)+" rd data=")))
                
            else:
                self.data.append(int(input("Enter "+str(i+1)+" th data=")))
            
    def arithmetic(self):
        self.sum=0
        
        for i in range(len(self.data)):
            self.sum+=self.data[i]
            
        return float("{:.2f}".format(self.sum/len(self.data)))

    def geometric(self):
        self.mul=1
        
        for i in range(len(self.data)):
            self.mul*=self.data[i]
            
        return float("{:.2f}".format(self.mul**(1/len(self.data))))
    
    def harmonic(self):
        self.sum2=0
        
        for i in range(len(self.data)):
            self.sum2+=(1/self.data[i])
            
        return float("{:.2f}".format(len(self.data)/self.sum2))
    
    def message(self):
        print("")
        print("Mean Calculator")
        print("a: Arithmetic")
        print("g: Geometric")
        print("h: Harmonic")
        
        self.choice=input("Please enter your choice:")
        
        return self.choice
    
    def selection(self):
        self.ans='y'
        
        while self.ans=='y' or self.ans=='Y':
            mean.message(self)

            if self.choice=='a':
                
                print("Arithmetic mean= {:.2f}".format(mean.arithmetic(self)))
                
            
            elif self.choice=='g':
                
                print("Arithmetic mean= {:.2f}".format(mean.geometric(self)))
                
            
            else:
                
                print("Arithmetic mean= {:.2f}".format(mean.harmonic(self)))
                
            self.ans=input("Would you like to proceed (y/N)?= ")
            
            if self.ans=='n' or self.ans=='N':
                break
  
        
  
if __name__=="__main__":
    
    try:
        n=int(input("How many numbers?="))
        k=mean(n)        
        l=k.data
        k.selection()
        
    except ValueError:
        print("Error!... Please enter a valid number...")