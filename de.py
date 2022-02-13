from tkinter import*
root=Tk()
root.geometry("300x100")
root.maxsize(300,200)
root.minsize(300,200)
d1={"Red":"लाल",
"Cow":"गाय",
"Green":"हरा",
"Byellow":"पिला",
"Orange":"नारंगी",
"Black":"काला",
"Pink":"गुलाबी",
"Door":"दरवाजा",
"Jewellery":"आभूषण",
"Ring":"अंगूठी",
"Box":"डिब्बा",
"Road":"रास्ता",
"Gill":"जाली",
"Tap":"नल",
"Fountain":"झरना",
"River":"नदी",
"Children":"बच्चे",
"Hair":"बाल",
"Comb":"कंघी",
"Soap":"साबुन",
"Money":"पैसे",
"Cab":"किराये की गाड़ी",
"Cabin":"छोटा कमरा",
"Cabinet":"गुप्त कमरा",
"Cable":"मजबूत तार",
"Cadet":"सेना का छात्र",
"Cadre":"केन्द्र",
"Cage":"पिंजरा",
"Cajole":"चापलूसी से ठगना",
"Calculate":"गणना करना",
"Calf":"बछड़ा",
"Calibre":"योग्यता",
"Call":"बुलाना",
"Calm":"शांति",
"Camp":"तंबू",
"Campaign":"नियमित युद्ध",
"Canal":"नहर",
"Cancel":"खत्म करना",
"Bold":"साहसी",
"Bomb":"बम गिराना",
"Bombastic":"दिखावा",
"Bonafide":"सत्य",
"Bond":"बंधन",
"Bondage":"गुलामी",
"Bone":"हड्डी",
"Bony":"दुबला पतला",
"Bonus":"लाभ में हिस्सा",
"Bookish":"किताबों का शौकीन",
"Book-maker":"लेखक",
"Boon":"वरदान",
"Booth":"झोपड़ी",
"Border":"किनारा, सीमा",
"Bore":"थकना",
"Bosom-friend":"खास दोस्त",
"Appendix":"परिशिष्ट",
"Appetite":"भूख",
"Hunger":"भूख",
"Applaud":"प्रशंसा करना",
"To praise":"प्रशंसा करना",
"Apple of the eye":"आँख का तारा",
"The pupil":"आँख का तारा",
"Appliance":"साधन",
"Tools":"साधन",
"Applicable":"काम में लाने योग्य",
"Fit to be used":"काम में लाने योग्य",
"Application":"अर्जी",
"Formal request":"अर्जी",
"Appoint":"काम में लगाना",
"To engage":"काम में लगाना",
"Appreciate":"मान देना",
"To esteem highly":"मान देना",
"Apprehend":"समझना",
"To understand":"समझना",
"Approach":"पहुँच",
"Reach":"पहुँच",
"Appropriate":"उचित",
"Fit":"उचित",
"Approval":"मंजूरी",
"Sanction":"मंजूरी",
"Approximate":"लगभग",
"Nearest":"लगभग",
"Apt":"योग्य",
"Aqua":"जल",
"Water":"जल",
"Architect":"घर बनाने वाला",
"Housemaker":"घर बनाने वाला",
"Ardent":"उत्सुक",
"Keen":"उत्सुक",
"Doss":"चारपाई, खटिया",
"Roof":"छत",
"Plaza":"चौक",
"Dung":"गोबर",
"Thread":"धागा",
"Pit":"गड्ढा",
"Mud":"कीचड़",
"Slippers":"चप्पल",
"Amused":"मन बहलाना",
"Blissful":"आनंदमय",
"Cheerful":"हंसमुख",
"Delighted":"प्रसन्न",
"Glad":"प्रसन्न",
"Joyful":"आनंदपूर्ण",
"Merry":"हंसमुख,आनंदित",
"Ecstatic":"अति प्रसन्न",
"Colossal":"प्रचंड",
"Gigantic":"भारी भरकम",
"Immense":"बहुत बड़ा",
"Mammoth":"विशालकाय",
"Massive":"बड़ा",
"Tiny":"बहुत छोटा",
"Petite":"पतली-दुबली",
"Puny":"नन्हा,कमजो",
"Borrow":"उधार लेना",
"Lend":"उधर देना",
"Donate":"दान करना",
"Contribute":"योगदान देना",
"Assets":"सम्पति",
"Emperor":"सम्राट",
"Splendor":"वैभव",
"Majesty":"महिमा",
"Theft":"चोरी",
"Robbery":"डकैती",
"Burglary":"सेंधमारी",
"Smuggling":"तस्करी",
"Murder":"हत्या",
"Fraud":"धोखा",
"Crime":"अपराध",
"Corruption":"भ्रष्टाचार",
"Democracy":"लिकतंत्र",
"Slavery":"गुलाम",
"Rebellion":"विद्रोह",
"Protest":"आन्दोलन",
"Boycott":"बहिस्कार",
"Constitution":"संविधान",
"Republic":"गणतंत्र",
"Possession":"अधिकार",
"Bride":"दुल्हन",
"Groom":"दूल्हा",
"Vermilion":"सिंदूर",
"Matrimony":"विवाह",
"Tradition":"परंपरा",
"Ceremony":"समारोह",
"Procession":"बरात",
"Farewell":"विदाई",
"Bitter":" कड़वा",
"Sweet":"मीठा",
"Moist":"गिला",
"Bland":"नरम",
"Spicy":"मसालेदार",
"Greasy":"तेलमय",
"Sour":"खट्टा",
"Delicious":"स्वादिष्ट",
"Pot": "मटका",
"Newspaper": "अख़बार",
"Paper": "काग़ज़",
"Belt": "पट्टा",
"Calendar": "पंचांग",
"Window": "खिड़की",
"Main gate": "मुख्य द्वार",
"Coins": "चिल्लर",
"Fork": "काटा",
"Spectacles": "चश्मा",
"Notification": "अधिसूचना",
"Walk":"चलना",
"Run":"दौड़ना",
"Play":"खेलना",
"Love":"प्यार",
"Like":"पसंद करना",
"Milk":"दूध",
"Tea":"चाय",
"Vegetables":"सब्ज़ी",
"Message":"संदेश",
"Dacoit":"डाकू",
"Daft": "मूर्ख",
"Dally":"देर करना",
"Dam":"पशुओं की मां",
"Damage":"हानि",
"Game":"खेल",
"Dame":"स्त्री",
"Damp":"ठंडक",
"Dandle":"लाड करना",
"Dandruff":"रूसी",
"Danger":"भय",
"Dazzle":"चकित करना",
"Dealer":"व्यापारी",
"Dear":"प्रिय",
"Dearth":"कमी"}
i=StringVar()
i.set("")

Entry(textvariable=i,font="mango 15 bold",bg="Yellow").grid(row=1,column=1)
def ma():
    try:

        global i
        # c = i.capitalize()
        Label(text="                       ", font="mango 15 bold", fg="white" ).grid(row=2, column=1)
        Label(text=d1[i.get()], font="mango 15 bold", fg="red").grid(row=2, column=1)
        # Label(text=d1[i.get()],font="mango 15 bold",fg="Blue",bg="red").grid(row=2,column=1)
        # del(i.get)
        # l2 = Label(text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t").grid(row=2, column=1)
    except Exception as e:
        print(f'{e} This word is not in this dictneary.')
# def ak():
#     Label(text="                                                                           ").grid(row=2,column=1)

Button(text="Search",command=ma ,font="mango 10 bold").grid(row=1,column=2)


# l2 = Label(text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t").grid(row=2, column=1)


root.mainloop()

