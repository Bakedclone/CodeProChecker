from tkinter import *
from PIL import ImageTk, Image
import bs4, requests

def show_frame(frame):
    frame.tkraise()

window = Tk()

window.title('CodeProChecker')
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
window.geometry('1200x700')
window.resizable(0,0)

home = Frame(window)
leetcode = Frame(window)
codeforces = Frame(window)
codechef = Frame(window)

for frame in (home, leetcode, codeforces, codechef):
    frame.grid(row=0, column=0, sticky='nsew')

homebg = Image.open('./images/homebg.jpg')
imgbg = Image.open('./images/background.jpg')
bg = ImageTk.PhotoImage(imgbg)
homebg1 = ImageTk.PhotoImage(homebg)
bglabel = Label(home, image=homebg1)
bglabel.place(x = 0,y = 0)
bglabel = Label(leetcode, image=bg)
bglabel.place(x = 0,y = 0)
bglabel = Label(codeforces, image=bg)
bglabel.place(x = 0,y = 0)
bglabel = Label(codechef, image=bg)
bglabel.place(x = 0,y = 0)

header = Label(home, text='Welcome to CodeProChecker')
header.config(font=('Arial Rounded MT Bold',36),foreground='black',bg='white')
header.grid(row=0, column=0, padx=(230), pady=(80,40))

leetcode_ico = PhotoImage(file='./images/leetcode.png')
leetcode_lbl = Label(image=leetcode_ico)
leetcode_btn = Button(home, image=leetcode_ico, bg='white', command=lambda:show_frame(leetcode), borderwidth=0)
leetcode_btn.grid(row=1, column=0, pady=(40,0))

codeforces_ico = PhotoImage(file='./images/codeforces.png')
codeforces_lbl = Label(image=codeforces_ico)
codeforces_btn = Button(home, image=codeforces_ico, bg='white',command=lambda:show_frame(codeforces), borderwidth=0)
codeforces_btn.grid(row=2, column=0, pady=(0,0))

codechef_ico = PhotoImage(file='./images/codechef.png')
codechef_lbl = Label(image=codechef_ico)
codechef_btn = Button(home, image=codechef_ico, bg='white',command=lambda:show_frame(codechef), borderwidth=0)
codechef_btn.grid(row=3, column=0, pady=(0,0))


# ========== Leetcode =========== 


def handle_submit_lc():
    global url
    url = 'https://leetcode.com/' + username_ip1.get() + '/'
    source = requests.get(url)
    print(source.status_code)
    if source.status_code == 200:
        try:
            source = source.text
            soup = bs4.BeautifulSoup(source,'html.parser')

            name_lbl = Label(leetcode, text='Name :',anchor="w",justify="left")
            name_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            name_lbl.grid(row=2, column=0, padx=(10), pady=(40, 0))
            
            Username = soup.find('div',{'class':'text-label-1 dark:text-dark-label-1 break-all text-base font-semibold'}).text
            name = Label(leetcode, text=Username)
            name.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            name.grid(row=2, column=1, padx=(10), pady=(40, 0))

            rank_lbl = Label(leetcode, text='Rank :')
            rank_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            rank_lbl.grid(row=3, column=0, padx=(10), pady=(25, 0))

            Rank = soup.find('span',{'class':'ttext-label-1 dark:text-dark-label-1 font-medium'}).text
            rank = Label(leetcode, text=Rank)
            rank.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            rank.grid(row=3, column=1, pady=(25, 0))

            solved_problems_lbl = Label(leetcode, text='Solved Problems :')
            solved_problems_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            solved_problems_lbl.grid(row=4, column=0, padx=(10), pady=(25, 0))

            Solved_Problems = soup.find('div',{'class':'text-[24px] font-medium text-label-1 dark:text-dark-label-1'}).text
            solved_problems = Label(leetcode, text=Solved_Problems)
            solved_problems.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            solved_problems.grid(row=4, column=1, pady=(25, 0))

            NoOfQuestion = soup.findAll('span',{'class':'mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1'})
            Easy = 'Easy : ' + NoOfQuestion[0].text
            easy = Label(leetcode, text=Easy)
            easy.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            easy.grid(row=5, column=0, pady=(25, 0))

            Medium = 'Medium : ' + NoOfQuestion[1].text
            medium = Label(leetcode, text=Medium)
            medium.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            medium.grid(row=5, column=1, pady=(25, 0))

            Hard = 'Hard : ' + NoOfQuestion[2].text
            hard = Label(leetcode, text=Hard)
            hard.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            hard.grid(row=5, column=2, pady=(25, 0))

            Skills = soup.findAll('span',{'class':'inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2'})
            skill_txt = 'Skills : \n'
            for skill in Skills:
                skill_txt = skill_txt + '\n' + skill.text 
            skill_lbl = Label(leetcode, text=skill_txt)
            skill_lbl.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            skill_lbl.grid(row=6, column=0, pady=(25, 0))

            RecentQuestions = soup.findAll('span', {'class' : 'text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium'})
            RecentQuestions_txt = 'Recent Questions : \n'
            for question in RecentQuestions:
                RecentQuestions_txt = RecentQuestions_txt + '\n' + question.text
            recentQuetion_lbl = Label(leetcode, text=RecentQuestions_txt)
            recentQuetion_lbl.config(font=('verdana',12),bg='#d2ebe9',foreground='black')
            recentQuetion_lbl.grid(row=6, column=1, pady=(25, 0))
        except:
            notFound = Label(leetcode, text='❌ Data not found')
            notFound.config(font=('verdana',10),bg='#d2ebe9',foreground='red')
            notFound.grid(row=2, column=1, pady=(10))
    else:
        notFound = Label(leetcode, text='❌ User not found')
        notFound.config(font=('verdana',10),bg='#d2ebe9',foreground='red')
        notFound.grid(row=2, column=1, pady=(40,0))

username_txt = Label(leetcode, text='Username :')
username_txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
username_txt.grid(row=0, column=0, padx=(220,0), pady=(30, 0))

username_ip1 = Entry(leetcode, width=20, font=('Arial', 20))
username_ip1.grid(row=0, column=1, padx=(30,0), pady=(30, 0))

submit = Button(leetcode, text='Submit', width=10, height=2, command=handle_submit_lc)
submit.grid(row=0, column=2, padx=(30,0), pady=(30, 0))

home_btn = Button(leetcode, text='Main Menu', width=10, height=2, command=lambda:show_frame(home))
home_btn.grid(row=0, column=3, padx=(30,0), pady=(30, 0))


# ========== Codeforces ===========

def handle_submit_cf():
    url = 'https://codeforces.com/profile/' + username_ip2.get()

    source = requests.get(url)
    if source.status_code == 200:
        try:
            source = source.text
            soup = bs4.BeautifulSoup(source,'html.parser')
            mainInfo = soup.find('div',{'class':'main-info'})

            Username = mainInfo.find('a').text
            name_lbl2 = Label(codeforces, text='Name :')
            name_lbl2.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            name_lbl2.grid(row=2, column=0, padx=(10), pady=(40, 0))
            name = Label(codeforces, text=Username)
            name.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            name.grid(row=2, column=1, pady=(40, 0))

            rank_lbl = Label(codeforces, text='Rank :')
            rank_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            rank_lbl.grid(row=3, column=0, padx=(10), pady=(25, 0))

            Rank = mainInfo.find('span').text
            rank = Label(codeforces, text=Rank)
            rank.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            rank.grid(row=3, column=1, pady=(25, 0))

            max_rank_lbl = Label(codeforces, text='Max Rank :')
            max_rank_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            max_rank_lbl.grid(row=4, column=0, padx=(10), pady=(25, 0))
            
            MaxRank = soup.findAll('span', {'class' : 'user-gray'})
            MaxRank = MaxRank[3].text
            maxrank = Label(codeforces, text=MaxRank)
            maxrank.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            maxrank.grid(row=4, column=1, pady=(25, 0))

            totalproblemsolved_lbl = Label(codeforces, text='Total Problem Solved :')
            totalproblemsolved_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            totalproblemsolved_lbl.grid(row=5, column=0, padx=(10), pady=(25, 0))

            TotalProblemsSolved = soup.find('div', {'class' : '_UserActivityFrame_counterValue'})
            TotalProblemsSolved = TotalProblemsSolved.text
            totalproblemssolved = Label(codeforces, text=TotalProblemsSolved)
            totalproblemssolved.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            totalproblemssolved.grid(row=5, column=1, pady=(25, 0))
        except:
            notFound = Label(codeforces, text='❌ Data not found')
            notFound.config(font=('verdana',10),bg='#d2ebe9',foreground='red')
            notFound.grid(row=2, column=1, pady=(40,0))
    else:
        notFound = Label(codeforces, text='❌ User not found')
        notFound.config(font=('verdana',10),bg='#d2ebe9',foreground='red')
        notFound.grid(row=2, column=1, pady=(10))

username_txt = Label(codeforces, text='Username :')
username_txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
username_txt.grid(row=0, column=0, padx=(220,0), pady=(30, 0))

username_ip2 = Entry(codeforces, width=20, font=('Arial', 20))
username_ip2.grid(row=0, column=1, padx=(30,0), pady=(30, 0))

submit = Button(codeforces, text='Submit', width=10, height=2, command=handle_submit_cf)
submit.grid(row=0, column=2, padx=(30,0), pady=(30, 0))

home_btn = Button(codeforces, text='Main Menu', width=10, height=2, command=lambda:show_frame(home))
home_btn.grid(row=0, column=3, padx=(30,0), pady=(30, 0))

# ========== Codechef ===========

def handle_submit_cc():
    url = 'https://www.codechef.com/users/' + username_ip3.get()

    source = requests.get(url)
    if source.status_code == 200:
        try:
            source = source.text
            soup = bs4.BeautifulSoup(source,'html.parser')

            name_lbl3 = Label(codechef, text='Name :')
            name_lbl3.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            name_lbl3.grid(row=2, column=0, padx=(10), pady=(40, 0))

            Username = soup.find('h1').text
            name = Label(codechef, text=Username)
            name.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            name.grid(row=2, column=1, pady=(40, 0))

            rating_lbl = Label(codechef, text='Rating :')
            rating_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            rating_lbl.grid(row=3, column=0, padx=(10), pady=(25, 0))

            Rating = soup.find('div', {'class' : 'rating-number'}).text
            rating = Label(codechef, text=Rating)
            rating.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            rating.grid(row=3, column=1, pady=(25, 0))

            ranks = soup.find('ul', {'class' : 'inline-list'})
            
            globalrank_lbl = Label(codechef, text='Global Rank :')
            globalrank_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            globalrank_lbl.grid(row=4, column=0, padx=(10), pady=(25, 0))

            GlobalRank = ranks.find('strong').text
            golbalrank = Label(codechef, text=GlobalRank)
            golbalrank.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            golbalrank.grid(row=4, column=1, pady=(25, 0))

            countryrank_lbl = Label(codechef, text='Country Rank :')
            countryrank_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            countryrank_lbl.grid(row=5, column=0, padx=(10), pady=(25, 0))

            CountryRank = ranks.findAll('li')
            CountryRank = CountryRank[1].find('strong').text
            countryrank = Label(codechef, text=CountryRank)
            countryrank.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            countryrank.grid(row=5, column=1, pady=(25, 0))

            ul = soup.find('ul', {'class' : 'side-nav'})
            li = ul.find_all('li')

            sp_lbl = Label(codechef, text='Student/Professional : ')
            sp_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            sp_lbl.grid(row=6, column=0, padx=(10), pady=(25, 0))

            Student_Professional = li[2].find('span').text
            student_professional = Label(codechef, text=Student_Professional)
            student_professional.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            student_professional.grid(row=6, column=1, pady=(25, 0))
            
            institute_lbl = Label(codechef, text='Institution :')
            institute_lbl.config(font=('Swis721 BT',18),bg='#d2ebe9',foreground='black')
            institute_lbl.grid(row=7, column=0, padx=(10), pady=(25, 0))

            Institute = li[3].find('span').text
            institute = Label(codechef, text=Institute)
            institute.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
            institute.grid(row=7, column=1, pady=(25, 0))
        except:
            notFound = Label(codechef, text='❌ Data not found')
            notFound.config(font=('verdana',10),bg='#d2ebe9',foreground='red')
            notFound.grid(row=2, column=1, pady=(40,0))
    else:
        notFound = Label(codechef, text='❌ User not found')
        notFound.config(font=('verdana',10),bg='#d2ebe9',foreground='red')
        notFound.grid(row=2, column=1, pady=(40,0))

username_txt = Label(codechef, text='Username :')
username_txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
username_txt.grid(row=0, column=0, padx=(220,0), pady=(30, 0))

username_ip3 = Entry(codechef, width=20, font=('Arial', 20))
username_ip3.grid(row=0, column=1, padx=(30,0), pady=(30, 0))

submit = Button(codechef, text='Submit', width=10, height=2, command=handle_submit_cc)
submit.grid(row=0, column=2, padx=(30,0), pady=(30, 0))

home_btn = Button(codechef, text='Main Menu', width=10, height=2, command=lambda:show_frame(home))
home_btn.grid(row=0, column=3, padx=(30,0), pady=(30, 0))

show_frame(home)
window.mainloop()
