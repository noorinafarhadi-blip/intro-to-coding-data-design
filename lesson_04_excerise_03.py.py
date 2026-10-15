#Write a program that asks the user for their favorite colors (up to 5)

favorite_colors = [] 
for color in range (5) : 
    color = input("Blue, Yellow: ")
    favorite_colors.append(color)

print(favorite_colors)

#and stores them in a list. Then, create a sentence that says,"Your favorite colors are: color1, color2, ..." using the .join() function.

Sentence = "Your Facorite colors are: "+" , ".join(favorite_colors)