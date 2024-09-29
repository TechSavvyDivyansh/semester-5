import xml.etree.ElementTree as ET


# Load XML data from a file
tree = ET.parse('breakfast_menu.xml')
root = tree.getroot()


# Retrieve all food items
print("---Food-menu---\n")

foods = root.findall('food')

for food in foods:
    name = food.find('name').text
    price = food.find('price').text
    description = food.find('description').text.strip()
    calories = food.find('calories').text
    print(f"Name: {name}, Price: {price}, Description: {description}, Calories: {calories}")


# retrieve specific food item by name
food_name = input("Enter the name of food: ")

found = False  

for food in root.findall('food'):
    name = food.find('name').text
    if name.lower() == food_name.lower():
        price = food.find('price').text
        description = food.find('description').text.strip()
        calories = food.find('calories').text
        print(f"Found Food: {name}, Price: {price}, Description: {description}, Calories: {calories}")
        found = True  
        break 

if not found:
    print("Food item not found.")



#add new food item
name=input("Enter a new food item:")
price=input("Enter price:")
description=input("Enter food description:")
calories=input("Enter the calories:")

new_food=ET.Element('food')
ET.SubElement(new_food,'name').text=name
ET.SubElement(new_food,'price').text=price
ET.SubElement(new_food,'description').text=description
ET.SubElement(new_food,'calories').text=calories

root.append(new_food)

tree.write('breakfast_menu.xml',encoding='utf-8',xml_declaration=True)
print(f"Food item '{name}' added")



#deleting food item by name
food_to_delete=input("Enter name of food to be deleted")
deleted_flag=0

for food in root.findall('food'):
    name=food.find('name').text 
    if name.lower() == food_name.lower():
        root.remove(food)
        tree.write('breakfast_menu.xml', encoding='utf-8', xml_declaration=True)
        print(f"Food item '{food_name}' has been deleted.")
        deleted_flag=1
        break
if deleted_flag==0:
    print("Food not found")