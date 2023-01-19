import time
import sys
import pync


# TODO: Break code into functions
def pomodoro():
    work_time = int(sys.argv[1])
    break_time = int(sys.argv[2])
    interval = int(sys.argv[3])

    pync.notify("Timer has started! ⏳", title = "Pom-CLI")

    for k in range(interval, -1, -1):
        for i in range(work_time, -1, -1):
            time.sleep(1 * 60)

        pync.notify("Work timer has ended! ✨", title = "Pom-CLI")

        for j in range(break_time, -1, -1):
            time.sleep(1 * 60)

        pync.notify("Break timer has ended! ✨", title = "Pom-CLI")

    pync.notify("You have finished all work blocks! 🏁", title = "Pom-CLI")


if __name__ == "__main__":
    pomodoro()
