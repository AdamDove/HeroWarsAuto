import time
setFindFailedResponse(SKIP)
Settings.MinSimilarity = 0.8

timePerVideo = 45

def goToTheater():
    return click("1578864027333.png")

def watchAllTheaterAds():
    while click("1578864129527.png"):
        time.sleep(timePerVideo)
        click("1578862420909.png")
        #This sleep gives the token animation time to clear the Get Ticket button.
        time.sleep(2)
    return

def watchAllFreeBoxAds():
    while not goToTheater():
        if click("1578862186245.png"):
            time.sleep(timePerVideo)
            click("1578862420909.png")
    return

def goToTheaterFromMain():
    click("1579750956755.png")
    click("1579750990714.png")
    return

def completeTheTower():
    click("1579837195304.png")
    wait("1579837315503.png")
    click("1579837340414.png")
    click("1579837363787.png")
    while (click(findBest("1579837405926.png", "1579837785595.png"))):
    click("1579837453409.png")
    if (click("1579837481622.png"))
        time.sleep(4)
    else:
        for _ in xrange(3):
            click("1579837920590.png")


completeTheTower()

#Watch all the ads
if (click("1578862062260.png")):
    watchAllFreeBoxAds()
else:
    goToTheaterFromMain()
watchAllTheaterAds()


