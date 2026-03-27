'''
DAY 25: Logic
Today I Learned that sometimes problems are easier to solve if we learn from our mistakes, so this time i'm going to resolve a totally random problem and trying to guess the best solution
Today's "side quest" is resolving a problem similar to the Longest Increasing Subsequence one, organizing the biggest number of meetings possible:
'''


Meetings = [(14, 15), (10, 15), (12, 13), (16, 18), 
    (8, 12), (11, 14), (9, 10), (15, 16), 
    (13, 16), (17, 19), (10, 11), (19, 20)]  # Hours for the meetings


# function to get the perfect combo
def find_best_combination(list_meetings: list):
    list_meetings.sort(key=lambda x: x[1])  # Sorts the finishing hours of the meetings
    
    result = []  # Result
    FH = 0  # Finishing hour
    
    # Add all possible meetings
    for i, v in list_meetings:
        if i >= FH:
            result.append((i, v))
            FH = v
    return result

result = str(find_best_combination(Meetings))
print(f"Perfect meetings combination: {result.replace("[", "").replace("]", "")}")


'''
At the start, I was really in crisis for this problem, I was literally creating something like a 100-line code with weighted sorting, thinking it was far more complicated
Then I saw the pattern with the meetings finishing hours, that's the result!
'''