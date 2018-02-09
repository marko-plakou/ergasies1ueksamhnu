#Άσκηση 7 σε python 3
import datetime
#Αρχικοποίηση των μεταβλητών.
current_date=datetime.date.today()
day1=current_date.day
year=current_date.year
day_of_wk1=current_date.isoweekday()
day2=0
k=0
new_year=0
new_day=0
for i in range(1,11):
##Ελέγχω εάν ο συγκεγκριμένος χρόνος είναι δύσεκτος και προσθέτω τις ανάλογες ημέρες στο συγκεκριμένο έτος.
    if (i==0):
        if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
            new_date=(current_date+(datetime.timedelta(days=(366))))
            new_year=new_date.year
        else:
            new_date=(current_date+(datetime.timedelta(days=(365))))
            new_year=new_date.year
##Ελέγχω εάν καποιο απο τα επόμενα 10 χρόνια είναι δύσεκτα και προσθέτω τις ανάλογες ημέρες στο εκάστοτε έτος.        
    else:
        if (( new_year%400 == 0)or ( new_year%4 == 0 )) and ( new_year%100 != 0):
            new_date=(current_date+(datetime.timedelta(days=(i*366))))
            new_year=new_date.year 
        else:
            new_date=(current_date+ (datetime.timedelta(days=(i*365))))
            new_year=new_date.year
##Απομονώνω την νέα ημέρα του μήνα ετσί ώστε να εξετάσω εάν είναι πρίν ή μετά απο την σημερινή.
        day2=new_date.day
##Εάν είναι πιο πρίν ή ίσες προσθέτω την διαφορά της σημερινής απο την νέα ωστε να πάρω σαν αποτέλεσμα την ακριβή σημερινή ημέρα(π.χ18) του μήνα τον επόμενο χρόνο.
    if (day1>=day2):
        new_date=new_date+(datetime.timedelta(days=(day1-day2)))
##Εάν είναι πιο μετά τότε αφαιρώ την διαφορά της νέας από την σημερινή ημέρα του μήνα ώστε να πάρω το ίδιο αποτέλεσμα όπως και πρίν. 
    else:
        new_date=new_date-(datetime.timedelta(days=(day2-day1)))
##Από την νέα αυτη ημερομηνία (η οποία θα είναι η ίδια με την σημερινή με μόνη διαφορά το έτος)βρίσκω την ημέρα της εβδομάδας που αντιστοιχεί η συγκεκριμένη ημερομηνία.
    day_of_wk2=new_date.isoweekday()
##Εξετάζω εάν η ημέρα της εβδομάδας ειναι η ίδια με την σημερινή (και αφού η ημέρα του μήνα είναι ίδια) καταλήγω εάν υπάρχει ημέρα του επόμενου χρόνου που να είναι η ίδια του συγκεκριμένου μήνα
##και ανάλογα αυξάνω τον μετρητή κ.
    if (day_of_wk1==day_of_wk2):
        k+=1
##Η διαδικασία επαναλαμβάνεται άλλες 9 φορές ώστε να εξετάσω συνολικά για τα επόμενα 10 χρόνια.
print ("Οι ήμερες του συγκεκριμένου μήνα που είναι ίδιες τα επόμενα 10 χρόνια είναι",k ,".")
