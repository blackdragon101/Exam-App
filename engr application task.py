set_1 = {'Usama','Adeela','Dua','Jihan','Maneeha','Areeba','Uzair','Rafia'}
engr_programs = set(set_1)
set_2 = {'Aleena','Rafia','Khushbakht','Aqsa','Ali','Asad','Jihan','Usama','Dua','Maheen'}
Non_engr = set(set_2)
both_programs = set_1.intersection(set_2)
candidates = set_1.union(set_2)
total_no = len(candidates)
print(f"The candidated who applied in both programs are:{both_programs}")
print(f"The total number of candidates who applied to uet are:{total_no}")
