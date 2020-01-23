import time
setFindFailedResponse(SKIP)
Settings.MinSimilarity = 0.8


def goToTheater():
    return click("1578864027333.png")

def watchAllTheaterAds():
    while click("1578864129527.png"):
        time.sleep(45)
        click("1578862420909.png")
        time.sleep(2)
    return

def watchAllFreeBoxAds():
    while not goToTheater():
        if click("1578862186245.png"):
            time.sleep(45)
            click("1578862420909.png")
    return

def goToTheaterFromMain():
    click("1579750956755.png")
    click("1579750990714.png")
    return

#Enter Free Boxes
if (click("1578862062260.png")):
    watchAllFreeBoxAds()
else:
    goToTheaterFromMain()
watchAllTheaterAds()

