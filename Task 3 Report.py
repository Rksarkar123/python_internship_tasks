from fpdf import FPDF
import pandas as pd


data = {
    "Metric": ["Sales", "Revenue", "Profit"],
    "Value": [10000, 50000, 15000]
}
df = pd.DataFrame(data)


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", style='B', size=16)
        self.cell(200, 10, "Automated Report", ln=True, align='C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=10)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

for index, row in df.iterrows():
    pdf.cell(40, 10, row["Metric"], border=1)
    pdf.cell(50, 10, str(row["Value"]), border=1, ln=True)


pdf.output("report.pdf")
print("PDF report generated successfully.")