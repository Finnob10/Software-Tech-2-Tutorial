count = 0  
def main():
    n = eval(input("Enter number of disks: "))
    print("The moves are:")
    moveDisks(n, 'A', 'B', 'C')    
    print(f"there are {count} iterations required")

def moveDisks(n, fromTower, toTower, auxTower): 
    global count 
    if n == 1:  # Stopping condition
        print("Move disk", n, "from", fromTower, "to", toTower) 
        count +=1 
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk", n, "from", fromTower, "to", toTower)
        moveDisks(n - 1, auxTower, toTower, fromTower) 
        count +=1  
    



main()