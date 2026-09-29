# mumbai metro ticketing system

a simple terminal project made in python that acts like a metro ticket counter it lets users pick a metro line plan a route see stops and pay using cash or metro smart card

---

## what it does

this is a basic college project made using basic python concepts like loops dicts and functions without any external libaries the project has 4 files

* stations.py has the list of stations and metro lines
* route.py finds the path and counts total stops
* fare.py calculates the fare based on stops and rush hour
* main.py runs the main menu loop and user inputs

---

## tech used

* python 3
* vs code or any basic text editor
* basic concepts like while loops if else conditions list and dictionary
* no extra packages or pip install needed just pure standard python

---

## main features

* choose from blue line 1 yellow line 2a and red line 7
* works even if you type station name in small or capital letters
* works for both forward and reverse journy
* fare prices based on stops
  * 1 to 2 stops rs 10
  * 3 to 5 stops rs 20
  * 6 to 7 stops rs 30
  * more than 7 stops rs 40
* 10% extra rush hour charge during morning 8 to 10 and evning 17 to 20
* supports smart card deduction and cash option

---

## how to run

1 download all the files and put them in one single folder
2 open command prompt or terminal in that folder
3 run this command

```bash
python main.py
```

---

## test cases to check

test 1 normal route
* run option 1 select line 1
* enter start as versova and destination as andheri
* enter hour 14
* check if it gives 3 stops and rs 20 fare

test 2 rush hour charge
* run option 1 and enter line 1
* pick versova to ghatkopar
* enter hour 9 (peak time)
* check if 10% rush charge is added to total

test 3 low balnce card test
* choose to pay by card
* enter balance lower than total fare
* it should show not enough balance error