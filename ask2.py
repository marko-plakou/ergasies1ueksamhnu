#Άσκηση 2  σε Python 2
import datetime
import urllib2
import json

#Αρχικοποιήση μεταβλητών και λίστας.
cur_date=datetime.datetime.now()
mynums=[]
epitixies=[]
thesh=[]
#Εισαγωγή αριθμών χρήστη στη λίστα.
for i in range(10):
    mynums[i]=int(input("Δώσε αριθμό"))
#Για τον επόμενο μήνα κάνω αίτηση για άνοιγμα των δεδομένων στις συγκεκριμένες ημερομηνίες.
for i in range(31):
    date1= date1 - datetime.timedelta(days=1)
    datetm= date1.strftime("%d-%m-%y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%datetm
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
#Ανάλυση στοιχείων javascript και αναζήτηση δεδομένων με value draws και draw.
    data=json.loads(data)
    kl= data['draws']['draw']
    klhr=[]
#Αναζήτηση για τα αποτελέσματα 
    for element in kl:
        pro=i["results"]
        sum=0
#Σύγκριση αποτελεσμάτων με τους αριθμούς του χρήστη και αύξηση του μετρητή .
        for i in mynums:
            if i in pro:
                sum+=1
        klhr.append(sum)
#Αναζήτηση του μεγιστου της λίστας 
    max(klhr),klhr.count(max(klhr))
#Η λίστα epitixies παίρνει ως στοιχεία τις επιτυχίες  που είχε ο χρήστης σε μια ημέρα και η λιστα thesh εχει ως στοιχεία την ημέρα.
    epitixies[i]= (max(klhr)*klhr.countmax(max(klhr)))
    thesh[i]=i
#Εύρεση μεγίστου και μηδενισμός των άλλων στοιχείων.
for K  in range (31):
    if epitixies[k+1]>epitixies[k]:
        epitixies[k]=0
#Εύρεση και εκτύπωση ημερομηνίας.
for j in range(31):
    if epitixies[j]!=0:
        date2=datetime.datetime.now()
        date3=date2.day
        if date3>thesh[j]:
            hm_epitixias=date2-datetime.timedelta(days=date3-thesh[j])
        else:
            hm_epitixias=date2-datetime.timedelta(days=(thesh[j]-date3)+date3)
print ("H ΗΜΕΡΑ ΜΕ ΤΗΝ ΜΕΓΑΛΥΤΕΡΗ ΕΙΤΥΧΙΑ ΕΙΝΑΙ",hm_epitixias)            
