from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import csv


#A function to store the days of the week and loop trought them
def weekday(days,x):
    lista = [i for i in days]
    
    if x == 0:
        return lista[0]
    elif x == 1:
        return lista[1]
    elif x == 2:
        return lista[2]
    elif x == 3:
        return lista[3]
    elif x == 4:
        return lista[4]
    elif x == 5:
        return lista[5]
    elif x == 6:
        return lista[6]
    
#We pick the url
url = "https://www.timeanddate.com/weather/chile/santiago"

#the headings so the site does not throws us a 403 Error
headings = {"User-Agent":"Mozilla/5.0"}

#We past the url and headers to the Request function
req = Request(url,headers=headings)

#We open our req variable with urlopen
page = urlopen(req)

#We parse it with BeatifulSoup
soup = BeautifulSoup(page,"html.parser")

#We select the "containers" than contain the we element we want
containers = soup.findAll("div",{"class":"fixed"})[7]

#create a list of days for our function to work
days = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"]

#Our headers with the day, month and the max/min temps
print("  Día","  ","   Mes","  Max / Min")

#we initialize a for loop with the len of the "containers" so that does throw us an out of range index
for x in range(1,len(containers) + 1):
    
    #Now for each container we'll take the weather rows to print our information
    weather_rows = containers.findAll("tr")[x]
    if x == 1:
        
        #The num variable is to select our initial day
        num = ["0","1","2","3","4","5","6"]
        
        #This is to set up the max number of possible days
        whole_week = 7
        
        #This selects a number corresponding to the days in the weather rows
        day = len(weather_rows.findAll("td",{"class":"wa"}))
        
        #And now we sustract the day to the whole week to get our current day
        number = int(num[whole_week - day])
        
        #We now loop the information from our weather row
        for i in range(0,len(weather_rows.findAll("td",{"class":"wa"}))):
            
            #We extract the text information
            info_rows = weather_rows.findAll("td",{"class":"wa"})[i]
            
            #We select the weather info and the day and we separate them
            weather_info = info_rows.p.text
            day = info_rows.findAll("div",{"class":"wt-dn"})[0].text
            
            #Now we call the weekday function to get our day of the week
            day_of_the_week = weekday(days,number)
            
            #We set up a fallback so that our function does not throws an out of range index error
            if number == 7:
                number = 0
                
            #The next if statements are only for stetics choices
            if number == 0:
                if int(day) <= 9:
                    print(day_of_the_week,"    | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
            elif number == 1:
                if int(day) <= 9:
                    print(day_of_the_week,"   |",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"   |",day,"","|",weather_info)
                    
            elif number == 2:
                if int(day) <= 9:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"|",day,"","|",weather_info)

            elif number == 3:
                if int(day) <= 9:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"   |",day,"","|",weather_info)
                    
            elif number == 5:
                if int(day) <= 9:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"   |",day,"","|",weather_info)
                    
            elif number == 4:
                if int(day) <= 9:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"  |",day,"","|",weather_info)
                    
            elif number == 6:
                if int(day) <= 9:
                    print(day_of_the_week,"  | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"  |",day,"","|",weather_info)

            #And finally we increment our number variable so that our weekday function get us the next day properly
            number += 1
            
    #We recreat the same proccess as x == 1
    if x == 2:
        number = 0
        for i in range(0,7):
            info_rows = weather_rows.findAll("td",{"class":"wa"})[i]
            
            weather_info = info_rows.p.text
            day = info_rows.findAll("div",{"class":"wt-dn"})[0].text
            
            day_of_the_week = weekday(days,number)
            
            if number == 7:
                number = 0
            
            if number == 0:
                if int(day) <= 9:
                    print(day_of_the_week,"    | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
            elif number == 1:
                if int(day) <= 9:
                    print(day_of_the_week,"   | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"   |",day,"","|",weather_info)
                    
            elif number == 2:
                if int(day) <= 9:
                    print(day_of_the_week,"| ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"|",day,"","|",weather_info)
                    
            elif number == 3:
                if int(day) <= 9:
                    print(day_of_the_week,"   | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"   |",day,"","|",weather_info)
                    
            elif number == 4:
                if int(day) <= 9:
                    print(day_of_the_week,"  | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"   |",day,"","|",weather_info)
                    
            elif number == 5:
                if int(day) <= 9:
                    print(day_of_the_week,"   | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"  |",day,"","|",weather_info)
                    
            elif number == 6:
                if int(day) <= 9:
                    print(day_of_the_week,"  | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"  |",day,"","|",weather_info)
                    
            number += 1
            
    #We recreat the same proccess as x == 2
    if x == 3:
        number = 0
        for i in range(0,len(weather_rows.findAll("td",{"class":"wa"}))):
            info_rows = weather_rows.findAll("td",{"class":"wa"})[i]
            weather_info = info_rows.p.text
            
            day = info_rows.findAll("div",{"class":"wt-dn"})[0].text
            
            day_of_the_week = weekday(days,number)

            if number == 7:
                number = 0
            
            if number == 0:
                if int(day) <= 9:
                    print(day_of_the_week,"    | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"     |",day,"","|",weather_info)
            elif number == 1:
                if int(day) <= 9:
                    print(day_of_the_week,"    | ",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                    
            elif number == 2:
                if int(day) <= 9:
                    print(day_of_the_week,"  |",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                    
            elif number == 3:
                if int(day) <= 9:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                    
            elif number == 5:
                if int(day) <= 9:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                    
            elif number == 4 or number == 6:
                if int(day) <= 9:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                else:
                    print(day_of_the_week,"    |",day,"","|",weather_info)
                    
            number += 1