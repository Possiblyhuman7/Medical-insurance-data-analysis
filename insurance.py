from statistics import mean
import pandas as pd

with open("insurance.csv") as insfile:
    df = pd.read_csv(insfile, header=0, index_col=None)
    ins_list = df.to_dict(orient="records")

# An example of the dict format
print(ins_list[0])

# The total number of participants
total_participants = len(ins_list)
print("The total number of participants is: " + str(total_participants))

# Average insurance cost, importing the mean function for convenience
avg_cost = round(mean((x["charges"]) for x in ins_list), 2)
print("The average insurance cost is :" + str(avg_cost))

# Maximum and minimum insurance costs and which participant they are for
max_cost = max((x["charges"]) for x in ins_list)
max_cost_r = round(max_cost, 2)
max_person = next(row for row in ins_list if row["charges"] == max_cost)
min_cost = min((x["charges"]) for x in ins_list)
min_cost_r = round(min_cost, 2)
min_person = next(row for row in ins_list if row["charges"] == min_cost)
print("The most expensive charge is " + str(max_cost_r) + " for \n" + str(max_person))
print("The cheapest charge is " + str(min_cost_r) + " for \n" + str(min_person))


# Finding out the sex distribution of the participants;
# Making counter function for each individual gender in case there will be more/other gender options later
def gender_count(gender):
    num = 0
    for x in range(0, total_participants):
        if ins_list[x]["sex"] == gender:
            num += 1
    return num


num_of_females = gender_count("female")
num_of_males = gender_count("male")

print("\nNumber of female participants: " + str(num_of_females))
print("Number of male participants: " + str(num_of_males))

# Researching the distribution between smoker and non-smokers among people with
# and without children

smoke_child = 0
nonsmoke_child = 0
smoke_nochild = 0
nosmoke_nochild = 0

for x in range(0, total_participants):
    if int(ins_list[x]["children"]) > 0:
        if ins_list[x]["smoker"] == "yes":
            smoke_child += 1
        else:
            nonsmoke_child += 1
    elif ins_list[x]["smoker"] == "yes":
        smoke_nochild += 1
    else:
        nosmoke_nochild += 1

# Counting percentages and overall smoker/non-smoker ratio
sc_percent = round((smoke_child / total_participants * 100), 1)
nsc_percent = round((nonsmoke_child / total_participants * 100), 1)
snc_percent = round((smoke_nochild / total_participants * 100), 1)
nsnc_percent = round((nosmoke_nochild / total_participants * 100), 1)
smokers_percent = round(((smoke_child + smoke_nochild) / total_participants), 1) * 100
nonsmoker_percent = 100.0 - smokers_percent
children = round(((smoke_child + nonsmoke_child) / total_participants), 1) * 100
nochildren = 100.0 - children

print("\nDistribution of smoking among childless people and people with children:")
print("       Smokers with children: " + str(smoke_child) + " or " + str(sc_percent) + "%")
print("    Smokers without children: " + str(smoke_nochild) + " or " + str(snc_percent) + "%")
print("   Non-smokers with children: " + str(nonsmoke_child) + " or " + str(nsc_percent) + "%")
print("Non-smokers without children: " + str(smoke_child) + " or " + str(sc_percent) + "%")
print("Overall percentages: " + str(smokers_percent) + "% smokers, " + str(nonsmoker_percent) + "% non-smokers")
print("                     " + str(children) + "% people with children, " + str(
    nochildren) + "% people without children")

smoker_child_ratio = round((smoke_child / (smoke_child + nonsmoke_child) * 100), 1)
smoker_nochild_ratio = round((smoke_nochild / (smoke_nochild + nosmoke_nochild) * 100), 1)
print("Compared to the overall percentages, " + str(smoker_child_ratio) + "% of people with children smoke,")
print("while " + str(smoker_nochild_ratio) + "% of childless people smoke")

# Calculating BMI to categorize according to the NHS website
def bmi_cat():
    underweight = 0
    healthy = 0
    overweight = 0
    obese = 0
    for x in ins_list:
        y = x["bmi"]
        if y < 18.5:
            underweight += 1
        elif y < 25:
            healthy += 1
        elif y < 30:
            overweight += 1
        else:
            obese += 1
    return underweight, healthy, overweight, obese

underweight, healthy, overweight, obese = bmi_cat()

# Calculating percentages
uw_percent = round((underweight / total_participants * 100), 1)
hw_percent = round((healthy / total_participants * 100), 1)
ow_percent = round((overweight / total_participants * 100), 1)
obw_percent = round((obese / total_participants * 100), 1)

print("\nBMI distribution of participants:")
print("Underweight: " + str(uw_percent) + "%")
print("Healthy weight: " + str(hw_percent) + "%")
print("Overweight: " + str(ow_percent) + "%")
print("Obese: " + str(obw_percent) + "%")
