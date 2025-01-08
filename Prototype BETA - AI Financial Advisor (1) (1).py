import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
import time
import math
import csv
import random


#NOTICE: my code is really messy, im sorry if i cause you a headache
#LAST MODIFIED: 2024-12-28: 1:20PM


DONEINT = False

oneQ = ""
twoQ = ""
threeQ = ""
fourQ = ""

AI_QUESTION = ""

root = tk.Tk()
root.geometry("1600x1200")

root.title("AI Financial Advisor")


sp500 = yf.Ticker('^GSPC')
data = sp500.history(period='5d')

price_at_start = data['Close'].iloc[-2]
price_now = data['Close'].iloc[-1]
per = round((((price_now - price_at_start) / price_at_start) * 100), 2)

Heading = tk.Label(root, text="Welcome to The AI Financial Advisor! \n Powered by yfinance™", font=('Elephant', 40))
Heading.pack(padx=0, pady=30)
time.sleep(5)
Question = tk.Label(root, text="\n What would you like to do today? \n 1. For Advice (S&P 500 is going up/down by %" + str(per) + " today.) \n 2. Saved stocks \n 3. Interview \n 4. About This Project \n 5. Search \n \n TYPE HERE (1,2,3,4,5): ", font=('Aparajita', 20))
Question.pack(padx=0, pady=30)

option = tk.Entry(root)
option.pack(padx=0, pady=10)

Thing_wtd = "0"

tkr = tk.Text(root, height=1, width=3, font=('Arial', 20))
tkr.pack()

#what... oh yeah, while true loops could crash..... It should be fine...... right?, . . . RIGHT?
while True:

    if Thing_wtd == "0":
        print("Welcome to The AI Financial Advisor! Powered by yfinance™")
        time.sleep(0.8)
        root.mainloop()

        Thing_wtd = input("\n What would you like to do today? \n 1. For Advice (S&P 500 is going up/down by %" + str(per) + " today.) \n 2. Saved stocks \n 3. Interview \n 4. About This Project \n 5. Search \n \n TYPE HERE (1,2,3,4,5): ")

    if Thing_wtd == "1":

        if DONEINT == True:

            #AI CODE:


            #API MODULE
            from openai import OpenAI

            

            QUESTION_STARTERS = ["Ask Away, Investing is my Middle Name!", "Today is a Great Day to invest, Got any ideas?", "Got cash questions? I’ve got cents-able answers!"] 

            AI_QUESTION = input(random.choice(QUESTION_STARTERS) + " \n \n Type Prompt Here: ")

            fullq = AI_QUESTION + " If you need to know, my overall budget for my career of investing is " + oneQ + ", and my main investment sector is " + twoQ + ", and if you need to know, my favourite stock(s) are " + fourQ + "."

            #MY API KEY:
            client = OpenAI(
              api_key="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"
            )

            completion = client.chat.completions.create(
              model="gpt-4o-mini",
              store=True,
              messages=[
                {"role": "system", "content": "You are an AI Financial Advisor, and first you answer their question, then you go into detail / advice"},
                    {
                        "role": "user",
                        "content": fullq
                    }])

            print("Loading.")
            time.sleep(0.1)
            print("Loading..")
            time.sleep(0.1)
            print("Loading...")
            time.sleep(0.1)
            print("Loading.")
            time.sleep(0.02)
            print("Loading..")
            time.sleep(0.02)
            print("Loading...")
            time.sleep(0.75)
            #Use slicing method: string[x: y: z]
            essagmeh = str(completion.choices[0].message)
            essagmeh2 = essagmeh[31:-83]
            print(essagmeh2)
            time.sleep(10)
            print("Sending you bck to homepage...")
            
            Thing_wtd = "0"
        else:

            print("First, complete the interview... \n \n \n ")

            time.sleep(2)

            Thing_wtd = "3"
        
    if Thing_wtd == "3":
        time.sleep(0.1)
        print("Loading.")
        time.sleep(0.3)
        print("Loading..")
        time.sleep(0.3)
        print("Loading...")
        time.sleep(0.3)
        print("Loading.")
        time.sleep(0.1)
        print("Loading..")
        time.sleep(0.1)
        print("Loading...")
        time.sleep(0.1)

        print("\n Question 1 out of 4: What is your budget? (How much money are you willing to invest)")
        time.sleep(1)
        print("A. $1,000 or UNDER")
        time.sleep(0.3)
        print("B. $1,000-$10,000")
        time.sleep(0.3)
        print("C. $10,000-$50,000")
        time.sleep(0.3)
        print("D. $50,000 or MORE")
        time.sleep(0.3)

        Q1 = input("Type Here (A/B/C/D): ")
        
        if Q1 == "A":
            oneQ = "$1,000 or UNDER"
        if Q1 == "B":
            oneQ = "$1,000-$10,000"
        if Q1 == "C":
            oneQ = "10,000-$50,000"
        if Q1 == "D":
            oneQ = "$50,000 or MORE"

        print("\n Question 2 out of 4: What is your main investment sector? (What type of company services do you mainly invest in)")
        time.sleep(1)
        print("A. Technology Sectors: (AAPL, MSFT, NVDA)")
        time.sleep(0.3)
        print("B. Financial Sectors: (JAM, BAC, V)")
        time.sleep(0.3)
        print("C. Healthcare Sectors: (JNJ, PFE, UNH)")
        time.sleep(0.3)
        print("D. Consumer Sectors: (AMZN, TSLA, HD)")
        time.sleep(0.3)

        Q2 = input("Type Here (A/B/C/D): ")

        if Q2 == "A":
            twoQ = "Technology Sectors: (AAPL, MSFT, NVDA)"
        if Q2 == "B":
            twoQ = "Financial Sectors: (JAM, BAC, V)"
        if Q2 == "C":
            twoQ = "Healthcare Sectors: (JNJ, PFE, UNH)"
        if Q2 == "D":
            twoQ = "Consumer Sectors: (AMZN, TSLA, HD)"

        print("\n Question 3 out of 4: DONT DO THIS QUESTION YET (How much money are you willing to invest)")
        time.sleep(1)
        print("A. 1,000 or UNDER")
        time.sleep(0.3)
        print("B. 1,000-10,000")
        time.sleep(0.3)
        print("C. 10,000-50,000")
        time.sleep(0.3)
        print("D. 50,000 or MORE")
        time.sleep(0.3)

        Q3 = input("Type Here (A/B/C/D): ")
        
        print("\n Question 4 out of 4: What are some of your favourite stocks? (What are some stocks you want to invest in)")
        time.sleep(1)

        Q4 = input("Type Here (E.G. WMT, SOFI or TSLA, NVDA): ")

        #dont ask, it just follows the pattern
        fourQ = Q4
        
        time.sleep(0.5)

        print("\n Thanks for taking the interview, sending you back to the Homepage... ")

        DONEINT = True

        time.sleep(3)

        Thing_wtd = "0"
        
        print("========================================================================================================================================================================================================================================")

        
    if Thing_wtd == "5":
        results = 0
        while results == 0:
            search = input("Search for tickers on N.Y.S.E. (E.G. LMT)")
            time.sleep(0.1)
            print("Loading.")
            time.sleep(0.3)
            print("Loading..")
            time.sleep(0.3)
            print("Loading...")
            time.sleep(0.3)
            print("Loading.")
            time.sleep(0.1)
            print("Loading..")
            time.sleep(0.1)
            print("Loading...")
            time.sleep(0.1)

            matches = []
            with open('NYSE-ALL-FUL.csv') as file:
                reader = csv.reader(file)
                stuff_in_nyse = list(reader)
            for numot in stuff_in_nyse:
                if search in numot:
                    matches.append(numot)
            results = str(len(matches))
            print("Found: " + results + " result(s)")
            if results == "0":
                print("INVALID TICKER")
        print(matches)
        a = input("PERIOD: 1d, 5d, 1mo, 3mo, 6mo, ytd, 1y, 2y, 5y, 10y, max: \n")
        tickerer = (str(matches[0]))[2:-2]
        otu = yf.download(tickerer, period=a)
        oes = yf.Ticker(tickerer)
        print(oes)
        sete = oes.info["longName"] + " Stock Graph"

        otu = otu['Close'].dropna()
        otu = otu[np.isfinite(otu)]
        y = np.array(otu.values)
        x = np.arange(len(y))
        x_scaled = x / np.max(x)
        y_scaled = y / np.max(y)
        z = np.polyfit(x_scaled, y_scaled, 1)
        trendline = z[0] * x_scaled + z[1]
        initial_price = y_scaled[0]
        final_price = x_scaled[-1]
        print(str(initial_price))
        percent_change = int(((final_price - initial_price) / initial_price) * 100)
        print(f"The stock price has changed by {percent_change:.2f}% over the selected period.")
        weg = input("What increase over a certian period do you want to estimate? (1d, 5d, 1mo, 3mo, 6mo, ytd, 1y, 2y, 5y, 10y, max)\n")
        www = yf.download(tickerer, period=weg)
        hehe = yf.Ticker(tickerer)
        www = www['Close'].dropna()
        www = www[np.isfinite(www)]
        alp = np.array(www.values)
        bet = np.arange(len(alp))
        ex_scaled = bet / np.max(bet)
        why_scaled = alp / np.max(alp)
        zee = np.polyfit(ex_scaled, why_scaled, 1)
        trendline2 = zee[0] * ex_scaled + z[1]
        initial_price2 = why_scaled[0]
        final_price2 = ex_scaled[-1]
        percent_change2 = int(((final_price2 - initial_price2) / initial_price2) * 100)
        print("The stock is estimated to increase by: " + str(percent_change2) + "% in " + str(weg) + " days.")
        plt.figure(figsize=(10, 5))
        plt.plot(otu.index, y, label='Close Price')
        plt.plot(otu.index, trendline * np.max(y), label='Trendline', linestyle='--', color='orange')
        plt.title(sete + " Over: " + a)
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.show()
        gpthp = ""
        
        while gpthp == "N":
            gbthp = input("\n \n Would you like to go back to the homepage? (Y/N) \n Type here:")
        Thing_wtd = "0"
        
