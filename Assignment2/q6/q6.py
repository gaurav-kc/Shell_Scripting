
from cryptography.fernet import Fernet
import sqlite3
import sys
import getpass
import random
import pyperclip
from datetime import datetime
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_char = ['!','@','#','$','&']
numbers = ['0','1','2','3','4','5','6','7','8','9']
def genpassword(len1=8,len2=15,ucc=1,lcc=1,scc=1,ncc=1,begwithupper=True):
    if (ucc+lcc+scc+ncc) > len2:
        print "Not Possible"
        return
    pass_len = random.randrange(len1,len2+1)
    password = []
    used_indices = []
    for i in range(0,pass_len):
        password.append('1')
    if begwithupper == True:
        password[0] = random.choice(upper_case)
        used_indices.append(0)
        ucc = ucc -1
    while ucc > 0:
        ind = random.randrange(0,pass_len)
        if ind not in used_indices:
            password[ind] = random.choice(upper_case)
            used_indices.append(ind)
            ucc = ucc - 1
    while lcc > 0:
        ind = random.randrange(0,pass_len)
        if ind not in used_indices:
            password[ind] = random.choice(lower_case)
            used_indices.append(ind)
            lcc = lcc - 1
    while scc > 0:
        ind = random.randrange(0,pass_len)
        if ind not in used_indices:
            password[ind] = random.choice(special_char)
            used_indices.append(ind)
            scc = scc - 1
    while ncc > 0:
        ind = random.randrange(0,pass_len)
        if ind not in used_indices:
            password[ind] = random.choice(numbers)
            used_indices.append(ind)
            ncc = ncc - 1
    for i in range(0,pass_len):
        if i not in used_indices:
            while(1):
                temp = random.randrange(0,4)
                if temp == 0 and ucc != -1:
                    password[i] = random.choice(upper_case)
                    break
                if temp == 1 and lcc != -1:
                    password[i] = random.choice(lower_case)
                    break
                if temp == 2 and ncc != -1:
                    password[i] = random.choice(numbers)
                    break
                if temp == 3 and scc != -1: 
                    password[i] = random.choice(special_char)
                    break
    passwordstr = "".join(password)
    return passwordstr
conn = sqlite3.connect('aliasdb.db')

while(1):
    print "1. Add new entry"
    print "2. Add alias"
    print "3. Get password"
    print "4. Generate Password"
    print "5. Remove"
    print "6. Update password"
    print "7. Exit"
    choice = input()
    if choice == 1:
        print "domain-name"
        domain_name = raw_input()
        print "user-id"
        userid = raw_input()
        try: 
            password = getpass.getpass() 
        except Exception as error: 
            print('ERROR', error)
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encoded_text = cipher.encrypt(password)
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        todaydate = str(day)+"/"+str(month)+"/"+str(year)
        try:
            query1 = "insert into passwordtable(uid,password,domain,modified_date,key) values(\""+userid+"\",\""+encoded_text+"\",\""+domain_name+"\",\""+todaydate+"\",\""+key+"\");"
            conn.execute(query1)
        except sqlite3.Error as error:
            print "Failed to insert entry ",error
            continue
        try:
            query2 = "insert into aliastable(domain,alias) values(\""+ domain_name+"\",\""+domain_name+"\");"
            conn.execute(query2)
            conn.commit()
        except sqlite3.Error as error:
            print "Failed to add alias ",error
            continue
        continue
    if choice == 2:
        print "list"
        try:
            cursor = conn.execute("Select distinct(domain) from aliastable")
        except sqlite3.Error as error:
            print "Did not find domain for the alias ",error
            continue
        index = 1
        map = {}
        for i in cursor:
            print str(index)+"  "+i[0]
            map[index] = i[0]
            index = index+1
        indchoice = input()
        print "Alias "
        aliasname = raw_input()
        try:
            query = "insert into aliastable(domain,alias) values(\""+ map[indchoice]+"\",\""+aliasname+"\");"
            conn.execute(query)
            conn.commit()
        except sqlite3.Error as error:
            print "Failed to add alias ",error
            continue
    if choice == 3:
        print "Alias"
        aliasname = raw_input()
        domain_name = ""
        try:
            cursor = conn.execute("select distinct(domain) from aliastable where alias=\""+aliasname+"\";")
        except sqlite3.Error as error:
            print "Failed to find domain for alias ",error
            continue
        for i in cursor:
            domain_name = i[0]
        try:
            cursor = conn.execute("select uid from passwordtable where domain=\""+domain_name+"\";")
        except sqlite3.Error as error:
            print "Failed to find user id for this domain ",error
            continue
        map = {}
        index = 1
        for i in cursor:
            print str(index) + "  " + i[0]
            map[index] = i[0]
            index = index+1
        uidchoice = input()
        try:
            cursor = conn.execute("select password,key from passwordtable where uid=\""+map[uidchoice]+"\" and domain=\""+domain_name+"\";")
            for i in cursor:
                encoded_text = i[0]
                key = i[1]
            cipher = Fernet(str(key))
            decoded_text = cipher.decrypt(str(encoded_text))
            pyperclip.copy(decoded_text)
            print "Copied to clipboard"
            conn.commit()
        except sqlite3.Error as error:
            print "Failed to get password ",error
            continue
        continue
    if choice == 4:
        print "1) len 8 to 15. Atleast 1 uc, 1 lc, 1 sc, 1 nc starting with capital letter"
        print "2) len 8 to 15. Atleast 1 uc, 1 lc, 1 nc starting with capital letter no spl chars"
        print "3) len 8 to 15. Atleast 1 uc, 1 lc starting with uppercase and no number/special chars"
        print "4) Custom"
        passtypechoice = input()
        password = ""
        if passtypechoice == 1:
            password = genpassword()
        if passtypechoice == 2:
            password = genpassword(8,15,1,1,-1,1,True)
        if passtypechoice == 3:
            password = genpassword(8,15,1,1,-1,-1,False)
        if passtypechoice == 4:
            print "Please enter -1 if 0 occurrences of some parameter is required"
            print "Lower Length limit"
            len1 = input()
            print "Upper length limit"
            len2 = input()
            print "Min Uppercase chars"
            ucc = input()
            print "Min Lowercase chars"
            lcc = input()
            print "Min Special chars"
            scc = input()
            print "Min Numbers"
            ncc = input()
            print "Should it begin with upper case 1/0"
            t = input()
            if t == 1:
                pref = True
            else:
                pref = False
            password = genpassword(len1,len2,ucc,lcc,scc,ncc,pref)
        pyperclip.copy(password)
        print "Password copied to clipboard"
        print "Would you like to add entry? 1/0"
        entrychoice = input()
        if entrychoice == 0:
            continue
        print "Enter domain name"
        domain_name = raw_input()
        print "user-id"
        userid = raw_input()
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encoded_text = cipher.encrypt(password)
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        todaydate = str(day)+"/"+str(month)+"/"+str(year)
        try:
            query1 = "insert into passwordtable(uid,password,domain,modified_date,key) values(\""+userid+"\",\""+encoded_text+"\",\""+domain_name+"\",\""+todaydate+"\",\""+key+"\");"
            conn.execute(query1)
        except sqlite3.Error as error:
            print "Insertion failed ",error
            continue
        try:
            query2 = "insert into aliastable(domain,alias) values(\""+ domain_name+"\",\""+domain_name+"\");"
            conn.execute(query2)
            conn.commit()
        except sqlite3.Error as error:
            print "Failed to add alias ",error
            continue
        continue
    if choice == 5:
        print "User id or entire domain? 0/1"
        removechoice = input()
        if removechoice == 0:
            print "Alias"
            aliasname = raw_input()
            domain_name = ""
            try:
                cursor = conn.execute("select distinct(domain) from aliastable where alias=\""+aliasname+"\";")
            except sqlite3.Error as error:
                print "Failed to find domain ",error
                continue
            for i in cursor:
                domain_name = i[0]
            try:
                cursor = conn.execute("select uid from passwordtable where domain=\""+domain_name+"\";")
            except sqlite3.Error as error:
                print "Failed to get userid ",error
                continue
            map = {}
            index = 1
            for i in cursor:
                print str(index) + "  " + i[0]
                map[index] = i[0]
                index = index+1
            uidchoice = input() 
            try: 
                conn.execute("delete from passwordtable where uid=\""+map[uidchoice]+"\" and domain=\""+domain_name+"\";") 
            except sqlite3.Error as error:
                print "Failed to delete ",error
                continue  
        if removechoice == 1:
            print "Enter alias"
            aliasname = raw_input() 
            domain_name = ""
            try:
                cursor = conn.execute("select distinct(domain) from aliastable where alias=\""+aliasname+"\";")
            except sqlite3.Error as error:
                print "Failed to find domain ",error
                continue
            for i in cursor:
                domain_name = i[0] 
            try: 
                conn.execute("delete from passwordtable where domain=\""+domain_name+"\";") 
                conn.commit()
            except sqlite3.Error as error:
                print "Failed to delete from main table ",error
                continue
        continue
    if choice == 6:
        print "Alias"
        aliasname = raw_input()
        domain_name = ""
        try:
            cursor = conn.execute("select distinct(domain) from aliastable where alias=\""+aliasname+"\";")
        except sqlite3.Error as error:
            print "Didn't find domain ",error
            continue
        for i in cursor:
            domain_name = i[0]
        try:
            cursor = conn.execute("select uid from passwordtable where domain=\""+domain_name+"\";")
        except sqlite3.Error as error:
            print "Did not find userid for the domain ",error
            continue
        map = {}
        index = 1
        for i in cursor:
            print str(index) + "  " + i[0]
            map[index] = i[0]
            index = index+1
        uidchoice = input()
        try: 
            password = getpass.getpass() 
        except Exception as error: 
            print('ERROR', error)
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encoded_text = cipher.encrypt(password)
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        todaydate = str(day)+"/"+str(month)+"/"+str(year)
        try:
            conn.execute("update passwordtable set password=\""+encoded_text+"\",key=\""+key+"\",modified_date=\""+todaydate+"\"  where uid=\""+map[uidchoice]+"\" and domain=\""+domain_name+"\";")
            print "updated"
            conn.commit()
        except sqlite3.Error as error:
            print "Update failed ",error
            continue
        continue
    if choice == 7:
        conn.close()
        print "Bye"
        exit()
