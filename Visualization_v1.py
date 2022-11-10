# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:28:40 2022

@author: laiba
"""
#Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#Reading data file
W_reps = pd.read_excel("Women in the House of Representatives.xlsx")

#Taking sample of data to be plotted
Sample1 = W_reps.iloc[41:]
print(Sample1)

#Line Plot
plt.figure()

# Plotting the line plot with magenta and red lines 
plt.plot(Sample1["Years"], Sample1["% of women (Rep)"], "m", 
         label = "% of Republican women in House")
plt.plot(Sample1["Years"], Sample1["% of women (Dem)"],"r",
         label = "% of Democratic women in House")
#Set xticks to tidy up the x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9], 
        labels = ["1999", " 2001", "2003", "2005", "2007", "2009",
                  "2011", "2013", "2015", "2017"])
#Creating labels for x and y axis
plt.xlabel("Year")
plt.ylabel("Percentage")

#Creating title for the line plot
plt.title("Women Representation in House by Party(1999-2017)")

#To show the legend labelling the lines in graph
plt.legend()

#saving the graph in my device
plt.savefig("Line Plot(Women Representation by party).png")
plt.show()


#Bar Plot
plt.figure()

#Making bar charts with the width of 0.5
plt.bar(Sample1["Years"], Sample1["% of women (Dem)"], width = 0.5, 
        label = "Democratic Women")
plt.bar(Sample1["Years"], Sample1["% of women (Rep)"], width = 0.5, 
        label = "Republican Women")

#Set xticks to tidy up the x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9], 
        labels = ["1999", " 2001", "2003", "2005", "2007", "2009",
                  "2011", "2013", "2015", "2017"])

#Creating labels for x and y axis
plt.xlabel("Years")
plt.ylabel("Percentage")

#Creating title for the line plot
plt.title("Women Representation in House by Party(1999-2017)")

#To show the legend labelling the multiple bars in graph in the upper left location
plt.legend(loc = "upper left")

#To save bar plot in my device
plt.savefig("Bar Plot(Women Representation by Party).png")
plt.show()

#Pie Chart
sample_A = sum(Sample1["% of women (Rep)"])
sample_B = sum(Sample1["% of women (Dem)"])

plt.figure()
plt.pie([sample_A, sample_B],  
        labels = ["Reublican women in House", " Democratic women in House"],
        autopct = '%1.1f%%')

#Creating title for the pie chart
plt.title("Women Representation in House by Party(1999-2017)")

#To save pie chart in my device
plt.savefig("Pie Plot(Women Representation by Party)")
plt.show()


