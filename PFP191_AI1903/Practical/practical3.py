import random
class Main:
            def guess(self, min, max):
                guess = random.randint(min, max)
                return guess
            #====================GuessNumber function====================
            def GuessNumber(self, number):
                # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
                min = 0
                max = int(number)
                guess = self.guess(min, max)
                while True:
                    awnser = input("Is {} too high(h), too low(l), or correct(c)? ".format(guess))
                    if awnser == 'l':
                        min = guess + 1
                        guess = self.guess(min, max)
                    elif awnser == 'h':
                        max = guess - 1
                        guess = self.guess(min, max)
                    elif awnser == 'c':
                        print("Welldone! The computer guessed your number {} correctly!".format(guess))
                        break
                    else:
                        print("Invalid awnser. Please enter h,l or c.")
                # end def

        #==================DO NOT CHANGE THE CODE BELOW=====================
            def main(self):
                number = input("Enter a range for guessed number: ")
                print("OUTPUT")
                self.GuessNumber(number)
                print("FINISH")
main = Main()
main.main()

