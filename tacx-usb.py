import time, sys
import trainer

def nice_exit():
    print "\nBye!!!\n"
    sys.exit(0)

while True:
    try:
        dev = trainer.get_trainer()
        if not dev:
            print "Waiting for Tacx next 5s."
            time.sleep(5)
        else:
            print "Found initializing"
            trainer.initialise_trainer(dev)
            break
    except KeyboardInterrupt:
        nice_exit()
while True:
    try:
        trainer.send(dev, 3, 0)
        time.sleep(0.3)
        speed, pedecho, heart_rate, force_index, cadence = trainer.receive(dev)
        if speed is None:
            print "No output"
            break
        else:
            print "SPEED: " + str(speed) + "\tPECHO: " + str(pedecho) + "\tHR: " + str(heart_rate) + "\tFORCE: " + str(force_index) + "\tCADENCE: " + str(cadence)
    except KeyboardInterrupt:
        nice_exit()