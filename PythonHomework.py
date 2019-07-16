import time
decision = ['Yes']
decision2 = ['No']
decision3 = ['Kids Version']
decision4 = ['Scary Version']

################################################################
name = input("What Can I Call You?")
time.sleep(2)
print("Very Cool Name" + name)
time.sleep(2)

decision = input("Do you want to listen to the Kids Version or the Scary Version?")
if (decision3 == 'Kids Version') or decision == 'kids version':
    print("Very Good Choice!")
elif (decision4 == 'Scary Version') or decision2 =='scary version':
    print ('WOW! your brave!)')
time.sleep (4)
###############################################################
print('Did you ever hear of Jack & Jill?')
time.sleep(3)
decision=('Did you hear what happened to them?')
if (decision == 'Yes') or decision == 'yes':
    print("They got taught SQL by Markson")
elif(decision2 == 'No') or decision2 == 'no':
    print ('WHERE HAVE YOU BEEN!')
decision=input('Do you know where they are now?')
if (decision == 'Yes') or decision == 'yes':
    print("You do! Then you know what SQL can do to you")
elif(decision2 == 'No') or decision2 == 'no':
    print ('IT FRIED THERE BRAIN"""')

print ('Thanks for listening :)')


