
# Libraries needed to import
import datetime
#PROBLEM SOLVING- COMMISSION BONUS

currDate = datetime.datetime.now()
currDate = currDate.strftime("%d-%m-%Y")
#UNCOMMENT BELOW TO CHECK DATE FUNCTION WORKS CORRECTLY
#currDate = '01-04-2023'

def commission_bonus():
    #FUNCTION TO DETERMINE EMPLOYEE COMMISSION BONUS
    # SETUP HEADER FOR LOOP
    print()
    print("SIMPSON CARPET WORLD")
    print("EMPLOYEE COMMISSION CHART")
    print()
    print("EMPLOYEE              TOTAL              COMMISSION")
    print("NUMBER                SALES                 TOTAL")
    print("*"*51)

    commission_rate = .06

    #reading sales.dat
    f=open('sales.dat', 'r')
    for sales in f:
        salesline = sales.split(",")
        empID = int(salesline[1].strip())
        subtotal = float(salesline[3].strip())

        subtotal_DSP = "${:,.2f}".format(subtotal)
        if subtotal >= 5000:
            commission = (subtotal * commission_rate) + 200

        else:
            commission = subtotal * commission_rate

        commission_DSP = "${:,.2f}".format(commission)




        print(f"{empID:<4}              {subtotal_DSP:>10}             {commission_DSP:>10}")
    print("*" * 51)
    input("Press enter to continue to the company services")
    f.close()


if currDate[0] == '0' and currDate[1] == '1':
    commission_bonus()


def newEmployee():
    #reading defaults file to get the constants for the program
    f = open('simpsonDef.dat', 'r')
    HIRE_NUM = int(f.readline())
    COMM_RATE = float(f.readline())
    BONUS_SALES = float(f.readline())
    COMM_BONUS = float(f.readline())
    HST_RATE = float(f.readline())
    f.close()


    while True:
        print("Log the information of the newest member of the Simpson Carpet World Family")
        while True:
            firstName = input("Log the new employee's first name: ").title()
            if firstName == "":
                print("Cannot be left blank, input valid name.")
            else:
                break

        while True:
            lastName = input("Log the new employee's last name: ").title()
            if lastName == "":
                print("Cannot be left blank, input valid name.")
            else:
                break

        while True:
            empBirthday = input("Log the new employee's date of birth (DD-MM-YYYY): ")
            if empBirthday == "":
                print("Cannot be left blank, input valid date.")

            elif len(empBirthday) != 10:
                print("Date too long or too short, input valid date.")

            elif empBirthday[2] != "-" or empBirthday[5] != "-":
                print("Must be a slash separating numbers, input valid date.")

            elif not empBirthday[:2].isdigit():
                print("Date must contain only numbers, input valid date.")
            elif not empBirthday[3:4].isdigit():
                print("Date must contain only numbers, input valid date.")
            elif not empBirthday[-4:].isdigit():
                print("Date must contain only numbers, input valid date.")
            else:
                break

        while True:
            empStreet = input("Log the new employee's street address: ").title()
            if empStreet == "":
                print("Cannot be left blank, input valid street address.")
            else:
                break

        while True:
            empCity = input("Log the new employee's city: ").title()
            if empCity == "":
                print("Cannot be left blank, input valid city.")
            else:
                break

        while True:
            provList = ["YT", "NT", "NU", "BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL"]
            empProv = input("Log the new employee's province (XX): ").upper()
            if empProv == "":
                print("Cannot be left blank, input valid province.")

            elif len(empProv) != 2:
                print("Use abbreviation for province, enter valid province.")

            elif not empProv in provList:
                print("Invalid province name, input valid province ")
            else:
                break

        while True:
            empPost = input("Log the new employee's postal code (X#X#X#): ").upper()
            if empPost == "":
                print("Cannot be left blank, input valid postal code.")

            elif len(empPost) != 6 :
                print("Not a valid postal code, input valid postal code.")

            elif not empPost[0].isalpha():
                print("Must be a letter, enter valid postal code.")
            elif not empPost[2].isalpha():
                print("Must be a letter, enter valid postal code.")
            elif not empPost[4].isalpha():
                print("Must be a letter, enter valid postal code.")
            elif  not empPost[1].isdigit():
                print("Must be a number, enter valid postal code.")
            elif not empPost[3].isdigit():
                print("Must be a number, enter valid postal code.")
            elif not empPost[5].isdigit():
                print("Must be a number, enter valid postal code.")

            else:
                break

        while True:
            empPhone = input("Log the new employee's phone number (###-###-####)")
            if empPhone == "":
                print("Cannot be left blank, input valid phone number.")

            elif len(empPhone) != 12:
                print("Phone number too long or too short, input valid phone number.")

            elif empPhone[3] != "-" or empPhone[7] != "-":
                print("Must be a hyphen separating numbers, input valid phone number.")

            elif not empPhone[:3].isdigit():
                print("Phone number must contain only numbers, input valid phone number.")
            elif not empPhone[4:6].isdigit():
                print("Phone number must contain only numbers, input valid phone number.")
            elif not empPhone[-3:].isdigit():
                print("Phone number must contain only numbers, input valid phone number.")
            else:
                break

        while True:
            dateOfHire = input("Log the new employee's date of hire (DD-MM-YYYY): ")
            if dateOfHire == "":
                print("Cannot be left blank, input valid date.")

            elif len(dateOfHire) != 10:
                print("Date too long or too short, input valid date.")

            elif dateOfHire[2] != "-" or dateOfHire[5] != "-":
                print("Must be a slash separating numbers, input valid date.")

            elif not dateOfHire[:2].isdigit():
                print("Date must contain only numbers, input valid date.")
            elif not dateOfHire[3:4].isdigit():
                print("Date must contain only numbers, input valid date.")
            elif not dateOfHire[-4:].isdigit():
                print("Date must contain only numbers, input valid date.")
            else:
                break


        while True:
            branch = input("Log the new employee's branch number of hire: ")
            if branch == "":
                print("Cannot be left blank, input valid branch.")
            elif not branch.isdigit():
                print("Branch identification must be a number, input valid branch number")
            else:
                break

        while True:
            empTitle = input("Log the new employee's title: ").title()
            if empTitle == "":
                print("Cannot be left blank, input valid title.")
            else:
                break

        while True:
            try:
                empWage = float(input("Log the new employee's hourly pay rate: "))
            except:
                print("Hourly pay rate is invalid, input valid rate.")
            else:
                break

        while True:
            empSkills = input("Log the new employee's relevant skills (separate with'/'): ")
            if empSkills == "":
                print("Cannot be left blank, input valid list of skills.")
            else:
                break

        # updating counter for number of people that have been hired
        HIRE_NUM += 1

        # creating output of all the new employees information
        print()
        print()
        print(" "* 16 + "Simpson Carpet World Employee Database" + " "* 16)
        print(" "* 15 + "*" * 40 + " "* 15)
        print()
        print("Information for:", firstName, lastName)
        print("Identification number:", HIRE_NUM)
        print()
        print("Personal information:" + " "*25 + "Employment Information:")
        print("-" * 26 + " " * 20 + "-" * 24)
        print("Date of birth:", f"{empBirthday:<31s}" + "Date of Hire:", dateOfHire)
        print("Phone number:", f"{empPhone:<32s}" + "Branch:", branch)
        print("Address:", f"{empStreet:<36s}", "Title:", empTitle)
        empWageDSP = "${:.2f}".format(empWage)
        print("        ", f"{empCity:<36s}", "Salary rate:", f"{empWageDSP:<6s}")
        print("        ", empProv)
        print("        ", empPost)
        print()


        # writing values for employee information to Employees.dat
        f = open('Employees.dat', 'a')
        f.write("{}, ".format(HIRE_NUM))
        f.write("{}, ".format(firstName))
        f.write("{}, ".format(lastName))
        f.write("{}, ".format(empBirthday))
        f.write("{}, ".format(empStreet))
        f.write("{}, ".format(empCity))
        f.write("{}, ".format(empProv))
        f.write("{}, ".format(empPost))
        f.write("{}, ".format(empPhone))
        f.write("{}, ".format(dateOfHire))
        f.write("{}, ".format(branch))
        f.write("{}, ".format(empTitle))
        f.write("{}, ".format(empWage))
        f.write("{}\n ".format(empSkills))
        f.close()

        # Writing back the defaults data sheet
        f = open('simpsonDef.dat', 'w')
        f.write("{}\n ".format(HIRE_NUM))
        f.write("{}\n ".format(COMM_RATE))
        f.write("{}\n ".format(BONUS_SALES))
        f.write("{}\n ".format(COMM_BONUS))
        f.write("{}\n ".format(HST_RATE))
        f.close()



        print()
        print("*"*16 + "The employee database has been updated" + "*"*16)
        print("="*70)
        exitEmployee = input("Continue with the next new employee? (Y for yes, END to quit): ").upper()
        if exitEmployee != "Y":
            break
        print()
        print()

def empListing():
    #Desigining report for employee listings
    print()
    print('\033[1m' + "SIMPSON CARPET WORLD" + '\033[0m')
    print()
    currDate = datetime.datetime.now()
    currDate = currDate.strftime("%d-%m-%Y")
    print('\033[1m' +"EMPLOYEE LISTING AS OF " + currDate + '\033[0m')
    print()
    print()
    print("Employee   " + "Employee       " + "Street       " + "Phone         " + "Date        " +"Branch      " +"Title")
    print("Number     " + "Name           " + "Address      " + "Number        " + "Hire")
    print("=" *90)

    f = open('Employees.dat', 'r')
    for employee in f:
        employeeLine = employee.split(",")
        empID = employeeLine[0].strip()
        firstName = employeeLine[1].strip()
        lastName = employeeLine[2].strip()
        birthday = employeeLine[3].strip()
        street = employeeLine[4].strip()
        city = employeeLine[5].strip()
        prov = employeeLine[6].strip()
        postCode = employeeLine[7].strip()
        phoneNum = employeeLine[8].strip()
        hireDate = employeeLine[9].strip()
        branch = employeeLine[10].strip()
        title = employeeLine[11].strip()
        wage = employeeLine[12].strip()
        skills = employeeLine[13].strip()
        print(f"{empID:<8s}" + f"{(firstName + ' ' + lastName):<16s}" + f"{street:<16s}" + "  " + f"{phoneNum:<15s}" + f"{hireDate:<13s}" + f"{branch:<10s}" + title)
    f.close()
    print("=" * 90)
    print()
    input("Press enter to continue")


def reorderListing():
    # Designing report for reorder listing
    print()
    print('\033[1m' + "SIMPSON CARPET WORLD" + '\033[0m')
    print()
    currDate = datetime.datetime.now()
    currDate = currDate.strftime("%d-%m-%Y")
    print('\033[1m' + "REORDER LISTING AS OF " + currDate + '\033[0m')
    print()
    print()
    print("Item" + " "*18 + "QOH" + " "*17 + "Reorder" + " "*19 + "Maximum")
    print("Number" + " "*36 + "Point" + " "*21 +"Level")
    print("=" * 82)
    # For loop for the data file

    reOrderCount = 0

    f = open('new_inventory.dat', 'r')
    for reOrder in f:
        reOrderLine = reOrder.split(",")
        itemNum =reOrderLine[0].strip()
        description = reOrderLine[1].strip()
        colour = reOrderLine[2].strip()
        pattern = reOrderLine[3].strip()
        size = reOrderLine[4].strip()
        type = reOrderLine[5].strip()
        itemCost = float(reOrderLine[6].strip())
        retailCost = float(reOrderLine[7].strip())
        qoh = int(reOrderLine[8].strip())
        reorderPoint = int(reOrderLine[9].strip())
        maxLevel = int(reOrderLine[10].strip())

        print(f"{itemNum:<21s}", f"{qoh:<19d}", f"{reorderPoint:<25d}", maxLevel)
        if qoh <= reorderPoint:
            reOrderCount += 1
    f.close()


    print("=" * 82)
    print("Total Items for Reorder:", reOrderCount)
    print()
    input("Press enter to continue")


def mainMenu():
    print("This section is currently not in use. ")
    input("Press enter to return back to the menu and continue logging your information...")


# pretty all this stuff up
while True:
    print()
    print()
    print(" " * 10 + "*" * 27)
    print(" " * 10 +"Simpson Carpet World")
    print(" " * 10 +"Company Services System")
    print()
    print(" " * 10 +"1. Enter a New Employee")
    print(" " * 10 +"2. Enter a New Customer")
    print(" " * 10 +"3. Enter a New Inventory Item")
    print(" " * 10 +"4. Record Customer Purchase")
    print(" " * 10 +"5. Print Employee Listing")
    print(" " * 10 +"6. Print Customers by Branch")
    print(" " * 10 +"7. Print Orders By Customer")
    print(" " * 10 +"8. Print Reorder Listing")
    print(" " * 10 +"9. Quit Program")
    choice = input(" " * 10 + "Enter choice (1-9): ")

# if statements for each choice including number validation at bottom

    if choice == "1":
        newEmployee()
    elif choice == "2":
        mainMenu()
    elif choice == "3":
        mainMenu()
    elif choice == "4":
        mainMenu()
    elif choice == "5":
        empListing()
    elif choice == "6":
        mainMenu()
    elif choice == "7":
        mainMenu()
    elif choice == "8":
        reorderListing()
    elif choice == "9":
         exit()
    elif choice != ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
         print("invalid input try again")

