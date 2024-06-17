'''

PART 1 MULTIPLE CHOICE

QUESTION 01: A

QUESTION 02: C

QUESTION 03: A

QUESTION 04: D

QUESTION 05: B

QUESTION 06: C

QUESTION 07: D

QUESTION 08: A

QUESTION 09: A

QUESTION 10: B

________________________________________________________

PART 2 EVALUATION


1)

Firstly, here is a syntax error after the department id declaration. A comma is missing. It should instead be:

SELECT
    department_id,
    COUNT(*) AS total_admissions
    
    
Secondly, the columns will be mismatched as the group by is using the declaration department_name. Instead it should use department_id, like this:

GROUP BY
    department_id;




2)

One option is to index the admission date column. This will help speed up output and performance

A second option for improvement would be to improve the readability of our table by using aliases


Finally we could add in some code in our parameters to handle potential null values




________________________________________________________

PART 3 CODING CHALLENGE

(find code below)

'''


def calculate_change(cost):
  
    coins = {
        2.0: 2,
        1.0: 6,
        0.5: 10,
        0.2: 4,
        0.1: 6,
        0.05: 7,
        0.02: 4,
        0.01: 6
    }

    change_dict = {
        2.0: 0,
        1.0: 0,
        0.5: 0,
        0.2: 0,
        0.1: 0,
        0.05: 0,
        0.02: 0,
        0.01: 0
    }
    

    total_coins = sum(coins[value] for value in coins)

    change_needed = total_coins - cost

    if change_needed < 0:
        return "Can't afford this with the available petty change"

    for value in sorted(coins.keys(), reverse=True):
        if change_needed <= 0:
            break
        num_coins = min(change_needed // value, coins[value])
        change_dict[value] = num_coins
        change_needed -= num_coins * value
    
    return change_dict


print(calculate_change(12.50)) 
print(calculate_change(16.89)) 
print(calculate_change(16.90))