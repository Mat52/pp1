from mymath import *
usernumber = read_number()
computernumber = generate_number()

if (computernumber == usernumber):
    print(f"Wygrałeś, komputer też podał {computernumber}")
else:
    print(f"Przegrałeś, ty podałeś {usernumber} a komputer {computernumber}")