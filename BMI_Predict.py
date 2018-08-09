def body_mass_index(weight, height):
    """Returns the BMI based on weight and height.

    weight: float or int

    height: float or int

    Returns: float or int
    """
    return round(weight / height ** 2 , 2)


def weight_category(bmi):
    """Returns the weight category of the user based on their BMI.

    Returns: str
    """
    if bmi < 18.5:
        return 'underweight'

    elif 18.5 <= bmi <= 24.99:
        return 'healthy weight'

    elif 25.0 <= bmi <= 29.99:
        return 'overweight'

    elif bmi > 30:
        return 'obese'


def wants_to_start():
    """Asks whether the user wants to start.

    Returns: bool
    """
    while True: 
        answer = input("Y to start N to exit: ").upper()

        if answer == 'Y':
            return True
        elif answer == 'N':
            return False

        print('Please try again.\n')


def get_user_data():
    """Asks for the user's weight and height.

    Rerurns: tuple of 2 floats or integers
    """   
    while True:
        try:
            weight = float(input('Enter your weight in kilograms: '))
            height = float(input('Enter your height in meters: '))

            if 0 < weight and 0 < height:
                return weight, height
            else:
                raise ValueError()

        except ValueError:
            print('Invalid input for weight or height')
            continue


def main():
    if wants_to_start():
        weight, height = get_user_data()
        bmi = body_mass_index(weight, height)
        category = weight_category(bmi)
        print('Your BMI is: ', bmi)
        print('Your are ', category, '.')

    else:
        quit()

#if __name__ == '__main__':
main()
