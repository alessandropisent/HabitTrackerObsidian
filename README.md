# HabitTrackerObsidian
Create a table with habit done in daily note

## Variables to modify
```python
pathHere          # Here it goes your absolute path to osidian vault
relativePathMonth # Here it goes your relative path to the mothly note
relativePathDay   # Here it goes your relative path to the daily note

MonthNote         # Here it goes the name of your mothly note that you want to modify M02-2022
gg                # Array with the names of the days of the week
end               # Last day of the month i.e. 28 for February
startDay          # 0 = Monday, 1 = Tuesday, ... 6 = Sunday
nHabits           # Number of habits that you are tracking

# Delimitators
sHabits           # Title of the start of the checklist of habits
eHabits           # The next delimitator to habits
```

## Examples 
### Examples of the dailynote template :
```
# <% tp.date.now("dddd DD-MM-YY") %>
----

![[<%tp.date.now("YYYY-MM-DD", -1)%>## Improve]]
## Morning page
- 

## Sogni
-

# General todo
#daily
- [ ] 

# Day
- (o) 

## Habits
- [ ] Habit 1
- [ ] Babit 2
- [ ] Habit 3
- [ ] Habit 4
- [ ] Habit 5
- [ ] Habit 6
- [ ] Habit 7
- [ ] Habit 8
- [ ] Habit 9



# Night reflections
## Improve
-

## Proude
-

## Gratitutude
1.
2. 
3.

## Thoughts
- 
```

---

## Examples of the mothly 


... Some text that will be kept

# Trackers 
| n°  | gg  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 01  |  M  |     |     |     |     |     |     |     |     |     |
| 02  |  M  |  x  |     |  x  |  x  |  x  |     |     |  x  |  x  |
| 03  |  G  |  x  |  x  |  x  |  x  |  x  |     |     |  x  |  x  |
| 04  |  V  |  x  |     |  x  |  x  |  x  |     |  x  |     |  x  |
| 05  |  S  |  x  |     |  x  |  x  |  x  |     |     |     |  x  |
| 06  |  D  |     |  x  |  x  |  x  |  x  |  x  |     |     |     |
| 07  |  L  |     |     |  x  |  x  |  x  |     |  x  |  x  |  x  |
| 08  |  M  |     |     |  x  |  x  |  x  |     |  x  |     |     |
| 09  |  M  |  x  |  x  |  x  |  x  |     |  x  |  x  |  x  |     |
| 10  |  G  |  x  |     |  x  |  x  |     |     |  x  |     |     |
| 11  |  V  |  x  |     |  x  |  x  |  x  |     |     |     |     |
| 12  |  S  |  x  |     |  x  |  x  |  x  |     |  x  |     |     |
| 13  |  D  |  x  |     |  x  |  x  |     |     |  x  |  x  |  x  |
| 14  |  L  |  x  |  x  |  x  |  x  |  x  |     |     |     |     |
| 15  |  M  |  x  |     |  x  |     |  x  |     |     |     |  x  |
| 16  |  M  |  x  |  x  |  x  |     |  x  |     |     |     |  x  |

## Names of the habits
1. Habit 1
2. Habit 2
3. Habit 3
4. Habit 4
5. Habit 5
6. Habit 6
7. Habit 7
8. Habit 8
9. Habit 9
