                            #Author :  MUMMIDI BALAJI   (01-10-2020) 
                            #This is a code is designed to convert Numbers to Words

print('                                                  ＣＯＤＥＤ ＢＹ ＢＡＬＡＪＩ                                             ')
print('\n*****************************************************NUMBERS TO WORDS*********************************************** \n')

words_upto_19                   =    ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
words_for_tens                  =    ['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
words_for_hundred           =    ['','One Hundred','Two Hundred','Three Hundred','Four Hundred','Five Hundred','Six Hundred','Seven Hundred','Eight Hundred','Nine Hundred']
words_for_Thousand         =   ['','Thousand','Two Thousand','Three Thousand','Four Thousand','Five Thousand','Six Thousand','Seven Thousand','Eight Thousand','Nine Thousand']
words_for_Lakhs                =   ['','One Lakh','Two Lakhs','Three Lakhs','Four Lakhs','Five Lakhs','Six Lakhs','Seven Lakhs','Eight Lakhs','Nine Lakhs','Ten Lakhs']
Higher_words                       =    ['','Lakhs','Crores','hundred']

a= int(input("Enter a number between \'0\' and  \'1 Crore\' :"))
if a == 0:
    print("ZERO")
    
elif a<=19:
    print(words_upto_19[a])
    
elif a<=99:
    print(words_for_tens[a//10]+" "+words_upto_19[a%10])
    
elif a<=999:
    print(words_for_hundred[a//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[(a%100)%10])
    

elif a<=9999:
    print(words_for_Thousand[a//1000]+' '+words_for_hundred[a//100%10]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%100%10])

elif a == 10000:
    print("Ten Thousand")

elif a == 20000:
    print("Twenty Thousand")

elif a == 30000:
    print("Thirty Thousand")

elif a == 40000:
    print("Fourty Thousand")


elif a == 50000:
    print("Fifty Thousand")

elif a == 60000:
    print("Sixty Thousand")

elif a ==70000:
    print("Seventy Thousand")

elif a == 80000:
    print("Eighty Thousand")

elif a == 90000:
    print("Ninety Thousand")

elif a>10000 and a<=19999:
    print(words_upto_19[a//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>20000 and a<=29999:
    print(words_for_tens[a//10000]+' '+words_upto_19[a%10000//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>30000and a<=39999:
    print(words_for_tens[a//10000]+' '+words_upto_19[a%10000//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])    

elif a>40000 and a<=49999:
    print(words_for_tens[a//10000]+' '+words_upto_19[a%10000//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>50000 and a<=59999:
    print(words_for_tens[a//10000]+' '+words_upto_19[a%10000//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])
    
elif a>60000 and a<=69999:
    print(words_for_tens[a//10000]+' '+words_upto_19[a%10000//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])
    
elif a>70000 and a<=79999:
    print(words_for_tens[a//10000]+' '+words_upto_19[a%10000//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>80000 and a<=89999:
    print(words_for_tens[a//10000]+' '+words_upto_19[a%10000//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>90000 and a<=99999:
    print(words_for_tens[a//10000]+' '+words_upto_19[a%10000//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a == 100000:
    print("One Lakh")
    
elif a>100000 and a<=1000000:
    print(words_for_Lakhs[a//100000]+' '+words_for_tens[a%100000//10000]+' '+words_for_Thousand[a%10000//1000]+' '+words_for_hundred[a%1000//100]+' '+words_upto_19[a%10])

elif a>1000000 and a<=1999999:
    print(words_upto_19[a//100000]+' '+Higher_words[1]+' '+words_for_tens[a%100000//10000]+' '+words_upto_19[a%10000//1000]+' '+words_for_Thousand[1]+' '+words_for_hundred[a%1000//100]+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a == 2000000:
    print("Ten Lakhs")

elif a == 3000000:
    print("Thirty Lakhs")

elif a == 4000000:
    print("Fourty Lakhs")

elif a == 5000000:
    print("Fifty Lakhs")    

elif a == 6000000:
    print("Sixty Lakhs")

elif a == 7000000:
    print("Seventy Lakhs")

elif a == 8000000:
    print("Eighty Lakhs")

elif a == 9000000:
    print("Ninty Lakhs")

elif a>2000000 and a<=2999999:
    print(words_for_tens[a//1000000]+' '+words_upto_19[a%1000000//100000]+' '+Higher_words[1]+' '+words_for_tens[a%100000//10000]+' '+words_for_Thousand[a%10000//1000]+' '+words_for_hundred[a%1000//100]+' '+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])
    
elif a>2999999 and a<=3999999:
    print(words_for_tens[a//1000000]+' '+words_upto_19[a%1000000//100000]+' '+Higher_words[1]+' '+words_for_tens[a%100000//10000]+' '+words_for_Thousand[a%10000//1000]+' '+words_for_hundred[a%1000//100]+' '+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>3999999 and a<=4999999:
 print(words_for_tens[a//1000000]+' '+words_upto_19[a%1000000//100000]+' '+Higher_words[1]+' '+words_for_tens[a%100000//10000]+' '+words_for_Thousand[a%10000//1000]+' '+words_for_hundred[a%1000//100]+' '+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>4999999 and a<=5999999:
    print(words_for_tens[a//1000000]+' '+words_upto_19[a%1000000//100000]+' '+Higher_words[1]+' '+words_for_tens[a%100000//10000]+' '+words_for_Thousand[a%10000//1000]+' '+words_for_hundred[a%1000//100]+' '+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>5999999 and a<=6999999:
    print(words_for_tens[a//1000000]+' '+words_upto_19[a%1000000//100000]+' '+Higher_words[1]+' '+words_for_tens[a%100000//10000]+' '+words_for_Thousand[a%10000//1000]+' '+words_for_hundred[a%1000//100]+' '+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>6999999 and a<=7999999:
    print(words_for_tens[a//1000000]+' '+words_upto_19[a%1000000//100000]+' '+Higher_words[1]+' '+words_for_tens[a%100000//10000]+' '+words_for_Thousand[a%10000//1000]+' '+words_for_hundred[a%1000//100]+' '+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>7999999 and a<=8999999:
    print(words_for_tens[a//1000000]+' '+words_upto_19[a%1000000//100000]+' '+Higher_words[1]+' '+words_for_tens[a%100000//10000]+' '+words_for_Thousand[a%10000//1000]+' '+words_for_hundred[a%1000//100]+' '+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a>8999999 and a<=9999999:
    print(words_for_tens[a//1000000]+' '+words_upto_19[a%1000000//100000]+' '+Higher_words[1]+' '+words_for_tens[a%100000//10000]+' '+words_for_Thousand[a%10000//1000]+' '+words_for_hundred[a%1000//100]+' '+' '+words_for_tens[a%100//10]+' '+words_upto_19[a%10])

elif a == 10000000:
    print("one Crore")

else:
    print("\nBrother, Please enter the value in between 0 and 1 Crore\n")
