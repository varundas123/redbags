from flask import Flask, render_template, request
from datetime import date, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    emi_total = 0.0

    if request.method == 'POST':
        principal = float(request.form['principal'])
        rate = float(request.form['rate'])
        tenure = int(request.form['tenure'])
        monthlyrate = rate / (12 * 100)
        
        emi_schedule = request.form.get('emi_schedule')
        
        if emi_schedule:
            today = date.today()
            remaining_tenure = tenure
            total_disbursed = 375000
            emi = 0.0
            
            for month in range(1, tenure + 1):
                if total_disbursed == 375000:
                    disbursed_amount = min(principal * 30 / 100, principal - total_disbursed)
                    total_disbursed += disbursed_amount
                    emi = round(float(total_disbursed * monthlyrate * (1 + monthlyrate) ** remaining_tenure) /
                                (((1 + monthlyrate) ** remaining_tenure) - 1))
                elif month % 3 == 1 and total_disbursed < principal:
                    disbursed_amount = min(principal * 10 / 100, principal - total_disbursed)
                    total_disbursed += disbursed_amount
                    emi = round(float(total_disbursed * monthlyrate * (1 + monthlyrate) ** remaining_tenure) /
                                (((1 + monthlyrate) ** remaining_tenure) - 1))
                
                emi_date = today.strftime("%d/%m/%Y")
                emi_total += emi
                
                result.append({
                    'date': emi_date,
                    'disbursed_amount': round(total_disbursed, 2),
                    'remaining_tenure': remaining_tenure,
                    'emi': emi
                })
                
                today += timedelta(days=30)
                remaining_tenure -= 1
    
    return render_template('index.html', result=result, emi_total=emi_total)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
