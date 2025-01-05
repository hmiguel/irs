
class IRS(object):
    def __init__(self, metadata, gross_income, withhold, deductions, county = None, family_quotient=1):
        self.metadata = metadata
        self.county = county
        self.family_quotient = family_quotient
        self.gross_income = gross_income # 1
        self.colectable_income = self.get_colectable_income() # 6
        self.total_income_for_tax_purposes = self.total_income_for_tax_purposes() # 9
        self.tax_values = self.get_tax_values_for_total_income() # 10
        self.amount_calculated = self.amount_calculated() # 11
        self.tax_parcel = self.tax_values['parcel'] # 12     
        self.total_collected = self.total_collected() # 18
        self.deductions = deductions # 19
        self.county_tax = self.metadata.get('county_tax', 0).get(self.county, 0)
        self.county_benefit = self.get_county_benefit() # 20
        self.net_amount = self.net_amount() # 22
        self.withhold = withhold # 24
        self.assessed_tax = self.assessed_tax() # 25
        self.total_value = self.get_total_value() # 30
        # effective tax rate
        self.effective_tax_rate = round(self.net_amount / self.colectable_income, 4)

    def get_total_value(self):
        n_26 = 0 # 26 Juros de retenção-poupança
        n_27 = 0 # 27 Sobretaxa-resultado
        n_28 = 0 # 28 Juros compensatórios
        n_29 = 0 # 29 Juros indemnizatórios
        return round(self.assessed_tax + n_26 + n_27 + n_28 + n_29, 2)

    def assessed_tax(self): # 25
        n_23 = 0 # 23 Pagamentos por conta
        return round(self.net_amount - (n_23 + self.withhold), 2)

    def get_county_benefit(self):
        print(self.county, self.county_tax)
        return round((self.total_collected - self.deductions) * (0.05 - self.county_tax), 2)

    def net_amount(self): # 22 
        n_21 = 0 # 21 Acréscimos à coleta
        return round(self.total_collected - self.deductions - max(0, self.county_benefit) + n_21, 2)

    def total_collected(self): # 18  
        n_13 = 0 # 13 Imposto correspondente a rendimentos anos anteriores       
        n_14 = 0 # 14 Imposto correspondente a rendimentos isentos      
        n_15 = 0 # 15 Taxa adicional (0,00 x 0,0% + 0,00 x 0%) x 1,00       
        n_16 = 0 # 16 Excesso em relação ao limite do quociente familiar      
        n_17 = 0 # 17 Imposto relativo a tributações autónomas
        return round((self.amount_calculated - self.tax_parcel) * 1 + n_13 - n_14 + n_15 + n_16 + n_17, 2)
    
    def get_colectable_income(self):
        specific_deduction = max(self.metadata['specific_deduction'], self.gross_income*self.metadata['social_security_tax']) #2
        returnable_losses = 0 #3
        minimum_existence_allowance = 0 #4
        income_deductions = 0 #5
        return round(self.gross_income - (specific_deduction + minimum_existence_allowance + returnable_losses + income_deductions), 2)

    def total_income_for_tax_purposes(self):
        previous_year_income_quotient = 0 #7
        exempt_income = 0 #8
        return round(self.colectable_income + exempt_income - previous_year_income_quotient , 2)

    def get_tax_values_for_total_income(self):
        irs_table = self.metadata['table']
        for i in range(1, len(irs_table) + 1):
            if self.colectable_income < irs_table[str(i)]['to']:
                return irs_table[str(i)]

    def amount_calculated(self):
        return round(self.total_income_for_tax_purposes / self.family_quotient * self.tax_values['tax'], 2)

if __name__ == "__main__":
    irs = IRS(2024, 60136.24, 16230, 892, "lisboa")
    print(irs.net_amount)
    print(irs.county_benefit)
    print(irs.total_value)