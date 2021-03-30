#cat years, dog years
"""Kata Task
I have a cat and a dog.
I got them at the same time as kitten/puppy. That was humanYears years ago.
Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that"""

def human_years_cat_years_dog_years(human_years):

    cat = [15,9,4]
    dog = [15,9,5]
    if human_years == 1:
        return [human_years, cat[0],dog[0]]
    elif human_years == 2:
        return [human_years,cat[0] + cat[1], dog[0] + dog[1]]
    else:
        return [human_years,cat[0] + cat[1] + ((human_years -2) * cat[2]) , dog[0] + dog[1] + ((human_years -2) * dog[2])]
