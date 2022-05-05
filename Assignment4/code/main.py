#Deepshikha
#CS21BTECH11016
#probability

#prob. to pass english
p_e=float(0.75)

#prob. to pass both hindi and english
p_eh=float(0.50)

#prob. that both not pass
p_both_not_pass=float(0.10)

p_both_pass=float(1-p_both_not_pass)


p_h=float(p_both_pass+p_eh-p_e)
p_h="{:.2f}".format(p_h)

print(" probability of passing the Hindi examination is ",p_h)
