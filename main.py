from p_airportatlas import *
from p_airport import *
from p_aircraft import *
from p_route import *
from p_currency import *
from p_rates import *

def main():
    plane=Aircraft()
    atlas=Intinerary()
    home=input("Please enter your home airport code (i.e DUB): ")
    print("==============================================================")
    print("You will now be asked to enter 4 airport codes (i.e DUB):")
    print("==============================================================")

    code1=input("Enter 1 of 4 airports to visit: ")
    code2=input("Enter 2 of 4 airports to visit: ")
    code3=input("Enter 3 of 4 airports to visit: ")
    code4=input("Enter 4 of 4 airports to visit: ")

    print("==============================================================")
    print(plane.printAircrafts("aircraft.csv"))
    print("==============================================================")
    acode=atlas.routeCheck(home,code1,code2,code3,code4)
    print("==============================================================")
    print("The best route is via: ", atlas.gethome(home,code1,code2,code3,code4))
    print("==============================================================")
    print("Total distance: ", atlas.minDistance(home,code1,code2,code3,code4))
    print("==============================================================")
    print("Cost of the journey in Euro: ", atlas.getcost(home,code1,code2,code3,code4,acode))
    print("==============================================================")
    print(input("Press Enter to finish!"))

main()