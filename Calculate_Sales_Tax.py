# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:57:03 2020

@author: hp
"""
# Depending on where an individual is from I tax them by the applicable tax rate, appropriately.
# Sales tax is calculated by multiplying the purchase price by the corresponding state tax rate.
# The following U.S. sales tax rates in this project is related to the year 2018.
# However, it becomes out of date as soon as the state or local tax authorities make changes to tax laws and rules.

# Insert your "State" and your "Purchase Amount".
state = "AL"
purchase_amount = 10000

# Alabama, AL, 9.1%
if state == "AL":
    tax_rate = .091
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is {},\nYour State Tax Rate {}.".format(state, total_cost, tax_rate)

# Alaska, AK, 1.8%    
elif state == "AK":
    tax_rate = .018
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# American Samoa, AS, 7.8%    
elif state == "AS":
    tax_rate = .078
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Arizona, AZ, 8.3%   
elif state == "AZ":
    tax_rate = .083
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is :{},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Arkansas, AR, 9.4%   
elif state == "AR":
    tax_rate = .094
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# California, CA, 8.5%  
elif state == "CA":
    tax_rate = .085
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Colorado, CO, 7.5% 
elif state == "CO":
    tax_rate = .075
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Connecticut, CT, 6.4% 
elif state == "CT":
    tax_rate = .064
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Delaware, DE, 0.0%
elif state == "DE":
    tax_rate = .000
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# District of Columbia, DC, 6%
elif state == "DC":
    tax_rate = .060
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Florida, FL, 6.8%
elif state == "FL":
    tax_rate = .068
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Georgia, GA, 7.2%
elif state == "GA":
    tax_rate = .072
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Guam, GU, 4%
elif state == "GU":
    tax_rate = .040
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Hawaii, HI, 4.3%
elif state == "HI":
    tax_rate = .043
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Idaho, ID, 6%
elif state == "ID":
    tax_rate = .060
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Illinois, IL, 8.7%
elif state == "IL":
    tax_rate = .087
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Indiana, IN, 7%
elif state == "IN":
    tax_rate = .070
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Iowa, IA, 6.8%
elif state == "IA":
    tax_rate = .068
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Kansas, KS, 8.7%
elif state == "KS":
    tax_rate = .087
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Kentucky, KY, 6%
elif state == "KY":
    tax_rate = .060
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Louisiana, LA, 10%
elif state == "LA":
    tax_rate = .010
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Maine, ME, 5.5%
elif state == "ME":
    tax_rate = .055
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Maryland, MD, 6%
elif state == "MD":
    tax_rate = .060
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Massachusetts, MA, 6.3%
elif state == "MA":
    tax_rate = .063
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Michigan, MI, 6%
elif state == "MI":
    tax_rate = .060
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Minnesota, MN, 7.4%
elif state == "MN":
    tax_rate = .074
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Mississippi, MS, 7.1%
elif state == "MS":
    tax_rate = .071
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Missouri, MO, 8%
elif state == "MO":
    tax_rate = .080
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Montana, MT, 0.0%
elif state == "MT":
    tax_rate = .000
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Nebraska, NE, 6.9%
elif state == "NE":
    tax_rate = .069
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Nevada, NV, 8.1%
elif state == "NV":
    tax_rate = .081
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# New Hampshire, NH, 0.0%
elif state == "NH":
    tax_rate = .000
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# New Jersey, NJ, 6.6%
elif state == "NJ":
    tax_rate = .066
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# New Mexico, NM, 7.7%
elif state == "NM":
    tax_rate = .077
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# New York, NY, 8.5%
elif state == "NY":
    tax_rate = .085
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# North Carolina, NC, 7%
elif state == "NC":
    tax_rate = .070
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# North Dakota, ND, 6.8%
elif state == "ND":
    tax_rate = .068
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Northern Mariana Islands, MP, 0.0%
elif state == "MP":
    tax_rate = .000
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Ohio, OH, 7.2%
elif state == "OH":
    tax_rate = .072
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Oklahoma, OK, 8.9%
elif state == "OK":
    tax_rate = .089
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Oregon, OR, 0.0%
elif state == "OR":
    tax_rate = .000
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Pennsylvania, PA, 6.3%
elif state == "PA":
    tax_rate = .063
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Puerto Rico, PR, 10.5%
elif state == "PR":
    tax_rate = .105
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Rhode Island, RI, 7%
elif state == "RI":
    tax_rate = .070
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# South Carolina, SC, 7.4%
elif state == "SC":
    tax_rate = .074
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# South Dakota, SD, 6.4%
elif state == "SD":
    tax_rate = .064
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Tennessee, TN, 9.5%
elif state == "TN":
    tax_rate = .095
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Texas, TX, 8.2%
elif state == "TX":
    tax_rate = .082
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Utah, UT, 6.8%
elif state == "UT":
    tax_rate = .068
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Vermont, VT, 6.2%
elif state == "VT":
    tax_rate = .062
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Virginia, VA, 5.6%
elif state == "VA":
    tax_rate = .056
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Virgin Islands, VI, 0.0%
elif state == "VI":
    tax_rate = .000
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Washington, WA, 9.2%
elif state == "WA":
    tax_rate = .092
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# West Virginia, WV, 6.4%
elif state == "WV":
    tax_rate = .064
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Wisconsin, WI, 5.4%
elif state == "WI":
    tax_rate = .054
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

# Wyoming, WY, 5.5%
elif state == "WY":
    tax_rate = .055
    total_cost = purchase_amount * (1 + tax_rate)
    receipt = "Since you are from {},\nYour Total Cost is: {},\nYour State Tax Rate is: {}.".format(state, total_cost, tax_rate)

print(receipt)    
    

