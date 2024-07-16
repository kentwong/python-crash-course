"""
// Define a recursive function for solving the Tower of Hanoi puzzle
FUNCTION hanoi(disks, source, helper, destination)
    // Check if there is only one disk to move
    IF disks EQUALS 1 THEN
        // Print the move of this single disk from source to destination
        PRINT "Disk 1 moves from tower [source] to tower [destination]."
        RETURN
    ENDIF

    // Move the top n-1 disks from source to helper, using destination as a temporary storage
    CALL hanoi with (disks - 1, source, destination, helper)

    // Move the remaining disk from source to destination
    PRINT "Disk [disks] moves from tower [source] to tower [destination]."

    // Move the n-1 disks from helper to destination, using source as a temporary storage
    CALL hanoi with (disks - 1, helper, source, destination)
END FUNCTION

// Main part of the program that drives the solution
// Ask the user for the number of disks
READ number of disks into disks

// Call the hanoi function with the number of disks and tower names A, B, C as source, helper, and destination respectively
CALL hanoi with (disks, "A", "B", "C")
"""

# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')