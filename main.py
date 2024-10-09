import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from homepage import *
import resources
import webbrowser as wb

#----------------------------------------------------------------------------
#The Main App Widget Window
#----------------------------------------------------------------------------
class MainApp(QWidget, Ui_Form):
        def __init__(self):
                super().__init__()
                self.setupUi(self)  

                self.exits.clicked.connect(self.exitProgram)  
                self.contacts.clicked.connect(self.showMembers)
                
                self.pushLinear.clicked.connect(self.showLinear)
                self.pushCombination.clicked.connect(self.showCombination)
                self.pushCircular.clicked.connect(self.showCircular)
                self.pushTruncated.clicked.connect(self.showTruncated)
                self.pushRepeated.clicked.connect(self.showRepeated)
                
        def showRepeated(self):
                self.rep = Repeated()
                self.rep.show()
                self.close()
        def showTruncated(self):
                self.truncated = Truncated()
                self.truncated.show()
                self.close()
        def showLinear(self):
                self.linear = Linear()
                self.linear.show()
                self.close()
        
        def showCombination(self):
                self.combination = Combination()
                self.combination.show()
                self.close()    
        
        def showCircular(self):
                self.circular = Circular()
                self.circular.show()
                self.close()
        
        def exitProgram(self):
                self.close()
        def showMembers(self):
                self.members = Members()
                self.members.show()
                self.close()


#----------------------------------------------------------------------------
#This is the members widget window
#----------------------------------------------------------------------------
class Members(QWidget, Ui_Members):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backMain)
                
                self.gabfb.clicked.connect(self.showGabFb)
                self.gabig.clicked.connect(self.showGabIg)
                
                self.jeffb.clicked.connect(self.showJefFb)
                self.jefig.clicked.connect(self.showJefIg)
                
                self.jpfb.clicked.connect(self.showJpFb)
                self.jpig.clicked.connect(self.showJpIg)   
                
        def backMain(self):
                self.main = MainApp()
                self.main.show()
                self.close()
        
        def showGabFb(self):
                wb.open("https://www.facebook.com/gab.alpuerto.5")
        
        def showGabIg(self):
                wb.open("https://www.instagram.com/gabmahiya/")
        
        def showJefFb(self):
                wb.open("https://www.facebook.com/jefersonruiz.cabalsa")
                
        def showJefIg(self):
                wb.open("https://www.instagram.com/jefersonruizz/")
                
        def showJpFb(self):
                wb.open("https://www.facebook.com/JohnPaul.Martirez18")
        
        def showJpIg(self):
                wb.open("https://www.instagram.com/lopnajj_/")


#----------------------------------------------------------------------------
#Linear Widget Windows
#----------------------------------------------------------------------------      
class Linear(QWidget, Ui_Linear):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.pushButton.clicked.connect(self.backMain)
                self.meaning.clicked.connect(self.showMeaning)
                self.application.clicked.connect(self.showApplication)
        
        def showApplication(self):
                self.app = LinearInstruct()
                self.app.show()
                self.close()
        def backMain(self):
                self.main = MainApp()
                self.main.show()
                self.close()
        
        def showMeaning(self):
                self.showMean = LinearMeaning()
                self.showMean.show()
                self.close()

class LinearMeaning(QWidget, Ui_LinearMeaning):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backLinear)
        
        def backLinear(self):
                self.linear = Linear()
                self.linear.show()
                self.close()

class LinearInstruct(QWidget, Ui_LinearApplication):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.backLinear.clicked.connect(self.backPage)
                self.tryLinear.clicked.connect(self.showSystem)
        
        def showSystem(self):
                self.system = LinearSystem()
                self.system.show()
                self.close()
                
        def backPage(self):
                self.main = Linear()
                self.main.show()
                self.close()

class LinearSystem(QWidget, Ui_LinearSystem):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backInstruct)
                self.generate_button.clicked.connect(self.generate_arrangements)
        
        def backInstruct(self):
                self.linear = LinearInstruct()
                self.linear.show()
                self.close()
        
        def generate_permutations(self, arr):
                n = len(arr)
                result = []
                
                arr.sort()  # Start with the sorted order
                result.append(arr[:])  # Add the first permutation
                while True:
                        # Step 1: Find the largest k such that arr[k] < arr[k + 1]
                        k = -1
                        for i in range(n - 1):
                                if arr[i] < arr[i + 1]:
                                        k = i
                        if k == -1:
                                break  # All permutations are done
                        
                        # Step 2: Find the largest l greater than k such that arr[k] < arr[l]
                        l = -1
                        for i in range(k + 1, n):
                                if arr[k] < arr[i]:
                                        l = i

                        # Step 3: Swap arr[k] with arr[l]
                        arr[k], arr[l] = arr[l], arr[k]

                        # Step 4: Reverse the sequence from k + 1 to the end
                        arr[k + 1:] = reversed(arr[k + 1:])
                        result.append(arr[:])  # Add the new permutation to the result
                        
                return result

    # Main function inside your PyQt6 class
        def generate_arrangements(self):
                # Get student names
                student_names_raw = self.name_input.text().split(',')
                student_names = []
                for name in student_names_raw:
                        student_names.append(name.strip())

                # If no names are provided, show an error message
                if student_names == ['']:
                        self.output_area.setText("Please enter at least one student name.")
                        return

                # Call the separated function to generate permutations
                arrangements = self.generate_permutations(student_names)

                # Convert permutations to display format
                result_text = ""
                result_text += f"Total Seat Arrangements: {len(arrangements)} \n\n"
                for arrangement in arrangements:
                        result_text += " -> ".join(arrangement) + "\n"
                
                self.output_area.setText(result_text)


#----------------------------------------------------------------------------
#Combination Widget Windows
#----------------------------------------------------------------------------
class Combination(QWidget, Ui_Combinations):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backMain)
                self.meaning.clicked.connect(self.showMeaning)
                self.application.clicked.connect(self.showInstruct)
                
        def showInstruct(self):
                self.app = CombinationInstruct()
                self.app.show()
                self.close()
                
        def showMeaning(self):
                self.showMean = CombinationMeaning()
                self.showMean.show()
                self.close()
        
        def backMain(self):
                self.main = MainApp()
                self.main.show()
                self.close()
                
class CombinationMeaning(QWidget, Ui_CombinationMean):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backCombination)
                
        def backCombination(self):
                self.back = Combination()
                self.back.show()
                self.close()
                
class CombinationInstruct(QWidget, Ui_CombinationApplication):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.backLinear.clicked.connect(self.backPage)
                self.tryLinear.clicked.connect(self.showSystem)
        
        def showSystem(self):
                self.showsys = CombinationSystem()
                self.showsys.show()
                self.close()
        
        def backPage(self):
                self.main = Combination()
                self.main.show()
                self.close()
                
class CombinationSystem(QWidget, Ui_CombinationSystem):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backInstruct)   
                self.generate_button.clicked.connect(self.generate_combinations)

        def backInstruct(self):
                self.instruction= CombinationInstruct()
                self.instruction.show()
                self.close()
                
        def generate_combinations(self):
                # Get user input for each category
                proteins = [item.strip() for item in self.protein_input.text().split(',') if item.strip()]
                vegetables = [item.strip() for item in self.veg_input.text().split(',') if item.strip()]
                grains = [item.strip() for item in self.grain_input.text().split(',') if item.strip()]
                fruits = [item.strip() for item in self.fruit_input.text().split(',') if item.strip()]

                # Check if inputs are provided
                if not proteins or not vegetables or not grains or not fruits:
                        self.output_area.setText("Please enter valid options for all categories.")
                        return

                # Generate combinations
                combinations = []
                for protein in proteins:
                        for veg in vegetables:
                                for grain in grains:
                                        for fruit in fruits:
                                                combinations.append(f"{protein} + {veg} + {grain} + {fruit}")

                # Calculate total number of combinations
                total_combinations = len(combinations)

                # Display results with total combinations count
                self.output_area.setText(f"Total Combinations: {total_combinations}\n\n" + "\n".join(combinations))

                
        

#----------------------------------------------------------------------------
#Circular Permutations Widget Windows
#----------------------------------------------------------------------------
class Circular(QWidget, Ui_Circular):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backMain)   
                self.meaning.clicked.connect(self.showMeaning) 
                self.application.clicked.connect(self.showInstruct)
                
        def showInstruct(self):
                self.app = CircularInstruct()
                self.app.show()
                self.close()
        
        def backMain(self):
                self.main = MainApp()
                self.main.show()
                self.close()
        
        def showMeaning(self):
                self.showMean = CircularMean()
                self.showMean.show()
                self.close()

class CircularMean(QWidget, Ui_CircularMean):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backCircular)
        
        def backCircular(self):
                self.circular = Circular()
                self.circular.show()
                self.close()
                
class CircularInstruct(QWidget, Ui_CircularApplication):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.backCircular.clicked.connect(self.backPage)
                self.tryCircular.clicked.connect(self.tryApp)
                        
        def tryApp(self):
                self.circularsys = CircularSystem()
                self.circularsys.show()
                self.close()
        
        def backPage(self):
                self.main = Circular()
                self.main.show()
                self.close()

class CircularSystem(QWidget, Ui_CircularSystem):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backPage)
                self.generate_button.clicked.connect(self.generate_arrangements)
                
        def backPage(self):
                self.main = CircularInstruct()
                self.main.show()
                self.close()
        
        def generate_circular_permutations(self, arr):
                n = len(arr)
                if n == 0:
                        return []

                # Fix the first dancer to handle circular permutations
                fixed_dancer = arr[0]
                circular_permutations = []

                # Initialize a list to hold current permutations
                current_permutations = [[]]

                # Iterate through the remaining dancers
                for dancer in arr[1:]:
                        new_permutations = []
                
                # Create new permutations by adding the current dancer to existing permutations
                        for perm in current_permutations:
                                for i in range(len(perm) + 1):
                                        new_permutations.append(perm[:i] + [dancer] + perm[i:])

                        current_permutations = new_permutations

                # Add the fixed dancer to each permutation
                for perm in current_permutations:
                        circular_permutations.append([fixed_dancer] + perm)

                return circular_permutations

        def generate_arrangements(self):
                # Get dancer names
                dancer_names_raw = self.name_input.text().split(',')
                dancer_names = []
                
                # Use a for loop to strip whitespace and filter out empty names
                for name in dancer_names_raw:
                        stripped_name = name.strip()
                        if stripped_name:  # Check if the name is not empty
                                dancer_names.append(stripped_name)
                        
                if dancer_names == []:
                        self.output_area.setText("Please enter at least one dancer name.")
                        return
                
                # Call the function to generate circular permutations
                arrangements = self.generate_circular_permutations(dancer_names)

                # Convert permutations to display format
                result_text = ""
                result_text += f"Total Circular Dance Formation: {len(arrangements)}\n\n"
                for arrangement in arrangements:
                        result_text += " -> ".join(arrangement) + "\n"

                self.output_area.setText(result_text)

#----------------------------------------------------------------------------
#Truncated Widget Windows
#----------------------------------------------------------------------------
class Truncated(QWidget, Ui_Truncated):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backMain)
                
                self.meaning.clicked.connect(self.showMeaning)
                self.application.clicked.connect(self.showApplication)
        
        def backMain(self):
                self.main = MainApp()
                self.main.show()
                self.close()
        
        def showMeaning(self):
                self.showMean = TruncatedMeaning()
                self.showMean.show()
                self.close()
        
        def showApplication(self):
                self.showInstruct = TruncatedInstruct()
                self.showInstruct.show()
                self.close()
                
class TruncatedMeaning(QWidget, Ui_TruncatedMeaning):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backTruncated)
                
        def backTruncated(self):
                self.trunc = Truncated()
                self.trunc.show()
                self.close()                
          
class TruncatedInstruct(QWidget, Ui_TruncatedApplication):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.backTruncated.clicked.connect(self.backPage)
                self.tryTruncated.clicked.connect(self.showApp)
        
        def showApp(self):
                self.showSystem = TruncatedSystem()
                self.showSystem.show()
                self.close()
        
        def backPage(self):
                self.main = Truncated()
                self.main.show()
                self.close()      

class TruncatedSystem(QWidget, Ui_TruncatedSystem):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backInstruct)
                self.generate_button.clicked.connect(self.generate_task_assignments)
                
        
        def backInstruct(self):
                self.main = TruncatedInstruct()
                self.main.show()
                self.close()
        
        def generate_task_assignments(self):
                tasks = ['First Aid', 'Search Operations', 'Supply Delivery']

                # Get the volunteers from the user input
                volunteers_raw = self.volunteer_input.text().split(',')
                volunteers = [volunteer.strip() for volunteer in volunteers_raw if volunteer.strip()]

                # Check if enough volunteers are provided
                if len(volunteers) < 3:
                        self.output_area.setText("Please input correct number of VOLUNTEERS! \nWe need at least 3 volunteers.")
                        return

                all_assignments = self.generate_permutations(volunteers)

                # Prepare output
                result_text = ""
                for assignment in all_assignments:
                        task_assignments = [f"{worker} -> {task}" for worker, task in zip(assignment, tasks)]
                        result_text += "\n".join(task_assignments) + "\n\n"

                # Display the total number of combinations and the assignments
                total_combinations = len(all_assignments)
                self.output_area.setText(f"Total Combinations: {total_combinations}\n\n{result_text}")

        # Function to generate permutations
        def generate_permutations(self, volunteers):
                if len(volunteers) < 3:
                        return []  
                
                results = []
                n = len(volunteers)

                # Generate permutations
                for i in range(n):
                        for j in range(n):
                                for k in range(n):
                                        if i != j and i != k and j != k:  
                                                results.append([volunteers[i], volunteers[j], volunteers[k]])

                return results
        
     

#-------------------------------------------------------------------------------------------------
#Repeated Permutations Widget Windows
#-------------------------------------------------------------------------------------------------              
class Repeated(QWidget, Ui_Repeated):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backMain)
                
                self.meaning.clicked.connect(self.showMeaning)
                self.application.clicked.connect(self.showApplication)
                
        def backMain(self):
                self.main = MainApp()
                self.main.show()
                self.close()
        
        def showMeaning(self):
                self.showMean = RepMeaning()
                self.showMean.show()
                self.close()
        
        def showApplication(self):
                self.tryRep = RepApp()
                self.tryRep.show()
                self.close()     
                
class RepMeaning(QWidget, Ui_RepMeaning):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backRep)
        
        def backRep(self):
                self.rep = Repeated()
                self.rep.show()
                self.close()          

class RepApp(QWidget, Ui_RepApp):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.backRepeated.clicked.connect(self.backRep)
                self.tryRepeated.clicked.connect(self.tryRep)
                
        def backRep(self):
                self.rep = Repeated()
                self.rep.show()
                self.close()

        def tryRep(self):
                self.trysys = RepeatedSystem()
                self.trysys.show()
                self.close()

class RepeatedSystem(QWidget, Ui_RepeatedSystem):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                
                self.back.clicked.connect(self.backInstruct)
                self.generate_button.clicked.connect(self.generate_arrangements)
                
        def backInstruct(self):
                self.main = RepApp()
                self.main.show()
                self.close()

        def generate_arrangements(self):
                # Get categories from input
                categories_raw = self.category_input.text().strip().split(',')
                categories = [category.strip() for category in categories_raw if category.strip()]

                if not categories:
                        self.output_area.setText("Please enter valid book categories.")
                        return

                # Count occurrences of each category
                category_counts = {}
                for category in categories:
                        if category in category_counts:
                                category_counts[category] += 1
                        else:
                                category_counts[category] = 1

                # Generate arrangements
                generated_arrangements = []
                self.generate_permutations([], category_counts, generated_arrangements)


                # Calculate the total number of arrangements
                total_permutations = len(generated_arrangements)
                
                # Display results
                result_text = "\n".join(generated_arrangements) if generated_arrangements else "No arrangements generated."
                result_summary = f"Total arrangements: {total_permutations}\n\n"
                self.output_area.setText(result_summary + result_text)

        def generate_permutations(self, current, counts, generated_arrangements):
                
                if sum(counts.values()) == 0:  # If all categories have been used
                        generated_arrangements.append(' -> '.join(current))
                        return

                for category in counts:
                        if counts[category] > 0:  # If there are still books of this category
                                current.append(category)  # Add the category to the current arrangement
                                counts[category] -= 1  # Decrease the count for this category
                                self.generate_permutations(current, counts, generated_arrangements)  # Recurse
                                counts[category] += 1  # Backtrack
                                current.pop()  # Remove the last added category

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainApp()
        window.show()
        sys.exit(app.exec())
