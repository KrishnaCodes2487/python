age=int(input('Enter the age of voter='))
if age >= 18:
    gender=input('Enter the gender of voter=')
    gender=gender.upper()
    if gender=='M'or gender=='MALE':
        print('Allowed the voter to vote from room no=20')

    else:
        print('Allowed the voter to vote from room no=30')
else:
    print('Voter not allowed')
