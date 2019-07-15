import time
decision = ['Yes', 'No']
################################################################
name = input("What Can I Call You?")
time.sleep(2)
print("Very Cool Name" + name)
time.sleep(2)

decision = input("Do you want to listen to a story?")
if (decision == 'Yes') or 'yes':

    print("Very Good Choice!")
else:
    print ('REALLY? Oh Well, Maybe Next Time :)')
time.sleep (4)
###############################################################
print('Did you ever hear of Jack & Jill?')
time.sleep(3)
decision=('Did you hear what happened to them?')
if (decision == 'Yes') or 'yes':
    print("They got taught SQL by Markson")
else:
    print ('WHERE HAVE YOU BEEN!')
time.sleep(1)
###############################################################
print ('Not just the basics! He taught them Joins aswell!!')
decision=input('Do you know where they are now?')
if (decision == 'Yes') or 'yes':
    print("You do! Then you know what SQL can do to you")
else:
    print ('IT FRIED THERE BRAIN"""')

print ('Thanks for listening :)')


