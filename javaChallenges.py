from fpdf import FPDF

# Define the challenges focused on arrays and objects in JavaScript
challenges = [
    "1. Write a function that takes an array of numbers and returns the sum of all numbers.",
    "2. Create a function that reverses an array without using the reverse() method.",
    "3. Write a function that filters out all odd numbers from an array.",
    "4. Create a function that counts how many times a value appears in an array.",
    "5. Write a function that takes two arrays and returns a new array with elements from both.",
    "6. Write a function to find the maximum number in an array.",
    "7. Create a function that removes all duplicates from an array.",
    "8. Write a function that returns an array of all the keys in an object.",
    "9. Create a function that returns an array of all the values in an object.",
    "10. Write a function that checks if a specific key exists in an object.",
    "11. Write a function that takes an object and returns a string in 'key: value' format.",
    "12. Write a function that returns the number of properties in an object.",
    "13. Write a function that merges two objects into one.",
    "14. Create a function that takes an array of objects and returns an array of a specific property value (e.g., names).",
    "15. Write a function that sorts an array of numbers in ascending order.",
    "16. Write a function that capitalizes the first letter of each word in an array of strings.",
    "17. Write a function that finds the intersection of two arrays (common values).",
    "18. Create a function that returns true if all values in an array are the same.",
    "19. Write a function that removes falsy values from an array.",
    "20. Create a function that groups an array of objects by a specific property."
]

# Create the PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="JavaScript Practice Challenges", ln=True, align="C")
pdf.ln(10)

for challenge in challenges:
    pdf.multi_cell(0, 10, txt=challenge)

# Save the PDF
pdf_path = "/mnt/data/JavaScript_Array_Object_Challenges.pdf"
pdf.output(pdf_path)

pdf_path