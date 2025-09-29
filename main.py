from pyscript import display


restaurant_name = 'Uncle Moe Shawarma Hub' # String
year_established = 2022 # Integer
owner_name = 'Oscar Barrientos' # String
business_hours = 'Opening Hours: 6 A.M to 7 P.M '




display(restaurant_name, owner_name, year_established, target="div1" )
display(business_hours, target="div4")
display("Welcome to " + restaurant_name + "! We are located in the heart of the city, serving delicious shawarma and manakeesh since " + str(year_established) + ". Our owner, " + owner_name + ", takes pride in providing the best quality food. Our popular items include Beef Manakeesh, Chicken Manakeesh, and Beef Shawarma, all at affordable prices. We also offer delivery services for your convenience. Our business hours are from " + business_hours + ". Thank you for choosing us!" , target="div2")






