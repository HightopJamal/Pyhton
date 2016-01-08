def main():
    date_str = input("Enter a date (mm/dd/yy): ")

    mnth_str, day_str, year_str = date_str.split('/')

    months = ["January", "February", "March", "April", "May", "June"
              "July", "August", "September", "October", "November",
              "December"]
    mnth_str = months[int(mnth_str)-1]

    print("The converted date is:",mnth_str, day_str + ",", year_str)

main()

