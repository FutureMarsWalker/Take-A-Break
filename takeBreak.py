# Its Good To Take a Break!!!

import sys
import time
# import webbrowser  # One can use this to open a web page instead of an alert box.
import pyautogui

sleepPeriod = int(input("Timer duration in full mins: "))
repeatCounter = int(input("How many timer repetitions: "))
iterable = sleepPeriod
counter = 0


while counter < repeatCounter:
    print("\nTimer started...")
    minCounter = 1
    iterable = sleepPeriod

    while iterable != 0:
        time.sleep(60)
        '''if minCounter % 10 == 0:  # This code does not print the numbers one after another.
            print(minCounter)
        else:
            print(minCounter, end=" ")'''
        if minCounter % 10 == 0:  # This code does print the numbers one after another.
            sys.stdout.write(str(minCounter))
        else:
            sys.stdout.write(str(minCounter) + ' ')
        sys.stdout.flush()
        iterable -= 1
        minCounter += 1

    pyautogui.alert(text='Get UP!', title='Reminder', button='Done')
    # webbrowser.open_new("https://www.youtube.com/watch?v=7KXGZAEWzn0")
    counter += 1
