import random
import xlwt

def exportExcel(batch, trials, score, zeroes):
    sheet.write(batch, 0, batch)
    sheet.write(batch, 1, trials)
    sheet.write(batch, 2, score)
    sheet.write(batch, 3, zeroes)
    
def runTrials(trials, batch):
    score = 0
    zeroes = 0
    for trial in range(0, trials):
        trial += 1
        win = random.randint(0,1)
        if win == 1:
            score += 1
        else:
            score -= 1
        if score == 0:
            zeroes += 1
            print("The score has become zero at trial {0}, occuring {1} times in total".format(trial, zeroes))
    print("The {0} trial experiment yielded a final score of {1}, with {2} total occurances of 0".format(trials, score, zeroes))
    number = 1
    exportExcel(batch, trials, score, zeroes)

def runExperiment(trials, repeats, fileName):

    book = xlwt.Workbook()
    global sheet
    sheet = book.add_sheet("Results")
    sheet.write(0, 0, "Batch")
    sheet.write(0, 1, "Trials")
    sheet.write(0, 2, "Score")
    sheet.write(0, 3, "Zeroes")
    
    for batch in range(1, repeats + 1):
        runTrials(trials, batch)
    
    book.save("{}.xls".format(fileName))

trials = int(input("How many trials do you want? "))
repeats = int(input("How many times should this set of trials be repeated? "))
fileName = input("Under what filename should the exported file be saved under? ")
runExperiment(trials, repeats, fileName)
