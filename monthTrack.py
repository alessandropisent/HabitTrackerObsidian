import numpy
# Paths variables
pathHere = "C:/Users/aless/OneDrive - Università degli Studi di Padova/Documenti/Learn/Sistema/"
# pathHere = "C:/Users/aless/OneDrive - Università degli Studi di Padova/Documenti/Development/MDtracker/"
relativePathMonth = "1Journal/2MonthlyLog/"
relativePathDay = "1Journal/0DailyLog/"

# Months
MonthNote = "M02-2022"
DailyNotes = "2022-"+MonthNote[1:3]+"-"
gg = ["L", "M", "M", "G", "V", "S", "D"]
end = 16        #Last day of month
startDay = 1    #0=L, 1=M, ...
nHabits = 9

#Delimitatori
sHabit = "## Habits"
eHabit = "# Night reflections"

#strings to memorize
exMonth = ""
state = "start"
habits = numpy.zeros((end+1,nHabits+1))
nameHabits = ""

#Lettura del file mese pre
with open(pathHere+relativePathMonth+MonthNote+".md","r", encoding="utf-8") as f:
    exMonth = f.read()

#ora su @exMonth ci sono solo le cose scritte prima di # Trackers
exMonth = exMonth[:exMonth.find("# Trackers")-1]


for nGiorno in range(1,end+1):
    # Lettura dei file giornalieri
    with open(pathHere+relativePathDay+DailyNotes+str("%02d" % nGiorno)+".md","r", encoding="utf-8") as f:
        #lettura del giorno
        day = f.read()
        #split della stringa per mettere solo la parte delle abitudini
        day = day[day.find(sHabit)+10:day.find(eHabit)]
        lhab = day.splitlines()
        i = 0
        # funzione per lettura di abitudini check
        for line in lhab:
            # Scrittura per i nomi delle abitudini
            if nGiorno==end:
                if "]" in line:
                    nameHabits += line.split("]")[1]+"\n"

            for c in line:
                if state == "sCheck" and c == "x":
                    habits[nGiorno][i] = 1
                    state = "start"
                    break

                if c == "[" : 
                    state = "sCheck"
                
                if c == "]":
                    state = "start"
            i +=1 
                

with open(pathHere+relativePathMonth+MonthNote+".md","w", encoding="utf-8") as month:
    # Scrittura di quello che c'era gia nel file del mese
    month.write(exMonth)
    month.write("\n# Trackers \n")

    # Scrittura del header tracker
    month.write("| n°  | gg  |")
    for i in range (1,nHabits+1):
        month.write(" %02d  |" % i)
    month.write("\n|")

    #Middle line
    for i in range(nHabits+2):
        month.write(":---:|")   
    month.write("\n")
    
    #Scrittura effettiva dei gg
    for day in range (1,end+1):

        #Selezione del gg della settimana, con array circolare
        dayWeek=gg[(day+startDay-1)%7]

        month.write("| %02d  |  " % day + dayWeek + "  |")

        for n in range(nHabits):
            if habits[day][n] == 1:
                month.write("  x  |")
            else:
                month.write("     |")
        month.write("\n")

    month.write("\n## Names of the habits\n")
    i = 1
    for ha in nameHabits.splitlines():
        month.write(str(i) + ". " + ha +"\n")
        i +=1

    
