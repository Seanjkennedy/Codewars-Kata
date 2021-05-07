
def sort_by_name(arr="zero"):

    single_repeating = {'1':'one','2':'two','3':'three', '4':'four', '5':'five', '6':'six', '7':'seven','8':'eight','9':'nine','0':''}
    non_repeating = {'10':'ten','11':'eleven','12':'twelve','13':'thirteen', '14':'fourteen','15':'fifteen','16':'sixteen',
                     '17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty'}
    tens_repeating  = {'2':'twenty','3':'thirty', '4':'forty', '5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety','0':''}

    word_list = []

    for number in arr:
        
        temp = []
        number = str(number)
        
        if number == "0":
        
            temp.append("zero")
            temp.append(0)
            word_list.append(temp)
            continue

        if len(number) == 1:
            
            temp.append(single_repeating[number])
            temp.append(number)
            word_list.append(temp)

        if len(number) == 2:
            
            if 10 <= int(number) <= 19:
                
                temp.append(non_repeating[number])
                temp.append(number)
                word_list.append(temp)
            
            else:
            
                temp.append(f'{tens_repeating[number[0]]} {single_repeating[number[1]]}')
                temp.append(number)
                word_list.append(temp)
                
        if len(number) == 3:
            
            if 10 <= int(number[1:]) <= 19:
                
                temp.append(f'{single_repeating[number[0]]} hundred {non_repeating[number[1:]]}')
                temp.append(number)
                word_list.append(temp)
            
            else:
                
                temp.append(f'{single_repeating[number[0]]} hundred {tens_repeating[number[1]]} '
                                 f'{single_repeating[number[2]]}')
                temp.append(number)
                word_list.append(temp)

    x = [[i[0].replace("  ", " "),i[1]]for i in word_list]
    x.sort()
    return [int(i[1]) for i in x]
  
