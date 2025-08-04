import pandas as pd
from fpdf import FPDF

# Step 1: Read the CSV file
data = pd.read_csv("sample_data.csv")

# Step 2: Analyze the data (average marks per student)
summary = data.groupby("Name")["Marks"].mean().reset_index()
summary.columns = ["Name", "Average Marks"]

# Step 3: Generate PDF Report
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Student Marks Report", ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Create PDF
pdf = PDFReport()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add Summary Table
pdf.cell(0, 10, "Average Marks per Student", ln=True, align="L")
pdf.ln(5)
for i in range(len(summary)):
    name = summary.iloc[i]["Name"]
    marks = round(summary.iloc[i]["Average Marks"], 2)
    pdf.cell(0, 10, f"{name}: {marks}", ln=True)

# Save the PDF
pdf.output("student_report.pdf")
