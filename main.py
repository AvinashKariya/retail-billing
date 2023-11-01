from tkinter import *
from tkinter import messagebox
import random,os,tempfile
#all functionality

def print_bill():
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error',"Bill is empty")
    else:
        file = tempfile.mktemp('.txt')
        open(file,'w').write(textArea.get(1.0,END))
        os.startfile(file,'print')

def clear():
    bathSoapEntry.delete(0,END)
    faceCreamEntry.delete(0,END)
    faceWashEntry.delete(0,END)
    hairSprayEntry.delete(0,END)
    hairGelEntry.delete(0,END)
    bodyLotionEntry.delete(0,END)
    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)
    maazaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    spriteEntry.delete(0,END)
    dewEntry.delete(0,END)
    frootiEntry.delete(0,END)
    colaEntry.delete(0,END)
    cosmeticPriceEntry.delete(0,END)
    cosmeticTexEntry.delete(0,END)
    groceryTexEntry.delete(0,END)
    groceryPriceEntry.delete(0,END)
    coldDrinkPriceEntry.delete(0,END)
    coldDrinkTexEntry.delete(0,END)

    bathSoapEntry.insert(0,0)
    faceCreamEntry.insert(0,0)
    faceWashEntry.insert(0,0)
    hairSprayEntry.insert(0,0)
    hairGelEntry.insert(0,0)
    bodyLotionEntry.insert(0,0)
    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)
    maazaEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    dewEntry.insert(0,0)
    frootiEntry.insert(0,0)
    colaEntry.insert(0,0)
    cosmeticPriceEntry.insert(0,0)
    cosmeticTexEntry.insert(0,0)
    groceryTexEntry.insert(0,0)
    groceryPriceEntry.insert(0,0)
    coldDrinkPriceEntry.insert(0,0)
    coldDrinkTexEntry.insert(0,0)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billNumberEntry.delete(0,END)
    textArea.delete(1.0,END)

def search():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billNumberEntry.get():
            f=open(f'bills/{i}','r')
            textArea.delete(1.0,END)
            for data in f:
                textArea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def savebill():
    global billNumber
    result=messagebox.askyesno('Confir','Do you want to save bill?')
    if result:
        bill_content=textArea.get(1.0,END)
        file=open(f'bills/{billNumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f"Bill {billNumber} is Saved Successfully")
        billNumber=random.randint(500,1000)

billNumber=random.randint(500,1000)


def total():
    global soap,facecream,facewash,spray,gel,lotion,totalbill
    soap=int(bathSoapEntry.get())*20
    facecream=int(faceCreamEntry.get())*80
    facewash=int(faceWashEntry.get())*120
    spray=int(hairSprayEntry.get())*200
    gel=int(hairGelEntry.get())*50
    lotion=int(bodyLotionEntry.get())*220

    totalCosmeticPrice = soap+facecream+facewash+spray+gel+lotion
    cosmeticPriceEntry.delete(0,END)
    cosmeticPriceEntry.insert(0,f'{totalCosmeticPrice} Rs.')
    cosmeticTex=totalCosmeticPrice*0.12
    cosmeticTexEntry.delete(0,END)
    cosmeticTexEntry.insert(0,f'{cosmeticTex} Rs.')

    global rice,oil,daal,wheat,sugar,tea
    rice=int(riceEntry.get())*200
    oil=int(oilEntry.get())*200
    daal=int(daalEntry.get())*250
    wheat=int(wheatEntry.get())*120
    sugar=int(sugarEntry.get())*120
    tea=int(teaEntry.get())*280

    totalGroceryPrice = rice+oil+daal+wheat+sugar+tea
    groceryPriceEntry.delete(0,END)
    groceryPriceEntry.insert(0,f'{totalGroceryPrice} Rs.')
    groceryTex=totalGroceryPrice*0.15
    groceryTexEntry.delete(0,END)
    groceryTexEntry.insert(0,f'{groceryTex} Rs.')

    global maza,pepsi,sprite,dew,froti,cola
    maza=int(maazaEntry.get())*20
    pepsi=int(pepsiEntry.get())*30
    sprite=int(spriteEntry.get())*50
    dew=int(dewEntry.get())*40
    froti=int(frootiEntry.get())*60
    cola=int(colaEntry.get())*30

    totalDrinksPrice = maza+pepsi+sprite+dew+froti+cola
    coldDrinkPriceEntry.delete(0,END)
    coldDrinkPriceEntry.insert(0,f'{totalDrinksPrice} Rs.')
    drinkTex=totalDrinksPrice*0.08
    coldDrinkTexEntry.delete(0,END)
    coldDrinkTexEntry.insert(0,f'{drinkTex} Rs.')

    totalbill=totalCosmeticPrice+totalDrinksPrice+totalGroceryPrice+drinkTex+cosmeticTex+groceryTex

def bill():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Required')
    
    elif cosmeticPriceEntry.get()=='' or groceryPriceEntry.get()=='' or coldDrinkPriceEntry.get()=='':
        messagebox.showerror('Error','No Products Purchased')
    
    elif cosmeticPriceEntry.get()=='0 Rs.' and groceryPriceEntry.get()=='0 Rs.' and coldDrinkPriceEntry.get()=='0 Rs.':
        messagebox.showerror('Error','No Products Purchased')
    
    else:
        textArea.delete(1.0,END)
        textArea.insert(END,'\t\t**Welcome Customer**\n')
        textArea.insert(END,f'\nBill Number: {billNumber}')
        textArea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
        textArea.insert(END,f'\nPhone Number: {phoneEntry.get()}\n')
        textArea.insert(END,'\n================================================\n')
        textArea.insert(END,'Product\t\tQuantity\t\t\tPrice')
        textArea.insert(END,'\n================================================\n')
        if bathSoapEntry.get()!='0':
            textArea.insert(END,f'Bath Soap\t\t{bathSoapEntry.get()}\t\t\t{soap}\n')
        if hairSprayEntry.get()!='0':
            textArea.insert(END,f'Hair Spray\t\t{hairSprayEntry.get()}\t\t\t{spray}\n')
        if hairGelEntry.get()!='0':
            textArea.insert(END,f'Hair Gel\t\t{hairGelEntry.get()}\t\t\t{gel}\n')
        if faceCreamEntry.get()!='0':
            textArea.insert(END,f'Face Cream\t\t{faceCreamEntry.get()}\t\t\t{facecream}\n')
        if faceWashEntry.get()!='0':
            textArea.insert(END,f'Face Wash\t\t{faceWashEntry.get()}\t\t\t{facewash}\n')
        if bodyLotionEntry.get()!='0':
            textArea.insert(END,f'Body lotion\t\t{bodyLotionEntry.get()}\t\t\t{lotion}\n')

        if riceEntry.get()!='0':
            textArea.insert(END,f'Rice\t\t{riceEntry.get()}\t\t\t{rice}\n')
        if daalEntry.get()!='0':
            textArea.insert(END,f'Daal\t\t{daalEntry.get()}\t\t\t{daal}\n')
        if wheatEntry.get()!='0':
            textArea.insert(END,f'Wheat\t\t{wheatEntry.get()}\t\t\t{wheat}\n')
        if teaEntry.get()!='0':
            textArea.insert(END,f'Tea\t\t{teaEntry.get()}\t\t\t{tea}\n')
        if oilEntry.get()!='0':
            textArea.insert(END,f'Oil\t\t{oilEntry.get()}\t\t\t{oil}\n')
        if sugarEntry.get()!='0':
            textArea.insert(END,f'Sugar\t\t{teaEntry.get()}\t\t\t{sugar}\n')
        
        if maazaEntry.get()!='0':
            textArea.insert(END,f'Maaza\t\t{maazaEntry.get()}\t\t\t{maza}\n')
        if colaEntry.get()!='0':
            textArea.insert(END,f'Coca cola\t\t{colaEntry.get()}\t\t\t{cola}\n')
        if pepsiEntry.get()!='0':
            textArea.insert(END,f'Pepsi\t\t{pepsiEntry.get()}\t\t\t{pepsi}\n')
        if spriteEntry.get()!='0':
            textArea.insert(END,f'Sprite\t\t{spriteEntry.get()}\t\t\t{sprite}\n')
        if frootiEntry.get()!='0':
            textArea.insert(END,f'Frooti\t\t{frootiEntry.get()}\t\t\t{froti}\n')
        if dewEntry.get()!='0':
            textArea.insert(END,f'Dew\t\t{dewEntry.get()}\t\t\t{dew}\n')
        textArea.insert(END,'\n================================================')
        
        if cosmeticTexEntry.get()!='0.0 Rs.':
            textArea.insert(END,f'\nCosmetics Tax\t\t\t{cosmeticTexEntry.get()}\n')
        if groceryTexEntry.get()!='0.0 Rs.':
            textArea.insert(END,f'Grocery Tax\t\t\t{groceryTexEntry.get()}\n')
        if coldDrinkTexEntry.get()!='0.0 Rs.':
            textArea.insert(END,f'Colddrinks Tax\t\t\t{coldDrinkTexEntry.get()}\n')
        
        textArea.insert(END,f'\nTotal Bill\t\t\t\t{totalbill} Rs.')
        savebill()

##gui part
root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685+100+50')

headingLabel = Label(root,text="Retail Billing System",font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)

customerDetailsFrame=LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
customerDetailsFrame.pack(fill=X)

nameLabel=Label(customerDetailsFrame,text="Name:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customerDetailsFrame,font=('arial',15),width=18)
nameEntry.grid(row=0,column=1,padx=5)

phoneLabel=Label(customerDetailsFrame,text="Phone Number:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
phoneLabel.grid(row=0,column=2,padx=20)

phoneEntry=Entry(customerDetailsFrame,font=('arial',15),width=18)
phoneEntry.grid(row=0,column=3,padx=5)

billNumberLabel=Label(customerDetailsFrame,text="Bill Number:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
billNumberLabel.grid(row=0,column=4,padx=20)

billNumberEntry=Entry(customerDetailsFrame,font=('arial',15),width=18)
billNumberEntry.grid(row=0,column=5,padx=5)

searchButton=Button(customerDetailsFrame,text="SEARCH",font=('arial',12,'bold'),bd=7,width=10,command=search)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack(pady=5,fill=X)

cosmeticsLabelFrame=LabelFrame(productsFrame,text="Cosmetics",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
cosmeticsLabelFrame.grid(row=0,column=0,padx=10)

bathSoapLabel=Label(cosmeticsLabelFrame,text="Bath Soap:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
bathSoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathSoapEntry=Entry(cosmeticsLabelFrame,font=('arial',15),width=10)
bathSoapEntry.grid(row=0,column=1,padx=5)
bathSoapEntry.insert(0,0)

faceCreamLabel=Label(cosmeticsLabelFrame,text="Face Cream:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
faceCreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
faceCreamEntry=Entry(cosmeticsLabelFrame,font=('arial',15),width=10)
faceCreamEntry.grid(row=1,column=1,padx=5)
faceCreamEntry.insert(0,0)

faceWashLabel=Label(cosmeticsLabelFrame,text="Face Wash:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
faceWashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
faceWashEntry=Entry(cosmeticsLabelFrame,font=('arial',15),width=10)
faceWashEntry.grid(row=2,column=1,padx=5)
faceWashEntry.insert(0,0)

hairSprayLabel=Label(cosmeticsLabelFrame,text="Hair Spray:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
hairSprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairSprayEntry=Entry(cosmeticsLabelFrame,font=('arial',15),width=10)
hairSprayEntry.grid(row=3,column=1,padx=5)
hairSprayEntry.insert(0,0)

hairGelLabel=Label(cosmeticsLabelFrame,text="Hair Gel:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
hairGelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairGelEntry=Entry(cosmeticsLabelFrame,font=('arial',15),width=10)
hairGelEntry.grid(row=4,column=1,padx=5)
hairGelEntry.insert(0,0)

bodyLotionLabel=Label(cosmeticsLabelFrame,text="Body Lotion:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
bodyLotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodyLotionEntry=Entry(cosmeticsLabelFrame,font=('arial',15),width=10)
bodyLotionEntry.grid(row=5,column=1,padx=5)
bodyLotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text="Grocery",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
groceryFrame.grid(row=0,column=1,padx=10)

riceLabel=Label(groceryFrame,text="Rice:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry=Entry(groceryFrame,font=('arial',15),width=10)
riceEntry.grid(row=0,column=1,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text="Oil:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceryFrame,font=('arial',15),width=10)
oilEntry.grid(row=1,column=1,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text="Daal:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
daalEntry=Entry(groceryFrame,font=('arial',15),width=10)
daalEntry.grid(row=2,column=1,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text="Wheat:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry=Entry(groceryFrame,font=('arial',15),width=10)
wheatEntry.grid(row=3,column=1,padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text="Sugar:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarEntry=Entry(groceryFrame,font=('arial',15),width=10)
sugarEntry.grid(row=4,column=1,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text="Tea:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
teaEntry=Entry(groceryFrame,font=('arial',15),width=10)
teaEntry.grid(row=5,column=1,padx=10)
teaEntry.insert(0,0)

coldDrinksFrame=LabelFrame(productsFrame,text="Cold Drinks",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
coldDrinksFrame.grid(row=0,column=2,padx=5)

maazaLabel=Label(coldDrinksFrame,text="Maaza:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
maazaEntry=Entry(coldDrinksFrame,font=('arial',15),width=10)
maazaEntry.grid(row=0,column=1,padx=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(coldDrinksFrame,text="Pepsi:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(coldDrinksFrame,font=('arial',15),width=10)
pepsiEntry.grid(row=1,column=1,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(coldDrinksFrame,text="Sprite:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry(coldDrinksFrame,font=('arial',15),width=10)
spriteEntry.grid(row=2,column=1,padx=10)
spriteEntry.insert(0,0)

dewLabel=Label(coldDrinksFrame,text="Dew:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
dewEntry=Entry(coldDrinksFrame,font=('arial',15),width=10)
dewEntry.grid(row=3,column=1,padx=10)
dewEntry.insert(0,0)

frootiLabel=Label(coldDrinksFrame,text="Frooti:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
frootiEntry=Entry(coldDrinksFrame,font=('arial',15),width=10)
frootiEntry.grid(row=4,column=1,padx=10)
frootiEntry.insert(0,0)

colaLabel=Label(coldDrinksFrame,text="Coca Cola:",font=('times new roman',15,'bold'),bg="gray20",fg="white")
colaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
colaEntry=Entry(coldDrinksFrame,font=('arial',15),width=10)
colaEntry.grid(row=5,column=1,padx=10)
colaEntry.insert(0,0)

billFrame = Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)

billAreaLabel = Label(billFrame,text="Bill Area",font=('times new roman',15,'bold'))
billAreaLabel.pack()

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textArea = Text(billFrame,height=17,width=48,yscrollcommand=scrollbar.set)
textArea.pack()
scrollbar.config(command=textArea.yview)

billMenuFrame=LabelFrame(root,text="Bill Menu",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
billMenuFrame.pack(fill=X,padx=5)

cosmeticPriceLabel=Label(billMenuFrame,text="Cosmetic Price:",font=('times new roman',12,'bold'),bg="gray20",fg="white")
cosmeticPriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
cosmeticPriceEntry=Entry(billMenuFrame,font=('arial',15),width=10)
cosmeticPriceEntry.grid(row=0,column=1,padx=10)

groceryPriceLabel=Label(billMenuFrame,text="Grocery Price:",font=('times new roman',12,'bold'),bg="gray20",fg="white")
groceryPriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
groceryPriceEntry=Entry(billMenuFrame,font=('arial',15),width=10)
groceryPriceEntry.grid(row=1,column=1,padx=10)

coldDrinkPriceLabel=Label(billMenuFrame,text="Cold Drink Price:",font=('times new roman',12,'bold'),bg="gray20",fg="white")
coldDrinkPriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
coldDrinkPriceEntry=Entry(billMenuFrame,font=('arial',15),width=10)
coldDrinkPriceEntry.grid(row=2,column=1,padx=10)

cosmeticTexLabel=Label(billMenuFrame,text="Cosmetic Tax:",font=('times new roman',12,'bold'),bg="gray20",fg="white")
cosmeticTexLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')
cosmeticTexEntry=Entry(billMenuFrame,font=('arial',15),width=10)
cosmeticTexEntry.grid(row=0,column=3,padx=10)

groceryTexLabel=Label(billMenuFrame,text="Grocery Tax:",font=('times new roman',12,'bold'),bg="gray20",fg="white")
groceryTexLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')
groceryTexEntry=Entry(billMenuFrame,font=('arial',15),width=10)
groceryTexEntry.grid(row=1,column=3,padx=10)

coldDrinkTexLabel=Label(billMenuFrame,text="Cold Drink Tax:",font=('times new roman',12,'bold'),bg="gray20",fg="white")
coldDrinkTexLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')
coldDrinkTexEntry=Entry(billMenuFrame,font=('arial',15),width=10)
coldDrinkTexEntry.grid(row=2,column=3,padx=10)

buttonFrame = Frame(billMenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,padx=10)

totalButton=Button(buttonFrame,text="Total",font=('arial',16,'bold'),bg="gray20",fg="white",width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,padx=10,pady=20)

billButton=Button(buttonFrame,text="Bill",font=('arial',16,'bold'),bg="gray20",fg="white",width=8,pady=10,command=bill)
billButton.grid(row=0,column=1,padx=10,pady=20)


printButton=Button(buttonFrame,text="Print",font=('arial',16,'bold'),bg="gray20",fg="white",width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,padx=10,pady=20)

clearButton=Button(buttonFrame,text="Clear",font=('arial',16,'bold'),bg="red",fg="white",width=8,pady=10,command=clear)
clearButton.grid(row=0,column=5,padx=10,pady=20)

root.mainloop()