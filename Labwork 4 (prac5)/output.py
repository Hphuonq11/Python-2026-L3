import curses

def showStudents(stdscr, Students):
    for i in range(len(Students)):
        stdscr.addstr(i, 0, "Student " + str(i + 1))
        stdscr.addstr(i + 1, 0, "ID: " + str(Students[i].ID))
        stdscr.addstr(i + 2, 0, "Name: " + Students[i].Name)
        stdscr.addstr(i + 3, 0, "DOB: " + Students[i].DOB)